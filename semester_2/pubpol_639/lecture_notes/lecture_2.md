## 2024-01-16

Causal Inference 1

Use the mixtape instead of mastering metrics

### today
- causal v. descriptive question
    - importance of establishing causality
- how do we design ideal experiments?
    - how do we get as close as possible to this ideal
- the selection problem and the fundamental problem of causal inference
    - example: health insurance

### waht is causla inference?
- key focus of the course
    - what does this mean
- inference: a conclusion reached on the basis of evidence and reasonning 
- causal inference: a conclusion about a casue and effect relationship
    - if you change x, what happens to y?
- this is different from statistical inference
    - what can we conclude about the population from a sample?
    - we will use statistical inference to help us with causal inference

### causal inference
- causal relationships are teh bread-and-butter of policy
- causal questions:
    - do smaller classes improve learning?
    - does job training reduce unemployment spells?
    - does the pell grant increase college enrollment?

### four key questions (from MHE)
1. what is the causal relationship of interest
2. what is the ideal experiment?
3. what is the identification strategy (or research method)
4. what is the mode of statistical inference?

### what is not a causal research question?
still potentially important descriptive things!
- have health insurance premiums increased over time?
- is air pollution worse in poor areas?
- has teen smoking increased or decreased since the 1970s?
- how many children are in $2/day poverty and has this risen?
> this is what matters for policy! 
    - can be turned into a causal question with some tweaks to the research question

### what is a causal question? 
- would lowering prices increase health care utilization?
- what is the effect of air pollution on health?
- does youth smoking increase mortality risk?
- would increasing the minimum wage reduce extreme poverty among children?

### how to determine if something is a coherent causal question
- could you devise an experiment to answer the question?
- many exp[erinments are conceivable but may not have occurred
    - imagine you have unlimited resources and no morals (for this mental exercise only)
- Examples:
    - class size: randomly assign some kids to small classes and others to large classes
    - health insurance: randomly assign medicaid eligibility

### does starting school improve academic achievement
- randomly assign some kids to start 1st grade at age 6 and others to start at age 7
- supposed you test each group when it finishes 1st grade
    - the 7-year-old group will be older at the time of the test, and we know age influences brain development
- suppose you test each group at age 8
    - the "effect" of starting school with always be confounded with age. 

### qwhy is causal inference challenging in many cases 
answer: the selectino problem!! (and other sources of bias)

### why do we care
- it's not enough to establish a correlation
    - we want to know if x causes y
- this has policy implications
    - if we're investing money intended to improve a specific outcome, we want to know if it will work.

### understanding the selection problem
example: effect of health insurance on health
- does health insurance make people healthier?
- compare the health of people with and without health insurance:
    - outcome: health
    - treatment: insurance
        - treatment group has insurance
        - control group (or comparison group) has no insurance
            - control group is technically only for randomized experiments. in observational studies, use "comparison group"
- "a good control group reveals the fate of the treated in a counterfactual world where they are not treated." (MM)

### health insurance in the US
- no universal health insurance

### data 
- national health interview study
    - 2009 survey, health status
    - health status 0-5 (0 = poor, 5 = excellent)
    - descriptive stats indicate that those with health insurance report better health.

### causal? 
- given what you know about US health insurance:
    - why might some people have health insurance and others not?
    - is this a positive bias or a negative bias?

### potential sources of bias:
- those w/ health insurance tend to have higher incomes
    - overestimates the effect of health insurance
- those with health insurance tend to be older
    - underestimates the effect of health insurance

### formalizing this intuition 
- Y_i = outcome (health status of person i)
- D_i = treatment (whether person i has health insurance)
    - D_i is a binary variable
    - D_i = 1 if person i has health insurance,
    - D_i = 0 if person i does not have health insurance
We are trying to imagine what would happen to the health of a given person i if she had insurance (D_i = 1) versus if she did not have insurance (D_i = 0)
$$
Potential Outcome = Y_i(1) if d_i = 1
Y_i(0) if d_i = 0
$$
- subscript 1 indicates different potential states of the world
- subscript 2 indicates people
- some more notation for the actual observed outcome in potential outcomes framework
    - Make $D_i$ either 1 or 1 to get the correct $Y_i$

### the causal effect of interest
- causal effect of insurance on person i
$$
\alpha_i = Y_1i - Y_0i
$$
- problem: cannot observe *both* $Y_1i$ and $Y_0i$
    - individuals either have insurance or they don't
    - time machine would be helpful
        - give person i insurance and then take it away

### what can we do?
- we can compare the outcomes of different individuals in different states:
$$
E[Y_i|D_i = 1] - E[Y_i|D_i = 0]
$$
- this is the observed difference in average health
- this creates another problem!

### decomposing the difference
- this observed difference can be decomposed into two parts (A and B)
$$
E[Y_i|D_i = 1] - E[Y_i|D_i = 0] \\ = E[Y_1i|D_i = 1] - E[Y_0i|D_i = 1] + E[Y_0i|D_i = 1] - E[Y_0i|D_i = 0]
$$
Or: 
$$
\text{observed difference} = \text{average treatment effect on the treated} + \text{selection bias}
$$

### Term A: What we want 
Effect of treatment effect on the treated:
$$
E[Y_1i|D_i = 1] - E[Y_0i|D_i = 1]
$$
- this is the effect of insurance on those who have insurance

### Term B: Selection Bias
$$
E[Y_0i|D_i = 1] - E[Y_0i|D_i = 0]
$$

### what we have: A+B
$$
E[Y_i|D_i = 1] - E[Y_i|D_i = 0] = E[Y_1i|D_i = 1] - E[Y_0i|D_i = 1] + E[Y_0i|D_i = 1] - E[Y_0i|D_i = 0]
$$

### where does this bias come from 
- difference in "baseline"
    - difference in average Y_0i between those with and without insurance

### undet what conditions is there no selection bias? 
- if Y is "independent" of D
- mean of Y is the same for all values of X
- E(Y) = E(Y|D = 0) = E(Y|D = 1)
