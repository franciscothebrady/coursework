## 2024-02-20

### Agenda
- multiple binary variables
- perfect multicollinearity
- start non-linearity: polynomials

### last time
- who has the hardest time finding a job
- how does duration of employment vary with:
    - experience
    - age
    - sex
    - region

### regression with many dummy variables
interpret as the relative difference in the dependent variable between the reference category and the category of interest

### perfect multicollinearity
- often associated with:
    - regressors constructed from other regressors
    - lots of dummy variables (collectively exhaustive and mutually exclusive) + a constant term
    --> dummy variable trap
    - quirk of the data
- usually results from a conceptual error from how the regression is specified

### constructing binary variables from continuous variables
```stata
gen dropout = (educ < 12)
gen highsch = (educ >= 12 & educ < 15)
gen college = (educ >= 16)
```

Why would you do this?
- you may think there is not a linear relationship between education and the dependent variable

### a few approaches for modeling nonlinear relationships
- create categorical variables
- polynomials
- log transformations
- interaction terms

### Example: prenatal visits and birthweight
- prenatal visits: number of prenatal visits
- birthweight: weight of the baby at birth

### interpretation
- a straight line does not fit the data
    - at low levels, the relationship appears steeper
    - flattens out at higher levels
- observations are below the line of best fit at low and high levels and above it at medium levels
    - errors do not have a mean of zero

### Modeling nonlinear relationships
- there are many ways to model nonliner relationships in OLS, even though you'll hear OLS referred to as a linear model

### Adding indicators for each pre-natal visit
- this line fits the data better
- but the point estimates are not very precise

### Quadratics help
- relatxing the linearity assumption
- adding x^2 tot eh regression allows us to add curvature to the line without adding a ton of parameters
$$
birthweight = \beta_0 + \beta_1 \times visits + \beta_2 \times visits^2 + u
$$

- when we include both X and X^2 in the regression, we say that we have "included a quadratic term"
