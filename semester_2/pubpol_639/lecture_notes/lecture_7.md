## 2024-02-01

### agenda
- homoskedasticity
- bivariate regression when X is binary
- intro to multiple regression

### back to assumption #2 of OLS
- the distribution of the error terms in the regression have implications for statistical inference
    - ban make a big difference in practice
- homoskedasticity:
    - if the variance of u (error term) is the same for all values of X, then u is said to be homoskedastic
    - you may also see this referred to as constant variance
    - the variance does not change with (depend on) X, so u is homoskedastic
    - var[u | X_i = x] = \sigma^2
- statistical packages assume this by default
- if the variance of u **depends** on X, so u is heteroskedastic

### how heteroskedasticity inflouences statistical inference in a refression
- OLS assumes errors are homoskedastic
    - in reality, errors are often heteroskedastic
- there is a slightly different way to calculate standard errors that provides an inbiased s.e. estimate
    - often called "robust" standard errors. easily generated and reported by all software packages
    - will not influence regression coefficients, but will influence the standard errors and thus the t-statistics and p-values.
- the upshot: always use heteroskedasticity-robust standard errors
    - in Stata, use the `robust` option
    - in R, use the `vcovHC` function in the `sandwich` package

### heteroskedasticity-robust standard error of beta_1
- just as we calculated the standard error of sample mean of difference in means, we can calculate on for beta_1
- the formula is a bit complicated, but it's easy to calculate in software

### summary of statistical inference:
- estimation
    - OLD estimators beta_0 and beta_1
    - beta_0 and beta_1 have a normal sampling distribution in large samples
- testing
    - h_0: beta_1 = a vs h_a: beta_1 != a

### Rregression when X is binary
- qualitative information is often captured by a binary variable, commonly called a dummy variable

x = 1 if received treatment, 0 if control
x = 1 if elderly, 0 if not
etc

### difference in means
- for binary variables, you can use a t-test to compare differences
- you can also use a regression to compare differences
    - the coefficient on the binary variable is the difference in means
    - the standard error of the coefficient is the standard error of the difference in means
    - the t-statistic is the t-statistic for the difference in means
- constant is meaningful in this context: it is the mean of the group coded as 0

### summary: regression when X is binary
- for X = 0 (ommited group)
- Y_i = \beta_0 + \beta_1(0) + u_i
- --> Y_i = \beta_0 + u_i

- for X = 1 (treatment group)
- Y_i = \beta_0 + \beta_1(1) + u_i
- --> Y_i = \beta_0 + \beta_1 + u_i

Therefore:
- \beta_1 = E[Y_i|X_i = 1] - E[Y_i|X_i = 0]

- standard eror of estimator has the usual interpretation
- t-statistics, CI's constructed in the usual way
- easy way to do a difference in means analysis
- this aproach is useful when we have multiple regressors

### Causal questions
- the bivariate regression (one x, one y) cannot (usually) answer causal questions
- multiple regressions get us one step closer to answering causal questions
- helps address concerns that there may be other variables that are confounding the relationship between X and Y

### multiple regression
- it is more plausible that X causes Y if we can control for other variables that might be confounding the relationship
- "taking things out of the error term"

### multiple regression
$$
Y_i = \beta_0 + \beta_1X_{1i} + \beta_2X_{2i} + ... + \beta_kX_{ki} + u_i
$$

- Y_i: dependent variable
- X_{1i}, X_{2i}, ..., X_{ki}: independent variables
- \beta_0: unknown population intercept. the expected value of Y_i when X1i = 0 and X_2i = 0, etc
- \beta_1 = effect of Y on a change in X_1, holding X_2 constant
- \beta_2 = effect of Y on a change in X_2, holding X_1 constant

### OLS estimator in multiple regression
- with two regressors, the ols estimator solves the following minimization problem:
$$
\min_{\beta_0, \beta_1, \beta_2} \sum_{i=1}^n (Y_i - \beta_0 - \beta_1X_{1i} - \beta_2X_{2i})^2
$$

