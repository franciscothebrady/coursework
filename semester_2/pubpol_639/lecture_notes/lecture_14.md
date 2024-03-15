## 2024-03-14

### 2 continuous variables -- no interactions

specification:
$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u
$$

- allows application/enrollment ratio to differ with SAT rank
    - what is the change in app/enroll associated with a one unit increase in SAT rank (holding year constant)
- allows the application/enrollment ratio to differ with year/over time (linearly)
    - what is the change in app/enroll associated with a one unit increase in year (holding SAT rank constant)
- does NOT allow the relationship between app/enroll and time to differ between high/low SAT institutions

### 2 continuous variables -- with interactions

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1 x_2 + u
$$

- the relationship between app/enroll and time now depends on SAT rank (and vice versa)
    - what is the yearly trend in application/enrollment?

### Interpretation

- what is the yearly trend in applications per enrollment?
    - Change in App/Enrollment /Change in Time for SAT Rank = 1:
        - 0.24 + .0399 (1) == .064
        - coefficient on time + coefficient on interaction * SAT rank

### Summary
- interaction are another way that we can have the relationshpui between y and x vary with x (like polynomials, logs, etc)
- however, now we are letting the relationship between Y and X_1 vary with some other variables (X_2)

### Binary dependent variable

#### agenda
- binary dependent variables
    - linear probability model
    - limitations of LPM
    - logit and probit models

### binary dependent variables
- we have used dummy (binary) variables as explanatory variables
- now we will use dummies as dependent variables
- examples:
    - college attendance (yes == 1/no == 0)
    - mortality (yes == 1 if you die in 10 years, 0 if you don't)
    - policy support (yes == 1 if voted for X, 0 if did not vote for X)
- three (interchangeable) approaches to binary dependent variables
    - linear probability model
    - logit model
    - probit model

### application to the boston hmda data
paper: https://www.jstor.org/stable/2118254
- mortgages (home loans) are an essential part of buying the a home
- is there differential access to home loans by race
- if two otherwise identical individuals, one white and one black, apply for a home loan, is there a difference in the probability of denial?

### the hmda data set
- data on individual characteristics, property characteristics, and loan denial/acceptance

### example: mortgage denial and race (boston fed hmda data)
- individual applications for SFH mortgages made in 1990 in greater boston
- 2380 observations
- 1 dependent variable: denied (1 if denied, 0 if not)

### summary statistics
- 12% denied
- pi_ratio: mean debt to income ratio (higher means more debt)
    - 0.33 for entire sample
- black: 1 if applicant is black, 0 if not
    - 0.14 for entire sample
- married: 1 if applicant is married, 0 if not
    - ~0.61 for entire sample
- default: previous bankruptcy

### linear probability model
- a natural starting point is the linear regression model with a single regressor:
$$
Y_u = \beta_0 + \beta_1 X_u + u
$$

- when you run OLS with a binary dependent variable, it is called the linear probability model (LPM)

### LPM Interpretation
- when y is binary, the model $Y_i = \beta_0 + \beta_1 X_i + u_i$ is a probability
- $\hat{Y_i} = E[Y|X] = $ the predicted probability that Y_1 = 1 given X_i
- $\beta_1$ is the change in probability of Y = 1 associated with a one unit change in X
$$
\beta_1 = \frac{PR[Y=1|X+\DeltaX] - PR[Y=1|X]}{\DeltaX}
$$

### interpretation
- as always, \beta_k is the predicted change in $\hat{Y}$ given a 1-unit increase in X_k

### LPM: limitations
- direct extension of OLS
- does notn require any new methods
- interpretation of coefficients is quick
- we can get predicted probabilities outside of 0-1 range

### nonlinear models for binary dependent variables
- probit and logit are non-linear regression models to examine the relationship between binary dependent variables and predictors
- common in program evaluation

### probit regression
- probit models the probability that Y = 1 using the cumulative standard normal distribution function evaluated at z = \beta_0 + \beta_1 X

- Pr(Y = 1|X) = \Phi(\beta_0 + \beta_1 X)
- where \Phi(z) is the area under the standard normal density function to the left of Z
- Z = \beta_0 + \beta_1 X is the z-value or z-index of the probit model

pros: bounded by [0,1]
con: harder to interpret the coefficients

### estimating probit and logit models
- not typically estimated by minimizing the sum of squared residuals
- instead they are maximum likelihood estimators (MLE)
- there is no "closed" form or "analytical" solutions, so one must use an iterative "optimization" algorithm to find the MLE

### Interpreting probit coefficients
- probit coefficients \beta_0 and \beta_1 are not directly interpretable
- \beta_1: change in the z-score associated with a x-unit change in X
- signs and statistical significance are interpretable
- the model is best interpreted by computing predicted probabilities to see how \hat{Y} when X changes

