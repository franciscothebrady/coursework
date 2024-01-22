* problem set 1 
* francisco brady 

* part 1
use assignment1race, clear

// create college variable 
gen college = 1 if education == 4
//tab college
replace college = 0 if college == .
//tab college

* test each variable for equal variance 
// college yearsexp linc
foreach var in college yearsexp linc {
	sdtest `var', by(race)
}
