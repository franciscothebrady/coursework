## 2024-02-15

### Stats in the wild
Pew on changing use of technology in polls.
Surveys were administered by phone but are increasingly responding to online surveys.

Angus Deaton: Randomization in the Tropics (2020)
- RCTs require a different kind of statistical thinking.
- RCTs do not inherently imply causality, and there can be issues in implementation and follow-up.

### Revisiting Dummy Variables!

Agenda:
- revisiting categorical variables
    - unordered categorical variables
    - categorical variables from continuous variables

### Interpreting Coefficients when there are multiple categorical variables in a regression

Research Question: Who has the hardest time finding a job?
- how does the duration of unemployment vary
    - by experience
    - by gender
    - by region
- purely descriptive but may be useful

### Data
From 2009 Current Population Survey (CPS)
- only currently unemployed individuals 26+
- key outcome variable: duration of unemployment

### Regression w/ continuous and dummy explanatory variables

$$
\text{duration} = \beta_0 + \beta_1 \text{female} + \beta_2 \text{experience} + u_i
$$

### Multiple Dummy Variables
- many quantitative variables have more than two categories
- for some, no ranking
    - region
    - race
    - industry
- for some, correspond to some ranking
    - education
         - high school dropout, high school graduate, college graduate
    - occupation

### Analyzing categorical variables

- easy to generate summary statistics by region

```stata
tab region, sum(durunemp) wrap
```

### Warning: Do not do this

- do not include categorical variables in regressions as continuous variables
- this will not give you meaningful results

### What do do: Create dummy variables
- create a dummy variable for each category (for example, regions)
- they should be mutually exclusive

```stata
gen region1 = (region == 1)
gen region2 = (region == 2)
gen region3 = (region == 3)
```

### Regression with many dummy variables
Note: You need to leave out one of the dummy variables to avoid perfect multicollinearity.
- this is called the reference category

```stata
reg durunemp female experience region2 region3
```

- interpreting the constant: the expected duration of unemployment for those in the reference category (region 1)
- interpreting experience (continuous): the expected change in duration of unemployment for a one year increase in experience, NOT relative to the reference category, because we are holding everything else constant.

### Are differences between regions statistically significant? (holding sex and experience constant)
There is a way to test this using the F-test (in Stata)
Null hypothesis: there are no differences in the expected duration of unemployment between the regions.
Alternative hypothesis: there are differences in the expected duration of unemployment between the regions.
(Do not include ommitted category in the test.)
```stata
test r_newengland r_midatlantic r_enorthcentral r_wnorthcentral r_southatlantic r_esouthcntral r_wsouthcentral r_mountain
```
Interpretation: None of them are statistically different to the omitted category.

Output:
```
    ( 1)  r_newengland = 0
    ( 2)  r_midatlantic = 0
    ( 3)  r_enorthcentral = 0
    ( 4)  r_wnorthcentral = 0
    ( 5)  r_southatlantic = 0
    ( 6)  r_esouthcntral = 0
    ( 7)  r_wsouthcentral = 0
    ( 8)  r_mountain = 0

         F(  8,  4472) =    3.55
                Prob > F =    0.0004
```
- Result: Can reject the null hypothesis that there are no differences in the expected duration of unemployment between the regions.

### What happens when you include all of the region dummy variables?

```stata
reg durunemp female experience region1 region2 region3 region4 region5 region6 region7 region8
```
Output:
```
note: region1 omitted because of collinearity
```

### Perfect Multi-collinearity

- when one of the refressors is an exact function of the other regressors (a linear combinatsion)
- example: include potential experience, age, and schooling in the same regression

- often associated with:
    - regressors constructed from other regressors
    - lots of dummy variables (collectively exhaustive, mutually exclusive) + a constant
    --> "dummy variable trap"
    - quirk of the data

### Imperfect Multi-collinearity
- imperfect and perfect multicollinearity are very different
- imperfect multicollinearity occurs when two or more regressors are highly correlated
- if two regressors are very highly correlated, it can be difficult to disentangle their effects
- imperfect multicollinearity implies that one or more of the regression coefficients will be imprecisely estimated

intuition: the coefficient on X1 is the effect of holding X2 constant, but if X1 and X2 are highly correlated, there is very little variation in X1 when X2 is held constant.

### Dummies from continuous variables

- sometimes may be more meaningful to compare dropouts to college graduates (indicators) and not years of education (continuous)

