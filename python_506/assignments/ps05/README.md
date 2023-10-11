# SI 506: Problem Set 05

## This week's Problem Set

This week's problem set includes eight (8) problems that
focus on functions, loops and conditional statements.

## Background

For this week's Problem Set, you will analyze data from the
[University of Michigan Maize Pages]("https://maizepages.umich.edu/organizations")
on activities organized by the student clubs in various categories.

You are provided with a list of strings named `club_events`. Each list element contains the
following information:

- Host Organization: Name of the student club
- Event Name: Name of the activity
- Date: The event start date is formatted as year/month/day.
- Start Time: Event start time
- Duration: Total number of hours of activity
- Location: Location of the event
- Theme: Type of activity/ event category

<br />

## Problem 01 (20 Points)

**Task:** Implement a function that converts each element in a list from a string to a list. Use
this function to update all elements in `club_events`.

1. Implement the function named `convert_str_to_list`.

   **Requirements**

   1. The function _must_ be provisioned with two parameters in the following order: `element` (a
      string element of the list `club_list`) and `separator` (a string delimiter).

   2. Within the function block, use an appropriate string method to convert the string element to
      a list

   3. Return the converted list to the caller.

2. Using a `for` loop with `range()` type, iterate over the elements in the
   `club_events` list.

   In the loop code block, call the `convert_str_to_list` function on each element in `club_events`. Make sure to pass the appropriate separator value as the second argument to your function call. Assign the return value of the function to the same index position in the `club_events` list as the element on which the function was called.

   :exclamation: After mutating the list, the `club_events` list _must_ match the list
   `club_events_check` (see Setup Code) after calling the list method. Uncomment the associated
   `assert` statement to confirm the variable matches the expected value.

<br />

## Problem 02 (20 Points)

**Task:** Implement 2 functions: one that retrieves event venue information, and another that
retrieves the location when the event will occur. Use both functions to extract information from
events in `club_events`.

1. Define and implement a function named `get_duration`.

   **Requirements**

   1. The function _must_ be provisioned with a single parameter `event_info` (a list element of
      `club_events`).

   2. Return a float representing the event duration to the caller.

   :bulb: You should utilize an appropriate string method to split the duration element, then
   extract the number.

2. Define and implement a function named `get_event_location`.

   **Requirements**

   1. The function _must_ be provisioned with a single parameter `event_info` (a list element of
      `club_events`).

   2. Return a string representation of event location to the caller.

:bulb: To check if you have implemented the functions correctly, try calling
`get_duration(club_events[1])` and `get_event_location(club_events[1])`. The correct answers should
match the values of `get_duration_check` and `get_event_location_check` (see Setup Code). Uncomment
the associated `assert` statements to confirm the return value of each function call matches the expected value.

<br />

## Problem 03 (30 Points)

**Task:** Implement a function that determines which event(s) in the list `club_events` has/have
the shortest duration.

1.  Define a function named `event_with_shortest_duration`.

    **Requirements**

    1.  The function _must_ be provisioned with a single parameter `club_events` (a list of nested event lists).

    2.  In the function code block, create an empty list and assign it to a variable named
        `shortest_event`. Assign hundred (100) to a variable named `shortest_duration`.

    3.  Using a `for` loop and skipping the headers list, iterate over `club_events`.

    4.  In the loop code block, call the `get_duration` function on the current event list to find the event duration and assign that value
        to a variable named `duration`. Then, construct an `if-elif` statement to check.

        1.  In the `if` block, check whether `duration` is less than the value of
            `shortest_duration`. If the `if` statement evaluates to `True`, update the value of
            `shortest_duration` to `duration`, clear the `shortest_event` list, then append to `shortest_event` a tuple containing event information in the following order:
            a) event name and
            b) duration.

        2.  In the `elif` block, check whether `duration` is equal to the value of
            `shortest_duration`. If the `elif` statement evaluates to `True`, append to `shortest_event` a tuple containing event information in the following order:
            a) event name and
            b) duration.

    5.  After the loop terminates, return `shortest_event`.

2.  Call the `event_with_shortest_duration` function passing to it the appropriate parameter value
    and assign the return value to a variable named
    `shortest_club_event`.

:exclamation: The `shortest_club_event` list you create _must_ match the list
`shortest_club_event_check` (see Setup Code) after calling the list method. Uncomment the associated
`assert` statement to confirm the variable matches the expected value.

<br />

## Problem 04 (30 Points)

**Task:** Create a function that returns a list of events that are happening in a specified location.

1. Define a function named `categorize_events_by_location`.

   **Requirements**

   1. The function _must_ be provisioned with two parameters in the following order: `club_events`
      (a list of events) and `location` (a string representing the location).

   2. In the function code block, initialize an empty list named `events_by_location`.

   3. Using a `for` loop and skipping the headers list, iterate over the event lists in
      `club_events`.

   4. In the loop code block, call the function `get_event_location` on the current event list to get a string representation of that event's location and store it in a variable named `event_location`.

   5. In the loop, using an `if` statement, check whether `event_location` is the same as the value
      of `location` we pass to the function `categorize_events_by_location`. If the `if` statement
      evaluates to `True`, append the event name _only_ to the `events_by_location` list.

   6. After the loop terminates, return the list `events_by_location`.

2. Call the function, passing the `club_events` list and the string "Intramural Sports Building" as
   arguments. Assign the return value to the variable named `intramural_events`.

:exclamation: The `intramural_events` list you create _must_ match the list
`intramural_events_check` (see Setup Code) after calling the list method. Uncomment the associated
`assert` statement to confirm the variable matches the expected value.

<br />

## Problem 05 (25 Points)

**Task:** Implement a function that extracts events from a list that have a specified theme.

