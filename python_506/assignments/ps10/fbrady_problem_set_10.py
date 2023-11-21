import json
import csv
import requests
import pprint
import os

print(f"\nProblem Set 10")
print(f"\n20th Century Fox")
print(f"\nA LUCASFILM LIMITED Production")
print(f"\nA long time ago in a galaxy far, far away....")
print(f"\nSWAPI: The Star Wars API")

# SETUP CODE
ENDPOINT = "https://swapi.py4e.com/api"

dialogue = {
    "C-3PO": [
        "Did you hear that?",
        "They've shut down the main reactor.",
        "We'll be destroyed for sure. This is madness!",
        "We're doomed!",
        "There'll be no escape for the Princess this time.",
        "What's that?",
    ],
    "R2-D2": ["beep, beep, boop.", "boop, beep, beep.", "boop, beeeep!"],
    "Darth Vader": ["sound of evil mechanical breathing"],
}
# END SETUP


def board_starship(starship, people):
    """Loops over the passed in people list, which is a list of tuples each representing
    people/passengers on the starship. Each tuple contains a variable assigned to a decoded
    JSON representing a person (in the 0th index) and a boolean indicating their intruder
    status (True, if intruder; False, if just a passenger) (in the 1st index).

    Example:
    [(< person_variable > , < intruder_bool > ), (< person_variable > , < intruder_bool > )]

    Utilizes sequence unpacking to access the 'person' element and the 'intruder' status
    element from the passed in list of tuples.

    Utilizes an if-elif-else statement and compound conditionals to evaluate the truth value
    of the 'intruder' status and check the following conditions:

        (1) If the 'intruder' status element evaluates to True and 'intruder' is already a
            key in the starship dictionary, then it simply appends the 'person' to the
            'intruder' key-value pair.
        (2) If the 'intruder' status element evaluates to True and 'intruder' is not yet a key
            in the starship dictionary, then it assigns a list literal containing the 'person'
            to the new 'intruder' key.
        (3) Otherwise, it appends the 'person' to the 'passengers' key.

    Parameters:
        starship (dict): a dictionary representation of the decoded JSON that contains
                         starship attributes.
        people (list): a list of tuples where, for each tuple, a variable assigned to
                       the decoded JSON representing a person is at the 0th index and a
                       bool value indicating whether they are an intruder is at the 1st index.

    Returns:
        dict: an updated dictionary of key-value pairs representing a starship.
    """
    for person, intruder in people:
        if intruder and "intruder" in starship.keys():
            starship["intruder"].append(person)
        elif intruder and "intruder" not in starship.keys():
            starship["intruder"] = [person]
        else:
            starship["passengers"].append(person)
    return starship


def capture_starship(attacker, prey):
    """Utilizes a conditional statement to check if the key 'primary_docking_bay'
    is not already present in the decoded JSON representing an attacking starship                                                     .

    If the conditional statement evaluates to 'True', it assigns the new key
    'primary_docking_bay' with a dictionary literal as its value. The dictionary
    literal has a key of 'docked' and a list literal containing the < prey >
    as its value. Otherwise, it gets access to the value of the key 'primary_docking_bay'
    and appends the < prey > to the 'docked' key.

    Parameters:
        attacker (dict): a dictionary representation of the decoded JSON
        that contains attributes of an attacking starship.
        prey (dict): a dictionary representation of the decoded JSON
        that contains attributes of a starship that is being captured.

    Returns:
        dict: an updated dictionary representation of the decoded JSON
        representing the attacking starship.
    """
    # if pdb in attacker, append prey to docked
    if "primary_docking_bay" in attacker:
        attacker["primary_docking_bay"]["docked"].append(prey)
    else:
        # create pdb key and assign docked:prey
        attacker["primary_docking_bay"] = {"docked": [prey]}
    return attacker


