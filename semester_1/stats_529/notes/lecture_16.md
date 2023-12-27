## $\chi^2$ test of indendence  

- assumption: we have a random sample with two categorical variables 
-  assumpetion: there is an expected frequency of at least 5 cases in every cell.  

-  $H_0$: the variable are independenct  
-  $H_a$: the variables are not independent  

### testing for independence 

- the $\chi^2$ test measures deviation of observed frequencies from expected.  
-  the expected freqs are those we **should** see if x and y are statistically independent.  
-  label the observed frequencies $f_o$, label the expected frequencies $f_e$  
-  the $\chi^2$ test statistic captures the overall deviation of $f_o$ from $f_e$ in all the interior cells of the table.  

### calculating the expected frequency  

$$
f_e = \frac{(row total) \cdot (column total)}{n}
$$

this calculation gives us the expected cell frequency if the row proportions down the column are the same as the overall row proportion  

### Calculating the $\chi^2$ statistic  

The $\chi^2$ statistic is a way to sum the deviations of $f_e$ and $f_o$ for all the interior cells. The formula is:  

$$
\chi^2 = \sum\frac{(f_o - f_e)^2}{f_e}
$$

For each cell, we square the deviation between $f_o$ and $f_e$ and divide the result by $f_e$. We then add up theve. the resulting numbers.  

### interpresting the $\chi^2$ statistic  

-  just like the other test statistics, the $\chi^2$ refers to a distribution.  
-  unlike the other test statistis, a $\chi^2$ is not negative. the bigger the $\chi^2$, the stronger the evidence for rejecting $H_0$. $\chi^2 = 0$ means  all $f_e$ and $f_o$ are equal.  

-  like the t distribution, the shape of the t 