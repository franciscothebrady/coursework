# PROBLEM SET 11
import copy
import five_oh_six as utl

# Cache
cache = utl.create_cache(utl.CACHE_FILEPATH)

SWAPI_ENDPOINT = "https://swapi.py4e.com/api"
SWAPI_CATEGORIES = f"{SWAPI_ENDPOINT}/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"
SWAPI_VEHICLES = f"{SWAPI_ENDPOINT}/vehicles/"


def board_passengers(starship, passengers):
    """Assigns < passengers > to the passed in < starship > but limits boarding to less than
    or equal to the starship's "max_passengers" value. The passengers list (in whole or in part)
    is then mapped (i.e., assigned) to the passed in starship's 'passengers_on_board' key. After
    boarding the passengers the starship is returned to the caller.

    WARN: The number of passengers permitted to board a starship is limited by the starship's
    "max_passengers" value. If the number of passengers attempting to board exceeds the starship's
    "max_passengers" value only the first n passengers (where `n` = "max_passengers") are
    permitted to board the vessel.

        Parameters:
            starship (dict): Representation of a starship.
            passengers (list): passengers to transport aboard starship.

        Returns:
            dict: starship with assigned passengers.
    """

    pass


def convert_gravity_value(value):
    """Convert a planet's "gravity" value to a float. Removes the "standard" unit of measure if
    it exists in the string (case-insensitive check). Delegates to the function
    < convert_to_float > the task of casting the < value > to a float.

    If an exception is encountered the < value > is passed to < convert_to_none > in an attempt
    to convert the < value > to None if the < value > matches a < NONE_VALUES > item. The return
    value of < convert_to_none > is then returned to the caller.

    Parameters:
        value (obj): string to be converted.

    Returns:
        float: if value successfully converted; otherwise returns value unchanged.
    """

    pass


def create_droid(data):
    """Returns a new dictionary representation of a droid from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        equipment -> equipment (str to list)

    Key order:
        url
        name
        model
        manufacturer
        create_year
        height_cm
        mass_kg
        equipment
        instructions

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """
    pass


def create_person(data, planets=None):
    """Returns a new dictionary representation of a person from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    If an optional Wookieepedia-sourced < planets > list is provided, the task of retrieving
    the appropriate nested dictionary (filtered on the passed in homeworld planet name) is
    delegated to the function < get_mandalorian_data >.

    If a < planets > list is not provided, the task of retrieving
    the appropriate nested dictionary (filtered on the passed in homeworld/planet)
    is delegated to the function < get_swapi_resource >.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Before the homeworld is mapped (e.g. assigned) to the person's "homeworld"
    key, the function < create_planet > is called
    in order to provide a new dictionary representation of the person's homeworld.

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        homeworld -> homeworld (str to dict)

    Key order:
        url
        name
        birth_year
        height_cm
        mass_kg
        homeworld
        force_sensitive

    Parameters:
        data (dict): source data.
        planets (list): optional supplemental planetary data.

    Returns:
        dict: new dictionary.
    """

    pass


