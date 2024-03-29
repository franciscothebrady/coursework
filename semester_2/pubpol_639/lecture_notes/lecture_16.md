## 2024-03-21

## Determining Causality
- OVB: Omitted Variable Bias
    - Omitted variable bias occurs when a model leaves out one or more important variables.
Example: Head Start Program
- participation is conditional on family income

### Dealing with OVB
- OVB causes problems because it generates a correlation between the treatment variable and the error term.
- this means that if we can control for other factors, we can (try) to eliminate the bias.

### dealing with OVB
- best way to deal with this is RCT
- work by eliminating the correlation between the treatment variable and the error term.
- we often cannot implement RCTs, so we need to use other methods to control for OVB.

### strategies for dealing with OVB
- find a treatment that is unrelated to unobservables (usually through some policy change that is quasi-random)
    - control for everything that might be correlated with the treatment and the error term.
- breaking the correlation between the treatment and the error term is key to claiming causality

### Fixed Effects
- can come in handy to address OVB when we think that the correlates between the treatment and unobserved factors are constant: time-invariant, across entities.

### Fixed Effects
- a trick that let's us control for fixed differences between groups is to put a dummy for each group in teh regression.
    - these are called "fixed effects"
- head start (currie and thomas, 1995)
    - control for fixed differences across families by including a dummy for each family (mother)
    - this only works if you have more than one observation per group
        - we have multiple kids in many families in our data (some hs, some not), which allows us to do family fixed effects.
- fixed effects control for unobserved and observed characteristics that are fixed (do not vary) within groups.
    - family (or mother) FEs control for unchanging family characteristics

### when does a FE model give you causal effects?
- when all the unobservables that are correlated with your X variable of interest (Head Start) are at the group-level and fixed.
- this is impossible to test
- credibility depends on context and assumptions

### Perspectives on FEs
- we have seen this already
    - including dummies across region = including region fixed effects
    - this controls for all (observed and unobserved) differences across regions
    - parameters of interest is identified from **within-region** variation
- mechanics are unchanged
    - still run OLS
    - inference is the same
    - works for continuous or discrete outcome and explanatory variables

Note: you cannot include both a FE and control variables that are constant within group
    - this would create perfect multicollinearity

### common uses of FEs
- state fixed effects
    - control for state-level differences
- year fixed effects

- common situation is to have multiple observations on the same unit over time
    - called "panel data"
    - e.g. states over time

### application: head start
- currie and thomas (1995)
    - data on children and their families

