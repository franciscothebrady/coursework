## 2024-03-19

## binary dependent variables II
- for next time: read the paper before class

### today
- binary dependent variables
    - probit
    - logit

### nonlinear models for binary dependent variables
- probit and logit are non-linear regression models to examine the relationship between a binary dependent variable and one or more independent variables (predictors)
- common in program evaluation
- important to be able to interpret the results of these models

### probit
- models that probability that Y = 1 using the cumulative stnadard normal distribution function evaluated at $z = \beta_0 + \beta_1X$
- $Pr(Y = 1|X) = \Phi(\beta_0 + \beta_1X)$
- $\Phi(z)$ is the area under the standard normal density function to the left of z
- $z = \beta_0 + \beta_1X$ is the linear predictor of the model

### interpreting probit coefficients
- probit coefficients $\beta_0$ and $\beta_1$ are not directly interpretable
    - $\beta_1$: the change in the z-score associated with a one-unit change in X
- signs and statistical significance of the coefficients are interpretable
- the model is best interpreted by computed predicted probabilities to see how $\hat{Y}$ changes as X changes

```stata
probit deny pi_ratio, r
```

### interpreting probit coefficients, 2
Steps:
1. calculate predicted probability of Y = 1 for a given value of X
- $\hat{Y} = \Phi(\hat{\beta_0} + \hat{\beta_1}X)$
2. change your X of interest by one unit
3. calculate the predicted probability of Y = 1 for the new value of X
4. subtract the new predicted probability from the original predicted probability

#### marginal effects
- you can calculate the marginal effect from the model using the means of the independent variables

### pro-bits
pros:
- gaining ability to model non-linear relationships
- never passes 1 or 0 in predicted values
cons:
- difficult to interpret coefficients

### probit with multiple predictors
- need to specify values of the other explanatory variables to calculate predicted change

### LPM vs. probit (and logit)
- how concerned should we be with predicted values -- i.e. E[Y|X]?
    - outside the range 0/1
- there are many cases i nwhich OLS with a continous outcome can produce E[Y|X] with implausible values
- oftern we are not interested in predicted values, but rather the change in Y associated with a change in X
    - LPM can often estimate these slopes correctly
- LPM will tend to get the slope and predicted probabilities correct for Xs near the mean.
    - close to the mean: little difference between the lpm, binary, logit
    - depends on how non-linear the model is

### measure of fit with binary outcomes 
- fraction correctly predicted
    - if yhat >.5 and y = 1, then correct prediction
    - if yhat <.5 and y = 0, then correct prediction
- pesudo R-squared
    - compares value of likelihood function with no predictors versus all predictors in the model

### logit
- logit model is similar to probit facter except is uses the logistic distribution function

### interpreting logit coefficients
- one can calculate the marginal effect of Y 

### probabilities on odds
- the odds ratio
- the odds of an event occurring (Y = 1), is the probabilty of the event occurring divided by the probability of the event not occurring

### logit
- the logit model is a linear model for the log odds of the dependent variable
