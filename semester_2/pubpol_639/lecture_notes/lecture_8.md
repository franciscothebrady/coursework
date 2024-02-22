## 2024-02-06

Quantitative Analysis/Program Evaluation
Today: Multiple Regression & Regression output
Agenda:
- multiple regression: interpreting and presenting results
- start omitted variable bias
- next time: understanding ommitted variable bias

### Last time
- want to estimate the relationship between student teacher ratio and test scores **holding all over factors constant**
- we need to do this to get the causal effect we want because in observational data some other variables may be responsible for the observed association between class size and test scores.
- multiple regression allows us to control for these other variables

In public policy we often want to isolate the relationship between two specific variables.

### Last time: California test schore data 
testscore = 8th grade test score in school district
str = student teacher ratio
avginc = average district family income (000s)

- population regression function (bivariate):
$$
testscore = \beta_0 + \beta_1str + u
$$
- population regression function (multiple):
$$
testscore = \beta_0 + \beta_1str + \beta_2avginc + u
$$

Last time: results
- bivariate regression: testscore = 698.93 - 2.279str
- multiple regression: testscore = 638.72 - .648str + 1.83avginc

### what happened?
- in this case, average income was correlated with both student teacher ratio and test scores
- part of the association between student teacher ratio and test scores found in the bivariate regression was attributable to average income
- when we control for average income, the coefficient on student teacher ratio changes (decrease)

### measures of fit for multiple regression
actual = predicted + residual: $y_i = \hat{y_i} + \hat{u_i}$
- R-squared: proportion of variance in the dependent variable explained by the independent variables
- adjusted R-squared: R-squared adjusted for the number of independent variables (degrees of freedom correction)

### motivation for the adjusted R-squared
- the R-squared is the fgraction of the variance explained = same definition as with a single regressor:
$$
R^2 = \frac{MSS}{TSS} = 1 - \frac{SSR}{TSS}
$$
Where
$$
MSS = \sum_{i=1}^n(\hat{y_i} - \bar{y})^2, SSR = \sum_{i=1}^n(\hat{u_i})^2, TSS = \sum_{i=1}^n(y_i - \bar{y})^2
$$

The $R^2$ always increases when you add another regressor- (why?) -- which can be a problem for measure of fit.

### the adjusted R-squared
The adjusted R-squared corrects this problem by "penalizing you for including another regressor - the adjusted R-squared does not necessarily increase when you add another regressor.

$$
\bar{R}^2 = 1 - \frac{n-1}{n-1-k} \cdot \frac{SSR}{TSS}
$$

Note that $\bar{R}^2 \leq R^2$

### What about other factors?
- what variables would you ideally control for in order to estimate the effect on test scores using school district data?
-- past student performance
-- parental education
-- teacher profiles (experience)

- variables actually in the california class size data set:
-- percent english learners in district
-- school expenditure per pupil
-- percent eligible for free lunch
-- percent on public income assistance
-- average district income

### which variables to include?
- one approach is to run a number of regressions including various combinations of these "control" variables
- then ask:
    - does the relationship between test scores and STR change when additional/different control variables are included?

### problem: lots of info to present
How to present regression results
- we have a number of regressions to present
- it is conventions to include a table of regression results


### omitted variable bias

- we have seen that adding variables to a regression can change coefficients
    - the relationship between class size and test scores got much smller when we controlled for measures of socioeconomic status
- why?
    - omitted variables are correlated with both class size and test scores
    - once we hold constant these factors, the observed relationship between class size and test scores changes
- this is called omitted variable bias
    - also called confounding factors

### Conditions for OVB
we are getting out coefficient wrong in the bivariate regression because income is moving with both class size and test scores.
- these two issues together cause OVB:
1. OV is a determinant of the dependent variable (Y)
    - X_2 is correlated with Y
    - X_2 is in u, the error term
2. OV is correlated with the other independent variable (X)

### magnitude and sign of OV
- how much bias is caused by omitting X_2?
- if you have X_2, then you can answer this question directoy by adding it to the regression
    - observe how the coefficient on X_1 changes
    - this is the bias caused by omitting X_2
- if you don't have X_2, then you can't answer this question directly
    - you may be assessing someone elses analysis
