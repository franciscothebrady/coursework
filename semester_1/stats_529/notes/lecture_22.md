## Linear Regression, part 3

### dichotomous independent variables  
- dichotomous variables can be used to represent a category 
- the value of 1 represents membership in that category 
- the value of 0 represents non-membership in that category
- commonly known as dummy variables  

### interpreting dummy variables  
$$
y_i = \beta_0 + \beta_1 Dummy_i + u_i
$$

- the intercept is used to calculate the value of y for all members in the sample 
- mathematcially, when the dummy variable is 1, $\beta_1$ is relevant. When the dummy variable is 0, $\beta_1$ is cancelled out.
- accordingly, $\beta_1$ represents the **effect** of membership in the category on the value of y  
- on **average**, members of the category would differ on y by the amount $\beta_1$. It is similar to a difference of means!  


### changing the base category 
- with any dichotomous variable, the category coded as 0 serves as the base category in a regression 
- the estimated coefficient on the variable indicated the difference versus that base  
- if we switch which category is the base, the coefficient just flips it's sign (+/-)

### key OLS assumptions 

$$
y_i = \beta_0 + \beta_1 x_i + u_i
$$

- if certain assumptions hold, then Ordinary Least Squares (OLS) is the best linear unbiased estimator (BLUE) 
- there are other possible estimators, such as minimizing the sum of absolute deviations between $\hat{y_i}$ and $y_i$ 
- the OLS estimator has the minimum variance among these estimators when the assumptions hold.  

### assumption 1: conditional mean of $u$ is 0  
$$
E[u_i|x_i] = 0
$$
- given value of x, u is uncorrelated with y. 
- on other words, there are no variables ommitted from the model (there is no ommitted variable bias)
- if this assumption does not hold, our $\hat{\beta_1}$ will be biased.
- there is no easy solution for this  

solution: identify the missing variables and bring them into the model  
> if you can't find any missing variables, you are stuck with biased estimates!!!

### assumption 2: data are i.i.d 
#### the data are independent and identically distributed  
- each observation is independenct of all other cases  
- all observations come from the same distribution  
- this is violated when there are connectioned between members of the sample. (e.g. students in the same school, individuals in the same household) 
- time series data violates this assumption  
- it is also violated if, for exmaple, each $x_i$ does not come from a distribution with the same mean and variance.  
### consequence of violations of assumption 2
- main consequence is that our estimated standard errors will be biased  
- there are straightfoward sollutions: we can use different formulas for the standard errors. 
- e.g. robust or clustered standard errors or corrections for serial correlation (over time) in the errors. 
 -we will learn about roduct standard errors in the next lecture. clustered standard errors will come on the next course.  

 ### assumption 3: large outliers unlikely  
 - outliers are most problematic when y is unusual given $x_i$ 
 - to see the impact, we can drop the outlier and resomes foras 
 - BUT: it may be3 tempting to just eliminate outliers, but **we need a good reason to do so**.
 e.g. it may be an error in recording the data or the case does not belong in the sample. 

 ### assumption 4: the error term u is homoskedastic

heteroskedasticity: the variance of u **does** change with, or depend on x. 
- this is a violation of assumption 4, variance of u is greater when x is larger. 

### consequences of heteroskedasticity
- the estimator for $\beta_1$ is still unbiased, but OLS is no longer efficient 
- the usual formula for the standard errors is invorrect. we get biased estimates of the standard errors. 
- to adjust for this, we can use a formula for "robust" standard errors.
- there is no harm to using robust standard errors

### robust standard errors 
- there are several formulas for robust standard errors, Stata and R use different formulas by default. 
- Stata defaults to a formula called "HC1", while R defaults to a formula called "HC3"
- the HC3 standard errors are more conservative and may be preferable, especially when n < 250. 
- there is little difference once n >= 500.  
