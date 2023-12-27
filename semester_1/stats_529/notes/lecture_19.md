## lecture 19: Linear regression 

### recap 
- pearson's R correlation coefficient measures the strength and direction of the relationship betwee two interval-level variables. 

### linear regression 
- fits dependent variable (y) as a linear function of the independent variable (x)
- extends to multiple variables 

### linear functional form 

$$
y = a + bx
$$

two basic parameters: 
- intercept (a): the point at which the line drawn crosses the y-axis. 
- slope (b): the amount by which y changes when x increases by 1 unit.

### example

$$
\hat{y_i} = 10.81 + 0.81x_i
$$
Note: $\hat{y_i}$ is the predicted value of $y_i$ given $x_i$. It is on the line. 
$$
\hat{y_i} = 10.81 + 0.81x_i + \hat{u_i}
$$
The different between $y_i$ and $\hat{y_i}$ is the prediction error $\hat{u_i}$.

### key points 

$$
\hat{y_i} = 10.81 + 0.81x_i
$$
$$
\hat{u_i} = 10.81 + 0.81x_i + \hat{u_i}
$$

- best-fit line is $\hat{y_i}$, the estimated of predicted value of y for a given level of x.
- for each one-unit increase in x, the estimated value of y rises by .81. 
- the prediction error (\hat{u_i}) is also called the residual. It is the vertical distance between y and $\hat{y}$.

### additional points

- when b is positive, y tends to increase as x increase 
- when b is negative, y tends to decrease as x increases
- when b is 0, there is no linear relationship between x and y.
- b is measured in the same units as y. it provides the magnitude by which y is expected to change as x changes.  

### general approach of linear estimation  
- we can think of the dependent variable y as being produced by systematic and stochastic factors.  
- with bivariate regression we model this systematic part of y as a linear function of x 
- this model may not be correct! the true relationship may not be linear, or x may not be related to y. 
- we estimate the regression to examine the fit of the model to the data.

### bivariate linear regression model 

$$
y_i = \beta_0 + \beta_1x_i + u_i
$$

the relationship between y and x is specified by the "true" population parameters: $\beta_0$ and $\beta_1$, and $u$.  
- $\beta_0$ is the intercept. It is the value of y when x is 0.
- $\beta_1$ is the slope. or the coefficient of x. It is the amount by which y changes when x increases by 1 unit.
- $u_i$ is the part of $y_i$ that is stochastic/random. It is unobserved and unknown.  

### what we estimate: the TRUE regression model 

$$
\hat{y_i} = \hat{\beta_0} + \hat{\beta_1}x_i
$$

with linear regression, we estimate the $\beta$ parameters. these produce the intercept and slope of the best-fit line.  
- $\hat{y}$ is determined mathematically by the $\beta$'s and x. The regression list depicts $\y$ across the values of x.  
- the difference between $y_i$ and $\hat{y_i}$, which is the prediction error, represents our best guess at $u_i$ for each observation.  

### estimating the $\beta$'s 

regression involves the values of beta that will minimuze the **sum of the squared deviations between y and x**. 

- for each observation i out of n in our sample, the squared deviation between $y_i$ and $\hat{y_i}$ is:
$$
(y_i - \hat{y_i})^2
$$
- we can called these squared deviations the "squared errors". The sum of the squared errors (SSE) across all n items in teh sample is thus:  

$$
SSE = \sum_{i=1}^n (y_i - \hat{y_i})^2
$$

- the best fit minimizes this sum.  

## minimizing the sum of the squared errors  

