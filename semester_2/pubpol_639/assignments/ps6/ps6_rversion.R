library(dplyr)
library(broom)
library(haven)
library(ggplot2)
library(janitor)

age21mort <- read_dta('~/Documents/umich/coursework/semester_2/pubpol_639/assignments/ps6/age21mort.dta')

age21mort <- age21mort %>%
  # center age 
  mutate(over_21 = ifelse(agecell > 21, 1, 0),
         age_centered = agecell - 21,
         age_sq = age_centered*age_centered)
# scatter 
age21mort %>% 
  ggplot(aes(x = age_centered, y = all)) +
  geom_point() +
  geom_vline(xintercept = 0, lty = 3)
# regs
model_1 <- lm(all ~ age_centered, data = age21mort)
model_2 <- lm(all ~ age_centered + over_21 + age_centered*over_21, data = age21mort)
model_3 <- lm(all ~ age_centered + over_21 + age_sq + age_centered*over_21 + age_sq*over_21, data = age21mort)
# filtered_age21mort <- age21mort %>% filter(agecell >= 20 & agecell <= 22)
model_4 <- lm(all ~ age_centered + over_21 + age_centered*over_21, 
              data = dplyr::filter(age21mort, agecell >= 20 & agecell <= 22))
# table 
stargazer::stargazer(model_1, model_2, model_3, model_4, 
           type = 'text', 
           dep.var.labels = c("All causes"),
           column.labels = c("Simple", "Interaction", "Squared", "Restricted"),
           omit.stat = "all", 
           digits = 3 )
