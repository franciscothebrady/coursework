capture log close
log using "ps1", smcl replace
//_1
display c(current_date)
//_2
*set graphics off
use solis_dataset.dta

//_3

//_4

//_^
log close
