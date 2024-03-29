## 2024-03-26

### Panel Data

### agenda
- finish fixed effects
- panel data: entity and time fixed effects
    - policy: traffic fatalities and alcohol taxes
- next time: difference in differences
    - policy: minimum wage and employment

### panel data
- dataset contains observatiosn on multiple entities (individuals, firms, countries, etc.), where each entity is observed over multiple time periods.
- examples:
    - data on number of college credits taken each year by 1000 students over eight years, for 8000 observations total
    - data on 420 CA school districts in 1999 and again in 2000, for 840 observations total
    - data on unemployment insurance take up in 50 states over 12 years, for 600 observations total
- also called longitudinal data

### Notation
- a double subscript distinguishes entities (e.g. states), and time periods (e.g. years)

```
i = entity, n = number of entities,
so i = 1, 2, ..., n
t = time period, T = number of time periods,
so t = 1, 2, ..., T
```

- data: suppose we have panel data with k regressors:
```
(X_1it, X_2it, ..., X_kit)
i = 1, 2, ..., n
t = 1, 2, ..., T
```

### why panel data are useful
- with panel data, we can control for factors that:
    - vary across entities but not over time
    - vary over time but not across entities
    - could cause omitted variable bias if they are omitted
    - are unobserved or unmeasured -- and therefore cannot be included in the regression model
- here's the key idea:
    - if an omitted variable does not change over time, then any changes in Y over time cannot be caused by the omitted variable

#### example: beer taxes and traffic fatalities
- research question: do higher taxes on beer reduce traffic fatalities in a state?
- observational unit: a year in a US state
    - 48 US states (No HI, AK, or territories), so n = 48
    - 7 years (1982 - 1988), so # of observations = 48 * 7 = 336
    - (unbalanced panel if T is not the same for all entities)
- variables:
    - traffic fatality rate (# of traffic deaths in that state in that year per 10,000 residents)
    - tax on a case of beer
    - other (legal driving age, drunk driving laws, etc.)

### raw correlation
- scatterplot of traffic fatality rate and beer tax
- x-axis: beer tax
- y-axis: traffic fatality rate
- shows weak positive correlation, bunching between 0 and 0.5
- several outliers with high taxes and fatality rates around the mean

### why might there be more traffic fatalities in states with higher beer taxes?
- other factors that determine traffic fatality rate:
    - quality (age) of automobiles
    - quality of roads
    - "Culture" around drinking and driving
    - density of cars on the road

### these could cause omitted variable bias
#1 traffic density:
- high traffic density could means more traffic fatalities
- western states with lower traffic density have lower beer taxes
- two conditions for ovb are satisfied:
    - high taxes could reflect high traffic density (so the OLS coefficient on would be biased positively)
#2 attitudes towards drinking and driving:
- arguably a determinant of traffic fatalities
- potentially correlated with beer taxes
- two conditions for ovb are satisfied:
    - high taxes could pick up the effect of a culture of drinking and driving (so the OLS coefficient on would be biased positively)

### panel data with two time periods
consider the panel data model:
$$
FatalityRate_{it} = \beta_0 + \beta_1 BeerTax_{it} + \Beta_2 Z_{it} + u_{it}
$$

- Z_i is a factor that does not change over time (density), at least during the years on which we have data.
    - Suppose Z_i is not observed, so it's omission could result in omitted variable bias.
    - The Effect of Z_i can be eliminated using T = 2 time periods.
- Key idea:
    - any change in the fatality rate from 1982 to 1989 cannot be caused by $Z_i$ because $Z_i$ (by assumption) does not change over time.

### The Math

- consider fatality rate in 1988 and 1982:
$$
FatalityRate_{i1988} = \beta_0 + \beta_1 BeerTax_{i1988} + \beta_2 Z_i + u_{i1988}
FatalityRate_{i1982} = \beta_0 + \beta_1 BeerTax_{i1982} + \beta_2 Z_i + u_{i1982}
$$
- subtracting the two equations removes the effect of $Z_i$

## A few notes
- this difference qualtion can be estimated by OLS, even if Z_i is not observed.


### State Fixed Effects
- Allows separate intercepts for each state
- accounts for fixed differences across states that do not change over time
- the model is:
$$
FatalityRate_{it} = \beta_0 + \beta_1 BeerTax_{it} + \beta_2 Z_{it} + \alpha_i + u_{it}
$$
- $\alpha_i$ is the state fixed effect: $\alpha_TX = Texas, \alpha_CA = California, etc.$
- In binary regressor form:
$$
FatalityRate_{it} = \beta_0 + \Upsilon_CA DCA_i + \Upsilon_TX DTX_i + \beta_1 BeerTax_{it} + u_{it}
$$

- DCA_i = 1 if state i is California, 0 otherwise
- DTX_i = 1 if state i is Texas, 0 otherwise
- Leave out one state to avoid perfect multicollinearity

### Two ways to write a FE model (Notation)
A bunch of dummy variables:
- $Y_{it} = \beta_0 + \beta_1 X_{it} + \gamma_1 D2_i + \gamma_2 D3_i + ... + \gamma_n Dn_i + u_{it}$
- Where $D2_i = 1$ if i = 2, 0 otherwise

Other notation (more compact):
- $Y_{it} = \beta_0 + \beta_1 X_{it} + \alpha_i + u_{it}$
- where $\alpha_i$ is a vector of state fixed effects (one for each state)

### Including Time Fixed Effects
- an omitted variable might vary over time but not across states
    - changes in national laws
    - anything that would cause a change in vehicle fatalities over time
- let these changes be denoted by the variable $W_t$, which changes over time but not states:
$$
Y_{it} = \beta_0 + \beta_1 BeerTax_{it} + \beta_2 Z_{it} + \beta_3 W_t + u_{it}
$$
- Now the intercept varies across states (with $Z_i$) and over time (with $W_t$)
- could also be written:
$$
Y_{it} = \beta_0 + \beta_1 BeerTax_{it} + \alpha_i + \lambda_t + u_{it}
$$

### what we find:
- state fixed effects control for unobservable variables that vary across states but not over time
    - these seem to make the biggest difference
- year fixed effects control for unobservable variables that vary over time but not across states
    - these do not make a big difference in terms of the beer tax.
- including both of these requires variation in beer taxes across states and within states over time.
    - we are comparing states that changed the taxes a lot to states that changed the taxes very little.


