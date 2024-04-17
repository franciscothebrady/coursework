## Regression Discontinuity (RD)

- RD is a powerful and widely applicable quasi-experimental identification strategy
- *setup*: treatment is assigned on the basis of one variable (sometimes called the assignment or the "running" variable)
    - if the value of the assignment variable is above a certain threshold, the treatment is assigned
    - if the value of the assignment variable is below the threshold, the treatment is not assigned
    - compare the outcomes of individuals just above and just below
        - in theory they should be comparable except for the treatment
- basic idea: treatment is **as if it was randomly assigned** when we look at observations right around the cutoff

### RDs used in:
- examples:
    - effects of k12 capital spending
    - effects of drinking laws
    - effects of punishment on crime
- common RD sources:
    - eligibility thresholds
    - close elections
    - geographic boundaries
    - any artibrary cutoff

### Age-based RD: Turn 21 --> More days drinking
Carpenter and Dobkin (2009) study the effect of turning 21 on mortality.

- First Stage: Looking at Running variable and treatment
    - Running variable: Age
    - Treatment: Turn 21
- Second Stage: Looking at outcome and treatment
    - Outcome: Mortality
    - Treatment: Turn 21

### Implementation
- Why not just compare observations right near the cutoff?
- it's a good way to think about it conceptually
- often it's impractical because there may not be many obervations right at the cutoff.
    - poor statistical power since outcomes for a small number of observations will be really noisy.

- instead also, use observations a little further from the cutoffs, but then control for a smooth function of the score.
    - only use observations with a certain bandwidth of the cutoff

### Controlling for the assignment variable
- the assignment variable ("score") often has it's own effect on the outcome
    - e.g. age has an effect on mortality
    - we want to control for this effect
    - we can do this by including the score in the regression
- or specifically, the assignment variable may be a measure of need, and so is almost certainly related to the outcome.
- we therefore need to control for a smooth function of score
    - include linear, quadratic, or cubic of the score and intercept change at the cutoff.
    - identifying the variation in the treatment is at the discontinuity

### Implementation
- regress outcome on treatment and a function of the score
$$
Y = \beta Treatment + f(Score) + \epsilon \\
\beta = effect of treatment on Y
$$

- Usually want this function to vary between treated and non-treated observations
    - e.g. different slopes on either side of the cutoff
$$
Y = \beta Treatment + f_1(Score)*(Score < 0) + f_2(Score)*(Score >= 0) + \epsilon \\
Treatment = 1 if Score >= 0 \\
\beta = \text{Effect of treatment on Y} \\
$$

### Implementation
- it is typical to try several different functional forms for the score
    - linear, quadratic, cubic, etc.

### Sharp RD or Fuzzy RD
- Sharp RD: likelihood of treatment goes from zero to 1 as the assignment variable crosses the threshold.
- Fuzzy RD: likelihood of treatment increases discontinuously (from some level greater than zerto to some level less than one) as the assignment variable crosses the threshold.

### Implementation: Fuzzy RD
- Regress outcome on score (as before):
$Y = \beta Treatment + f_1(Score)*(Score < 0) + f_2(Score)*(Score >= 0) + \epsilon$

- Regress treatment on score:
$\delta Treatment + g_1(Score)*(Score < 0) + g_2(Score)*(Score >= 0) + \epsilon$

- $g_1(X)$ and $g_2(X)$ are smooth functions below and above the cutoff
- Effect of treatment on Y is $\beta = \alpha/\delta$

### Implementation
- there are many implementation decisions
    - what size bin should I use to make graphs?
    - what functional form for the f(score) function?
    - what bandwidth should I use?
    - should I drop the outermost points?
    - should I control for covariates (to increase precision)?
- there have been some procedures developed to guide you in making these decisions.

### Threats to Identification
- Manipulation of the assignment variable (score)
    - rests on the assumption that being above or below the cutoff is as good as random
    - if people can manipulate the score, this assumption is violated
    - you can try to convince yourself by showing a smooth density of the score around the cutoff.
- is there anything else that happens at the same cutoff point?
    - there could be other confounding factors.
    - e.g. elibigibility for other programs.