1.  Define a helper function named `has_theme`.

    **Requirements**

    1. The function _must_ be provisioned with two parameters in the following order: `event`
       (a list element of `club_events`) and `theme` (a string representing an event category).

    2. In the function code block, write an `if` statement to check whether the value of `theme`
       passed to the function is a substring of the string representing the theme in the `event` list. If the `if`
       statement evaluates to `True`, return `True`. Otherwise, return `False`.

2.  Define a function named `categorize_events_by_theme`.

    **Requirements**

    1.  The function _must_ be provisioned with two parameters in the following order: `club_events`
        (a list of events) and `theme` (a string representing an event category).

    2.  In the function code block, create an empty list and assign it to a variable named
        `events_by_theme`.

    3.  Using a `for` loop and skipping the headers list, iterate over the event lists in
        `club_events`.

    4.  In the loop code block, call the `has_theme` helper function (implemented
        previously) in an `if` statement, to check whether the `theme` string exists in the current _event's_ theme string.
        If the `if` statement evaluates to `True`, append the event name to the `events_by_theme`
        list.

        :bulb: You _must_ use the helper function in your `if` statement appropriately.

    5.  After the loop terminates, return the `events_by_theme`.

3.  Create an empty list and assign it to a variable named `specified_theme_events`.

4.  Using a `for` loop, iterate over the provided `themes` list. Inside the loop code block, call the
    `categorize_events_by_theme` function on each element in the `themes` list. Make sure to pass `club_events` as the first argument to each `categorize_events_by_theme` function call. Append the return
    value from each function call to the `specified_theme_events` list.

:exclamation: The `specified_theme_events` list you create _must_ match the list
`specified_theme_events_check` (see Setup Code) after calling the list method. Uncomment the
associated `assert` statement to confirm the variable matches the expected value.

<br />

## Problem 06 (20 Points)

**Task:** Implement a function that identifies events that have a specific start time and duration.

1. Define a function named `categorize_events_by_time`.

   **Requirements**

   1. The function _must_ be provisioned by three parameters in the following order: `club_events`
      (a list of events), an optional argument `time` (a string representing the event start time)
      with default value `'7 PM'` and another optional argument `duration` (an integer representing
      the event duration) with default value `1`.

   2. In the function code block, initialize an empty list named `events_by_time`.

   3. Using a `for` loop and skipping the headers list, iterate over the event lists in `club_events`.

   4. In the loop code block, using a compound `if` statement, check whether the current event start time is the same
      as the value of `time` and whether the current event duration is **greater than or equal to** the value
      of `duration`. If the `if` statement evaluates to `True`, append **only** the _event name_ to the
      `events_by_time` list.

   5. After the loop terminates, return the `events_by_time` list.

2. Call the function `categorize_events_by_time`, passing the `club_events` list as its required argument. Assign the return
   value to a variable named `evening_events`.

:exclamation: The `evening_events` list you create _must_ match the list
`evening_events_check` (see Setup Code) after calling the list method. Uncomment the associated
`assert` statement to confirm the variable matches the expected value.

<br />

## Problem 07 (20 Points)

**Task:** Implement a function that identifies the number of events hosted by a specific student
organization.

1. Define a function named `calculate_num_events`.

   **Requirements**

   1. The function _must_ be provisioned with two parameters in the following order: `club_events`
      (a list of events), `host_org` (a string representing the student organization's name).

   2. In the function code block, assign zero (0) to a variable named `num_events`.

   3. Using a `for` loop and skipping the headers list, iterate over the event lists in `club_events`.

   4. In the loop code block, if the name of the student organization pertaining to the current event is the same as the value of `host_org`,
      increment the value of `num_events` by one (1).

   5. After the loop terminates, return the `num_events`.

2. Call the function `calculate_num_events`, passing the `club_events` list and the string `'A2 Movimiento Latino'` as
   arguments. Assign the return value to the variable named `num_events_for_a2`.

:exclamation: The `num_events_for_a2` variable you create _must_ match the variable
`num_events_for_a2_check` (see Setup Code). Uncomment the associated
`assert` statement to confirm the variable matches the expected value.

<br />

## Problem 08 (10 points)

**Task:** Implement a function that identifies events of a particular theme (or type of event).
Unpack the function's return value into multiple variables.

1.  Define a function named `categorize_events_by_specific_theme`.

    **Requirements**

    1. The function _must_ be provisioned with two parameters in the following order: `club_events`
       (a list of events) and `theme` (a string representing an event theme).

    2. In the function code block, create an empty list and assign it to a variable named
       `events_at_theme`.

    3. Using a `for` loop, iterate over each event in club_events (skipping the header).

    4. In the for loop block, extract the theme of the current event and assign it to a variable named `event_theme`.

    5. Using an `if` statement, check whether `event_theme` is the same as the value
       of `theme` we pass to the function `categorize_events_by_specific_theme`. If the `if` statement evaluates to `True`, append `events_at_theme` with a tuple containing the following contents (in the order specified): 1) event name, 2) event date, and 3) event theme.

    6. After the loop terminates, return `events_at_theme`.

2.  Call `categorize_events_by_specific_theme` and pass it the following arugments: `club_events`
    and `'social'` (all lowercase). Assign the return value to a variable named `social_events`.

3.  Unpack `social_events` into the following variables: `social_event_1`, `social_event_2`, and
    `social_event_3`.

    :exclamation: This step _must_ be completed using a single statement on a single line of code.

    :exclamation: The variables `social_event_1`, `social_event_2` and `social_event_3` you create
    _must_ match the variables `social_event_1_check`, `social_event_2_check` and `social_event_3_check`
    (see Setup Code) after unpacking. Uncomment the associated `assert` statements to confirm the
    variable matches the expected value.
