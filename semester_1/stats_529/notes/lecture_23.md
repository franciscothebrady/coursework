## linear regression pt. 4 

### recap: key old assumptions 

1. conditional mean of $u$ is zero: $E[u_i|x_i] = 0$
- if this isn't the case, then there is some additional thing that we haven't accounted for. 
- what this is telling us is that our model is *not complete*
- this problem is called **omitted variable bias**  
- our coefficient on our included variable is likely biased
- solution is to bring in the ommitted factors -- this may or may not be possible
2. data are independently and identically distributed 
- treating all cases in our sample as unconnected to any other cases in our sample.
- this will be violated when we are considering groups. 
- this implies that the random error has some systematic aspect to it. 
- an example is geographic components affecting each other, i.e. the unemployment rate in one county affecting the unemployment rate in another close-by county.
- the result of this is that our standard errors are biased.
- solution is to use **clustered standard errors**.

3. large outliers are unlikely 
- prompt to evaluate whether there is measurement error 
- may indicate that you need to bring in another model 
- last resort is to drop the outlier, but you should have a strong reason to do so. 

4. the error term ($u$) is homoskedastic
- all random stochastic disturbances have the same variance. 
- one solution to this is to use robust standard errors to account for this. 

It is important to understnad these assumptions, the consequences when they are violated, and what can be done to address the violations. 

### what can we do? 

- an outlier is a violation of OLS assumptions, and could cause our coefficients to be misleading 
- but we cannot just drop 
- solutions: think about the situation, it could we that there are missing variables 
- is there measurement error? 
- we MAY drop if we decide that it doesn't belong in the same population as our population of interest. 

### heteroskedasticity

- we can test for heteroskedasticity using a breusch-pagan test
- the null hypothesis is homoskedasticity (no heteroskedasticity)
- if we reject the null hypothesis, we need to take measures to address the bias in our standard errors.

### testing for heteroskedasticity
Stata
```
// after running the regression
estat hettest, iid
```
R
```
library(lmtest)
bptest(model)
```
the test returns a test-statistic and p-value. if p < $\alpha$ then we reject the null hypothesis of homoskedasticity.  

