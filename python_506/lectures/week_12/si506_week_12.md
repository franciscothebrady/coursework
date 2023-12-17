# SI 506 Week 12

## Topics

1. The Requests package
   1. Install `requests`
   2. Confirm installation
2. HTTP Request/Response cycle
3. The Star Wars API
   1. SWAPI: request resource categories (`/api/`)
   2. SWAPI: request resources by category (`/api/:category/`)
   3. SWAPI: request single resource by id (`/api/:category/:id/`)
   4. SWAPI: search category with querystring (`/api/:category/?search=<search term>`)
   5. SWAPI: search limitations
   6. Challenge 01
4. Coding Tips
   1. Expression chaining
   2. `get_swapi_resource()` function
   3. Challenge 02
   4. `create_< entity >()` functions
   5. Other `requests.Response` object properties and methods
5. Sorting: controlling the sort order with a user-defined function
   1. Challenge 03
6. Additional challenges
   1. Challenge 04
   2. Challenge 05
   3. Challenge 06
   4. Challenge 07

## Vocabulary

* __API__: Application Programming Interface that specifies a set of permitted interactions between
  systems.
* __HTTP__: The Hypertext Transport Protocol is an application layer protocol designed to facilitate
  the distributed transmission of hypermedia. Web data communications largely depends on HTTP.
* __JSON__: Javascript Object Notation, a lightweight data interchange format.
* __Querystring__: That part of a Uniform Resouce Locator (URL) that assigns values to specified
  parameters.
* __Resource__: A named object (e.g., document, image, service, collection of objects) that is both
  addressable and accessible via an API.
* __URI__: Uniform Resource Identifier that identifies unambiguously a particular resource.
* __URL__: Uniform Resource Locator is a type of URI that specifies the _location_ of a resource on
  a network and provides the means to retrieve it.
* __URN__: Uniform Resource Name is a type of URI that provides a unique identifier for a resource
  but does not specify its location on a network.

## 1.0 The Requests package

