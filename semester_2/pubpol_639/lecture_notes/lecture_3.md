## 2024-01-18

### Causal Inference and Randomized Control Trials

### last time
- the selection problem
    - can't make a causal statement about how health insurance affects health becuase those with insurance differ from those who do not -- the selection problem!
    - this is the fundamental challenge we try to overcome in causal inference

### today 
- solution to the selection problem: randomized control trials
    - RAND health insurance experiment 
    - Oregon medicaid study

### overcoming selection problem
- strategy 1: randomized control trials
    - rely on random assignment to overcome selection problem
    - means only difference between treatment and control groups is the treatment itself (we can verify this)

### example: RAND health insurance experiment
- question: what is the impact on health insurance coverage on health outcomes?
- randomly assign health insurance coverage of varying terms:
    - lots of different treatments
    - some people get no insurance, some get full coverage, some get partial coverage
    - coverage ranged from "everything free" to "pay 95% of the cost up to $1000"
- participants stayed in the study for 3-5 years, were paid
- N=3,958

### example: RAND health insurance experiment
- first order of business:
    - check balance
    - i.e. do the treatment and control groups look similar?
    - ideally, only difference (on average) between treatment and control groups is the treatment itself
    - if there are differences, we would worry that some other factor influences the outcome

### example: RAND health insurance experiment
- in balance table:
    - showing means of catastrophic group and difference of means across different characteristics
    - small difference in means and standard errors means (t-tests) indicate that the differences are not statistically significant (which we want)
- also showing means of the control group across different characteristics

### checking balance
- calculate t-statistics for female identifying
- treatment mean: 0.53
- control mean: 0.56
- difference in means: -0.03
- standard error: 0.013
- null hypothesis: H_0: diff = 0
- alternative hypothesis: H_A: diff != 0
- t-statistic: -2.31
- do we reject the null hypothesis? yes!

### checking balance
- is the fact that there are more women in the control group a problem? 
    - maybe! it's possible that women are in better health or make different choices about health care
    - but we can control for differences in a regression context
- given the number of characteristics we're testing, we're bound to find one difference between treatment and control by luck alone.
    - remember what the 95% confidence interval tells us
    - 5% of the time we'll reject the null when we shouldn't

### results: health care usage
- general health index actually decreased among covered groups
- no significant difference in terms of general health, cholesterol, blood pressure
- takeaway: treatment means that costs went up, no obviosu benefits to health

### oregon medicaid study
- oregon had limited space in it's medicaid program for poor adults
- opened waiting list in 2008
    - over subscribed
    - 75,000 went onto the list, 30,000 spots
- randomly selected from the waiting list
    - winners allowed to apply for medicaid
    - had to meet medicaid criteria to get coverage
        - age 19-64, uninsured 6 months, lower income, few assets

### results
- winning lottery increased likelihood of enrolling in medicaid
- treatment group significant increases in mental health
- treatment group increase in reporting good health
- treatment group less likely to have any medical debt

### takeaways
- winning medicaid lottery:
    - increased mental health
    - no impact on cholesterol, other physical health measures
- reduced financial stress
- less likely to incur medical expenses
- but: also increased costs
- some people in control group received medicaid anyways
    - how would this impact results?
- was the policy a success?

### summary
[ fill in ]

### threats to experimental validity
- internal validity: did we estimate an unbiased causal effect for our sample?
    - fails when treatment and control groups are difference in ways that affect the outcome
    - non-complicance: some people in treatment group don't receive treatment, some people in control group do receive treatment
    - attrition: some people in treatment group drop out, some people in control group drop in
    - evaluation-driven effects: people in treatment group change behavior because they know they're being studied
- external validity: can we extrapolate these estimates to other populations? to whom can we generalize?
    - fails when the treatment effect is different outside the evaluation context
    - non-representative sample, non-representative program (implementation differences), scaling effects

### evaluation-driven effects
- being part of an evaluation can change the way people behave, separate from the impacts of the program itself.
1. hawthorne effect
    - overestimate effects
    - people in treatment group works harder than normal.
    - e.g. student randomly assigned scholarship might work especially hard because they're been given an opportunity, if scholarships are given to all eligible students, effort may be lower.
2. john henry effect:
    - underestimate effects
    - comparison group competes with treatment group
    - e.g. students in control group work harder because they're competing with students in treatment group
3. resentment/demoralization effects
    - overestimate effects
    - comparison group members behave in ways that worsen outcomes.
4. demand effects
    - unclear which direction this would bias
    - people in treatment group change behavior because they know they're being studied
    - e.g. students in treatment group work harder because they know they're being studied
5. anticipation effects:
    - unclear which direction this would bias
    - comparison group changes behavior because they think they will receive program in the future.
        - e.g. comparison group in micro-finance program might take out other loans, expecting to repay them with micro-finance loan.

### evaluation-driven effects
how do we limit these effects?
1. make interaction with evaluation staff as equal as possible across treatment and control groups
2. randomize at a higher level
    - limit treatment-comparison interactions: competition, anticipation, demoralization
3. announce phase-in
    - limit demoralization effects
4. do not announce phase-in

### partial compliance
1. individuals in treatment do not receive treatment
    - some students assigned to training never show up
    - some parents whose children are assigned deworming pills refuse consent
    - impassable roads in rainy season precent program from delivering fertilizer to some farmers in time
2. individuals in treatment group do not complete treatment course
    - students in training drop out after a few sessions
    - farmers in fertilizer program save fertilizer for next year

### partial compliance ("control crossover")
3. individuals in comparison group receive treatment
    - some people in comparison may have been receiving program already
        - e.g. some parents already giving children deworming pills
    - some individuals may move to a treatment group location
        - e.g. transfer children to school with after school education program
    - outside actors may deliver treatment to individuals in comparison group
        - e.g. another NGO may come in and decide to distribute mosquito nets through some of the clinics that in comparison group of our own programs.
**- these tend to bias estimates towards zero**

### partial compliance
why is this a problem
- reduce difference between treatment and control groups in terms of program exposure, which will bias estimates toward zero.
- will return to issue of non-compliers later

how do we limit it?
1. make take-up of program easy (e.g. avoid complicated application process)
2. incentiviize program take-up (provide small incentive to take-up program, but not large enough to affect program)
3. randomize at a higher level (reduce likelihood of exposure to program outside of evaluation)

### attrition
occurs when outcome cannot be measures for some study participants
1. individuals drop out of experiment and can no longer be measured
    - move out of area, withdraw cooperation, die

why is this a problem?
- can bias estimates by reducing comparability of treatment and control groups
    - if rates OR type of attrition differ between treatment and control groups
- statistical power
    - reduce sample size
    - if attrition is non-random (more people leaving from treatment or control)

[fill in other slides here ]

### how to limit
1. improve data collection
2. use a resedarch design that promises access to program to all eventually (phase-in design)