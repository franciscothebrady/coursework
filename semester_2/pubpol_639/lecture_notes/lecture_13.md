## 2024-03-12

### nonlinearity -continued

### agenda
- today: finish up right-hand side non-linearity
- interaction terms
    - interacting binary variables with continuous variables
    - interacting two binary variables
    - interacting two continuous variables

- next time; left-hand side non-linearity
    - binary dependent variables
        - linear probability model

### example: demand for college
questions:
- how has the demand for college changed over time?
- what types of colleges had the greatest increase in demand?

facts: there has been a large increase in college enrollment over 1986 - 2003

### questions:
use # applicantion per enrollment slot as an indicator of demand for each specific college
- how has the demand for college changed over time?
- do trends in the demand for college differ for private v.s. public colleges?
- do trends vary by the selectivity of the college?

### data
- data on colleges from petersons (college planning)
    - applications (freshman)
    - enrollment
    - public/private indicator
    - sat rank: high/low (students over 600 on SAT)
    cost rank: high/low (low cost = 0, high cost = 1)

### no interactions 
$$
Applications Per Enrollment = \beta_0 + \beta_1 Time + \beta_2 Public + u
$$

This specification:
- allows the application/enrollment (A/E) ratio to differ between public/private institutions
    - what is the difference on average between public and private colleges?
- allows the A/E ratio to change over time (linearly)
- does NOT allow the relationship between A/E and time to differ between public/private institutions

### motivation for interactions
- the assumption of similar slopes between public and private institutions may not be realistic
- we can instead allow a different slope (= time trend in this application) for a/e ratio over time for public and private institutions
- to do so, we add the interaction of public and time to the model

### interaction terms, conceptually
- so far we have been estimating models where we allow public schools to had a different intercept from private schools

### generating interactions
- you can multiple the two terms together
```stata
gen time_public = time * public
```

### interpreting coefficients
$$
A/E = \beta_0 + \beta_1 Time + \beta_2 Public + \beta_3 Time \times Public + u
$$

- Formula for public institutions:
$$
A/E = \beta_0 + \beta_1 Time + \beta_2(1) + \beta_3 Time(1) + u
= (\beta_0 + \beta_2) + (\beta_1 + \beta_3) Time + u
$$
- Formula for private institutions:
$$
A/E = \beta_0 + \beta_1 Time + \beta_2(0) + \beta_3 Time(0) + u
= \beta_0 + \beta_1 Time + u
$$

### interactions with calculus
- calculus provides an easy way to quickly interpret equations with interactions
- regressions with no interaction terms:
$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + u
dY/dX_1 = \beta_1
dY/dX_2 = \beta_2
$$

- Regression with interaction terms
$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_1 X_2 + u
dY/dX_1 = \beta_1 + \beta_3 X_2
dY/dX_2 = \beta_2 + \beta_3 X_1
$$

### interpreting interactions
regression with interaction terms:
$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_1 X_2 + u
$$
Now change X_1:
$$
Y+ \delta Y = \beta_0 + \beta_1 (X_1 + \delta X_1) + \beta_2 X_2 + \beta_3 (X_1 + \delta X_1) X_2 + u
$$
Subtract the original equation from the new equation:
$$
\delta Y = \beta_1 \delta X_1 + \beta_3 X_2 \delta X_1
$$
- the effect of a change in X_1 on Y depends on the value of X_2
- the effect of a change in X_1 on Y is $\beta_1 + \beta_3 X_2$


### interactions with 2 binary variables
- suppose there was a change in the application process in 1991
- you want to examine whether this policy changeds application rates
- create a binary variable for post1991
- create an interaction term between post1991 and public
- the coefficient on the interaction term will tell you the difference in the effect of post1991 on public v.s. private institutions
- the coefficient on post1991 will tell you the effect of post1991 on private institutions