def create_person(person, url):
    """Returns a dictionary literal with the following keys:

    name, height, mass, birth_year, eye_color, homeworld, dialogue

    Leverages the get() method to access the corresponding value
    for certain keys (indicated above) present in the passed in person dictionary,
    except for the 'dialogue' key. Assign an empty list to the 'dialogue' key instead
    of utilizing the < get() > function.

    When assigning the "homeworld" value, leverage the < get_homeworld > function
    by passing to it both the return value from < get() > and the passed
    in < url >.

    Parameters:
        person (dict): a dictionary representation of the decoded JSON that contains
                       people attributes.

    Returns:
        dict: a dictionary of key-value pairs representing a person.
    """
    return {
        "name": person.get("name"),
        "height": person.get("height"),
        "mass": person.get("mass"),
        "birth_year": person.get("birth_year"),
        "eye_color": person.get("eye_color"),
        "homeworld": get_homeworld(person.get("homeworld"), url),
        "dialogue": [],
    }


def create_starship(starship):
    """Returns a dictionary literal with the following keys:

       name, model, passengers, max_atmosphering_speed, length

    Leverages the get() function to access the corresponding value
    for certain keys (indicated above) present in the passed in starship dictionary,
    except for the 'passengers' key. Assign an empty list to the 'passengers' key instead
    of utilizing the get() function.

    Parameters:
        starship (dict): a dictionary representation of the decoded JSON that contains
                         starship attributes.

    Returns:
        dict: a dictionary of key-value pairs representing a starship.
    """
    return {"name": starship.get("name"),
            "model": starship.get("model"),
            "passengers": [],
            "max_atmosphering_speed": starship.get("max_atmosphering_speed"),
            "length": starship.get("length")}


def get_homeworld(identifier, url):
    """Attempts to retrieve a SWAPI representation of a home planet using the provided
    < identifier >. The < identifier > is assumed to be either a planet name (e.g.,
    Dagobah) or a SWAPI planet URL (e.g., https://swapi.py4e.com/api/planets/5/).

    If the < identifier > commences with the substring "https://" the < identifier > is
    considered a URL and is passed to the function < get_swapi_resource() > as its < url >
    argument. Otherwise the < identifier > is assumed to be a planet name and is passed
    to < get_swapi_resource() > as a < params > value, while the < url > argument is
    passed to < get_swapi_resource() > as its < url > argument.

    The return value is a "thinned" dictionary literal with the following keys:

    name, diameter, climate, terrain, population


    Parameters:
        identifier (str): either a planet name or a SWAPI planet URL
        url (str): the URL pattern for a resource category

    Returns:
        dict: "thinned" dictionary literal representation of a planet
    """
    if identifier.startswith("https://"):
        planet = get_swapi_resource(url=identifier)
    else:
        planet = get_swapi_resource(url=url, params={"search": identifier})["results"][0]

    return {
        "name": planet.get("name"),
        "diameter": planet.get("diameter"),
        "climate": planet.get("climate"),
        "terrain": planet.get("terrain"),
        "population": planet.get("population"),
    }


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
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


def insert_dialogue(person, dialogue):
    """Loops over the < dialogue > dictionary key-value pairs accessing the dictionary's
    items leveraging the dictionary method `dict.items()`. Utilizes a conditional statement
    to check if the value corresponding to the 'name' key in the < person > dictionary
    matches a key in the < dialogue > dictionary.

    If the conditional statement evaluates to 'True', a list method that adds the
    elements of a list to the end of the current list is leveraged to update the
    'dialogue' key-value pair in the < person > dictionary.

    Parameters:
        person (dict): a dictionary representation of the decoded JSON that contains
                       people attributes.
        dialogue (dict): a dictionary whose key-value pairs each represent a person
                         and their dialogue.

    Returns:
        person (dict): a dictionary representation of the decoded JSON that contains
                       people attributes.
    """
    for key, val in dialogue.items():
        # print(key)
        if person.get("name") == key:
            person["dialogue"].extend(val)
    return person


