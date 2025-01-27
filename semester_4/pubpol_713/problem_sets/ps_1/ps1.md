---
title: Problem Set 1
author: Francisco Brady
date: "{{.1}}"
---


{{2}}


### 1. Generate three variables for time period 1:  

#### a. An indicator that flags students scoring above the cutoff of 475  


{{3}}


#### b. An indicator for "pre-selected" status. Pre-selected students are those for whom income quintile is less than 5  

#### c. A running or forcing variable centered at the cutoff score of 475  

### 2. Calculate some descriptive statistics and describe what you find:  

#### a. For time period 1, how many individuals are "pre-selected?" What proportion of PSU takers are pre-selected? What proportion of those scoring below/above the cutoff are pre-selected?  

#### b. Summarize and plot the distribution of the forcing variable (or of the PSU score) for time period 1. Briefly describe what you find. Do you see any evidence of bunching or manipulation around the 475-point threshold?  

#### c. Based on time period 1, calculate the rates of immediate enrollment (enrolt1) and ever enrollment (everenroll1) for 3 groups: non-pre-selected students and, among pre-selected students, those above and below the 475-point PSU cutoff. Do this only for observations that have a non-missing value for PSU in time period 1.  

#### d. Calculate the rate of immediate and ever enrollment for all students by family income quintile (again, among those with a value for PSU in time period 1).  

### 3. There are two key assumptions to a regression discontinuity analysis: (1) the likelihood of being assigned to the treatment varies discontinuously through the cutoff; and (2) characteristics that are associated with the outcome of interest change smoothly through the cutoff. Present evidence (figures and/or tables) of assumption (2) by analyzing the distribution of scores across family income quintiles. Briefly discuss your findings. See the bottom panel of Figure A1 in the paper for an example. Also discuss any remaining sources of bias that your RD analysis cannot rule out.  


### 4. Replicate columns 1 and 2 of Table 3, where the outcome is immediate college enrollment. Put these findings in a nice, clear table with all necessary information including bandwidth used. Briefly explain the relevant coefficient(s) in each column.  

### 5. The loan eligibility rule lends itself to a "sharp" RD specification in the short term. However, the fact that individuals may retake the test and become eligible in later years introduces some "fuzziness" to the treatment assignment. Use a 2SLS RD setup where exceeding the threshold in year 1 is an instrument for `everelig1` to replicate Table 4 columns 1 and 2. Report first-stage results as well. What do you infer from column 1-2 results? Is this consistent with your estimates from question 4?  

### 6. One of the nice features of this paper is that the RDD findings so clearly show the main result. Create your own version of Figure 1. [Just to warn you, you almost certainly will NEVER get an RD graph that looks this clean!]  

### 7. This final question asks you to estimate a series of placebo effects to gauge the size of the enrollment discontinuity at a score of 475 relative to other discontinuities at irrelevant scores.  

#### a. First, estimate the Table 3 column 1 specification for every value of $\tau$ between 431 and 519. That is, substitute placebo values of $\tau$ in the equation (1) term $1(T_i \geq \tau)$. Use a 44-unit bandwidth as in the main results, but note that this bandwidth will cover different PSU values in each placebo estimate. Store coefficients for the $1(T_i \geq \tau)$ indicator ($\beta_1$), and plot the distribution of placebo coefficients. Mark where the true effect of $\tau = 475$ lies in the distribution of placebo effects. What share of placebo effects are smaller in absolute value than the true $\beta_1$?  

#### b. Repeat part 7a, but for the Table 3 column 2 specification.  




{{4}}

