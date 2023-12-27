## October 2, 2023: Significance Tests, Part 2  

### The big picture  

-  baseline assumption: puts the null hypothesis at the center of the distribution  
-  level of significance sets a threshold for rejecting $H_0$  
    -  expressed as a probability (what threshold of probability of type II error is acceptable?)  
-  test statistics to show where our point falls on the distribution (as a normalized t or z statistic)
-  set up a rejection standard: if our statistic exceeds a threshold (critical value) defined by the alpha level, then we will reject the null hypothesis  
-  the p-value represents the probability that we are making an error, or that we would reject the null hypothesis as a result of random chance.  
    -  interpretation: under the scenario that the null hypothesis is true, what is the probability that we would observe a test statistic as extreme or more than the one we have from random chance?  
    -  ultimately we will compare our -value with our alpha level, to determine whether we will reject the null hypothesis or not.  

> as test statistic rises, the p-value falls. that is because the p-value is the area under the curve to the right of the test statistic.  

### steps for significance tests:  
1.  check our assumptions 
2.  state out hypotheses  
3.  take our point estimate and turn it into a test statistic, and compare that to our critical value.  
4.  calculate the p-value and compare it to our alpha level.  
5.  state a formal conclusion.  

### check assumptions  
-  random sample?  
-  other sources of bias?  
-  are the data quantitative or categorical?  
    -  when testing means, use the t-distribution, when using proportions use the z-distribution
-  do we know about the population distribution?  
    -  sample size > 30?
    -  if we know the population standard deviation, use the z-distribution  
    -  if we don't know the population standard deviation, use the t-distribution
-  what is the appropriate test statistic?  
    -  z-test for proportions  
    -  t-test for means

### state hypotheses  
a significance test considers two hypotheses about a parameter:  
- null hypothesis: $H_0$  
- alternative hypothesis: $H_a$

## calculating the test statistic  

-  how many standard errors is our sample statistic away from the null hypothesis?  
-  identify the appropriate test statistic for a test involving the mean, though t and z are identical for large samples (n > 1000)  
-  for a test involving proportions, use the z-test statistic  
-  for a test involving means, use the t-test statistic  
-  tests involving categorical data are based on the chi-squared distribution  

### calculate the p-value  

-  generally running two-tailed tests.  
-  for a two-tailed test, double the p-value for the one-tailed test.
-  one-tailed tests (less common), where the alternative hypothesis is directional.

## state a conclusion  
-  if our test statistic exceeds our critical value, we reject the null hypothesis.  
-  if our p-value is less than our alpha level, we reject the null hypothesis.
>  two ways of saying the same thing   

## example: immunization education programs  

-  null hypothesis: typical rate of immuinization is 72.2%  
-  we randomly select 400 babies whose parents agree to listen to an immunization education presentation before leaving the hospital.  
-  we follow up 3-years later to measure the percentage of children in the sample that receive the full series.  
-  we can test to see if the rate of immunization is appreciably different  
-  we will use a two-tailed test, because we are interested in whether the rate is higher or lower than the null hypothesis.
    -  the rate can be higher or lower.  

### basic approach  
- we start with the premise that the null hypothesis is true, i.e. the rate of immunization is equal to the population rate of 72.2%.  

### write out our hypotheses  
1.  $H_0: \pi = 0.722$ (the rate for the sample is no different than population)  
2.  $H_a: \pi \neq 0.722$ (the rate for the sample is different than the population)

assuming .722 is the true proportion, the central limit theorem tells us that 95% of the time, the sample proportion will be within 1.96 standard errors of the true proportion.  

### the level of significance 
-  in only 5% of samples will the sample proportion be more than 1.96 standard errors away from .722 that it's z-score is larger than 1.96 in magnitude.  

### the sample data  
-  in our sample, the proportion is .751  
-  the standard error based on the null:  

$$
\sigma_{\pi_0} = \sqrt{\frac{\pi_0(1-\pi_0)}{n}} = \sqrt{\frac{0.722(1-0.722)}{400}} = 0.024
$$

now we're ready to calculate our z-statistic:  
$$
z = \frac{\hat{\pi} - \pi_0}{\sigma_{\pi_0}} = (0.751 - 0.722) / 0.024 = 1.29
$$

### compare the test statistic to the critical value  

- our z was 1.29, for alpha = 0.05, the critical value is 1.96.  
-  since 1.29 < 1.96, we cannot reject the null hypothesis.  

### find the p-value  

-  p-value represents the probability that a random sample would produce a proportion that is at least as far from .722 as our sample proportion of .751.  
- we look up the area under the standard normal for the z-score associated with .751, then double it.  
-  the area above the z=1.29 is .0985. Double this number to include the area from the lower tail: $p=.197$  
-  p > alpha (0.05), so we cannot reject the null hypothesis.  

### revised scenario  

- increased sample size  
-  sampe percentage of immunized: .751  
-  sized of the standard error will shrink due to larger n.  
-  the z-statistic for our sample proportion will be larger than before (2.04):

> this is a good example of the difference between a statistical significance and substantively meaningful differences. here the sample size increased and so the difference becomes significant.  

### assessment  

[fill in here about shifted p-value]


### summary  
[fill in here about summary]  

## why the t-distribution?  
t-distribution is a lot like the z-distribution, but it's shape adjusts based on the amount of data we have.  
    -  smaller samples have more variability, so the t-distribution is wider (bigger tails)  
-  as the sample size increases, the t-distribution approaches the z-distribution.  

When do we use this:  
-  means and not proportions  
-  if sample size < 30 or $\sigma$ is unknown.  
    -  $\sigma$ is basically always unknown. so we should always be using the t-distribution for small samples.  
-  when n > 1000, the t and the z are basically identical. they are th esame to 2 decimal places when df $\geq$ 473.  

### the t and degrees of freedom  
-  since the t-distribution adjusts shape according to the sample size, the critical value of t for a specific area under the curve depends on n.  
-  since we are dealing with sample statstics, and not population parameters, we must also correct for degrees of freedom.  

### degrees of freedom  

-  we are using s, rather than $\sigma$ to calculate the standard error, which is the dispersion of the sampling distribution.  

### t and degrees of freedom  
-  when we use the t-distribution, we always need to know the degrees of freedom.  

- numbers inside the table are t-statistics.  

## October 11, 2023: Significance Tests, Part 2  

Using t table sometimes you can only find an approximate value.  
find p for t = 1.49.  
The area in teh right-hand tail is between .01 and .025  
the range for the two-tailed p-value is thus: 0.1 < p < .025  
If you double that, you get 0.2 < p < 0.05  

## Step 5: conclude  
at $\alpha 
in $\chi^2$ tests you do not need to double the p-value.  

### one tailed tests? 

-  we have a hypothesis about the specific direction of a relationship.  
-  e.g. biden's approval ratings will be **lower** among men than women.  

### one tailed rejection region  

All of $\alpha$ moves to teh side where we would reject $H_0$.  
If $H_a$ specifies that $\mu < H_0$, the rejection region is on the left-hand/lower tail. 

For these tests, it actually becomes easier to reject the null hypothesis.  

### air quality example  
follow all the same procedures as before, producing the same t-statistic of -2.49.  

$$
t = \frac{\bar{y} = \mu_0}{\frac{s}{\sqrt{n}}} = \frac{155 - 175}{\frac{30}{\sqrt{14}}} = -2.49
$$