def read_csv_to_dicts(filepath, encoding="utf-8-sig", newline="", delimiter=","):
    """
    Accepts a file path for a .csv file to be read, creates a file object,
    and uses csv.DictReader() to return a list of dictionaries
    that represent the row values from the file.

    Parameters:
        filepath (str): path to csv file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
    """

    with open(filepath, "r", newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:  # take out for loop and have students finish
            data.append(line)
        return data


def read_json(filepath, encoding="utf-8"):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, "r", encoding=encoding) as file_obj:
        return json.load(file_obj)


def write_json(filepath, data, encoding="utf-8", indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file

        data (dict)/(list): the data to be encoded as JSON and written to
        the file

        encoding (str): name of encoding used to encode the file

        indent (int): number of "pretty printed" indention spaces applied to
        encoded JSON

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(data, file_obj, indent=indent)


def main():
    """
    This function serves as the point of entry and controls the flow of this Python script.

    Parameters:
        None

    Returns:
        None
    """

    # Configure pretty printer
    pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)
    # pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

    # Problem 01
    print("\nProblem 01:")

    # TODO 1.1
    SWAPI_FILMS = ENDPOINT + "/films/"
    SWAPI_STARSHIPS = ENDPOINT + "/starships/"
    SWAPI_PEOPLE = ENDPOINT + "/people/"

    # TODO 1.2
    swapi_new_hope = get_swapi_resource(SWAPI_FILMS, params={"search": "new hope"})["results"][0]

    pp.pprint(swapi_new_hope)
    assert swapi_new_hope["title"] == "A New Hope"

    # Problem 02
    print("\nProblem 02:")

    # TODO 2.1
    new_hope = {
        "title": swapi_new_hope.get("title"),
        "episode_id": swapi_new_hope.get("episode_id"),
        "opening_crawl": swapi_new_hope.get("opening_crawl"),
        "director": swapi_new_hope.get("director"),
        "release_date": swapi_new_hope.get("release_date"),
        # empty last key to be filled in later
        "starships": [],
    }

    pp.pprint(new_hope)

    assert set(new_hope) == {
        "title",
        "episode_id",
        "opening_crawl",
        "director",
        "release_date",
        "starships",
    }

    # TODO 2.2
    write_json("stu-newhope_filtered.json", new_hope)
    # ## compare to fxt
    # ## IF RUNNING ON francisco
    # if os.getenv("USER") == "francisco":
    #     stu = read_json("stu-newhope_filtered.json")
    #     fxt = read_json("fxt-newhope_filtered.json")
    #     assert set(stu) == set(fxt)

    # Problem 03
    print("\nProblem 03:")

    # TODO 3.3
    params = {"search": "CR90 corvette"}
    swapi_rebel_blockade = get_swapi_resource(SWAPI_STARSHIPS, params).get("results")[0]

    params = {"search": "destroyer"}
    swapi_stardestroyer = get_swapi_resource(SWAPI_STARSHIPS, params).get("results")[0]

    # TODO 3.4
    rebel_blockade = create_starship(swapi_rebel_blockade)
    stardestroyer = create_starship(swapi_stardestroyer)

    assert rebel_blockade.get("max_atmosphering_speed") == "950"
    assert stardestroyer.get("max_atmosphering_speed") == "975"

    # Problem 04
    print("\nProblem 04:")

    # TODO 4.3
    params = {"search": "R2-D2"}
    swapi_r2d2 = get_swapi_resource(SWAPI_PEOPLE, params).get("results")[0]

    params = {"search": "C-3PO"}
    swapi_c3po = get_swapi_resource(SWAPI_PEOPLE, params).get("results")[0]

    params = {"search": "Leia Organa"}
    swapi_leia = get_swapi_resource(SWAPI_PEOPLE, params).get("results")[0]

    # TODO 4.4
    assert get_homeworld(swapi_r2d2["homeworld"], SWAPI_PEOPLE) == {
        "name": "Naboo",
        "diameter": "12120",
        "climate": "temperate",
        "terrain": "grassy hills, swamps, forests, mountains",
        "population": "4500000000",
    }
    assert get_homeworld(swapi_c3po["homeworld"], SWAPI_PEOPLE) == {
        "name": "Tatooine",
        "diameter": "10465",
        "climate": "arid",
        "terrain": "desert",
        "population": "200000",
    }

    # Problem 05
    print("\nProblem 05:")

    # TODO 5.3
    r2d2 = create_person(swapi_r2d2, SWAPI_PEOPLE)
    c3po = create_person(swapi_c3po, SWAPI_PEOPLE)
    leia = create_person(swapi_leia, SWAPI_PEOPLE)

    # Problem 06
    print("\nProblem 06:")

    # TODO 6.3
    people = [(r2d2, False), (c3po, False), (leia, False)]

    # TODO 6.4
    board_starship(rebel_blockade, people)

    pp.pprint(rebel_blockade)
    # assert that c3po is in the passengers list
    assert c3po in rebel_blockade["passengers"]

    # Problem 07
    print("\nProblem 07:")

    # TODO 7.1
    troopers = read_csv_to_dicts("data-troopers.csv")
    # TODO 7.2
    trooper_list = [(trooper, bool(int(trooper["intruder"]))) for trooper in troopers]
    # TODO 7.3
    board_starship(rebel_blockade, trooper_list)
    # assert that stormtrooper 1 is in the intruder list
    assert rebel_blockade.get("intruder")[0]["person"] == "stormtrooper 1"
    # Problem 08
    print("\nProblem 08:")

    # TODO 8.2
    capture_starship(stardestroyer, rebel_blockade)
    # pp.pprint(stardestroyer)
    # assert that stardestroyer was updated to include new key-value pair primary_docking_bay
    # with dict docked:rebel_blockade as it's value
    assert stardestroyer.get("primary_docking_bay") == {"docked": [rebel_blockade]}
    # Problem 09
    print("\nProblem 09:")

    # TODO 9.2
    insert_dialogue(r2d2, dialogue)
    insert_dialogue(c3po, dialogue)

    # assert dialoge in r2d2 is not empty
    assert r2d2["dialogue"] != []
    pp.pprint(r2d2.get("dialogue"))
    # assert c3po's dialogue is not empty
    assert c3po["dialogue"] != []
    pp.pprint(c3po.get("dialogue"))

    # Problem 10
    print("\nProblem 10:")

    # TODO 10.1.1
    swapi_vader = get_swapi_resource(SWAPI_PEOPLE, params={"search": "vader"}).get("results")[0]

    # TODO 10.1.2
    vader = create_person(swapi_vader, SWAPI_PEOPLE)

    # TODO 10.1.3
    people = [(vader, True)]
    board_starship(rebel_blockade, people)
    # TODO 10.1.4
    insert_dialogue(vader, dialogue)
    # assert vader's dialogue is not empty
    assert vader["dialogue"] != []
    pp.pprint(vader.get("dialogue"))
    # assert vader is in rebel_blockade intruder list
    assert vader in rebel_blockade["intruder"]

    # Problem 11
    print("\nProblem 11:")

    # TODO 11.1
    new_hope["starships"] = [stardestroyer]

    # TODO 11.2
    droids = [r2d2, c3po]
    for droid in droids:
        droid["end_vessel"] = "escape_pod"

    # TODO 11.3
    new_hope["escaped_passengers"] = droids
    # TODO 11.4
    write_json("stu-newhope_final.json", new_hope)

    # ## compare to fxt
    # ## ONLY IF RUNNING ON francisco
    # if os.getenv("USER") == "francisco":
    #     stu = read_json("stu-newhope_final.json")
    #     fxt = read_json("fxt-newhope_final.json")
    #     assert set(stu) == set(fxt)


if __name__ == "__main__":
    main()
