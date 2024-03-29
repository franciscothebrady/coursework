## 2024-03-28

### Difference in Differences

- **Difference in Differences** (DiD) is a method to estimate the causal effect of a treatment on a treatment group compared to a control group.
- one of the most often used "quasi-experimental" methods in economics
- we want to evaluate the effect of some "Treatment"
    - having a high minimum wage
    - participating in local EITC program
    - etc
- but "treatment" is not randomly assigned
    - simple outcome difference between treatment and control groups may suffer from omitted variable bias
- DiD approach compares the before/after change in outcomes for the treatment group to the before/after change in outcomes for the control group
- requires data on the treatment group and a plausible control group both before and after the treatment

### Simple Difference
- measures difference in outcome between groups that received and did not receive a program at the same point in time. (i.e., after the program has been implemented)

**assumption:** intervention and comparison group would have the same outcome in **in the absence of the program/treatment**

- **source of bias:** we don't know what the change in outcome would have been in the absence of the program (a lot of other things might have changed as well)

- limitation: treatment and control groups may be systematically different in ways that are not observed

### pre-post difference
- compare outcomes of the same group both before and after the treatment


### How does DD method improve on this

- combines 'pre-post' and 'simple difference' by comparing the change in outcome over time between intervention and comparison groups

- requires a 2x2 panel dataset
    - one treatment group and one control group
    - one observation before the treatment and one afterwards

### difference in differences visual

| Group       | Before  | After |
|-------------|-------- |-------|
| Treatment   | T1      | T2    |
| Control     | C1      | C2    |
| Difference  | T1 - C1 | T2-C2 |

### pre-post difference

| Group       | Before  | After | Difference |
|-------------|-------- |-------|------------|
| Treatment   | T1      | T2    | T2 - T1    |
| Control     | C1      | C2    | C2 - C1    |

- pre-post is potentially biased bewcause we don't know what the time trend in the outcome looks like in absence of the program.

Card/Krugman (1994) - NJ was experiencing a recession at the time.

### Difference in Differences
Subtract out the time trend in the comparison group:
(T2 - T1) - (C2 - C1)

| Group       | Before  | After | Difference |
|-------------|-------- |-------|------------|
| Treatment   | T1      | T2    | T2 - T1    |
| Control     | C1      | C2    | C2 - C1    |

### implementing a diff-in-diff

- panel data on entities that either do or do not receive treatment both before and after the treatment takes place.

- simplest version:
$$
Y_{it} = \beta_0 + \beta_1 Post_t + \beta_2 Treat_i + \beta_3 Post_t \times Treat_i + \epsilon_{it}
$$

Where:
    - $Y_{it}$ is the outcome variable for entity i at time t
    - $Post_t$ is a dummy variable for all time periods AFTER the treatment has happened
    - $Treat_i$ is a dummy variable for all entities that receive the treatment
    - $Post_t \times Treat_i$ is the interaction term for all treatment observations after the treatment has happened
    - **$\beta_3$** is the estimated effect of the treatment

#### notation
- another way to represent this:
$$
Y_{it} = \lambda_t + \gamma_i + \beta_3 Treat_i \times Post_t + \beta_4 X_{it} + \epsilon_{it}
$$

Where:
    - $\lambda_t$ is a year fixed effect
    - $\gamma_i$ is an entity fixed effect
    - $X_{it}$ is a vector of control variables

### Card and Krueger (1994)
- increase in minimum wage in NJ in April 1992
- compared fast food restaurants in NJ and PA

- in the framework above:
    - $Y_{it}$ is employment
    - $Post_t$ is a dummy for after the minimum wage increase
    - $Treat_i$ is a dummy for NJ
    - $Treat_i \times Post_t$ is the interaction term for being in NJ after the minimum wage increased.

### DiD as a fixed effected model
- wre can use our entity and time fixed effects model to study this:
$$
Y_{ist} = \gamma_s + \lambda_t + \delta D_{st} + \epsilon_{ist}
$$

Where:
    - $Y_{ist}$ is employment at restaurant i in state s at time t
    - $\gamma_s$ is a state fixed effect
    - $\lambda_t$ is a time fixed effect
    - $D_{st}$ is a dummy for being in NJ after the minimum wage increase
        - $D_{st} = 1$ if $s = NJ$ and $t = Apr$


### Interpretation

$$
E[Y_{ist} | S = PA, t = Nov ] - E[Y_{ist} | S = PA, t = Feb] = \lambda_{Nov} - \lambda_{Feb} \\

E[Y_{ist} | S = NJ, t = Nov ] - E[Y_{ist} | S = NJ, t = Feb] = \lambda_{Nov} - \lambda_{Feb} + \delta \\

$$

## Results table

|           | PA    | NJ    | Diff  |
|-----------|-------|------ |-------|
| FTE Before| 23.33 | 20.44 | -2.89 |
| FTE After | 21.17 | 21.03 | -0.14 |
| Diff      | -2.16 | 0.59  | 2.75  |

Conclusions:
- employment fell in PA and rose in NJ

### Key assumption: Common Trends
or parallel trends assumption
- the treatment and control groups would have followed the same trend in the absence of the treatment
- this is a strong assumption
- card and krueger only used one pre-period

### Other findings
- no effect on number of full-time vs. part-time workers
- no evidence of decline in fringe benefits
- passes the placebo test -- no effect on employment in PA restaurants paying < $5.05 an hour.

- So how did NJ fast food restaurants offset the increased cost of labor?
    - increased prices
    - measured change in log price of a full meal

### DiD summary
- this is probably the most common program evaluation method in economics
- easy to implement using group and time fixed effects
- much more convincing if you can show that the trends between treatment and control groups were parallel before the treatment
- easy to generalize to multiple time periods, multiple treatment groups, and policy changes that happen at different times for different groups

### Two Main Threats to DiD
1. Continuation of pre-trend differences between treatment and control groups
    - Potential solution: find another control group to test whether results are similar
    - potential solution: look at pre-treatment differences between treatment and control groups
2. other "Treatments" or events or policy changes that occurred at the same time **that disproportionately affect the treatment group, and not the control group**
    - potential solution: control for other factors changing at the same time (year fixed effects will address this to some extent)
    - potential solution: investigate whether other policy changes occurred at the same time.



