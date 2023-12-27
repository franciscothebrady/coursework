## zillow rents

library(dplyr)
library(readr)
library(tidyr)
library(lubridate)
library(tidycensus)
library(ggplot2)
census_api_key("6ac387b0502d560fc46b0a76bbc7865b6354c7de", install = TRUE, overwrite = TRUE)

## zillow 
zori <- read_csv('City_zori_sm_month.csv')

# search for mpls
mpls_zori <- zori %>% 
  filter(grepl('Minneapolis', RegionName)) %>% 
  pivot_longer(cols = -c(RegionID:CountyName), 
               names_to = 'date', values_to = 'ZORI') %>%
  select(RegionName, date, ZORI) %>%
  mutate(date = as.Date(date),
         year = lubridate::year(date)) %>% 
  group_by(year) %>%
  summarise(annual_zori = mean(ZORI, na.rm = T))

zori_16 <- mpls_zori %>% filter(year == 2016) %>% pull(annual_zori)
zori_21 <- mpls_zori %>% filter(year == 2021) %>% pull(annual_zori)

mpls_zori %>% 
  ggplot() + 
  geom_line(aes(x = year, y = annual_zori)) + 
  geom_segment(aes(x = 2016,
                   xend = 2016,
                   y = 1200,
                   yend = zori_16), color = "cadetblue") + 
  geom_segment(aes(x = 2021,
                   xend = 2021,
                   y = 1200,
                   yend = zori_21), color = "#800000") + 
  theme_linedraw(base_size = 10) + 
  geom_text(aes(x = 2016, 
                y = zori_16, 
                label = round(zori_16, 2)), check_overlap = T) + 
  labs(title = "Zillow Rent Index: 2015 - 2023", caption = 'Annualized from monthly values')

