* problem set 1 
* francisco brady 

* log
capture log close
log using ps1_log, text replace 


* part 1
  
  use assignment1race, clear

// create college variable 
gen college = 1 if education == 4
//tab college
replace college = 0 if college == .
//tab college
label variable college "indicator for college attendance (education >= 4)"

* test each variable for equal variance 
// college yearsexp linc
foreach var in college yearsexp linc {
	display "`var'"
	sdtest `var', by(race)
}

* since p-value for alternative hypothesis is > .05, we cannot reject null hypothesis that the variances are equal

* ttests 
foreach var in college yearsexp linc {
	display "`var'"
	ttest `var', by(race)
}

* ttests for subgroups
foreach var in college yearsexp linc {
	display "`var'"
	ttest `var' if military == 1, by(race)
}

// callback rate by race 
 ttest call, by(race)
// military subsample
ttest call if military == 1, by(race)

// charter school dataset
use 

* create table with means 
//preserve
//collapse 
//estpost ttest college yearsexp linc, by(race)
*esttab, mtitle("diff") // gives the difference with the t-stat below  
//esttab , cell((mu_2 mu_1 t(star) ))
estpost ttest college yearsexp linc, by(race)
esttab , noobs cells("mu_1(star fmt(3)) mu_2(star fmt(3)) b(star fmt(3)) se(fmt(3)) t(fmt(3))") star(* 0.1 ** .05 *** 0.01) ///
collabels("Black Mean" "White Mean" "Difference of Means" "Std. Error of Difference" "t-stat")


use mich_charters_2014, clear
estpost ttest per_fl per_as per_hi per_bl per_wh pp_curr_opp_exp, by(charter) unequal 
esttab ., noobs cells("mu_1(star fmt(3)) mu_2(star fmt(3)) b(star fmt(3)) se(fmt(3)) t(fmt(3))") star(* 0.1 ** .05 *** 0.01) collabels("Public School" "Charter" "Difference of Means" "Std. Error of Difference" "t-stat")


// part 4 


// close log
log close
