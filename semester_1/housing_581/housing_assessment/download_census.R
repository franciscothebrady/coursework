
## set up ---- 

library(dplyr)
library(tidyr)
library(tidycensus)
library(purrr)
library(stringr)
library(ggplot2)
library(googlesheets4)
library(writexl)
library(janitor)
library(wesanderson)
library(ggthemes)
## ggtheme 
# theme_hsg <- function() {
#   theme_bw() %+replace%
#     theme(legend.position = 'none',
#             plot.title = element_text(size=12),
#             plot.caption = element_text(size = 10),
#             axis.title.y = element_text(size = 8),
#             axis.title.x = element_text(size = 8))
# }

## google auth 
googlesheets4::gs4_auth(email = 'fbrady@umich.edu')

## params ----
start_year <- 2016
end_year <- 2021

census_api_key("6ac387b0502d560fc46b0a76bbc7865b6354c7de", install = TRUE, overwrite = TRUE)
# Median rent as pct of income: B25071
# acs5_geography %>% filter(table == 'B25071')
## census variables 
vars <- load_variables(year = 2021, dataset = "acs1")

# demographic ---- 
## B01003 - total population ----
table_codes <- vars %>% filter(grepl('B01003', name)) 

total_pop <- c(start_year:end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = ifelse(x == 2020, "acs5", "acs1"),
                  variables = c('B01003_001'),
                  year = x,
                  state = 'MN', 
                  geometry = F),
          .id = 'year') %>%
  # filter(grepl("Hennepin", NAME))
  filter(grepl("Minneapolis", NAME))

# total_pop %>% sf::st_drop_geometry() %>%
#   ggplot() + 
#   geom_col(aes(x = year, y = estimate, fill = year)) +
#   scale_y_continuous(labels = scales::comma)

# pct average 
total_pop %>%
  mutate(pct_change = 100*(estimate - lag(estimate)) / lag(estimate)) %>%
  ungroup() %>%
  mutate(avg_growth = mean(pct_change, na.rm = T))
  # ggplot() + 
  # geom_line(aes(x = year, y = pct_change, group = 1)) + 
  # scale_y_continuous(labels = scales::label_percent()) +
  # theme_bw() +
  # theme(legend.position = 'none',
  #       plot.title = element_text(size=12),
  #       plot.caption = element_text(size = 10),
  #       axis.title.y = element_text(size = 8),
  #       axis.title.x = element_text(size = 8)) + 
  # labs(title = 'Minneapolis Population', 
  #      subtitle = '2016 - 2021',
  #      ) + 
  # ylab(label = 'Population (Thousands)') + 
  # xlab(label = 'Year') + 
  # scale_fill_viridis_d()

# pop_chart
output_tbls <- list(B01003_total_population = total_pop %>% sf::st_drop_geometry())

## B02001: race ---- 
table_codes <- vars %>% filter(name %in% c('B02001_002', 
                                           'B02001_003', 
                                           'B02001_004', 
                                           'B02001_005', 
                                           'B02001_006', 
                                           'B02001_007', 
                                           'B02001_008', 
                                           'B02001_009')) %>%
  mutate(race_label = str_replace(label, '.+!!(.+)', '\\1')) %>%
  mutate(race_label = gsub(':', '', race_label))
  

population_race <- 
  c(c(start_year, end_year)) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = ifelse(x == 2020, "acs5", "acs1"),
                  variables = c(table_codes$name),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) %>%
  left_join(table_codes, by = c('variable' = 'name')) %>%
  select(year, estimate, race = race_label) %>%
  # recode race to shorter names 
  mutate(race_label = case_when(race == "White alone" ~ "white", 
                          race == "Black or African American alone" ~ "Black",
                          race == "American Indian and Alaska Native alone" ~ "Other", 
                          race == "Asian alone" ~ "Asian",
                          race == "Native Hawaiian and Other Pacific Islander alone" ~ "Other", 
                          race == "Some other race alone" ~ "Other",
                          race == "Two or more races" ~ "Other", 
                          race == "Two races including Some other race" ~ "Other"))

population_race %>%
  group_by(year) %>%
  mutate(pct = estimate / sum(estimate)) %>%
  pivot_wider(id_cols = c(-race_label, -estimate), 
              names_from = 'year', 
              values_from = pct) %>% kableExtra::kable() %>% kableExtra::kable_classic()

