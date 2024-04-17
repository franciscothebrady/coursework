## 2024-04-02

### Difference-in-Differences

### Today
- Discussion of difference-in-differences analysis
- Discussion of Currie and Walker (2011) "Traffic Congestion and Infant Health: Evidence from E-ZPass"
#### Background
- Gas-powered cars are a major source of air pollution
- Traffic congestion is also a major concern
- Currie and Walker (2011) study the impact of traffic congestion on infant health
- How a policy that's intended to reduce traffic congestion can affect infant health.

### Causal Question of Interest
- How does a policy to reduce traffic congestion affect infant health?
    - pollution is bad for health

### Ideal Experiment
- How would you design an ideal experiment to answer the causal question of interest?
    - randomly assign exposure to traffic congestions on pregnant women, and asses differences in infant birth outcomes.
- What are some concerns and limitations with implementing an experiment of this type?
    - ethical concerns: unethical to knowingly expose pregnant women to things that are unhealthy on purpose.

- Why can't we just observe the outcomes of pregnant women who live in more congested areas to those who live in less congested areas?
    - selection bias: people who live in more congested areas might be different from those who live in less congested areas.
    - Congestion is likely correlated with lots of other factors that might impact health.

### Assume a simple regression of infant health on air pollution produces a negative relationship
- How might a simple comparison of outcomes for those located in more congested vs. less congested areas overestimate the negative effects of pollution on birth outcomes?
    - farther out areas could be cheaper to live in and a proxy for income, which could be associateds with worse health outcomes.
- How might a simple comparison of outcomes for those located in more congested vs. less congested areas underestimate the negative effects of pollution on birth outcomes?
    - rural areas might have less congestion but less access to healthcare.

### Empirical Strategy
- Since an experiment is not possible in this scenario, the authors make use of a natural experiment that resulted in less traffic congestion to examine the impact of air pollution on infant birth outcomes.
- Authors use a difference-in-differences analysis to investigate this question.
- What are the two differences used in the study?
    - Pre/Post: Before and After E-ZPass introduction in NJ and PA.
    - Treatment/Comparison: Women living within 2 kilometers of a toll plaza (treatment) and women living between 2 and 10 kilometers of a toll plaza (and also within 3 kilometers of a highway) (comparison).

|       | Pre-E-ZPass     | Post-E-ZPass   |
|-------|-----------------|----------------|
|Close  | High Congestion | Low Congestion |
|Farther| Low Congestion  | Low Congestion |

### Empirical Strategy, cont.
- The authors estimate equations of the following form:
$$
Outcome_{it} = a + b_1 E-ZPass_{it} + b_2 Close_{it} + b_3 Plaza_{it} + b_4 E-ZPass_{it} \times Close_{it} + b_5 Year + b_6 Month + b_7 X_{it} + b_8 Distance_{it} + e_{it}
$$
- Where the outcome of interest is represented for each individual mother (i) in time (t). (e.g.g low birth weight, premature birth)
- E-ZPass is a time-varying indivator for whether E-ZPass is in place in time t (similar to a pre/post indicator).
- Close is an indicator for whether the mother lived near the E-ZPass toll plaza. (similar to an indicator for treatment).
- Other controls in the model to account for geographic-specific controls, time trends (year fixed effects), and seasonal patters (month fixed effects).

### Threats to identification
- What are the key potential threats to identification in this analysis?
- What do the authors do to address these concerns:
    - show that EZ pass adoption does not affect demographic characteristics of mothers; does not appear to impact housing prices.
        - evidence that EZ pass adoption does not change the composition of individuals treated over time, which could also lead to change in birth outcomes.
    - examine trends in observable characteristics of mothers in the treated group versus the comparison group before and after the introduction of E-ZPass.

### Results
- What are the main results of the study?
    - The introduction of E-ZPass reduced premature births by 0.86 percentage points, and low birth weight by 0.94 percentage points.
    - The authors conduct a number of robustness checks to ensure the results are not driven by other factors.
        - Mother fixed effects
        - Time trends
        - Seasonal patterns
        - Other geographic controls


### Discussion