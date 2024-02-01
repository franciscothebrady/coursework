## 2024-01-30

### how do (most) economists explain the recent surge in income inequality

Goals:
- understand the recent increase
    - discuss two different approches to this question
- understand how economists try to explain the world using models

What are models?
- simple representation of the truth
- usually has predictive capacity
    - models are judged by their ability to predict outcomes

What is income?
- income according to CBO (tax + census data)
    - market income: labor income (wages and fringe benefits like healthcare), business income (if you own), capital income (dividends, interest, capital gains), income received in retirement for past services (private pensions0, and other non-governmental income)
    - income before transfers and taxes: market income + social insurance benefits (income replacement tied to old age, i.e. including social security, medicare, unemployment insurance, and workers' compensation)
    - income after transfers and taxes: income before transfers and taxes + means-tested transfers (Medicaid, CHIP, SNAP, and SSI) - federal individual and corporate income taxes, payroll taxes, etc.

Trends in market income:
- one way to measure changes in market income over time is to create a ratio of average income / the 50th percentile (median).
- this is because inequality is about the tails of the distribution
- so average will be affected by larger changes in the tails, and the median will not

What explains the "return" of market inequality?
|          | Labor Income  |  Capital Income (includes business income) |
|----------|:-------------:|------:|
| Focused on the fact the the increase is top heavy |  Assignement 1 readings | Thursday's Lecture and reading will tackle some of this |
| Focus on the whole income distribution, discounting trends at the top |    Today (Tuesday)   |   $12 |

Today:
- Tuesdays Reading: Factors discussed in this literature: technology, offshoring, union decline, etc. Focuses on labor income.
- Thursday: Capital income

Today:
- we will mostly focus on labor income (for that we have excellent data)
- the data generation process for labor income is through the labor market

Empirical Puzzle to Explain:
- Labor income in the united states
- growing gap between median hourly earnings and mean hourly earnings
    - trend in mean is increasing faster than trend in median
- on average all measures of labor income are increasing in the same direction

Three measures are capturing the increase in income:
- gini coefficient
- 90-10 ratio
- other measures of labor income

The canonical model: assumptions
- if some peopel are being paid more and more for their work, then it must be that their work is more and more 'valuable"
- "valuable" means that employing these people is profitable (they produce goods and services that are worth a lot, i.e., worth more than cost)
- if some people are being paid less, that means their work is less "Valuable", i.e., they produce goods and services that are worth less than their cost.
> assumes a competitive labor market

What explains this change in market value?
Who is positively affected?
Who is negatively affected?

The canonical model:
$$
Y = [A{_L}L^{\frac{\sigma -1}{\sigma}} + A{_H}H^{\frac{\sigma -1}{\sigma}}]^{\frac{\sigma}{\sigma -1}}
$$
Production function for the aggregate economy (2 factor model)
- Y = output
- H = high skill labor
- L = low skill labor
- A = technology that affects productivity
- technological change is captured by changing these parameters (\sigma)
- Captures whether H and L are substitutes or complements

If the labor market is competitite, then the equilibrium wage for L is equal to the marginal product of L, whuich is obtained by differentiating the equation above. Similarly for H.

The skills premium is the ratio between the two:
- $w = w_h/w_l = (\frac{A_h}{A_l})^{\frac{\sigma-1}{\sigma}}$

Based on this theory, what explains the changes in the skill premium w?
- $ln(w) = \frac{\sigma-1}{\sigma} ln(\frac{A_H}{A_L}) - \frac{-1}{\sigma}(\frac{H}{L})$
- the way this is equation is written, the changes in technology and skills are EXOGENOUS to the model.

Cannot measure $ln(\frac{A_H,t}{A_L,t})$ directly, instead assume that there is a linear increase over time in the relative demand for H, modeled as: $\gamma_t = \gamma_0 + \gamma_1 t$

The model is then:
$$
ln(w)_t = \frac{\sigma-1}{\sigma} \gamma_0 + \frac{\sigma -1}{\sigma}\gamma_1t - \frac{1}{\sigma}ln(\frac{H_t}{L_t})
$$

Judging the model:
1. R^2: 0.56 if we use data from 63-87, 0.94 if we use 63-08 data
2. out of sample testing: we use the data from 63-87 to predict the data from 88-08. The model does a good job of predicting the data.
The model is good enough that you can use it to back out the estimates for skills-based technological change.

### to sum up

canonical model:
- 60s through 1970s, supply was increasing faster than technological "need"
- if the model is correct, from 1982 on the supply of college graduates relative to high school is not large enough.

Theory:
- technology takes a factor-augmenting form, complementing some skills more than others: in other words, technological change is skill-biased
- changes in income-inequality are partly the product of a race between skill supply and technology: improvements in technology increase the demand in more skilled workers, if the supply does not follow, the the skill premium increases and so does the wage of inequality.
Hypothesis:
- part of th eincreas in labor income inequality comes from educations/training having not kept up with technological change.
Empirical evidence:
- a simple 2 factor model, which models the skills premium as a function of SBTC and relative skill supply does a surprisingly good job of explaining changes in returns to a college degree.
Policy implications:
- increase supply of in-demand skills (if you believe the model!!!!!!)