def create_planet(data):
    """Returns a new dictionary representation of a planet from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    < data > values that are members of < utl.NONE_VALUES > (case insensitive comparison)
    are first converted to < None > by calling < utl.convert_none_values > and returning
    a new dictionary. Once that task is accomplished other < utl.convert_to_*() > functions
    are called as necessary in an attempt to convert certain values to more appropriate types
    per the "Type conversions" and "New/repurposed key-value pairs" listed below. Key-value
    pairs that are retained, renamed, or added are listed below under "Key order".

    Type conversions:
        suns -> suns (str->int)
        moons -> moons (str->int)
        orbital_period -> orbital_period_days (str to float)
        diameter -> diameter_km (str to int)
        gravity -> gravity_std (str to float)
        climate -> climate (str to list)
        terrain -> terrain (str to list)
        population -> population (str->int)

    Key order:
        url
        name
        region
        sector
        suns
        moons
        orbital_period_days
        diameter_km
        gravity_std
        climate
        terrain
        population

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """
    pass


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible.

    Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        crew -> crew_size (str to int)
        passengers -> max_passengers (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to int)

    Key order:
        url
        name
        model
        starship_class
        manufacturer
        length_m
        max_atmosphering_speed
        hyperdrive_rating
        top_speed_mglt
        armament
        crew_size
        crew_members
        max_passengers
        passengers_on_board
        cargo_capacity_kg
        consumables

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """
    pass


def create_vehicle(data):
    """Returns a new vehicle dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible.

    Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        crew -> crew_size (str to int)
        passengers -> max_passengers (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to int)

    Key order:
        url
        name
        model
        vehicle_class
        manufacturer
        length_m
        max_atmosphering_speed
        armament
        crew_size
        crew_members
        passengers
        passengers_on_board
        cargo_capacity_kg
        consumables

    Parameters:
        data (dict): source data.

    Returns:
        dict: new dictionary.
    """

    pass


def get_mandalorian_data(mandalorian_data, filter):
    """Attempts to retrieve a Wookieepedia sourced dictionary representation of a
    Star Wars entity (e.g., droid, person, planet, species, starship, or vehicle)
    from the < mandalorian_data > list using the passed in filter value. The function performs
    a case-insensitive comparison of each nested dictionary's "name" value against the
    passed in < filter > value. If a match is obtained the dictionary is returned to the
    caller; otherwise None is returned.

    Parameters:
        mandalorian_data (list): Wookieepedia-sourced data stored in a list of nested dictionaries.
        filter (str): name value used to match on a dictionary's "name" value.

    Returns
        dict|None: Wookieepedia-sourced data dictionary if match on the filter is obtained;
                   otherwise returns None.
    """
    pass


def get_swapi_resource(url, params=None, timeout=10):
    """Retrieves a deep copy of a SWAPI resource from either the local < cache >
    dictionary or from a remote API if no local copy exists. Delegates to the function
    < utl.create_cache_key > the task of minting a key that is used to identify a cached
    resource. If the desired resource is not located in the cache, delegates to the
    function < get_resource > the task of retrieving the resource from SWAPI.
    A deep copy of the resource retrieved remotely is then added to the local < cache > by
    mapping it to a new < cache[key] >. The mutated cache is written to the file
    system before a deep copy of the resource is returned to the caller.

    WARN: Deep copying is required to guard against possible mutatation of the cached
    objects when dictionaries representing SWAPI entities (e.g., films, people, planets,
    species, starships, and vehicles) are modified by other processes.

    Parameters:
        url (str): a uniform resource locator that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict|list: requested resource sourced from either the local cache or a remote API
    """

    key = utl.create_cache_key(url, params)
    if key in cache.keys():
        return copy.deepcopy(cache[key])  # recursive copy of objects
    else:
        resource = utl.get_resource(url, params, timeout)
        cache[key] = copy.deepcopy(resource)  # recursive copy of objects
        utl.write_json(utl.CACHE_FILEPATH, cache)  # persist mutated cache

        return resource


def update_planets_visited(data, planet):
    """Adds new planet name to the key 'planets_visited' in the < data > dictionary. If the
    key 'planets_visited' is not in the < data > dictionary keys, the key is added to the dictionary.
    If the planet is not already stored in the key-value pair of 'planets_visited'
    then the planet's dictionary is added to the list.

    Parameters:
        data (dict): dictionary representation of a starship.
        planet (dict): dictionary representation of a planet.

    Returns:
        dict: dictionary with the 'planets_visited' key updated.
    """
    pass


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """
    # PROBLEM 01
    # Problem 1.2
    # TODO call function
    mandalorian_people = None

    # Problem 1.3-1.6
    # TODO call function
    mandalorian_starships = None
    mandalorian_planets = None
    mandalorian_droids = None
    mandalorian_vehicles = None

    # PROBLEM 02
    # Problem 2.1 Test convert_to_none(), convert_to_int(), convert_to_float(), convert_to_list()

    # TODO uncomment
    # Problem 2.2
    # assert utl.convert_to_none(" N/A ", utl.NONE_VALUES) == None
    # assert utl.convert_to_none("", utl.NONE_VALUES) == None
    # assert utl.convert_to_none("Yoda ", utl.NONE_VALUES) == "Yoda "

    # Problem 2.3
    # assert utl.convert_none_values(mandalorian_people[1], utl.NONE_VALUES) == {
    #     "name": "Carasynthia Dune",
    #     "height": "173",
    #     "mass": None,
    #     "hair_color": "black",
    #     "skin_color": "light",
    #     "eye_color": "brown",
    #     "birth_year": None,
    #     "gender": "female",
    #     "homeworld": "https://swapi.py4e.com/api/planets/2/",
    #     "species": "https://swapi.py4e.com/api/species/1/",
    #     "force_sensitive": "False",
    #     "url": "https://starwars.fandom.com/wiki/Carasynthia_Dune",
    # }
    # assert utl.convert_none_values(mandalorian_people[3], utl.NONE_VALUES) == {
    #     "name": "Gideon",
    #     "height": "183",
    #     "mass": None,
    #     "hair_color": "black, graying",
    #     "skin_color": "dark",
    #     "eye_color": "brown",
    #     "birth_year": None,
    #     "gender": "male",
    #     "homeworld": None,
    #     "species": "https://swapi.py4e.com/api/species/1/",
    #     "force_sensitive": "False",
    #     "url": "https://starwars.fandom.com/wiki/Gideon",
    # }

    # Problem 2.4
    # assert utl.convert_to_float("4.0") == 4.0
    # assert utl.convert_to_float("5,000") == 5000.0
    # assert utl.convert_to_float([618, 664]) == [618, 664]

    # Problem 2.5
    # assert utl.convert_to_int("506 ") == 506
    # assert utl.convert_to_int(" unknown") == " unknown"
    # assert utl.convert_to_int([506, 507]) == [506, 507]

    # Problem 2.6
    # assert utl.convert_to_list("Diag, Hatcher, North Quad", ", ") == ["Diag", "Hatcher", "North Quad"]
    # assert utl.convert_to_list("Han, Leia, Luke", ", ") == ["Han", "Leia", "Luke"]
    # assert utl.convert_to_list([506, 507], ", ") == [506, 507]

    # # Problem 2.8
    # assert convert_gravity_value("1 standard") == 1.0
    # assert convert_gravity_value("50 standard") == 50.0
    # assert convert_gravity_value("0.98") == 0.98

    # PROBLEM 3
    # Problem 3.2 Call get_mandalorian_data()
    # TODO call function
    mandalorian_nevarro = None
    mandalorian_arvala_7 = None

    # Problem 3.3 Write to file
    # TODO call function


    # Problem 3.5-3.6  Test < create_planet >
    # TODO call function
    swapi_tatooine = None
    tatooine = None

    # Problem 3.7 Write to file
    # TODO call function

    # PROBLEM 4
    # Problem 4.2-4.3 Test < create_droid >
    mandalorian_ig_11 = None
    ig_11 = None

    # Problem 4.4 Write to file
    # TODO call function

    # Problem 4.6-4.7 Test < create_person >
    # TODO call function
    mandalorian_din_djarin = None
    mando = None

    # Problem 4.8 Write to file
    # TODO call function

    # PROBLEM 5
    # Problem 5.2 Test < create_starship >
    # TODO call function
    razor_crest = None

    # Problem 5.3  Write to file
    # TODO call function

    # Problem 5.5-5.6 Test < create_vehicle >
    # TODO call function

    # Problem 5.7 Write to file
    # TODO call function

    # Problem 5.9 Test < board_passengers >
    # TODO call function

    # 5.10 print razor crest passengers
    # TODO uncomment print statement
    # print(f"\n5.3.1 razor crest passengers on board = {razor_crest['passengers_on_board']}")

    # PROBLEM 6
    # 6.2 Call update_planets_visited
    # TODO call function

    # 6.3 print razor crest visited planets
    # TODO uncomment print statement
    # print(f"\n6.3 razor crest visited planets = {razor_crest['planets_visited']}")

    # 6.4 Get Greef Karga
    # TODO call function

    # 6.5 Write to file
    # TODO call function

    # 6.6 Update planets_visited with Arvala-7
    # TODO call function

    # 6.7 print razor crest visited planets
    # TODO uncomment print statement
    # print(f"\n6.7 razor crest visited planets = {razor_crest['planets_visited']}")

    # PROBLEM 7

    # 7.1 Get Kuiil
    # TODO call function


    # 7.2 Write to file
    # TODO call function

    # 7.3 Get Grogu
    # TODO call function

    # 7.4 Write to file
    # TODO call function

    # 7.5-6 Get hovering pram
    # TODO call functions


    # 7.7 Write to file
    # TODO call function

    # 7.8 Reprogram IG-11
    new_instructions = "Protect Grogu and assist the Mandalorian"
    # TODO call dictionary method

    # Problem 7.9 Write to file
    # TODO call function

    # PROBLEM 08
    # Problem 8.1 Get planet Sorgan
    # TODO call function

    # Problem 8.2 Update razor crest planets
    # TODO call function

    # 8.3 print razor crest visited planets
    # TODO uncomment print statement
    # print(f"\n8.3 razor crest visited planets = {razor_crest['planets_visited']}")

    # Problem 8.4 Get Cara
    # TODO call function

    # Problem 8.5 Write to file
    # TODO call function

    # Problem 8.6 Get Gideon
    # TODO call function

    # Problem 8.7 Get imperial transport
    # TODO call function

    # Problem 8.8 Board imperial transport
    # TODO call function

    # Problem 8.9 Write to file
    # TODO call function

    # Problem 8.10 Update razor crest passengers
    # TODO call function

    # PROBLEM 09
    # Problem 9.1-9.2 Update razor crest
    # TODO call functions


    # Problem 9.3 Test use of lambda to sort planets
    # TODO call function

    # Problem 9.4 Print razor crest visited planets
    # TODO uncomment print statement
    # print(f"\n9.4 razor crest visited planets = {razor_crest['planets_visited']}")

    # Problem 9.5 Write to file
    # TODO call function

    # PERSIST util.cache (DO NOT COMMENT OUT BELOW)
    utl.write_json(utl.CACHE_FILEPATH, cache)


if __name__ == "__main__":
    main()
