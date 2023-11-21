
## recap: the chi^2 test of independence 

- this test applies when our variables of interest are categorical and we have a relatively large sample  
-  in a joint freq distribution, the $\chi^2$ statistic measures deviation from the scenario in which the variables are independent.  
-  the $\chi^2$ statistic is non-negative, and 0 indicates the variables are independent  
-  we reject the null hypothesis of independence when the $\chi^2$ statistic is sufficiently large
-  this critival value of $\chi^2$ depends on $\alpha$ and the degrees of freedom, which is a function of the number of rows and columns in the joint freq distribution

## formula for the test statistic 

take the frequency that we observe ($f_o$), subtract the frequency that we expect ($f_e$), square the difference, and divide by the expected frequency.  Do this for each cell in the table.  Then add up all of these values.  This is the $\chi^2$ statistic.  

$$
\chi^2 = \sum \frac{(f_o - f_e)^2}{f_e}
$$

### in stata 

```
tab owngun fear, col chi
```

### in r 
```
mytable <- table(data$y, data$x)
chisq.test(mytable)
```

## example  

education program
- graduation rate of a participants in a program.  
-  previously, we used a difference of proportions test, and we could not reject $H_0$. The z-statistic was 1.049. Let's use a $\chi^2$ test.  

## calculate expected frequencies  

-  what proportion of people are in the first row, and what proportion are in the second row?  
-  Take the overall proportions in each row, and multiply that by the total, to get the expected frequencies.  

- Each cell contains: $ \frac{(f_0 - f_e)^2}{f_e} $

## calculate the $\chi^2$ statistic

-  summing all the expected inner proportions together, we get the $\chi^2$ statistic. (1.1 in this example)
-  Compare that value with teh critical value with 1 degree of freedom (3.84).  
-  since 1.1 < 3.84, we fail to reject $H_0$.  

## comparison of results  

-  the results are the same as the difference of proportions test.  
-  the z-statistic was 1.049, we could not reject the null hypothesis  
-  with the $\chi^2$ test, the $\chi^2$ statistic was 1.1, we could not reject the null hypothesis.  
-  these tests are related. Note that $1.049^2 = 1.1$, in other words, $z^2 = \chi^2$  
-  likewise, the area in the tails of the two distributions is the same for these tests (p= 0.294)  
-  the $\chi^2$ test generalizes to variables of more than two categories.  

## example: ACA  

-  dependent variable: level of satisfaction with health insurance (satisfied, neutral, dissatisfied)  
-  independent variable: halth plan type (ACA or other)  

What distribution should we see if satisfaction and health plan type are independent?  

## expected distribution under $H_0$  

-  to test independence, we need to know the expected distribution of satisfaction under $H_0$.  
-  calculate that using the row proportions, and apply that proportion to each inner cell.  

## residuals  

-  the difference between the observed and expected frequencies is called the residual.
-  we can calculate a z-statistic for each cell, which is the residual divided by the standard error.

$$
z = \frac{f_o - f_e}{se} = \sqrt{\frac{f_o - f_e}{f_e (1 - row proportion ) (1 - column proportion )}}
$$

## working with ordinal variables  

-  when variables are ordinal, there can be a positive or negative relationship between them  
-  by positive we mean: when a variable is increasing, then the other variable is increasing.  
-  the $\chi^2$ statistic does not measure this  
-  a variety of statistics do this: gamma, mkendalls, tau-b, etc.  
very accurate. Instead, you could say som
## interpretation  

-  both the gamma statistic and the tau-b statistic suggest a mild negative relationship between the two variables.  
-  e.g. people who are opposed to legalizing marijuana are more likely to favor making it easier to buy guns, and vice versa.  
-  these measure allow us to be a bit more systematic when assessing the relationship between ordinal variables.  

## gamma and kendall tau-b statistics in R  
-  in `DescTools` library  
-  `GoodmanKruskalGamma(mytable)`
-  `KendallTauB(mytable)`


