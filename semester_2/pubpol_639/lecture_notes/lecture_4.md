## 2024-01-23

### causal interence & randomized control trials (RCTs)
today's agenda:
- randomized control trials (RCTs) II
- brief background: racial discrimination in the labor market
- discuss marianne bertrand and sendhil mullainathan's 2004 paper "are emily and greg more employable than lakisha and jamal? a field experiment on labor market discrimination"

### knowledge check
- which of the following is necessary for a randomized control trial (RCT)?
    - [ ] a. random sampling of participants for the study
    - [X] b. random assignment of participants into treatment and control
    - [ ] c. ability to observe (and control for) all factors that may influence the outcome of interest
    - [ ] d. equal numbers of participants in the treatmetn and control groups

### descriptive vs. causal questions 
$$
E[Y_i|D_i = 1] - E[Y_i|D_i = 0] = \\
\text{Observed Difference in Average Outcomes} \\
E[Y_1i | D_i = 1] - E[Y_0i | D_i = 0] + \\
\text{Average treatment effect on the treated} \\
 E[Y_0i | D_i = 1] - E[Y_0i | D_i = 0] \\
\text{Selection Bias}
$$

### Random Assignment
- create two groups that should be similar in absence of treatment
    - e.g. initial health status is independent of treatment
- randomize people into two groups:
    - individuals will not be identical acorss groups
    - group averages will be the same if groups are big enough
    - holds for variables we can see (e.g. race) and those we can't see (e.g. motivation)
> typically the concern when you don't have a randomized trial -- unobserved differences

###  causal question of interest
- how much does race affect chances of employment

### approach 1: simple comparison
- you can see wage outcomes across different groups
- this will not help identify causal factors driving difference in wages

### can we conclude from that there is discrimination in teh labor market from this evidence?
- no
- could be driven by differences in occupation
- differences in educational attainment

### problem: pre-labor market differences
- white men have more education, more years of exp., more likley to be married compared to other groups.
    - note: all of these factors likely reflect some degree of discrimination and structural racism.
- there are all confoudning factors!

### ideal experiment!
- how could we manipulate employers perceptions of race
- and make perceived race independent of other factors

### approach 2: audit study
- long history in social science
- typically send two people (actors) with similar qualifications but different race to apply for the same job
- observe differences in outcomes

### audit study - drawbacks
- participant knowledg of the experiment
- relies on comparability of paired subjects (which is not testable)
- expensive --> small samples
- bertrand and mullainathan are able to address all three of these concerns

### bertrand and mullainathan 2004
- large scale audit-like study examining perceived race and hiring
- broad research question: is there racial discrimination in the labor market?
- approach: sent out real-ish resumes to job applications manipulating the race of the applicant to observe whether there are differences in callback rates by race.

### benefits of method over audit study
- much larger sample size
    - inference
    - sub-sample analysis
- can precisely control information given to employers
- no "interference" by audit actors

### background
- experiments are useful for identifying causality because we holkd all other factors constant

### research design
- outcome: callback rates
- identification strategy: construct two resumes, vary the name
    - one black sounding name
    - one white sounding name

### how do you determine a white or black-sounding name?
- birth registryt data
    - top 10 names for black and white children
- limitation:
    - perceptions of racialized names based on survey responses
    - perceptions of names might also be associated with different socioeconomic status

### research design, 2
- job postings: chicago and boston newspapers
- job types: entry-level positions in sales, administrative support, clerical, and customer service
- two resumes for each post:
    - black-sounding name resume
    - white-sounding name resume
    - similar otherwise
- causal inference: any difference is due to name, not other factors

### what does randomization do?
- random assignment creates independence between treatment (here perception as black) and other determinants

### are these differences statistically significant?
- to test the null hypothesis that mean of years experience is the same for black and white applicants, against the alternative hypothesis that it differs:
$$
h_0: \mu_{black} - \mu_{white} = 0
h_a: \mu_{black} - \mu_{white} \neq 0
$$
- we can use a t-test to test this hypothesis
- the t-statistic is:
$$
t = \frac{\bar{x}_{black} - \bar{x}_{white}}{s_{pooled} \sqrt{\frac{1}{n_{black}} + \frac{1}{n_{white}}}}
$$
- where $s_{pooled}$ is the pooled standard deviation of the two samples

### results: overalll callback rates
- compare the two means
- 9.65% for white applicants get a callback
- 6.45% for black applicants get a callback
- ratio of 1.5
- white names 1.5 times more likely to get a callback
- statistically significant


### how large is this difference: characterizing the "economic" significance of the impacts
- percentage points (3pp diff)
- percent change (50% increase)
- ratios (1.5x the call back rate)
- black-white difference in callback rates = about 8 years of experience

### limitations
- can only make inference on very white-sounding names and very black-sounding names
- cannot speak to ambiguous names
- names could also be associated with socioeconomic status, not race-based discrimination
- only analyzed callback rates, not hiring
- types of jobs: posted in the newspaper only, entry-level, administrative jobs

### experimental validity
- internal validity: did we estimate an unbiased causal effect for our sample?
    - fails when treatment and control groups are different in ways that may affect the outcome
    - non-compliance, attrition, evaluation-driven effects.

- external validity - can we extrapolate these estimates to other contexts?
    - fails when the treatment effect is different in outside the evaluation
    - non-representative sample, non-representative program (implementation differences), scaling effects

### idealized experiment
- we can't often do idealized experiments


### knowledge check
the table below presents two outcomes for people who did and did not participate in a job training program. under what circumstances can we interpret the difference in outcomes as the causal effect of the program?  
a. - [ ] only if treatment is randomly assigned 
b. - [X] only if treatment status is for some reason completely independent of other factors that affect the outcome
c. - [ ] only if treatment is determied by program administrators finding people that would most benefit from the program

### wrap up
- we will talk about basics and build our way up to more complex designs
- bivariate ordinary least squares (OLS) regression
- read stock and watson chapter 4
