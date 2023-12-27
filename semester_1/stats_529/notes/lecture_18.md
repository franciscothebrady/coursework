## lecture 18: ANOVA

### on the quiz 
- one and two sample tests for significance 
- confidence intervals
- significance tests involving two means 
- basic interpretation of a chi squared test
    - calculating degrees of freedom and calculating critical values 
    - expected frequencies

### outline 
1. comparing several means 
2. mathematical details 
3. examples 

### why analysis of variance? (ANOVA) 

- we have learned how to perform comparison of means tests involving two means 
- when there were more than two categories, we could only compare two at a time 
- we may was to perform a comparison of means across groups simultaneously 
    - e.g. the mean final exam scores across five sections of a course that had different GSIs
- we can do this with anova 

For example: Mean thermometer opinion on Obama and party ID. 

Independent variable: Party ID (Democrat, Independent, Republican)
Dependent variable: Mean thermometer opinion on Obama

| Party ID | Mean thermometer | Std. Dev. | Frequency |
|----------|------------------|-----------|-----------|
|Democratic| 85.31            | 19.1      |  40.1%    |
|Independent| 55.73            | 31.5      |  36.2%    |
|Republican| 26.62           | 26.7      |  23.6    |

Null hypothesis: is it possible that it was just random sampling error that led to the differences in these means?

### Basic idea behind ANOVA 

- we have interval level dependent variable AND one or more categorical independent variables
- does the population distribution of the dependent variable (y) differ for the groups formed by the independent variable(s)?
- ANOVA partitions variation in y into within-group variation in y and between-group variation in y  
- if between group variation is high relative to within-group variation, we reject $H_0$ that the mean of y is the same for all groups.  

> note: variation between groups is about deviations between the individual group means and the overall sample mean of y.  

### illustration
- in sample a, within group variance is much smaller, so it is easier to distinguish the between group variance. 
- in sample b, the within group variance is much larger, so it is harder to distinguish the between group variance.  

### forming a test statistic 

the test involves the ratio of the between-group variance to the within-group variance. This is called an F statistic:  
$$
F   = \frac{\text{Variance in y between groups}}{\text{Variance in y within groups}}
$$

If there are G groups, this statistic has G - 1 degrees of freedom in the numerator and N - G degrees of freedom in the denominator.

(In our example, G would be 3, and our degrees of freedom would be reduced by 3.)

### illustration

- over all mean of y: 32.2. The means of y for three categories of x: 31.5, 32, 33
- two scenarios: 
    1) within-group variance is small, 
    2) within-group variance is large.
- between group variance is the same in both scenarions 
- we will see why the F-statistic will be much larger in the first scenario  

## mathematical details

### stating the hypothesis
supposed the number of group sis G. The null hypothesis is: 
$$
H_0: \mu_1 = \mu_2 = \mu_3 = ... = \mu_G
$$
The alternative hypothesis is: 
$$
H_a: \text{at least one of the } \mu_i \text{ is different from the others}
$$
In other words, $H_0$ can be rejected in a variety of circumstances 

### within-group variance vs between-group variance

suppose we have a sample of size n. observation $y_i$ is the ith observation of y, where i goes from 1 to n. 

now suppose this sample is divided according to the categories of another variable (x) such that there are G different groups. The sample size of group g is $n_g$. 

- Within group variance is about deviations of $y_gi$ from $\bar{y}_g$. The mean of y for group g is $\bar{y}_g$.
- between-group variance is about deviations of $\bar{y}_g$ from $\bar{y}$, the overall mean of y.

### between-group variance

1. find the sum of the squared deviations between groups:  
$$
BSS = n_1(\bar{y}_1 - \bar{y})^2 + n_2(\bar{y}_2 - \bar{y})^2 + ... + n_G(\bar{y}_G - \bar{y})^2
$$

2. divide by the degrees of freedom:, which is G - 1, to get the estimate of the between group variance: 
$$
\frac{BSS}{df_{BSS}} = \frac{\Sigma n_g(\bar{y}_g - \bar{y})^2}{G - 1}
$$

This is the numerator of our F-statistic.. It has G - 1 degrees of freedom.

### within-group variance

two methods:  

1. add up the sums of the squared deviations within each groups (within sum of squares). 
$$
WSS = SS_1 + SS_2 + ... + SS_G
$$

where each $SS_g$ is: 
$$
SS_g = \Sigma_{i = 1}^{n_g} (y_i - \bar{y}_g)^2
$$

2. Divide by the degrees of freedom, which is N - G, to get the estimate of the within-group variance:
$$
\frac{WSS}{df_{WSS}} = \frac{\Sigma_{g = 1}^G \Sigma_{i = 1}^{n_g} (y_i - \bar{y}_g)^2}{N - G}
$$
This is the denominator of the F statistic. It has n - G degrees of freedom.

## putting it all together

we are now ready to create out F statistic 

$$
F_{G-1, n - G} = [Finish this]
$$

Reminder: this is the ratio of the between-group variance to the within-group variance. If the F statistic is sufficiently high, we can reject the null hypothesis that there is no difference in the means between the groups.  

## examples

### one way ANOVA 
- tests whether variation in the dependent variable is connected with the categories of one independent variable. 

### in stata 

```
anova ombama_therm pid_3
```
- F statistic and p-value are reported 

### in R 

```
anova <- aov(obama_therm ~ as.factor(pid_3), data = nes2012)
summary(aov)
```

- outputs df, sum of squares, mean square, F-statistic, and p-value

### two way ANOVA  

- tests whether variation sin the dependent variable is connected with the categories created by different combinations of two independent variables.

-  test is wehter the population means are ideantical accross the categories of one variable when controlling for the other one.

#### stata
```
anova obama_therm pid_3 south
```

### in R
```
anova2 <- aov(obama_therm = as.factor(pic_3) + as.factor(south), data = nes2012)
```

### interpretation 

-  we can reject the null hypothesis that the mean obama therm in different categories of the party id variable, even after we control for whether or not a respondent lives .  

### summary 

when do we use this? 
- when the independent variable has more than two categories, or when we havce multiple categories 