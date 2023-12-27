# SI 506 Week 10 Bonus Challenges

## Gradescope URL

[https://www.gradescope.com/courses/569572](https://www.gradescope.com/courses/569572)

:bulb: You can resubmit your solution as many times as needed until the submission period expires.

## Code formatting

The autograder assumes that you have formatted your code submission(s) using VS Code's Black
Formatter extension and that you have set the maximum `line-length` to 100 characters. See the VS
Code [install guides](https://si506.org/guides/) for set up instructions.

## Challenge 04

__Task__: Create a `keyword_values` dictionary consisting of empty list values that will later be
used to hold the associated keyword values. Then, write the dictionary to a JSON file.

bulb: The goal is to create a dictionary comprising the following key-value pairs. See the fixture
file "fxt-nyt-keyword_values_v1.json" for the expected output.

1. In `main()` instantiate an instance of `Path`, passing to it the file named
   "data-nyt-articles-research.json". Ensure that the path object you create represents an
   __absolute__ path by calling the appropriate path method. Assign the variable `filepath` to the
   path object.

2. Call the function named `read_json()` and pass the argument `filepath` to it. Assign the variable
   `articles` to the return value (a list of article dictionaries).

3. Implement a nested loop.

   Outer loop: loop over each article in `articles`.
   Inner loop: loop over each article's "keywords" list.

   Inside the nested loop block, write an `if` statement that evaluates whether or not the keyword's
   "name" value is __a key__ in the accumulator dictionary `keyword_values`. If the "name" value
   (e.g., "subject") is __not__ found among the `keyword_values` keys, add a __new__ key-value pair
   to the target dictionary, structured as follows:

      * key = "name" value
      * value = `[]` (empty `list`)

4. Uncomment `write_json()` and write the `keyword_values` dictionary to a JSON file. Run your code.
   Review the file output against the appropriate fixture file. If the files match, submit your code
   to Gradescope.

## Challenge 05

__Task__: Populate the `keyword_values` dictionary with lists of unique keyword values. Then write
the dictionary to a JSON file.

bulb: See the fixture file "fxt-nyt-keyword_values_v2.json" for the expected output.

1. In `main()` __copy__ your Challenge 04 nested loop and __paste__ it below the Challenge 05 1.0
   comment.

   :bulb: Inside the inner loop consider accessing each keyword's "name" and "value" and assigning
   a variable to each. You will find it easier to work with the variables when adjusting the inner
   loop's conditional logic as specified below.

2. Inside the nested loop block, modify the existing conditional logic as follows:

   1. Adjust the current `if` statement block by replacing the empty list `[]` assignment with a
      list literal that contains the current keyword "value" as an element.

      :bulb: This action creates a new key-value pair in `keyword_values`.

   2. Add an `elif` statement that evaluates whether or not the current keyword "value" is a
      member of the `keyword_values[< some_name >]` list. If the value is __not__ a member of the
      the list whose key matches the "name" string __append__ the value to the list.

      :bulb: This action prevents duplicate values from being appended to each list in the
      `keyword_values` dictionary.

3. Sort the `keyword_values` keys and values by uncommenting the `keyword_values_sorted` variable
   assignment.

4. Uncomment `write_json()` and write the `keyword_values_sorted` dictionary to a JSON file. Run
   your code. Review the file output against the appropriate fixture file. If the files match,
   submit your code to Gradescope.

## Challenge 06

__Task__: Create a dictionary that holds keyword "value" counts. Populate the dictionary by
implementing a nested loop. Then write the dictionary to a JSON file.

:bulb: The goal is to adjust the nested loop code so that it can assign to each keyword "name" a
dictionary of key-value pairs that hold counts of the number of articles associated with each
keyword value. See the fixture file "fxt-nyt-keyword_value_counts.json" for the expected output.

1. In `main()` __copy__ your Challenge 05 nested loop and __paste__ it below the Challenge 06 1.0
   comment.

2. Change all the copied `keyword_values` variable references to `keyword_counts`.

3. Adjust the inner loop's conditional logic as follows:

   1. `if` statement: if `name` is __not__ a key in `keyword_counts` create a new `keyword_counts`
      key-value pair structured as follows:

      * key = "name"
      * value = a ___`dict` literal__ featuring "value" as the key and `1` as the value

   2. `elif` statement: if `value` does __not__ not match an existing `keyword_counts[name]` key
      assign a new key-value pair to the `keyword_counts[name]` dictionary:

      * key = `value`
      * value = `1`

   3. `else` statement: __increment__ `keyword_counts[name][value]` by `1`.

4. Sort the `keyword_counts` keys and values by uncommenting the `keyword_counts_sorted` variable
   assignment.

5. Uncomment `write_json()` and write the `keyword_counts_sorted` dictionary to a JSON file. Run
   your code. Review the file output against the appropriate fixture file. If the files match, submit
   your code to Gradescope.
