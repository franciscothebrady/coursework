## Linear regression, pt 2
2023-11-20

### recap

#### linear regression 
- x helps us understand the value of y 
- we are specifying the relationship between the two to be linear
- we've already measures the correlation using the correlation coefficient
- linear regression will show us the magnitude of the relationship 
- dependent variable is interval-level. the independent variables are interval-level or dichotomous. 

### bivariate linrear regression

> the "real" model 
- because it's using population parameters, not samples

$$
y_i = \beta_0 + \beta_1 x_i + u_i
$$

$u_1$ is the part of each $y_i$ that is stochastic. we model it as drawn from the normal distribution with a mean of 0 and variance $\sigma^2$. 
- these assumptions allow us to estimate standard errors.  

### what we estimate 

$$
\hat{y_i} = \hat{\beta_0} + \hat{\beta_1} x_i
$$

- we estimate the $\beta$ 
- $\hat{y_i}$ is mathematically determined by the $\hat{\beta}$ and $x_i$
- the difference between $y_i$ and $\hat{y_i}$ is the "miss", or the error.

$$
y_i - \hat{y_i} = \hat{u_i}
$$

- we use these prediction errors to estimate the variance of $u_i$, in other words $\hat{\sigma_{u}^2}$

## example

$$
\hat{\text{infmort}} = 167.3 - 1.5 \text{water}
$$

- generic: for each [one-unit] increase in [water], infmort is predicted to be 1.5 [units] lower. 
> don't use only generic interpretation 

- substantive: for each percentage point increase in the population with access to improved water, we predict 1.5 fewer infant deahts out of every 1000 births.  

### interpretation  
$$
\hat{\text{infmort}} = 167.3 - 1.5 \text{water}
$$

- the predicted infant mortality rate in a country with no access to improved water sources would be 167.3  

### statistical significance  
- regression output reports some combination of stqandard errors, t-statistics, p-values, and 85% confidence intervals. 
- standard error of $\hat\beta$ is interpreted as the typical deviation of $\hat\beta$ from the "true" $\beta$ across samples.

- the formula for the standard error in bivariate regression requires some explanation.  
-  this gets more complicated when we add more independent variables (beyond our scope)  

### the sampling distribution for $\hat\beta_1$  
- across repeated samples, the estimated coefficients will vary -- they have a samlping distribution 

- knowing the size of that distribution is important.  
- we want tools to; 
    - quantify the sampling uncertainty associated with $\hat\beta_1$
    - use $\hat\beta_1$ to test hypotheses, such as $H_0: \beta_1 = 0$
    - construct a confidence interval for $\hat\beta_1$

- the sampling distribution of $\hat\beta_1$ is normal and centered upon the true population regression slope $\beta_1$.
- the standard deviation of this distribution is the standard error of $\hat\beta_1$, which is $\sigma_{\hat\beta_1}$. We need to estimate this standard error.  

### the standard error of $\hat\beta_1$

_ if key assumptions hold, the true standard error of $\hat\beta_1$ can be expressed as:  

$$
se(\hat\beta_1) = \sigma_{\hat\beta_1} = \frac{\sigma_{u}^2}{\sqrt{\sum (x_i - \bar{x})^2}}
$$

- just like the standard error for the sample mean, however, we must estimate the standard error for $\hat\beta$:  

$$
est. se(\hat\beta) = \hat\sigma_{\hat\beta_1} = \frac{\frac{1}{n-2}\sum\hat{u_i}^2}{\sqrt{\sum (x_i - \bar{x})^2}}
$$

### interpreting the standard error of $\hat\beta_1$

- the standard error of $\hat\beta_1$ is the typical deviation of $\hat\beta_1$ from the true $\beta_1$ across repeated samples.
- represents our estimated amount for which the estimated beta will vary from the true beta across repeated samples.
- it thus measures our level of precision and provides the basis for constructing a confidence interval. 

- degrees of freedom = our sample size - the number of coefficients being estimated in the model (including the intercept/constant)

### testing hypothesis in OLS

- null hypothesis: true value for the slope ($\beta$) is = 0. x is useless! 

- the tests follow the usual form:  


