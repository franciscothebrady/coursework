### mismatch ratio 

library(dplyr)
library(tidycensus)
library(stringr)
library(purrr)

## params 
start_year <- 2016
end_year <- 2021

## load vars 
vars <- load_variables(year = 2016, dataset = 'acs1')
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
  left_join(table_codes, by = c('variable' = 'name')) %>%
  select(year, estimate, income_range)
# wrangle income 
mpls_income <- mpls_income %>%
  mutate(temp = str_extract_all(income_range, "\\d+",)) %>%
  unnest_wider(c(temp))