pop_race <- population_race %>%
  group_by(year) %>%
  mutate(Percent = round(estimate/sum(estimate), 2)) %>% 
ggplot() +
  geom_col(aes(x = race, y = Percent, fill = year), 
           position = 'dodge') + 
  scale_fill_manual(values = c(wes_palettes$Darjeeling1, wes_palettes$Darjeeling2[1])) +
  scale_y_continuous(labels = scales::label_percent()) + 
  theme_bw() + 
  labs(title = 'Population by race', caption = 'Note: 2020 5-Year estimates, rest 1-Year estimates.\nOther includes NHPI, AIAN and multiple') + 
  ylab(label = 'Population (percent)') + 
  theme(plot.title = element_text(size=12),
        plot.caption = element_text(size = 6),
        plot.subtitle = element_text(size = 10),
        axis.title.y = element_text(size = 8),
        axis.title.x = element_text(size = 8)) + 
  xlab('Race') + labs(fill = 'Year')
  
pop_race  
  
## S1701 - poverty status (by tenure) ---- 
# S1701
table_codes <- vars %>% 
  filter(grepl('C17019', name)) %>%
  filter(!grepl('001$', name)) %>% 
  mutate(tenure = case_when(grepl('Owner', label) ~ 'Owner',
                            grepl('Renter', label) ~ 'Renter',
                            TRUE ~ 'Total')) %>%
  mutate(poverty_status = case_when(grepl('below', label) ~ 'below_poverty',
                                    grepl('above', label) ~ 'at_or_above_poverty'))
  
poverty_by_tenure <- 
  c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = "acs1",
                  variables = c(table_codes$name),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) %>%
  left_join(table_codes, by = c('variable' = 'name')) %>%
  select(year, estimate, moe, tenure, poverty_status)

## table output 
poverty_by_tenure %>%
  filter(tenure != 'Total') %>%
  select(-moe) %>%
  pivot_wider(names_from = c('tenure', 'poverty_status'), 
              values_from = 'estimate') %>% 
  
  

output_tbls <- append(output_tbls, list(C17019_pov_by_tenure = poverty_by_tenure))
  
## S1901 - Income Ranges ---- 
table_codes <- vars %>% 
  filter(grepl('B19001_', name)) %>% 
  # pull income ranges 
  mutate(income_range = str_replace(label, '.+!!(.+)', '\\1')) 

 mpls_income <- 
  c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = "acs1",
                  variables = c(table_codes$name),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) %>%
  left_join(table_codes, by = c('variable' = 'name')) 
 
 output_tbls <- append(output_tbls, list(B19001_income = mpls_income))
 
 ## median income by race 
table_codes <- vars %>% filter(grepl('B19013[A-Z]', name)) 

mpls_income_race <- 
  c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = "acs1",
                  variables = c(table_codes$name),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) %>%
  left_join(table_codes, by = c('variable' = 'name')) %>%
  mutate(race = gsub('MEDIAN HOUSEHOLD INCOME IN THE PAST 12 MONTHS \\(IN 2021 INFLATION-ADJUSTED DOLLARS\\)',
                     '', concept)) 
mpls_income_race <- mpls_income_race %>%
  select(year, estimate, race)


 ## median gross rents ----
 vars %>% filter(grepl('\\brent\\b', label)) %>% View 

## B25003 - tenure by race ----
codes <- 
vars %>% 
  filter(grepl('B25003', name)) %>% 
  filter(!grepl('001$', name)) %>% 
  mutate(tenure = case_when(grepl('Owner', label) ~ 'Owner',
                            grepl('Renter', label) ~ 'Renter')) %>%
  mutate(race_ethnicity = tolower(str_extract(concept, "(?<=\\().+?(?=\\))"))) %>%
  select(name, tenure, race_ethnicity)

tenure_by_race <- 
  c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
    get_acs(geography = "place", 
                survey = "acs1",
                variables = c(codes$name),
                year = x,
                state = 'MN'),.id = 'year' ) %>%
      filter(grepl("Minneapolis", NAME)) %>%
  left_join(codes, by = c('variable' = 'name')) %>%
  mutate(race_ethnicity = ifelse(is.na(race_ethnicity), 'total', race_ethnicity)) 

