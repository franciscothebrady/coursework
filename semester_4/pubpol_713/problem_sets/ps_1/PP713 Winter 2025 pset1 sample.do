capture log close
log using pp713_assignment1_solns.txt, text replace

********************************************************************************
** PubPol 713 / Educ 714
** Assignment 2
** Author: Kevin Stange 
** January 2, 2025
********************************************************************************
* 
* be sure to load the rdrobust package in Stata first.
* you can type "search rdrobust" into stata. Then click the hyperlinks to install.

clear all
set more off
set linesize 200
*set graphics off
* Note: if you want to run it without displaying the graphs (but just saving them), 
* then  set graphics off

* Load data
use solis_dataset.dta

* Question 1. Generate key variables: dummy for passing threshold, dummy for pre-selected, re-centered running variable
gen m475t1=(psut1>=475)
label variable m475t1 "Indicator for scored above cutoff in year 1"


*** DO ALL THE OTHER GREAT STUFF HERE!!! ***



* End of program
log close
