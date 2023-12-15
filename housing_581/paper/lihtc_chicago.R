## public housing in chicago 

### OOO
# 1. read in lihtc map 
# 2. count developtments put in service by year 


## set up 
library(dplyr)
library(sf)
library(tigris)
library(readr)
library(janitor)
library(ggplot2)
library(ggthemes)

## load public housing data 
housing <- read_csv('Affordable_Rental_Housing_Developments_20231205.csv') %>% clean_names()
# glimpse(housing)
lihtc_chicago <- read_csv('lihtc_chicago.csv') %>%

# chi base map 
# downloaded from: https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6
chi_base <- st_read('Boundaries - Community Areas (current).geojson')
  

## how many missing coordinates 
tabyl(is.na(lihtc_chicago$LATITUDE))

## year allocated is when lihtc funding was allocated
tabyl(lihtc_chicago$YR_ALLOC)

## convert to sf 
lihtc_sf <- lihtc_chicago %>%
  filter(!is.na(LATITUDE)) %>%
  # replace missing values with NAs
  mutate(YR_PIS = as.factor(ifelse(YR_PIS %in% c(9999, 8888), NA, YR_PIS))) %>%
  st_as_sf(coords = c('LONGITUDE', 'LATITUDE'), crs=4326)

ggplot() + 
  geom_sf(data = chi_base) +
  geom_sf(aes(color = YR_PIS), data = lihtc_sf)

lihtc_chicago %>%
  mutate(YR_PIS = ifelse(YR_PIS %in% c(9999, 8888), NA, YR_PIS)) %>%
  distinct(.keep_all = TRUE) %>%
  group_by(YR_PIS) %>%
  summarise(n = n()) %>%
  ggplot() + 
  geom_col(aes(x = YR_PIS, y = n))