The authors of the [Requests package](https://requests.readthedocs.io/en/master/) describe it as
"an elegant and simple HTTP library for Python, built for human beings." With a single line of code
you can initiate communication over HTTP with a platform that provides an
application programming interface (API) for accessing resources (i.e., objects) remotely. You can
utilize the requests package&mdash;imported as a module&mdash;to create, retrieve, modify, and
delete resources stored on servers and accessible via the HTTP protocol.

### 1.1 Install `requests`

Read the relevant install guide and use `pip` from the command line to install the
[requests](https://pypi.org/project/requests/) package.

* [macOS](https://si506.org/guides/install_requests_package_macos/)
* [Windows](https://si506.org/guides/install_requests_package_windows/)

:exclamation: If you use [Anaconda](https://www.anaconda.com/) see the companion
["Updating the requests package (Anaconda users)"](https://si506.org/guides/conda_update_requests_package/).

### 1.2 Confirm installation

Open VS Code or your source code editor/IDE of choice and run the file `si506_test_swapi.py` from
either the command line (preferred) or directly from inside VS Code or other source code editor/IDE.

:exclamation: if VS Code does not recognize the `import requests` statement in your Python file or
you encounter a `ModuleNotFoundError` when running the file after pressing the run button,
then VS Code is likely using the wrong Python environment. You can check which Python environment
VS Code is using by first checking the Python version listed in the Side Bar (bottom left) of the
interface. If it is a version other than what you installed at the beginning of the course, you may
need to "repoint" VS Code to the right environment.

To do so, type `Cmd-Shift-P` (macOS) or `Ctrl-Shift-P` (Windows) to activate the Command Palette.
Then in the search box type: "Python: Select Interpreter". From the list of options, click on the
relevant Python interepreter (e.g., Python 3.9.7 64-bit). You may need to restart VS Code before
re-running the file. If the runtime error persists contact the teaching team via Slack.

For more info see, VS Code's
["Using Python Environments in VS Code"](https://code.visualstudio.com/docs/python/environments)

## 2.0 HTTP Request/Response cycle

The `swapi_get_test.py` script utilizes the `requests` module to send a message (known as a _request_)
to a remote server. The message is sent over HTTP (Hypertext Transfer Protocol), an application
layer protocol that supports data exchange between clients and servers. The server replies with a
message (known as a _response_). If the client is authorized to access the requested data (known
as a _resource_) identified by the provided Uniform Resource Identifier (URI, but in our case a URL)
the response will contain a representation of the resource, usually in the form of a JSON document.

HTTP and its extension HTTPS (Hypertext Transfer Protocol Secure) rely on lower level transport
layer protocols such as the Transmission Control Protocol (TCP) or the User Datagram Protocol (UDP)
to transmit packets of data between a client and a server. TCP privileges reliable
message delivery over speed and requires the server to acknowledge the receipt of data and permit
retransmission. UDP privileges speed over reliability and offers no guarantee of message delivery.
Exchanging messages with the Star Wars API (SWAPI) leverages HTTPS over TCP and the still
lower-level Internet Protocol (IP).

An HTTP request consists of an HTTP verb (e.g., `GET`), a resource identifier (e.g.,
`https://swapi.py4e.com/api/people/10/`), the protocol version (`HTTP/1.1`), optional headers, and
an optional body (itself a resource). An HTTP response consists of the protocol version, status code
(e.g., `200`), status message (e.g., `OK`), headers, and an optional body (the requested resource).

The HTTP request methods utilized most frequently include `GET`, `PUT`, `POST`, and `DELETE`.
Other HTTP methods include `CONNECT`, `HEAD`, `OPTIONS`, `PATCH` and `TRACE`.

:bulb: For SI 506 you need only concern yourself with the `GET` method.

<br />
    <img src="./http_swapi.png" alt="Composition" style="display:block;margin-left:auto;margin-right:auto;width:80%">
<br />

The Python [requests](https://docs.python-requests.org/) package abstracts away much of the
complexity associated with creating an HTTP request. In the case of `swapi_test.py` we need only
pass a URL to the `requests` module's
[`get()` function](https://requests.readthedocs.io/en/latest/api/#requests.get) to initiate a valid
HTTP `GET` request.

The `requests.get()` function's return value is an instance of
[`request.Response`](https://requests.readthedocs.io/en/latest/api/#requests.Response), an object
which contains the JSON-encoded representation of the requested resource. We can access the
`response.text` property to return the JSON documents as a string. Better yet, we can call the
`response.json()` method in order to decode the JSON document into a dictionary.

## 3.0 The Star Wars API (SWAPI)

The [Star Wars API](https://swapi.py4e.com/) (SWAPI) provides an API for retrieving representations
of films, people, planets, species, starships, and vehicles from
_a long time ago in a galaxy far, far away. . . ._

:exclamation: The SWAPI API currently accepts HTTP `GET` requests only (no `PUT`, `POST`, `DELETE`
requests accepted).

SWAPI provides the following endpoint for requesting resources:

```python
endpoint = "https://swapi.py4e.com/api"
```

### 3.1 SWAPI: request resource categories (`/api/`)

To return a dictionary of key-value pairs that represent the current SWAPI resource categories,
add a trailing slash (`/`) to the endpoint when passing the URL to the `requests.get()` method.

:bulb: call the response object's `json()` method to "decode" the message as a list or dictionary.

```python
response = requests.get(endpoint + "/") # note trailing slash
resources = response.json() # convert message content to dict

print(f"\n2.1 SWAPI Resources (n={len(resources)})")
for key, val in resources.items():
    print(f"{key.capitalize()}: {val}")
```

:bulb: For more information on how to utilize SWAPI to retrieve resources, see the SWAPI
[documentation](https://swapi.py4e.com/documentation) page.

:exclamation: Do _not_ use any of the available SWAPI helper libraries to write your code. You will
interact with SWAPI using the [requests](https://pypi.org/project/requests/) module and your own
code only.

### 3.2 SWAPI: request resources by category (`/api/:category/`)

You can retrieve a collection of resources by category (e.g., people) by employing the following
URL pattern:

`/api/:category/`

as in

`https://swapi.py4e.com/api/people/`

:exclamation: Note that SWAPI will _not_ respond by returning a collection of all people resources.
Instead, SWAPI responses are _paged_, with each paged response limited to a max of ten (`10`)
records per request.

```python
url = f"{endpoint}/people/"
response = requests.get(url)

content = response.json() # decode
content_count = content["count"]
people_returned = len(content["results"]) # SWAPI only returns max 10 records per request
people = content["results"]

for person in people:
    print(person["name"])
```

SWAPI will respond with the following JSON document that provides a paged list of resources stored in a
"results" list along with a URI that can be used to retrieve the `next` set of paged resources.

```json
{
   "count": 87,
   "next": "https://swapi.py4e.com/api/people/?page=2",
   "previous": null,
   "results": [
     {< Person object >},
     {< Person object >},
     {< Person object >},
     {< Person object >},
     {< Person object >},
     {< Person object >},
     {< Person object >},
     {< Person object >},
     {< Person object >},
     {< Person object >}
   ]
}
```

### 3.3 SWAPI: request single resource by id (`/api/:category/:id/`)

You can retrieve a single resource by specifying both its category and identifier (number only)
by employing the following URL pattern:

`/api/:category/:id/`

as in

`https://swapi.py4e.com/api/people/1/`

```python
url = f"{endpoint}/people/1/" # Luke Skywalker
response = requests.get(url) # JSON representation of person returned
person = response.json() # decode to dict
```

### 3.4 SWAPI: search category with querystring (`/api/:category/?search=<search term>`)

The SWAPI API also facilitates text-based searching of resources. This feature is limited currently
to searching on the following attributes:

* `< name >` (all resources)
* `< title >` (Film)
* `< model >` (Starship, Vehicle)

The search feature employs _case-insensitive_ partial matches (i.e., contains) on searchable fields.

You can search a category by employing the following URL pattern, which appends a querystring to
the URL:

`/api/:category/?search=<search term>`

as in

`https://swapi.py4e.com/api/starships/?search=wing`

Convienently, the `requests.get()` function defines a second parameter named "params" for passing
querystring key-value pairs as dictionary key-value pairs as an optional argument.

```python
url = f"{endpoint}/starships/"
params = {"search": "wing"} # dict
response = requests.get(url, params) # pass search parameters as 2nd argument

content = response.json() # decode
starships = content["results"]
```

:bulb: one can solve the paging challenge by writing a
[recursive function](https://realpython.com/python-thinking-recursively/) that calls itself
repeatedly in order to return every paged set of records. But learning how to write such a function
is out of scope for SI 506.

### 3.5 SWAPI: search limitations

1. Only accepts two query string types:

   a. `search=< string >` (name, title, or model depending on entity)

   b. `page=< num >`

2. Search employs case-insensitive partial matches on search fields.

3. Response results are paged and limited to a maixum of __10 records__ per request.

SWAPI will respond with a JSON document of the requested resource if it exists:

__Request__

`https://swapi.py4e.com/api/people/?search=rey`

__Response__

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "name": "Rey",
      "height": "unknown",
      "mass": "unknown",
      "hair_color": "brown",
      "skin_color": "light",
      "eye_color": "hazel",
      "birth_year": "unknown",
      "gender": "female",
      "homeworld": "https://swapi.py4e.com/api/planets/28/",
      "films": [
        "https://swapi.py4e.com/api/films/7/"
      ],
      "species": [
        "https://swapi.py4e.com/api/species/1/"
      ],
      "vehicles": [],
      "starships": [],
      "created": "2015-04-17T06:54:01.495077Z",
      "edited": "2015-04-17T06:54:01.495128Z",
      "url": "https://swapi.py4e.com/api/people/85/"
    }
  ]
}
```

### 3.6 Challenge 01

__Task__: Retrieve a SWAPI representation of Chewbacca and supplement the representation with
homeland and species data.

1. In `main()` call the function `requests.get()` passing the correct URL value and the
   querystring name-value pair "search" (name) and "chewbacca" (value) as arguments. Retrieve a
   response that contains a representation of the Wookiee Chewbacca (a.k.a Chewie). Assign the
   return value to a variable named `response`.

2. Decode the response by calling the `response` object's `json()` method. Assign the return value
   to a variable named `content`.

   :exclamation: The JSON response that is decoded into a dictionary is structured as follows:

   ```json
   {
     "count": 1,
     "next": null,
     "previous": null,
     "results": [
       {< Chewbacca >}
     ]
   }
   ```

3. Access the Chewbacca dictionary from `content` and assign it to variable named `chewie`.

4. Uncomment the call to `write_json()` that writes `chewie` to a JSON document named
   `stu-chewie.json`. Run your code and check the file.

## 4.0 Coding tips

### 4.1 Expression chaining

Note that you can chain the `response.json()` method call to `requests.get()` function call:

```python
# Get the Empire Strikes Back (1980)
url = f"{endpoint}/films/"
params = {"search": "empire strikes back"}
content = requests.get(url, params).json() # response.json() method chaining
film = content['results'][0]

print(f"\n2.5: Film = {film['title']} ({film['release_date']})")
```

Note that you can also add bracket notation to retrieve an element from the returned "results" list:

```python
# Get Yoda
url = f"{endpoint}/people/"
params = {"search": "yoda"}
yoda = requests.get(url, params).json()["results"][0] # whoa
```

### 4.2 `get_swapi_resource()` function

Given that you will be making frequent requests to the SWAPI endpoint in order to retrieve resources
we should implement a function to handle the task. The function `get_swapi_resource` "wraps" the
request module's `requests.get()` function and permits sending requests with and without
querystring parameters. The function returns a decoded dictionary or list of dictionaries.

:bulb: note that the function also sets a timeout value in seconds. This sets a limit on the wait
time allowed for a remote service to send back a response. If the wait time exceeds the timeout
value an exception is raised. You can test this feature by calling the function and passing to it a
timeout value of 0.001.

```python
def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    content of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()
```

### 4.3 Challenge 02

__Task__: Enrich the current dictionary representation of Chewbacca with his SWAPI homeland and
species data.

1. Access the `homeworld` URL in `chewie` and retrieve the Wookiee's home planet by calling
   `get_swapi_resource()` and passing the "homeworld" URL to it as an argument
   (_no search string required_). Map (i.e., assign) the return value to the `chewie` dictionary's
   "homeworld" key.

2. Access the `species` URL in `chewie` and retrieve the Wookiee's species by
   calling `get_swapi_resource()` and passing the URL to it as an argument (again,
   _no search string required_). Assign the return value to the `chewie` dictionary's "species"
   key.

   :exclamation: Take heed, the expression `chewie["species"]` resolves to a `list`.

3. Uncomment the call to `write_json()` that writes the "enriched" `chewie` dictionary to a file
   named `stu-chewie_enriched.json`. Run your code and check the file.

### 4.4 `create_< entity >()` functions

SWAPI entity representations contain data that may prove superfluous to your needs. Thinning
the data and/or converting values to different types is best handled by implementing "helper"
functions to handling the reshaping of the data. Both `create_person()` and `create_species()`
illustrate the technique:

```python
def create_person(data):
    """..."""

    if data.get("species"):
        species_data = get_swapi_resource(data["species"][0]) # checks cache
        species = create_species(species_data) # trim
    else:
        species = None

    return {
        "url": data.get("url"),
        "name": data.get("name"),
        "birth_year": data.get("birth_year"),
        "species": species
        }


def create_species(data):
    """..."""

    return {
        "url": data.get("url"),
        "name": data.get("name"),
        "classification": data.get("classification"),
        "designation": data.get("designation"),
        "average_lifespan": convert_to_int(data.get("average_lifespan")),
        "language": data.get("language")
    }
```

As the function `create_species()` illustrates the `create_*()` functions work in tandem with
utility functions such as `convert_to_int()` to both clean and manipulate data.

In the example below, the SWAPI representation of Princess Leia Organa is restructured by calling
the function `create_person()` and passing `swapi_leia` to it.

```python
# Get Leia Organa
swapi_leia = get_swapi_resource(f"{endpoint}/people/", params={"search": "Leia Organa"})["results"][0]
leia = create_person(swapi_leia) # retrieves species from SWAPI

# Write to file
write_json("./stu-leia.json", leia)
```

The workflow results in a revised JSON representation of Leia:

```json
{
  "url": "https://swapi.py4e.com/api/people/5/",
  "name": "Leia Organa",
  "birth_year": "19BBY",
  "species": {
    "url": "https://swapi.py4e.com/api/species/1/",
    "name": "Human",
    "classification": "mammal",
    "designation": "sentient",
    "average_lifespan": 120,
    "language": "Galactic Basic"
  }
}
```

### 4.5 Other `requests.Response` object properties and methods

The return value of the `requests.get()` function is an instance of the `requests.Response` class.
The object is provisioned with a number of instance variables and methods. Although you will not be
required to make use of these variables or methods you should consider familiarizing yourself with
the request module's [API](https://requests.readthedocs.io/en/latest/api/#) as you learn how to
use it.

```python
# Get Yoda
url = f"{endpoint}/people/"
params = {"search": "chewbacca"}
response = requests.get(url, params)

# Status code
print(f"\nResponse status code = {response.status_code}")

# Response headers
print(f"\nResponse headers = {response.headers}")

# Encoding
print(f"\nResponse encoding = {response.encoding}")

# Check for bad request
if response.raise_for_status():
    print(f"\nBad request")
else:
    print(f"\nValid request")

# Decode response
name = response.json()["results"][0]["name"]
print(f"\nResource name = {name}")
```

## 5.0 Sorting: controlling the sort order with a user-defined function

In earlier lectures I included "bonus" code illustrating how to sort lists and dictionaries using
the built-in function `sorted()` and the `list.sort()` method. For example, I sorted NYT Times
article subject dictionaries employing a dictionary comprehension and the built-in function
`sorted()`:

```python
# Sort dict items
subjects = {k: v for k, v in sorted(subjects.items())}
```

I sorted counts of NYT Time article keywords employing a dictionary comprehension, the built-in
function `sorted()` and an anonymous function called a `lambda`.

```python
# Sort by value (reversed = -x[1]), then by key (x[0])
keyword_counts = {k: v for k, v in sorted(keyword_counts.items(), key=lambda x: (-x[1], x[0]))}
```

You will learn how to work with lambdas the week after. In the meantime I
want to show you how to sort lists using either `sorted()` or `list.sort()` and a user-defined function.

First, let's review the built-in function `sorted()`. Passing an _iterable_ to the function will
return a _new_ list with the elements in _ascending_ order. Consider the following select list of
planet names extracted from the `data-swapi_planets.json` file.

```python
planets = read_json("./data-swapi_planets.json")
planet_names = [planet["name"] for planet in planets]
```

Passing the list to `sorted()` results in a new list being returned with its integer elements sorted
in ascending order:

```python
planet_names_sorted = sorted(planet_names[:6]) # slice (61 planets in total)
# ["Alderaan", "Bespin", "Dagobah", "Hoth", "Tatooine", "Yavin IV"]
```

If you wanted to reverse the sort order and the return the course numbers in _descending_ order you
can pass to `sorted()` the optional keyword argument `reverse=True`:

```python
planet_names_sorted = sorted(planet_names[:6], reverse=True)
# ["Yavin IV", "Tatooine", "Hoth", "Dagobah", "Bespin", "Alderaan"]
```

Recall that `sorted()` returns a new list. If you want to sort the `courses` list without generating
a new list you can call the `list.sort()` method. This performs an _in-place_ operation, mutating
`courses` directly, and returning `None` to the caller implicitly.

```python
planet_names.sort() # ascending
planet_names.sort(reverse=True) # descending
```

:exclamation: Note that you cannot use `sorted()` or `list.sorted()` to sort lists that contain
non-compatible data types (e.g., a mix of strings and integers).

```python
mix = [1, 2, "One", "one", "ONE", 1.1, "1", "01", 506]
mix_sorted = sorted(mix) # Triggers TypeError
mix.sort() # Triggers TypeError
```

You can provide your own sort _algorithm_ (i.e., process or set of rules) by creating a user-defined
function and passing the __name__ of the function to either the built-in function `sorted()` or
`list.sort()` method using the keyword argument `key`.

In the following example a list of SWAPI planet dictionaries is sorted by each planet's population
value. This is achieved by implementing the function named `sort_by_population` and then passing the
__name__ of the function bound to the keyword argument `key` to either `sorted()` or `list.sort()`:

```python
def sort_by_population(entity):
    """Tries to return an < entity > dictionary's population value converted to
    an integer.

    WARN: If the < entity > population value cannot be converted to an integer the
    function returns zero (0) to the caller.

    Parameters:
        entity (dict): dictionary to parse

    Returns:
        int: returns an integer if the original value can be cast to a string;
             otherwise, returns zero (0).
    """

    try:
        return int(entity["population"])
    except:
        return 0

# Sort by population size (ascending order, smallest to largest)
planets_sorted = sorted(planets, key=sort_by_population) # name of function only

# Sort by population size (descending order, largest to smallest)
planets_sorted = sorted(planets, key=sort_by_population, reverse=True)

# Sort in-place: list.sort() method
planets.sort(key=sort_by_population, reverse=True)
```

:exclamation: Bear in mind that limitations exist with this approach:

1. The function passed to `sorted()` or `list.sort()` can only define a _single_ parameter.
   Provisioning the function with multiple parameters will trigger a `TypeError` when it is passed
   to `sorted()` or `list.sort()`.

2. The function _must_ be able to process all sequence/dictionary values encountered. Otherwise a
   `ValueError` will be triggered .

In the SWAPI planets example certain planets possess a population value of "unknown" that
cannot be converted to an integer.

```json
{
    "name": "Hoth",
    ...
    "population": "unknown",
    ...
    "url": "https://swapi.py4e.com/api/planets/4/"
  }
```

The function `sort_by_population()` handles this challenge with `try` and `except` blocks that
return a value of zero (`0`) if a value cannot be converted to an integer by passing it to the
built-in `int()` function. This ensures that all values can be processed when sorting.

### 5.1 Challenge 03

__Task__: Sort the `wookiee_starships` by length in reverse order.

1. Implement the function named `sort_by_length`. Review the function's docstring regarding its
   expected behavior, parameters, and return value.

2. After implementing the function return to `main()`. Uncomment the call to the function
   `read_csv_to_dicts()` that returns a list of starships sourced from the
   [Wookieepedia](https://starwars.fandom.com/) site.

3. Perform an __in-place__ sort of the `wookiee_starships` list. Sort the list by the following
   criteria:

     * Length of the starship
     * Length in descending order

   :bulb: Recall that an in-place sort will mutate existing list rather than create a new list.

4. After sorting `wookiee_starships` uncomment the call to `write_json()` that writes the
   list to a file named `stu-wookiee_starships_sorted.json`. Run your code and check the file.

## 6.0 Additional challenges

### 6.3 Challenge 04

__Task__: Combine SWAPI T-65 X-wing starfighter data with data sourced from the
[Wookieepedia](https://starwars.fandom.com/) X-wing starfighter "Legends"
[article](https://starwars.fandom.com/wiki/X-wing_starfighter/Legends).

1. In `main()` call `get_swapi_resource()` and retrieve a dictionary representation of a
   __T-65 X-wing__ starfighter. Assign the return value to a variable named `swapi_x_wing`.

   :bulb: Employ the search string "t-65 x-wing" rather than "x-wing" as there are two models of
   X-wing starfighters available for retrieval. If you opt to pass "x-wing" as the search string
   you will need to loop over the `result` list elements in order to access the T-65 X-Wing
   starfighter.

2. Call the function `read_csv_to_dicts` and retrieve the Wookieepedia starfighter data stored in
   the file `data-wookieepedia_starships.csv`. Assign the list of dictionaries to the variable named
   `wookiee_starships`.

3. Implement a `for` loop to access the T-65 Starfighter dictionary in the `wookiee_starships` list.
   Filter on each dictionary's "model" name. Assign the starfighter dictionary to a variable named
   `wookiee_x_wing`.

4. __Update__ the `x_wing` dictionary with the `wookiee_x_wing` dictionary, __if and only if__, the
   value assigned to `wookiee_x_wing` is _truthy_.

   :bulb: If you don't recall how to update one dictionary with another have a look at w3school's
   ["Python Dictionary Methods"](https://www.w3schools.com/python/python_ref_dictionary.asp) page;
   there is a handy `dict` method available to accomplish this task.

5. Uncomment the call to `write_json()` that writes `x_wing` to a JSON document named
   `stu-x_wing_enriched.json`. Run your code and check the file.

### 6.4 Challenge 05

__Task__: Implement a function that removes key-value pairs from a passed in dictionary. Then use
the function to "thin out" the T-65 X-Wing starfighter dictionary.

1. Implement the function named `drop_data`. Review the function's docstring regarding its expected
   behavior, parameters, and return value.

   __Function requirements and hints__

   1. The tuple of key names that you pass to the function will be employed as a filter that targets
      matching key-value pairs for removal from the passed in dictionary.

   2. Leverage a certain built-in function to perform the removals.

2. After implementing the function return to `main()`.

3. Call the function `drop_data` passing to it as arguments `x_wing` and `drop_keys`. Assign the
   return value to `x_wing`.

4. Uncomment the call to `write_json()` that writes `x_wing` to a JSON document named
   `stu-x_wing.json`.  Run your code and check the file.

### 6.5 Challenge 06

__Task__: Replace the list of `x_wing` pilot URLs with dictionary representations of each pilot.
When adding the pilot dictionaries to `x_wing` add the pilot's home planet and drop unneeded
key-value pairs.

1. Utilize a `for i in range()` loop to loop over the `x_wing` dictionary's __"pilots" list__.
   Provide `range()` with the appropriate `stop` value (an expression).

2. In the loop block peform the following tasks:

   1. Access each `x_wing` pilot's URL and pass it to the function `get_swapi_resource()` as the
      argument. Assign the return value to a variable named `pilot`.

   2. Call the function `drop_data()` and pass `pilot` and `drop_keys` to it as arguments. Remove
      unneeded key-value pairs. Assign the return value to `pilot`.

   3. Call the function `get_swapi_resource()` and pass the pilot's "homeworld" URL to it as the
      argument. Assign the return value to a variable named `homeworld`.

   4. Call the function `drop_data()` and pass `homeworld` and `drop_keys` to it as arguments.
      Remove unneeded key-value pairs. Map (i.e., assign) the return value to `pilot` dictionary's
      "homeworld" key.

   5. Finally, assign the mutated `pilot` dictionary to the `x_wing` dictionary's "pilots" list by
      replacing the URL string element used to retrieve the SWAPI pilot resource with `pilot`.

3. After updating `x_wing` uncomment the call to `write_json()` that writes `x_wing` to a JSON
    document named `stu-x_wing_pilots.json`. Run your code and check the file.

### 6.6 Challenge 07

__Task__: Retrieve Luke Skywalker and the astromech droid R2-D2 from SWAPI. Get R2-D2's home world.
Remove all unneeded key-value pairs. Assign Luke and R2-D2 as the `x_wing` crew members.

1. Access Luke Skywalker from the `x_wing` "pilots" list. Luke is conveniently the first element in
   the list. Assign the Skywalker dictionary to a variable named `luke`.

2. After retrieving Luke from the list, remove the `x_wing` `pilots` key-value pair. Pass
   __a single item tuple__ containing the appropriate key name to `drop_data` to accomplish the
   task.

3. Retrieve a SWAPI representation of astromech droid
   [R2-D2](https://starwars.fandom.com/wiki/R2-D2). Assign the return value to a variable named
   `r2`.

4. Remove unneeded key-value pairs from `r2`.

5. Retrieve R2-D2's home planet. Remove unneeded key-value pairs from the planet. Map (i.e., assign)
   the planet dictionary to the "homeworld" key in `r2`.

6. Next, assign `luke` and `r2` as `x_wing` crew members. Create a "crew members" dictionary
   comprising the following keys:

   * pilot
   * astromech_droid

   Assign `luke` as the "pilot" and `r2` as the "astromech_droid".

7. Mutate `x_wing` by adding a new "crew_members" key-value pair to the dictionary.

   ```python
   "crew_members": {"pilot": luke, "astromech_droid": r2}
   ```

8. Uncomment the call to `write_json()` and write `x_wing` to a JSON document named
   `stu-x_wing_crew.json`. Run your code and check the file.
