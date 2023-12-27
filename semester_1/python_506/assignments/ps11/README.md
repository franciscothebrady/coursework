# SI 506: Problem Set 11

## This week's Problem Set

This week, we focus on modules and caching.
You will work with two Python files:

- `problem_set_11.py`: the main workspace
- `five_oh_six.py`: a module containing utility functions

## Data

The data used in this
assignment is sourced from the [Star Wars API](https://swapi.py4e.com/) (SWAPI) and
[Wookieepedia](https://starwars.fandom.com/wiki/Main_Page).

__Caching__: This assignment utilizes a local "cache" dictionary located in the utilities module
that eliminates redundant HTTP GET requests made to SWAPI by storing the SWAPI responses locally.
The caching workflow is implemented _fully_ and all you _must_ do is call the function
`get_swapi_resource()` whenever you need to retrieve a SWAPI representation of a person/droid,
planet, or starship.

:exclamation: _Do not_ call `utl.get_resource` directly. Doing so sidesteps the
cache and undercuts the built-in caching optimization strategy.

The cache dictionary is written to a JSON file every time you run `problem_set_11.py`:

```python
# PERSIST CACHE (DO NOT COMMENT OUT)
utl.write_json(utl.CACHE_FILEPATH, utl.cache)
```

The cache JSON document will remain empty until you start working on the problem set. Thereafter
the cache file will record resources retrieved from SWAPI.

## PROBLEM 01

__Task:__ Implement the function `read_csv_to_dicts()` in the `five_oh_six.py` file.

1. In `five_oh_six.py`, examine the commented out code in the `read_csv_to_dicts()` function
   (__do not__ uncomment). Reimplement the function by replacing the `pass` in the `with` block
   with code that retrieves an instance of `csv.DictReader` and employs a list comprehension that
   traverses the lines in the reader object and returns a new list of line elements to the caller.

   **Requirements**

      - You are limited to writing two (2) lines of code.
      - Line 01 assigns an instance of `csv.DictReader` to a variable named `reader`.
      - Line 02 returns a new list of `reader` `line` elements to the caller using
         __a list comprehension__.
      - You _must_ employ existing variable names that appear in the commented out code when
      writing your list comprehension (i.e., `reader`, `line`).

   :exclamation: Review lecture notes and code solution files if you have forgotten how to write
   a list comprehension. If you are unsuccessful in your endeavors, uncomment the code in
   `utl.read_csv_to_dicts` and get the function working so you can continue with the
   assignment.

2. After refactoring `read_csv_to_dicts()` in `five_oh_six.py`, navigate to `main()` in
   `problem_set_11.py`. Call the function `read_csv_to_dicts()`, accessed from the imported
   `five_oh_six.py` module using the alias `utl.`, and retrieve the data contained in the file
   `data-mandalorian_people.csv`. Assign the return value to a variable named `mandalorian_people`.

3. Call the function `read_json()`, accessed from the imported `five_oh_six.py` module using the
   alias `utl.`, and retrieve the data contained in the file `data-mandalorian_starships.json`.
   Assign the return value to a variable named `mandalorian_starships`.

4. Call the function `read_json()`, accessed from the imported `five_oh_six.py` module using the
   alias `utl.`, and retrieve the data contained in the file `data-mandalorian_planets.json`. Assign
   the return value to a variable named `mandalorian_planets`.

5. Call the function `read_json()`, accessed from the imported `five_oh_six.py` module using the
   alias `utl.`, and retrieve the data contained in the file `data-mandalorian_droids.json`. Assign
   the return value to a variable named `mandalorian_droids`.

6. Call the function `read_json`, accessed from the imported `five_oh_six.py` module using the alias
   `utl.`, and retrieve the data contained in the file `data-mandalorian_vehicles.json`. Assign the
   return value to a variable named `mandalorian_vehicles`.

:exclamation: After completing this problem, your `main()` should include __five__ (5) local
variables.

## PROBLEM 02

__Task__: Implement each of the `convert_to_*()` functions in `five_oh_six.py` and
`problem_set_11.py`. Each function attempts to convert a passed in `value` to a more appropriate
type or format.

1. For each `convert_*()` function in `five_oh_six.py` and `problem_set_11.py`, you will replace
   `pass` with a code block that attempts to convert the passed in `value` to the requested value
   type and format.

   :exclamation: Review each function's docstring to better understand the task it is to
   perform, the parameters it defines, and the return value it computes.

   :bulb: The five (5) `convert_*()` functions carry out the tasks of converting strings to
   either `int`, `float`, `list`, or `None`.

2. In `five_oh_six.py`, navigate to the `convert_to_none()` function definition. Replace `pass`
   with a code block that attempts to convert the passed in `value` to `None`. Review the
   function's docstring to better understand the task it is to perform, the parameters it defines,
   and the return value it computes.

   **Requirements**

   - The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
     whenever an invalid type conversion is attempted. __Do not__ place code outside the
     `try`/`except` code blocks.

   - The function _must_ perform a __case-insensitive__ comparison between the passed in `value`
     and the items in the passed in tuple `convert`.

   - If a match is obtained inside the `try` block the function will immediately return `None` to
     the caller, otherwise, the value will be immediately returned unchanged.

      :exclamation: You may assume `convert` is "clean"; however, do not assume that `value` is
      "clean". Program defensively and remove leading/trailing spaces before checking if the
      "cleaned" version of the string matches elements in the `convert` tuple.

   - If a runtime exception is encountered the `except` block will "catch" the exception and the
     `value` will be returned to the caller _unchanged_.

     :bulb: You do not need to specify a specific exception in the `except` statement.

   - After implementing the function, navigate to Problem 02 in `main()` and uncomment the first
     three (3) `assert` statements to check your implementation.

3. In `five_oh_six.py`, navigate to the `convert_none_values()` function definition. Replace `pass`
   with a code block that attempts to convert each value in the passed in `data` to `None` by
   leveraging the function `convert_to_none()`. Review the function's docstring to better
   understand the task it is to perform, the parameters it defines, and the return value it
   computes.

   **Requirements**
   - The function _must_ employ a dictionary comprehension in
      one line of code which loops over
      the items of a passed in `data` dictionary. Within the
      loop, the function calls `convert_to_none()` and
      attempts to transform `values` matching any of the
      strings found in the `convert` tuple from within a
      dictionary comprehension.

   - The function _must_ assign each converted value back to
      its existing key and immediately return the new
      dictionary produced by the comprehension.

   - After implementing the function, navigate back to
      Problem 02 in `main()` and uncomment the
      next two (2) `assert` statements to check your
      implementation.

4. In `five_oh_six.py`, navigate to the `convert_to_float()` function definition. Replace `pass`
   with a code block that attempts to convert the passed in `value` to a `float`. Review the
   function's docstring to better understand the task it is to perform, the parameters it defines,
   and the return value it computes.

   **Requirements**

   - The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
      whenever an invalid type conversion is attempted. __Do not__ place code outside the
      `try`/`except` code blocks.

   - If a runtime exception is encountered the `except` block will "catch" the exception and
     immediately return the `value` __unchanged__.

      :bulb: You do not need to specify a specific exception in the `except` statement.

   - After implementing the function, navigate back to Problem 02 in `main()` and uncomment the
     next three (3) `assert` statements to check your implementation.

5. In `five_oh_six.py`, navigate to the `convert_to_int()` function definition. Replace `pass` with
   a code block that attempts to convert the passed in `value` to an `int`. Review the function's
   docstring to better understand the task it is to perform, the parameters it defines, and the
   return value it computes.

   **Requirements**

   - The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
     whenever an invalid type conversion is attempted. __Do not__ place code outside the
     `try`/`except` code blocks.

   - The function _must_ convert numbers masquerading as strings, including those with commas that
     represent a separator:

      - "5" -> 5
      - "50,000" -> 50000
      - "5,000,000" -> 5000000

      :bulb: Try to leverage one of the `convert_to_*()` functions you have already implemented
      to achieve this task and reduce repeated code.

   - If a runtime exception is encountered the `except` block will "catch" the exception and
     immediately return the `value` __unchanged__.

   - After implementing the function, navigate back to Problem 02 in `main()` and uncomment the
     next three (3) `assert` statements to check your implementation.

6. In `five_oh_six.py`, navigate to the `convert_to_list()` function definition. Replace `pass`
   with a code block that attempts to convert the passed in `value` to a `list` using a
   `delimiter` if one is provided. Review the function's docstring to better understand the task
   it is to perform, the parameters it defines, and the return value it computes.

   :bulb: Model `convert_to_list()` after the other type conversion functions. This challenge
   involves adjusting your implementation per the hints below so that the function can handle
   converting strings to lists or return the passed in value _unchanged_ if a runtime exception
   is encountered.

   **Requirements**

   - The function _must_ employ `try` and `except` statements in order to handle runtime exceptions
     whenever an invalid type conversion is attempted. __Do not__ place code outside the
     `try`/`except` code blocks.

   - If a delimiter value is provided, the function will use it to split the `value`; otherwise,
     the string will be split without specifying a delimiter value.

      :bulb: Note that the function's `delimiter` parameter defaults to `None`. You _must_ check
      the truth value of `delimiter` in the function block. If `True`, pass the delimiter value to
      the appropriate `str` method; otherwise rely on the `str` method's default behavior.

      :exclamation: Don't assume that `value` is "clean"; program defensively and remove
      leading/trailing spaces before attempting to convert the "cleaned" version of the string to
      a list.

   - If a runtime exception is encountered the `except` block will "catch" the exception and the
     `value` will be returned to the caller _unchanged_.

      :bulb: You do not need to specify a specific exception in the `except` statement.

   - After implementing the function, navigate back to Problem 02 in `main()` and uncomment the
     next three (3) `assert` statements to check your implementation.

7. Switch over to the `problem_set_11.py` file and navigate to the `convert_gravity_value()`
   function definition. Replace `pass` with a code block that attempts to convert a planet's
   `"gravity"` value to a float by first removing the "standard" unit of measure substring (if it
   exists) before converting the remaining number to a float.

   Review the function's docstring to better understand the task it is to perform, the parameters
   it defines, and the return value it computes.

   :bulb: Note that `"gravity"` values vary from planet to planet. The following examples
   illustrate the challenge:

   ```python
   {
      'name': Tatooine,
      ...
      'gravity': '1 standard',
      ...
   }
   ```

   ```python
   {
      'name': Dagobah,
      ...,
      'gravity': 'N/A',
      ...
   }
   ```

   ```python
   {
      'name': Haruun Kal,
      ...
      'gravity': '0.98',
      ...
   }
   ```

   **Requirements**

      - The function _must_ employ `try` and `except` statements in order to handle runtime
        exceptions whenever an invalid type conversion is attempted. __Do not__ place code
        outside the `try`/`except` code blocks.

      - The function _must_ __remove__ the substring `"standard"` if it exists anywhere in the
        passed in `value` _irrespective of case_. In other words lowercase, mixed case, and
        uppercase versions of the substring _must_ be removed.

      - If the substring `"standard"` exists in `value`, remove it and return a version of `value`
        that contains only the numeric portion of the string.

         :bulb: A handy `str` method exists for locating substrings in a string.

         :exclamation: Don't assume that `value` is "clean"; program defensively and remove
         leading/trailing spaces before attempting to convert the "cleaned" version of the string
         to a float.

      - The function _must_ delegate to the function `utl.convert_to_float` the task of converting
        the "numeric" version of `value` to a float. The return value of `utl.convert_to_float` is
        then returned to the caller.

      - If a runtime exception is encountered, the `except` block will "catch" the exception, pass
        the `value` to the function `utl.convert_to_none()`, and then return the value returned by
        `utl.convert_to_none()` to the caller.

8. After implementing `convert_gravity_value()` test the function in `main()` by uncommenting the
   `assert` statements provided. These statements call the `convert_gravity_value()` function and
   check if the value is equivalent to the expected value.

## PROBLEM 03

__Task:__ Implement the functions `get_mandalorian_data()` and `create_planet()` in the
`problem_set_11.py` file.

1. In `problem_set_11.py`, navigate to the `get_mandalorian_data()` function definition. Replace
   `pass` with a code block that utilizes a `filter` string to return a nested dictionary from
   the passed in `mandalorian_data` list if the dictionary's `"name"` value matches the `filter`
   value. Review the function's docstring to better understand the task it is to perform, the
   parameters it defines, and the return value it computes.

   The function will be employed to traverse lists of nested dictionaries sourced from the
   following files in search of a particular dictionary representations of a Star Wars droid,
   person, planet, or starship:

   - `data-mandalorian_droids.json`
   - `data-mandalorian_people.csv`
   - `data-mandalorian_planets.json`
   - `data-mandalorian_starships.json`
   - `data-mandalorian_vehicles.json`

   **Requirements**

   - The function _must_ perform a __case insenstitive__ comparison between the passed in `filter`
     value and each nested dictionary's `"name"` value. If a match is obtained it returns the
     nested dictionary to the caller.

   - If no match is obtained the function returns `None` to the caller.

2. After implementing `get_madalorian_data()`, return to the `main()` function:

   - Call `get_madalorian_data()` and pass it `mandalorian_planets` and the `str`
     `'nevarro'`. Assign the return value to the variable named `mandalorian_nevarro`
   - Call `get_madalorian_data()` and pass it `mandalorian_planets` and the `str`
     `'ARVALA-7'`. Assign the return value to the variable named `mandalorian_arvala_7`

3. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, to write `mandalorian_nevarro` to a file named `stu-mandalorian_nevarro.json` and write
   `mandalorian_arvala_7` to a file named `stu-mandalorian_arvala_7.json`. Compare your files to
   the test fixture files `fxt-mandalorian_nevarro.json` and `fxt-mandalorian_arvala_7.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character, and
   indent-for-indent.

4. In `problem_set_11.py`, navigate to the `create_planet()` function definition. Replace `pass`
   with a code block that returns a new planet dictionary based on the passed in `data` dictionary.
   Review the function's docstring to better understand the task it is to perform, the parameters
   it defines, and the return value it computes.

   **Requirements**

   Certain `data` values require special handling and are subject to the following type conversion
   rules:

   - Leverage the `utl.convert_none_values()` function and pass it the `data` dictionary in
     order to attempt to convert all data values that are members of `utl.NONE_VALUES` (case
     insensitive comparison) to `None`. Assign the updated dictionary to the variable `planet`.

   - Within the dictionary _literal_ convert other `data` values to `int`, `float` or `list` as
     specified in the table below.

      :exclamation: The new dictionary may contain keys that differ from the passed in `data`
      dictionary keys.

      | `data`                 | Convert to
      | :--------------------- | :----------------------------
      | suns (`str`)           | suns (`int`)
      | moons (`str`)          | moons (`int`)
      | orbital_period (`str`) | orbital_period_days (`float`)
      | diameter (`str`)       | diameter_km (`int`)
      | gravity (`str`)        | gravity_std (`float`)
      | climate (`str`)        | climate (`list`)
      | terrain (`str`)        | terrain (`list`)
      | population (`str`)     | population (`int`)

5. After implementing `create_planet()` return to `main()`. Call the function
   `get_swapi_resource()` and retrieve a SWAPI representation of the planet
   [Tatooine](https://starwars.fandom.com/wiki/Tatooine). Access the "Tatooine" dictionary
   which is stored in the response object and assign the value to `swapi_tatooine`.

   :bulb: The `problem_set_11.py` file includes a SWAPI "planets" URL constant that you can pass
   as the `url` argument. If you need help constructing the `params` argument, review the lecture
   notes and code.

6. Call the function `create_planet()` and pass
   `swapi_tatooine` as the argument.
   Assign the return value to a variable named `tatooine`.

7. Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py`
   module, and write `tatooine` to the file `stu-tatooine.json`. Compare your file to the test
   fixture file `fxt-tatooine.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character, and
   indent-for-indent.

## PROBLEM 04

__Task:__ Implement the functions `create_droid()` and `create_person()` in the `problem_set_11.py`
file.

1. In `problem_set_11.py`, navigate to the `create_droid()` function definition. Replace `pass`
   with a code block that returns a new droid dictionary based on the passed in `data` dictionary.
   Review the function's docstring to better understand the task it is to perform, the parameters
   it defines, and the return value it computes.

   **Requirements**

   Certain `data` values require special handling and are subject to the following type conversion
   rules:

   - Leverage the `utl.convert_none_values()` function and pass it the `data` dictionary in
     order to attempt to convert all data values that are members of `utl.NONE_VALUES` (case
     insensitive comparison) to `None`. Assign the updated dictionary to the variable `droid`.

   - Convert other `data` values to `int`, `float` or `list` as specified in the table below.

      | `data`            | `Droid`             | Notes                                              |
      | :---------------- | :------------------ | :------------------------------------------------- |
      | height (`str`)    | height_cm (`float`) |                                                    |
      | mass (`str`)      | mass_kg (`float`)   |                                                    |
      | equipment (`str`) | equipment (`list`)  | Check delimiter in `data-mandalorian_droids.json`. |

2. After implementing `create_droid()`, return to `main()`. Call the `get_mandalorian_data()`
   function and retrieve a dictionary representation of the droid 'IG-11' by passing
   `mandalorian_droids` and `ig-11` as arguments. Assign the return value to `mandalorian_ig_11`.

3. Call the function `create_droid()` and pass the `mandalorian_ig_11` dictionary as the argument.
   Assign the return value to a variable named `ig_11`.

4. Check your work. Call the function `write_json`, accessed from the imported `five_oh_six.py`
   module, and write `ig_11` to the file `stu-ig_11.json`. Compare your file to the test fixture
   file `fxt-ig_11json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character, and
   indent-for-indent.

5. In `problem_set_11.py`, navigate to the `create_person()` function definition. Replace `pass`
   with a code block that returns a new person dictionary based on the passed in `data` dictionary.
   Review the function's docstring to better understand the task it is to perform, the
   parameters it defines, and the return value it computes.

   **Requirements**

   Certain `data` values require special handling and are subject to the following type conversion
   rules:

   - Leverage the `utl.convert_none_values()` function and pass it the `data` dictionary in
     order to attempt to convert all data values that are members of `utl.NONE_VALUES` (case
     insensitive comparison) to `None`. Assign the updated dictionary to the variable `person`.

   - Convert other `data` values to `int`, `float`, `dict`, or `list` as specified in the table
     below.

      | `data` | `Person` | Notes |
      | :----- | :------- | :---- |
      | height (`str`) | height_cm(`float`) | |
      | mass (`str`) | mass_kg (`float`) | |
      | homeworld (`str`) | homeworld (`dict`) | Retrieve from the cache or from SWAPI if the data is not available locally; update values with the passed in `planets` data if not `None`. |
      | species (`str`) | species (`dict`) | Retrieve from the cache or from SWAPI if the data is not available locally. |

     :exclamation: The person's "homeworld" value _must_ be converted to a dictionary
     representation of the home planet. Implement the following steps using an `if-elif-else`
     statement to produce the required "homeworld" key-value pairs __before__ `homeworld` is
     mapped to the person's "homeworld" key:

      - Check if an optional Wookieepedia-sourced `planets` list is provided. Call
        `get_mandalorian_data()` and attempt to retrieve data that can be used to update the
        homeworld dictionary by implementing the proper dictionary method. Assign the return
        value to a variable named `mandalorian_planet`.

         :bulb: Retrieve the planet dictionary from the cache or from SWAPI if the data is not
         available locally.

         - If `mandalorian_planet` is _truthy_, call `create_planet()` and pass it the (updated)
           homeworld dictionary.

         - Assign the return value to the person's `homeworld` key.

      - Otherwise, if a `planets` list is not provided but the attempt to retrieve data that can
        be used to update the homeworld dictionary is _truthy_, call the function
        `get_swapi_resource` to retrieve the appropriate nested dictionary (filtered on the passed
        in homeworld/planet). Then call `create_planet()`, pass it the (updated)
        homeworld dictionary and assign the return value to the person's `homeworld` key.

         :bulb: The value stored in homeworld and species may differ depending on the person.
         Implement a `try`/`except` block when retrieving information from SWAPI using
         `get_swapi_resource()`. The following examples illustrate the challenge:

      ```python
      {
      "name": "Carasynthia Dune",
      ...
      "homeworld": "https://swapi.py4e.com/api/planets/2/",
      "species": "https://swapi.py4e.com/api/species/1/",
      ...
      },
      {
      "name": "Boba Fett",
      ...
      "homeworld": "Kamino",
      "species": "Human",
      ...
      }
      ```

      - Otherwise, assign the variable `homeworld` to `None`.

6. Since the fall of the Mandalorians, one of the few surviving Mandalorians, Din Djarin, works as
   a bounty hunter for the Bounty Hunters' Guild. After implementing `create_person()` return to
   `main()`. Call the `get_mandalorian_data()` function and pass it `mandalorian_people` and
   the `str` `'Din Djarin'`. Assign the return value to `mandalorian_din_djarin`.

7. Call the function `create_person()` and pass `mandalorian_din_djarin` _and_
   `mandalorian_planets` as the arguments. Assign the return value to a variable named `mando`.

8. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `mando` to the file `stu-mando.json`. Compare your file to the test fixture
   file `fxt-mando.json`.

      :exclamation: Both files _must_ match line-for-line, character-for-character, and
      indent-for-indent.

## PROBLEM 05

__Task:__ Implement the functions `create_starship()`, `create_vehicle()`, `board_passengers()` in
the `problem_set_11.py` file.

1. In `problem_set_11.py`, navigate to the `create_starship()` function definition. Replace `pass`
   with a code block that returns a new starship dictionary based on the passed in `data`
   dictionary. Review the function's docstring to better understand the task it is to perform, the
   parameters it defines, and the return value it computes.

   **Requirements**

   Certain `data` values require special handling and are subject to the following type conversion
   rules:

   - Leverage the `utl.convert_none_values()` function and pass it the `data` dictionary in
     order to attempt to convert all data values that are members of `utl.NONE_VALUES` (case
     insensitive comparison) to `None`. Assign the updated dictionary to the variable `starship`.

   - Convert other `data` values to `int`, `float` or `list` as specified in the table below.

      | `data`                         | `Starship`                     | Notes                                                 |
      | :----------------------------- | :----------------------------- | :---------------------------------------------------- |
      | length (`str`)                 | length_m (`float`)             |                                                       |
      | max_atmosphering_speed (`str`) | max_atmosphering_speed (`int`) |                                                       |
      | hyperdrive_rating (`str`)      | hyperdrive_rating (`float`)    |                                                       |
      | armament (`str`)               | armament (`list`)              | Check delimiter in `data-mandalorian_starships.json`. |
      | cargo_capacity (`str`)         | cargo_capacity_kg (`int`)      |                                                       |

2. After defining the function, navigate to `main()`. Call `get_mandalorian_data()` passing the
   appropriate arguments and retrieve the starship named
   [_Razor Crest_](https://starwars.fandom.com/wiki/Razor_Crest) in `mandalorian_starships`.
   Pass its return value to the function `create_starship()`. Assign the final return value to a
   variable named `razor_crest`.

3. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `razor_crest` to the file `stu-razor_crest.json`. Compare your file to the
  test fixture file `fxt-razor_crest.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character, and
   indent-for-indent.

4. Navigate to the function `create_vehicle()`. Replace `pass`
   with a code block that returns a new vehicle dictionary based on the passed in `data`
   dictionary. Review the function's docstring to better understand the task it is to perform,
   the parameters it defines, and the return value it computes.

   **Requirements**

   Certain `data` values require special handling and are subject to the following type conversion
   rules:

   - Leverage the `utl.convert_none_values()` function and pass it the `data` dictionary in
     order to attempt to convert all data values that are members of `utl.NONE_VALUES` (case
     insensitive comparison) to `None`. Assign the updated dictionary to the variable `vehicle`.

   - Convert other `data` values to `int`, `float` or `list` as specified in the table below.

      | `data`                         | `Vehicle`                      | Notes                                                 |
      | :----------------------------- | :----------------------------- | :---------------------------------------------------- |
      | length (`str`)                 | length_m (`float`)             |                                                       |
      | max_atmosphering_speed (`str`) | max_atmosphering_speed (`int`) |                                                       |
      | hyperdrive_rating (`str`)      | hyperdrive_rating (`float`)    |                                                       |
      | MGLT (`str`)                   | top_speed_mglt (`int`)         | A megalight, the standard unit of distance in space.  |
      | armament (`str`)               | armament (`list`)              | Check delimiter in `data-mandalorian_starships.json`. |
      | cargo_capacity (`str`)         | cargo_capacity_kg (`int`)      |                                                       |

5. After implementing `create_vehicle()`, return to `main()`. Call the function
   `get_swapi_resource()` and retrieve a SWAPI representation of the sand crawler vehicle. Assign
   the return value to `swapi_sand_crawler()`.

      :bulb: The `problem_set_11.py` file includes a SWAPI "vehicles" URL constant that you can
      pass as the `url` argument. If you need help constructing the `params` argument, review the
      lecture notes and code.

6. Call the function `create_vehicle()` and pass `swapi_sand_crawler` as the argument. Assign the
   return value to a variable named `sand_crawler`.

7. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `sand_crawler` to a file name `stu-sand_crawler.json`. Compare your file to
   the test fixture file `fxt-sand_crawler.json`.

      :exclamation: Both files _must_ match line-for-line, character-for-character, and
      indent-for-indent.

8. In `problem_set_11.py`, navigate to the `board_passengers()` function definition. Replace `pass`
   with a code block that assigns passengers to a starship. Review the function's docstring to
   better understand the task it is to perform, the parameters it defines, and the return value it
   computes.

   **Requirements**

   - The passengers _must_ be passed in a list to the `board_passengers` function.

   - The number of passengers permitted to board a starship is limited by the starship's
      `"max_passengers"` value. If the number of passengers attempting to board exceeds the
      starship's `"max_passengers"` value only the first `n` passengers
      (where `n` = "max_passengers") are permitted to board the vessel. This limitation _must_
      be imposed by the `board_passengers` function and will be subject to auto grader testing.

      For example, if a starship's `"max_passengers"` value equals `10` and `20` passengers attempt
      to board the starship, only the first `10` passengers are permitted to board the vessel.

   - After boarding the passengers, return the starship to the caller.

9. After implementing `board_passengers()`, return to `main()`. Call the function
   `board_passengers()` and pass the following arguments to it:

      - `razor_crest`
      - a list of passengers comprising only of the variable `mando`

   1. Assign the return value of the function to the variable `razor_crest`.

## PROBLEM 06

__Task:__ Implement the function `update_planets_visited()` in the `problem_set_11.py` file.

**Background:** The Mandalorian's story begins on the planet Nevarro. The function
`update_planets_visited()` will keep track of the planets the Mandalorian visits. Greef Karga
is an inhabitant of the planet Nevarro and leader of the Nevarro Bounty Hunters' Guild (aka the Nevarro Hunters). Greef Karga
provides intel on bounty hunter assignments. Greef Karga informs the Mandalorian Din of a bounty on
the planet of Arvala-7. The bounty is a 50-year-old sentient being with a large reward for their
capture. The Mandalorian accepts the mission and leaves for Arvala-7.

1. In `problem_set_11.py`, navigate to the `update_planets_visited()` function definition. Replace
   `pass` with a code block that adds a starship's dictionary representation to the
   `'planets_visited'` key. Review the function's docstring to better understand the task it is to
   perform, the parameters it defines, and the return value it computes.

2. After implementing `update_planets_visited()`, return to the `main()` function. Call
   `update_planets_visited()` and pass `razor_crest` and the `mandalorian_nevarro` dictionary as
   arguments. Assign the return value to `razor_crest`.

3. Check your work by uncommenting the `print` statement provided for you.

   Expected output:

   ```python
   6.3 razor crest visited planets = [
         {
            'name': 'Nevarro',
            'region': 'Outer Rim Territories',
            'sector': 'Nevarro sector',
            'suns': 1,
            'orbital_position': None,
            'moons': None,
            'class': 'terrestrial',
            'atmosphere':'breathable',
            'rotation_period': None,
            'orbital_period': None,
            'diameter': None,
            'climate': 'arid',
            'gravity': None,
            'terrain': 'ashen, rocky, volcanic',
            'surface_water': None,
            'population': None,
            'url': 'https://starwars.fandom.com/wiki/Nevarro'
         }
      ]
   ```

4. In `main()`, call the `get_mandalorian_data()` function and pass it `mandalorian_people`
   and the `'greef karga'` dictionary as arguments. Pass its return value to `create_person()`.
   Assign the final return value to `greef_karga`.

5. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `greef_karga` to the file `stu-greef_karga.json`. Compare your file to the
   test fixture file `fxt-greef_karga.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character,
   and indent-for-indent.

6. Still in `main()`, call `update_planets_visited()` and pass `razor_crest` and the
   `mandalorian_arvala_7` dictionary as arguments.

7. Check your work by uncommenting the `print` statement provided for you.

   Expected output:

   ```python
   6.7 razor crest visited planets =
   [
      {
         'name': 'Nevarro',
         'region': 'Outer Rim Territories',
         'sector': 'Nevarro sector',
         ...
      },
      {
         'name': 'Arvala-7',
         'region': None,
         'sector': None,
         ...
      }
   ]
   ```

## PROBLEM 07

__Task:__ Call the functions `get_mandalorian_data()`, `create_person()`, `create_vehicle()`, and
`board_passengers()`. Then, leverage a dictionary method to reprogram the IG-11.

**Background:** On planet Arvala-7, the Mandalorian runs into an inhabitant named Kuiil who helps
him locate the bounty. Later, the Mandalorian encounters the droid IG-11 that serves as a programmed
bounty hunter. With the same bounty as their target, they decide to work together. Once they reach
their target, they discover the bounty is a green, child-like creature with big ears ensconced in a
floating ball transport. Once Grogu is with the Mandalorian and IG-11, IG-11 attempts to harm Grogu
due to his programming. With the help of Kuiil, the Mandalorian is able to stop IG-11 and Kuiil
reprograms IG-11 to protect baby Grogu instead. Update the `'instructions'` key accessed from
the `ig_11` dictionary and replace its value with provided `new_instructions`, leveraging the
appropriate dictionary method.

1. In `main()`, call the `get_mandalorian_data()` function and pass it `mandalorian_people` and
   `'Kuiil'`. Pass its return value and `mandalorian_planets` to `create_person()`. Assign the
   final return value to `kuiil`.

2. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `kuiil` to the file `stu-kuiil.json`. Compare your file to the test fixture
   file `fxt-kuiil.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character, and
   indent-for-indent.

3. In `main()`, call the `get_mandalorian_data()` function and pass it `mandalorian_people` and
   `'Grogu'` as arguments. Pass its return value to `create_person()` Assign the final return value
   to `grogu`.

4. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `grogu` to the file `stu-grogu.json`. Compare your file to the test fixture
   file `fxt-grogu.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character and
   indent-for-indent.

5. Call `get_mandalorian_data()` and pass it the appropriate arguments in order to retrieve the
   vehicle named [_Hovering Pram_](https://starwars.fandom.com/wiki/Hovering_Pram) in
   `mandalorian_vehicles`. Pass its return value to `create_vehicle()`. Assign the final return
   value to a variable named `hovering_pram`.

6. Call `board_passengers()` and pass `hovering_pram` and `grogu` as the arguments. Assign the
   return value to `hovering_pram`.

7. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `hovering_pram` to the file `stu-grogu_hovering_pram.json`. Compare your file
   to the test fixture file `fxt-grogu_hovering_pram.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character, and
   indent-for-indent.

8. Reprogram `ig_11` using the proper method to update the `”instructions”` key in the `ig_11`
   dictionary, previously defined in problem 04, with the `new_instructions` provided in `main()`.

9. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `ig_11` to the file `stu-ig_11_reprogrammed.json`. Compare your file to the
   test fixture file `fxt-ig_11_reprogrammed.json`.

      :exclamation: Both files _must_ match line-for-line, character-for-character, and
      indent-for-indent.

## PROBLEM 08

__Task:__ Call the functions `get_mandalorian_data()`, `create_person()`, `create_starship()`, and
`board_passengers()`.

**Background:** The Mandalorian, Grogu, and IG-11 head back to Nevarro in the Razor Crest to turn
Grogu in to the client who requested him. The Mandalorian notes the client who wants Grogu is part
of the Galactic Empire with malintent. The Mandalorian decides to betray the Empire by fleeing to
the planet Sorgan with Grogu and IG-11. On planet Sorgan, the Mandalorian meets Carasynthia "Cara"
Dune. Cara has previous experience in the Alliance military and now serves as a mercenary on Sorgan.
While on planet Sorgan, the Mandalorian receives word from Greef Karga informing
him that his actions with Grogu has led to the Empire warlord, Gideon, wreaking havoc on Nevarro.
Gideon's Imperial transport is stationed on Nevarro and Gideon will not leave until he has Grogu.
The Mandalorian decides to go back to Nevarro to face Gideon. Cara Dune offers
her support and is willing to fight alongside the Mandalorian against Gideon. The Mandalorian,
Cara, Grogu, and IG-11 board the Razor Crest and head back to Nevarro.

1. In `main()`, call `get_mandalorian_data()` and pass it `mandalorian_planets` and the filter
   `"sorgan"` as arguments. Assign the return value to `mandalorian_sorgan`.

2. Next, call `update_planets_visited()` and pass it `razor_crest` and the planet
   `mandalorian_sorgan` as arguments. Assign the return value to `razor_crest`.

3. Check your work by uncommenting the `print` statement provided for you.

   Expected output:

   ```python
   8.3 razor crest visited planets =
   [
      {
         'name': 'Nevarro',
         'region': 'Outer Rim Territories',
         ...
      },
      {
         'name': 'Sorgan',
         'region': 'Outer Rim Territories',
         ...
      }
   ]
   ```

4. In the `main` function, call the `get_mandalorian_data()` function and pass it
   `mandalorian_people` and `'Carasynthia Dune'`. Pass the return value to `create_person`. Assign
   the final return value to `cara_dune`.

5. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `cara_dune` to the file `stu-cara_dune.json`. Compare your file to the test
   fixture file `fxt-cara_dune.json`.

   :exclamation: Both files _must_ match line-for-line, character-for-character, and
   indent-for-indent.

6. In `main()`, call the `get_mandalorian_data()` function and pass it `mandalorian_people` and
   `'gideon'`. Pass the return value  to `create_person()`. Assign the final return value to
   `gideon`.

7. Then, call the `get_mandalorian_data()` function and pass it `mandalorian_starships` and
   `'imperial transport'`. Pass the return value  to `create_starship()`. Assign the final return
   value to `imperial_transport`.

8. Call `board_passengers` passing to it `imperial_transport` and `gideon` pass within a list
   _literal_. Assign the return value to `imperial_transport`.

9. Check your work. Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `imperial_transport` to the file `stu-gideon_imperial_transport.json`.
   Compare your file to the test fixture file `fxt-gideon_imperial_transport.json`.

      :exclamation: Both files _must_ match line-for-line, character-for-character, and
      indent-for-indent.

10. In `main()`, call `board_passengers()` and pass `razor_crest` and the passengers `mando`,
   `grogu`, `cara_dune`, and `ig_11` contained in a list _literal_ (in that order).

## PROBLEM 09

__Task:__ Call the functions `board_passengers()` and `update_planets_visited()`.

**Background:** On planet Nevarro, the Mandalorian and his allies defeat Gideon forcing him to
leave Nevarro. Cara decides to stay and help defend the planet. The Mandalorian decides to
depart Nevarro with Grogu to reunite Grogu with his people. Their first destination is Tatooine.

1. In `main()`, call `board_passengers()` and pass it `razor_crest` and the passengers `mando`,
   `grogu` contained in a list _literal_ (in that order).

2. Call `update_planets_visited()` and pass it `razor_crest` and the planet `tatooine` as
   arguments. Assign the return value to `razor_crest`

3. Using the built-in `sorted` function and a lambda expression, sort the values in the
   `'planets_visited'` key of the `razor_crest` dictionary by `'name'`, in ascending order.

4. Check your work by uncommenting the `print` statement provided for you.

   Expected output:

   ```python
   9.4 razor crest visited planets =
   [
      {
         'name': 'Arvala-7',
         ...
      },
      {
         'name': 'Nevarro',
         ...
      },
      {
         'name': 'Sorgan',
         ...
      },
      {
         'url': 'https://swapi.py4e.com/api/planets/1/', 'name': 'Tatooine',
         ...
      }
   ]
   ```

5. Check your work.  Call the function `write_json()`, accessed from the imported `five_oh_six.py`
   module, and write `razor_crest` to the file `stu-razor_crest_departs.json`. Compare your file
   to the test fixture file `fxt-razor_crest_departs.json`.

     :exclamation: Both files _must_ match line-for-line, character-for-character, and
     indent-for-indent.
