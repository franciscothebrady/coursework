## linear regression part 2

R-squared and Adjusted R-squared:  
- adjustment corrects for the mechanical increase in R-squared that occurs every time a predictor is added to the model.  
- R-squared and adjusted R-squared are both reported in regression output from R and Stata 

### Root MSE or the Standard Error of the Estimate  
- The estimate is the predicted value of the estimate ($\hat{y}$)
- On average,m by how far is out estimate wrong? 
> when we are trying to predict Y using X, on average we are wrong by this amount.  

### similarities to ANOVA  

- if we ran a regression with a dichotomous independent variable, the results would be similar to the output from ANOVA.  
- between-group variance from ANOVA would be similar to the ESS output from linear regression 
- the "within-group variable" from ANOVA would match the SSE output from linear regression.
- the $R^2$ from both would be the same  

### the f-test
- think of this as the statistical significance of the model as a whole 
- the t statistics are for individual coefficients, the F test is for all of them working together. 
- together with the F test, Stata reports an associated p-value  


