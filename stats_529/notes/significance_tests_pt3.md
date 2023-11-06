## outline: oct 11, 2023  

## preliminaries  
significance tests involving proportions  
-  for larger samples, z statistics are appropriate. the sampling distribution of $\hat{p}$ is approximately normal.    
-  rule of thumb: at least 15 cases per categroy  
-  the formula for the standard error uses $\pi_0$, the value of the population proportion specified by the null hypothesis.  

$$
se = \hat{\sigma}_{\hat{\pi}} = \sqrt{\frac{\pi_0(1-\pi_0)}{n}}
$$

> OJO: this is using the null hypothesis, not the sample proportion.  

### standard errors for proportions  
note this is different than the formula for confidence intervals, which uses the sample proportion.  

### 1. state your assumptions  
we are dealing with large enough samples that we can use the normal approximation. 
- a z statistic is appropriate.  

### 2. state hypothesis 
suppose the true hypothesis is .40  
$H_0$: $\pi = 0.40$  
$H_a$: $\pi \neq 0.40$  

### 3. calculate the test statistic  

assume $\alpha = 0.05$ , so the z-critical value is 1.96.  
- the difference between $H_0$ and our point estimate is measures in standard errors:  
$$
z = \frac{\hat{\pi} - \pi_0}{\hat{\sigma}_{\hat{\pi}}} = \frac{0.41 - 0.40}{\sqrt{\frac{0.40(1-0.40)}{5,884}}} = \frac{.01}{.006} = 1.67
$$

### 4. calculate the p-value  

-  our z statistic is 1.67, which falls short of the critical value.  
-  the p value is the probability of getting a sample proportion at least 1.67 standard errors away from the null hypothesis (.40), in either direction, **assuming $H_0$ is true**.  

-  using the z-table, the right hand tail for z = 1.67 is .0475. this makes the p-value = .0475 * 2 = .095.  

on the problem set:
- what would need to be true, in order for our confidence interval to not give us the true value.  

### conclude  
- since p > $\alpha$, we cannot reject $H_0$.  
-  we could also see this by comparing the z statistic 

### small sample tests with proportions  

-  sample proportions are highly discrete at small sample sizes.  
e.g proportion of heads vs. tails with 5 tosses.  
if n = 5 and x = the number of heads, then $\hat{\pi}$:  

$$
\hat{\pi} = \frac{x}{n} = \frac{0}{5}, \frac{1}{5}, \frac{2}{5}, \frac{3}{5}, \frac{4}{5}, \frac{5}{5}, \text{or } 1
$$

### small sample tests for proportions  
-  for larger n, z stat is appropriate. because the sampling distribution of $\hat{\pi}$ is approximately normal.  
-  for smaller n, neither t or z is appropriate, instead we use the binomial distribution.  

### the binomial distribution  
for sample size n, and a population proportion of $\pi$ for one of the categories, the probability of x outcomes in that category is:  
$$
P(x) = \frac{n!}{x!(n-x)!}\pi^x(1-\pi)^{n-x}
$$  

### small sample significance testing  

-  we can use the binomial distribution for small sample significance tests involving proportions.  
-  why? the distribution tells us the probability of getting a particular sample proportion under the scenario that the null hypothesis is true.  
-  just like with the z or t statistic, we can add up the probability of getting a result out in the tails of the distribution.  
-  this allows us to measure p, the probability that we might incorrectly reject the null hypothesis. under the scenario that $H_0$ is true.  

### example: bias in hiring  
-  the p-value is the sum of P(x) for every x at least as unlikely as the x we observed.  
-  in a two tailed test, that includes either hiring 0-1 white candidates as well as hiring 9-10 white candidates.  
-  the p-value = P(0) + P(1) + P(9) + P(10) = 0.22  

### decision rule  
-  if applicants were hired randomly, the probability of getting 0-1 from either category is 0.22.  

-  this result provides evidence against $H_0$, which we can reject at the 0.05 level, but not at the 0.01 level.  
-  we were able to perform a this significance test with n = 10 and without a z distribution.  

### comparison of binomial and normal distributions  

-  with large enough n, a binomial will look like a normal distribution.  
-  when $\pi$ is close to 0.5, the binomial distribution tends to a normal distribution more quickly.  
-  with the binomial, we do not calculate means and standard deviations. **we calculate p directly**. it is an "exact" test.  

### types of errors in hypothesis tests  

there is always a possibility of being wrong with a hypothesis test due to random sampling error.  
1.  type I error ($\alpha$): reject the null when it is in fact true. False positive!  
2.  type II ($\beta$): fail to reject the null when it is in fact false. False negative!  

### possible results from a hypothesis test  

| |  |  decision | 
|---|---|---|  
|  | reject $H_0$ | fail to reject $H_0$ | 
| $H_0$ is true | type I error | correct |
| $H_0$ is false | correct | type II error |