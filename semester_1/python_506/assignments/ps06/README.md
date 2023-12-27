# SI 506: Problem Set 6

## This week's Problem Set

This week's problem set will focus on reading and writing CSV files, creating and using functions,
and using the `main()` function.

## Background

You will be working with election data! Midterm elections were held in the United States on
November 8, 2022. Though the US President was not on the ballot, midterms are still important
elections since many state and local officials and proposals are on the ballot.

In Michigan, three (3) important proposals were on the ballot, allowing citizens to directly affect
the future of Michigan's state laws.

These were:

- Prop 1 - Voters for Transparency and Term Limits
- Prop 2 - Promote the Vote 2022
- Prop 3 - Reproductive Freedom for All

Learn more [here](https://www.bridgemi.com/michigan-government/2022-michigan-ballot-issues-tracker-what-know-about-election-proposals).

## Data

You have been provided with two (2) files that contain election-related data for Washtenaw
county (where Ann Arbor is located).

- `data-washtenaw_registered_voters.csv`: Each row contains the county, city or township name (both
  referred to simply as 'city' or 'unit'), voting equipment, number of precincts (smaller
  divisions within the city), registered voters, and active voters for a city in Washtenaw
  county in August 2022.

- `data-washtenaw_2022_election_results.csv`: The 2022 Michigan Midterm election occured in November.
  Each row contains a lot of information, but notable attributes are the election date, office code,
  county name, office description, party name, party description, candidate last name, candidate
  first name, and candidate votes.

<br />

## Template scaffolding

:exclamation: The template includes several function definitions. The functions are arranged in
**alphabetical** order by name. During this assignment, you will be asked to define additional
functions. We encourage you to maintain the current alphabetical order by inserting each new
function between existing definitions.

:exclamation: It is important to note that not all the information you need to correctly implement this problem set will be in the README. Much of this information will be in the provided function docstrings.

<br />

## Problem 01 (10 Points)

**Task:** Re-order the statements and expressions in the `read_csv()` function block so that
the function can interact with a file object and return data to a caller.

The function `read_csv()` is defined for you, but several lines of code are ordered incorrectly.

1. Review the function's docstring to better understand the task it is to perform, the parameters it
   defines, and the return value it computes.

2. Uncomment the function definition. Reorder the lines of code so that they follow the function
   logic correctly.

   :exclamation: Remove the `pass` statement once you have working code.

3. After fixing `read_csv()`, proceed to the `main()` function.

4. Create a `Path()` instance to construct an **absolute** path to this `*.py` file's parent
   directory. Assign the path to a variable named `parent_path`.

   :bulb: The `pathlib` module has already been imported for you.

5. Leverage the appropriate `Path()` method to construct an **absolute** path to
   `data-washtenaw_registered_voters.csv` by using the appropriate method to join the
   `parent_path` with the file name. Assign the absolute path to a variable named `voters_path`.

6. Call `read_csv()` and pass to it the argument `voters_path`. Assign the return value to a
   variable named `registered_voters`.

   :exclamation: Do **not** conduct any data cleaning in the `read_csv()` function.

   Uncomment the assert statement. Your `registered_voters` list must match the structure of `registered_voters_check` list.

7. While still in `main()`, leverage the appropriate `Path()` method to construct an **absolute**
   path to `data-washtenaw_2022_election_results.csv` by leveraging the appropriate method to join
   the `parent_path` with the file name. Assign the absolute path to a variable named
   `election_path`.

8. Call `read_csv()` and pass to it the argument `election_path`. Assign the return value to a
   variable named `election_results`.

   :exclamation: Do **not** conduct any data cleaning in the `read_csv()` function.

   Uncomment the assert statement. Your `election_results` list must match the structure of `election_results_check` list.

9. While still in `main()`, assign the "headers" from `registered_voters` to a variable named
   `registered_headers`. Reassign `registered_voters` to a list slice that excludes the headers and uncomment the assert statement to check.

10. Do the same for `election_results`, creating `election_headers` and `election_results`,
    respectively, and uncomment the assert statement to check.

:exclamation: `registered_headers` and `registered_voters` _must_ have no lists in common. Same
for the election results lists.

<br />

## Problem 02 (5 Points)

**Task:** Implement a function that accepts a `str` element and attempts to convert it to an
integer.

1. Implement a function named `convert_to_int()`. Review the function's docstring regarding its
   expected behavior, parameters, and return value (if any).

   **Requirements**

   1. Utilize `try` and `except` statements to attempt to cast the passed in `value` element to
      an integer. Return the converted element.

   2. If the `value` element cannot be converted to an `int`, return the value unchanged.

   :exclamation: You _must_ explicitly return the `value` element regardless of whether it can be
   converted.

2. After defining the function, navigate to `main()` and uncomment the `assert` statements
   to check your work.

<br />

## Problem 03 (10 Points)

**Task:** Implement a function that accepts a `str` element and an optional substring value to be
trimmed from the element.

1. Implement a function named `trim_str()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value (if any).

   **Requirements**

   1. Utilize `try` and `except` statements to attempt to remove any leading and trailing substrings
      from the `value`.

   2. Check if a `substring` argument was passed to the function by the caller. If a `substring`
      argument was passed, use an appropriate string method to trim that `substring` from the beginning
      and end of the `value`. Return the trimmed `value`.

   3. If no `substring` argument was passed, use an appropriate string method to trim any leading and
      trailing spaces (`' '`) from the beginning and end of the `value`. Return the trimmed `value`.

   4. If the `value` cannot be trimmed because it is the incorrect type, return the `value`
      unchanged.

   :exclamation: You _must_ explicitly return the `value` element regardless of whether a substring
   is passed to the function or whether the `value` can be successfully trimmed.

2. After defining the function, navigate to `main()` and uncomment the `assert` statements to
   check your work.

<br />

## Problem 04 (25 Points)

**Task:** Implement a function that "cleans" a list of `str` elements by leveraging the two (2)
utility functions defined in Problems 2 and 3.

1. Implement a function named `clean_data()`. Review the function's docstring regarding its expected
   behavior, parameters, and return value (if any).

   **Requirements**

   1. Iterate over a list of `str` elements utilizing the `range()` type `for` loop.

   2. Check whether the date requires trimmming. If `strip=True`, call the appropriate utility
      function passing to it the correct arguments, including each element of the passed in list.
      Assign the element back to its original position.

   3. If `strip=False`, call the appropriate utility function to attempt to convert each element of
      the list to an `int`. Assign the element back to its original position.

   :exclamation: This function _must_ explicitly return a "cleaned" list.

2. After implementing the function, return to `main()`.

3. Loop over the `registered_voters` list utilizing the `range()` type and call `clean_data()` on
   each nested list, making sure to assign each "cleaned" list element back to its original
   position.

4. Then, loop over the `election_results` utilizing the `range()` type and call `clean_data()` on
   each nested list. Pass the appropriate arguments so that you do not end up with any negative
   integers as `CandidateIDs`. Ensure you are assigning each "cleaned" list element back to its
   original position.

   :exclamation: Use the correct _keyword arguments_ when passing in arguments to the optional
   parameters.

   Uncomment the assert statement. Your `election_results` list must match the structure of
   `election_results_check_2` list, if your `clean_data()` has been
   implemented correctly.

<br />

## Problem 05 (40 Points)

**Task:** Implement a function that accepts a `str` representing a single column's name, a `list` of
column headers, and a `list` of nested lists representing election data, in order to locate the
list(s) with the smallest value for the specified column.

1. Implement a function named `find_min_values()`. Review the function's docstring regarding its
   expected behavior, parameters, and return value (if any).

   **Requirements**

   1. Create a variable named `smallest_value` and assign the Pythonic expression for infinity to
      it.

   2. Create an empty list and assign it to the variable `smallest_unit`.

   3. Use the `list.index()` method on `headers` to determine the index values throughout.

   4. Use an `if-elif` statement as a method for handling potential ties.

   5. Append the **entire** "row" that contains the `smallest_value` to the list named
      `smallest_unit`.

2. After defining the function, navigate to `main()`.

3. Call `find_min_values()`. Pass to it the
   appropriate arguments to determine the cities/townships in the `registered_voters` list with
   the fewest precincts. Assign the return value to a variable named `fewest_precincts`.

4. Uncomment the `assert` statement. The `fewest_precincts` list _must_ match the `fewest_precincts_check` list.

5. Call `find_min_values()` once again and pass to it the appropriate arguments to determine the
   candidate(s) in the `election_results` list with the fewest `CandidateVotes`. Assign the return
   value to a variable named `fewest_votes`.

6. Uncomment the `assert` statement. Your `fewest_votes` list _must_ match the `fewest_votes_check` list.

<br />

## Problem 06 (45 Points)

**Task:** Define two (2) functions that accept a `list` representing a voting precinct and
calculate the city or township in Washtenaw County that has the highest percentage of active
voters (based on the total registered). Then loop through a list of cities or townships in
Washtenaw County to locate the most active unit.

1. Define a function named `get_active_voters()` provisioned with two (2) parameters:

   - `data` (list): a list of elements that describe voter registration data for one city or
     township.

   - `percent` (Bool): Default False. If True, return the calculation as a percentage instead of a
     decimal value.

   **Requirements**

   1. Access the 'active_voters' and 'registered_voters' elements for the city or township,
      utilizing **negative** indexing.

   2. **Return** the percentage of registered voters for the city or township that are active
      (`float`), if `percent=True`. Otherwise, return the calculated value as a decimal (`float`)
      only.

   3. Round the calculated _percentage_ value to **one (1)** decimal place and round the calculated
      _decimal_ value to **two (2)** decimal places.

   :exclamation: You do **not** need to use `list.index()` or the headers in this function
   definition.

2. After defining the function, navigate to `main()`.

3. Uncomment the `assert` statements to check your work before moving onto the next function
   definition.

4. Next, Define a function named `find_most_active_unit()` provisioned with the same parameters as
   `get_active_voters()`:.

   The function _must_ `return` a two-item tuple ordered as follows:

   - `most_active_unit` (list): a list of the city/township name(s) of the unit(s) with the most
     active voters, as a percent of registered voters.

   - `highest_percent` (int): the percent of registered voters that are active in the most active
     unit.

   **Requirements**

   1. Assign zero (`0`) to a variable named `highest_percent`.

   2. Create an empty list and assign it to the variable `most_active_unit`.

   3. Loop over the data and call `get_active_voters()` to determine the `percent_active` for each
      unit/city.

   4. Use an `if-elif` statement as a method for handling potential ties.

   5. Append the "city_township" **name only** of the unit with the `highest_percent` to the
      `most_active_unit` list.

   6. Return a tuple comprising `most_active_unit` and `highest_percent`.

5. After defining the function, return to `main()`.

6. Call `find_most_active_unit()` on `registered_voters` and **unpack** the tuple that is returned
   into the variables `most_active_unit` and `percent`, respectively.

7. Uncomment the print and assert statements. Your `most_active_unit` _must_ match `most_active_unit_check` and your `percent` _must_ match `percent_check` as provided in the setup code.

<br />

## Problem 07 (60 Points)

**Task:** Define a function that accepts a `list` of election results data, a list of column
`headers`, and an `office_code`, in order to determine how many votes were cast for various
political parties.

1. Define a function named `get_votes_by_party()` provisioned with three (3) parameters:

   - `results` (list): A list of lists, each containing a candidate's information from the 2022
     primary (e.g., name, office, office code, party name, number of votes).

   - `headers` (list): A list containing the headers from the primary election results data.

   - `office_code` (int): the office code for the different offices up for election during the
     November general election, such as code '2' for Governor.

   The function _must_ return a _four-item_ tuple ordered as follows:

   - `democratic_votes` (int): the number of votes cast for Democratic candidates
     for this position.

   - `republican_votes` (int): the number of votes cast for Republican candidates
     for this position.

   - `libertarian_votes` (int): the number of votes cast for Libertarian candidates
     for this position.

   - `green_votes` (int): the number of votes cast for Green Party candidates
     for this position.

   **Requirements**

   1. Assign zero (`0`) to variables named `democratic_votes`, `republican_votes`,
      `libertarian_votes`, and `green_votes`.

   2. Loop over the `results` list.

   3. Use `headers` and `list.index()` throughout to help with indexing.

   4. If the 'OfficeCode(Text)' matches the `office_code` and the 'PartyName' is 'DEM', add the
      count of 'CandidateVotes' to `democratic_votes`.

   5. If the 'OfficeCode(Text)' matches the `office_code` and the 'PartyName' is 'REP', add the
      count of 'CandidateVotes' to `republican_votes`.

   6. If the 'OfficeCode(Text)' matches the `office_code` and the 'PartyName' is 'LIB', add the
      count of 'CandidateVotes' to `libertarian_votes`.

   7. If the 'OfficeCode(Text)' matches the `office_code` and the 'PartyName' is 'GRN', add the
      count of 'CandidateVotes' to `green_votes`.

   8. Return a tuple comprising all four variables in the order indicated above.

2. After defining the function, return to `main()`.

3. Underneath the provided list fixtures, loop over `vote_totals` using a range() type loop. Call `get_votes_by_party()` and
   pass to it the `election_results`, `election_headers`, and each element's "Office Code" as
   arguments. Assign each element in the return value to an appropriate variable, utilizing
   _iterable unpacking_. Append _each_ returned value for _each_ party to `vote_total`, ensuring
   that you are appending the votes counts in the correct order.

4. Uncomment the `assert` statement. The final `vote_totals` `list` of nested lists _must_ match the `vote_totals_check` list.

<br />

## Problem 08 (5 Points)

**Task:** Write the _updated_ `vote_totals` list to a new CSV file.

1. Review the `write_csv()` function's docstring regarding its expected behavior, parameters, and
   return value. The function has been defined and implemented for you.

2. In `main()` call `write_csv()` using the `vote_totals_headers` element as the `headers` argument
   and write the data in `vote_totals` to a new file named `stu-election_votes_by_party.csv`.

   :exclamation: Use the correct _keyword argument_ when passing in the "headers" element. Do
   **not** use keyword arguments for the other two arguments when calling the function.
