## 2024-02-13

### Example: Smoking and Infant Health

- concerns about the influence of parental behavior during pregnancy on infant health
other guidelines on:
- smoking & drinking
- food
- exercise
- vitamins

### Smoking and Infant Health
- big selection problem: mother's who smoke during pregnancy are different from those who don't
- in other words, we are worried about omitted variable bias
- multiple regression is a useful way of "controling" for these differences

### Omittted Variable Bias

$$
Bias = \alpha_1 - \beta_1
= [\beta_1 + \beta_2 \gamma_1] - \beta_1
= \beta_2 \gamma_1
$$

### Potential omitted variables
- Parent's education
    - Positive correlation with APGAR (x_2 + Y)
    - Negative correlation with smoking (x_2 + x_1)
    - Omittted variable bias: negative
- Quality of prenatal care
    - Positive correlation with APGAR (x_2 + Y)
    - Negative correlation with smoking (x_2 + x_1)
    - Omittted variable bias: negative
- Mother's best friend smokes
    - No correlation with APGAR (x_2 + Y)
    - Positive correlation with smoking (x_2 + x_1)
    - Omittted variable bias: None!
- Baby is male:
    - Negative correlation with APGAR (x_2 + Y)
    - No correlation with smoking (x_2 + x_1)
    - Omittted variable bias: No bias!

> Both conditions have to be met in order to have omitted variable bias.

### Test of Joint Hypothesis

- The population regression function is given by:
$$
1-min apgar = \beta_0 + \beta_1 smoking + \beta_2 mother's education + \beta_3 father's education + u
$$
- Test the null hypothesis that both mother's and father's education have no effect on infant health against the alternative that at least one of them does.
- $H_0: \beta_2 = 0 and \beta_3 = 0$
- $H_a: \beta_2 \neq 0 or \beta_3 \neq 0$ or both

- joint hypothesis specifices a value for two or more coefficients, or ("imposes a restriction on the coefficients")
- joint hypothesis requires q restrictions
- in the example above:
    - restrictions are: \beta_2 = 0 and \beta_3 = 0
    - q = 2

### F-statistic for Joint Hypothesis
- the f-statistic tests all parts of a joint hypothesis at the same time
- as with the t-test, we reject the null hypothesis if the f-statistic is large
- Large t -> small p-value -> reject $H_0$

### when errors are homoskedastic
There is a simple intuitive algorithm
1. run two regressions:
    - simple model/short regression - leave out meduc and feduc
    - more complicated model/long regression - include meduc and feduc
2. Compare the R^2 for both regressions.
3. If the unrestricted model fits sufficiently better than the restricted model, then we reject the null hypothesis.