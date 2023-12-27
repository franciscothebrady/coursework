## non-parametric tests 

- non-parametric tests are used when the data is not normally distributed (skewed)  
-  non-parametric tests == we're not estimating a parameter like a mean.  
- instead some tests are based on ordinal rankings of cases from high to low.  

## example: wilcoxon-mann-whitney test  

-  rank test for independent samples  
-  calculate a rank for cases in each sample, computing a test statistic (U)  
-  $U_1$ is the total number of times in which an observation from sample 1 is ranked higher than one from sample 2, compared with the expected sum of rankings.  

### in stata 
```
ranksum outcome, by(catvar)
```
### in r 
```
wilcox.text(outcome ~ catvar, data=dataset_name)
```

### example: democracy and gdp per capita  

-  test whether gdp per capita is differs across democracies and non-democracies
-  the wilcoxon-mann-whitney test ranks the combined samples in order of gdp per capita.  

### example: wilcoxon test for paired samples  

-  the null hypothesis is that there is no difference in the rankings  

## controlled comparison of means  

-  we went over comparison of means tables for two variables (x and y)  
-  we can add a another categorical variable (z) to control for the effect of that variable  

-  specifically, we can obtain the mean of y for all combinations of x and z to see how the mean changes when holding the value of z constant.  

### example: controlled comparison of means  

suppose we are interested in the effect of democracy on life expectancy in a country.  
-  we can measure life expectancy levels from various sources  
-  we have several different dichotomous measures of democracy
-  given that national wealth affects life expectancy, we can control for level of wealth to get a better sense of the effect of democracy on life expectancy.  

### controlled comparison of means  

mean level of life expectancy
|  | level of gdp per capita |  | |  | 
| democracy? | low wealth | medium wealth | high wealth | total | 
| no | 58.8 | 67.4 | 72.6 | 64.5 | 
| yes | 63.1 | 73.0 | 78.3 | 72.5 |
| total | 61.0 | 70.6 | 77.1 | 69.5 |  

> note: we could have seen no change after controlling for gdp per capita, that would indicate that the effect of democracy on life expectancy is not conditional on gdp. 

## other types of relationship  
-  we found an additive relationship: both variables matter, and the effect of one variable is close to the same for each value of the other variable.  
- spurious relationship: after adding the control, we might have found that democracy made no difference at all, the apparent differences were due to gdp 