output_tbls <- append(output_tbls, list(B25003_ten_by_race = tenure_by_race))

## B25070 - rent pct of income ----
# all rent as a percentage of incomes 
# GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME IN THE PAST 12 MONTHS
table_codes <- vars %>% 
  filter(grepl('25070', name)) 
# median rent as a percentage of incomes   
median_rent_pct_income <- c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = "acs1",
                  variables = c('B25071_001'),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) 

output_tbls <- append(output_tbls, list(B25071_median_rent = median_rent_pct_income))

rents_pct_income <- 
  c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = "acs1",
                  variables = c(table_codes$name),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) %>%
  left_join(table_codes, by = c('variable' = 'name')) %>%
  mutate(pct_range = str_replace(label, '.+!!(.+)', '\\1'))

output_tbls <- append(output_tbls, list(B25070_rents_pct_income = rents_pct_income))

## plot something fun 
rents_pct_income %>% 
  filter(!pct_range %in% c('Total:', 'Not computed')) %>% 
  ggplot() + geom_col(aes(x = pct_range, y = estimate)) + 
  facet_wrap(~year) + 
  coord_flip() + 
  labs(y = 'Estimate', x = 'Rent as % of Income') 
  
# units ---- 
## units by rent
## 25063
table_codes <- 
vars %>%
  filter(grepl('25063', name))

units_by_rent <- 
  c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = "acs1",
                  variables = c(table_codes$name),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) %>%
  left_join(table_codes, by = c('variable' = 'name'))
            
output_tbls <- append(output_tbls, list(B25063_units_By_rent = units_by_rent))

## structure ----
# B25034
# table_codes <- 
# vars %>% filter(grepl('BUILT', concept)) %>% View

table_codes <-
  vars %>% filter(grepl('25034', name)) %>%
  mutate(category = str_replace(label, '.+!!(.+)', '\\1')) %>%
  mutate(category = gsub(':', '', category))

# download 
units_year_built <- 
  c(start_year, end_year) %>% 
  set_names() %>%
  map_dfr(\(x) 
          get_acs(geography = "place", 
                  survey = "acs1",
                  variables = c(table_codes$name),
                  year = x,
                  state = 'MN'),
          .id = 'year' ) %>%
  filter(grepl("Minneapolis", NAME)) %>%
  left_join(table_codes, by = c('variable' = 'name')) %>%
  select(year, estimate, moe, category) %>%
  mutate(category = gsub('Built', '', category))
  

yearbuilt_plot <- 
units_year_built %>%
  filter(category != "Total") %>%
  group_by(year) %>%
  mutate(total = sum(estimate)) %>%
  mutate(pct = round(100*(estimate/total), 2)) %>% #View
  ggplot() +
  geom_bar(aes(x = category, y = pct), 
           stat = "identity", position = "dodge", 
           fill = 'cadetblue') + 
  # scale_color_manual(values = "cadetblue") + 
  #labs(fill = "Year Built", caption = 'For 2016, last bar is built 2014 or later') + 
  ylab('Percent of Total Housing') + 
  xlab('') +
  theme_bw() + 
  scale_fill_viridis_d() + 
  facet_grid(~year)

# units_year_built %>% filter(category != "Total") %>% group_by(year) %>% mutate(total = sum(estimate)) %>%
#  mutate(pct = estimate/total) %>% filter(year == 2016) %>% summarise(should_be_one = sum(pct))


output_tbls <- append(output_tbls, list(B25034_units_year_built = units_year_built))

## gather all tables 
write_xlsx(output_tbls, 'housing_tables.xlsx')

## plumbing 
# B25016

acs1_profile <- load_variables(year = 2016, dataset = "acs1/profile")
year_built <- acs1_profile %>%
  filter(grepl('DP04', name)) %>% 
  filter(grepl('BUILT', label)) %>% 
  filter(grepl('Estimate', label)) %>% 
  mutate(category = str_replace(label, '.+!!(.+)', '\\1')) %>%
  mutate(category = gsub(':', '', category)) 

tidycensus::pums_variables %>% View
median_incomes_by_race <- get_pums(variables = 'HINC', 'SPORDER', 'RA')
