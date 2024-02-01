## 2024-01-30

### Example: Avg Income and Test Scores
- how might income be related to test scores
- do we think the relationship is positive, negative, or no relationship?

### Reading regression table:
- $\beta_1$ is the estimate
- t is the t-statistic
- `_cons` is the intercept

### measures of "fit"
- how well does our regression lline "fit" or "explain" the data?
-- $R^2$ is the statistic that helps answer this question

- $R^2$ is the share of the variance in the dependent variable (Y) that is explained by the independent variable (X)
    - $R^2$ is between 0 and 1
    - $R^2$ = 1 means that the regression line perfectly fits the data
    - $R^2$ = 0 means that the regression line does not fit the data at all
- SW discuss another measure called SER (Standard error of the regression)
    - this is the standard deviation of the error terms
    - less commonly used, will not discuss in class

### Calculating $R^2$
- recall that:
    y_i = \hat{y_i} + \hat{u_i where \hat{y_i} = \hat{\beta_0} + \hat{\beta_1}x_i
    = OLS prediction + OLS residual
    = what we explain + what we don't explain
- we can use this equation to decompose the variance of Y:
    - Var(Y_i) = var(\hat{y_i}) + var(\hat{u_i})
    - var(y_i) - Total Sum of Squares (TSS)
    - var(\hat{y_i}) - Explained Sum of Squares (ESS)
    - var(\hat{u_i}) - Sum of Squared Residuals (SSR)

TSS = ESS + SSR
1 = ESS/TSS + SSR/TSS
Define: R^2 = ESS/TSS = 1 - SSR/TSS

### calculating $R^2$ 
- definition of $R^2$:
    - $R^2$ = ESS/TSS = 1 - SSR/TSS
$$
R^2 = \frac{\sum_{i=1}^n (\hat{y_i} - \bar{y})^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
$$
Or equivalently:
$$
R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y_i})^2}{\sum_{i=1}^n (y_i - \bar{y})^2}
$$

### stata and $R^2$
- stata reports $R^2$ as "R-squared" in the regression output
- example:
    - R-squared = 0.0512
    - this means that 5.12% of the variance in test scores is explained by student-teach ratio
### what is a "large" $R^2$?
- depends on the context
- R-squared measures the importance of the explanatory variable we model relative to the importance of other factors.
- If R-squared is low, then there are other important factors influencing the outcome
- Models of human behavior tend to have low R-squared because there are many things people do that we cannot well explain (or model)

### R-squared and causation
- R-squared is not informative about causation
- can have high R-squared even if there is no causal relationship
- can have low R-squared even if there is a causal relationship

### the least squares assumptions
- under what conditions is OLS an unbiased estimator of the true population parameters?
- to answer this, we need to make some assumptions about how Y and X are related to each other, and about how our sample is collected

### bias
- recall: we are looking for an unbiased estimate of the population parameters $\beta_0$ and $\beta_1$
- unbiased means that our estimate equals the true value in expectation: E(\hat{\beta_1}) = \beta_1

### the least squares assumptions
1. the conditional distribution of u given X has mean zero, that is E(u|X = x) = 0
    - this implies that \hat{\beta_1} is unbiased
2. (X_i, Y_i), i=1, ..., n are i.i.d (independent and identically distributed)
     -this is true is X,Y are collected by simple random sampling
     - this delivers the sampling distribution of \hat{\beta_0} and \hat{\beta_1}
3. large outliers of X and Y are unlikely

### the least squares assumptions #2: i.i.d
- observations are uncorrelated with each other
- this arises automatically if the entity is sampled by simple random sampling: the entity is selected then, for that entity, X and Y are observed.
- the main place we will encounter non-i.i.d sampling is when we sample time series data
    - in this case, we will need to use time series methods to estimate the parameters

### the least squares assumptions #3: outliers
- outliers in the Y dimension can serve as anchor points
- can affect regression line

### the least squares assumptions #1: E(u|X=x) = 0

- We expect that the error term is uncorrelated with the X variable

Example: Health Insurance Concerns
- Is age or current income a better predictor of expectations for health insurance coverage?
- Health insurance expectations and age regression:
$$
ExpHealthIns+_i = \beta_0 + \beta_1 Age_i + u_i
$$
- OLS assumes E[u_i|Age_i] = 0
- But what about income?

### Violating LSA #1: E(u|X=x) = 0
- Income and Age are more correlated than income and expected health insurance!
- this tells us that a regression of expected health insurance on age will **have income incorporated into the error term**

