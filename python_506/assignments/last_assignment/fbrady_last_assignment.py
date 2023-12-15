import copy
import five_oh_six as utl
import os
import pprint

pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)

from pathlib import Path


# Constants
CACHE_FILEPATH = "./CACHE.json"
NONE_VALUES = ("", "n/a", "none", "unknown")
SWAPI_ENDPOINT = "https://swapi.py4e.com/api"
SWAPI_CATEGORES = f"{SWAPI_ENDPOINT}/"
SWAPI_PEOPLE = f"{SWAPI_ENDPOINT}/people/"
SWAPI_PLANETS = f"{SWAPI_ENDPOINT}/planets/"
SWAPI_SPECIES = f"{SWAPI_ENDPOINT}/species/"
SWAPI_STARSHIPS = f"{SWAPI_ENDPOINT}/starships/"

# Create/retrieve cache
cache = utl.create_cache(CACHE_FILEPATH)


def assign_crew_members(crew_size, crew_positions, personnel):
    """Returns a dictionary of crew members mapped (i.e., assigned) by position and limited in
    size by the < crew_size > value.

    The < crew_positions > and < personnel > tuples must contain the same number of elements. The
    individual < crew_positions > and < personnel > elements are then paired by index position and
    stored in a dictionary structured as follows:

    {< crew_position[0] >: < personnel[0] >, < crew_position[1] >: < personnel[1] >, ...}

    WARN: The number of crew positions/members is limited by the < crew size > value. No additional
    crew positions/members are permitted to be assigned to the crew members dictionary even if
    passed to the function. Crew positions/members are assigned to the dictionary as key-value pairs
    by index position (0, 1, ...).

    A single line dictionary comprehension is employed to create the new crew members dictionary.

    Parameters:
        crew_size (int): max crew members permitted
        crew_positions (tuple): crew positions (e.g., 'pilot', 'copilot', etc.)
        personnel (tuple): flight crew to be assigned to the crew positions

    Returns:
        dict: crew members by position
    """
    return {crew_positions[i]: personnel[i] for i in range(crew_size)}


def board_passengers(max_passengers, passengers):
    """Returns a list of passengers that are permitted to board a starship or other vehicle. The
    size of the list is governed by the < max_passengers > value.

    WARN: The number of passengers permitted to board a starship or other vehicle is limited by the
    provided < max_passengers > value. If the number of passengers attempting to board exceeds
    < max_passengers > only the first < n > passengers (where `n` = "max_passengers") are permitted
    to board the vessel.

    Parameters:
        max_passengers (int): max number of passengers permitted to board a vessel
        passengers (list): passengers seeking permission to board

    Returns:
        list: passengers to board
    """
    allowed_passengers = []
    for passenger in passengers:
        if len(allowed_passengers) < max_passengers:
            allowed_passengers.append(passenger)
        else:
            break
    return allowed_passengers


def calculate_articles_mean_word_count(articles):
    """Calculates the mean (e.g., average) "word_count" of the passed in list of < articles >.
    Excludes from the calculation any article with a word count of zero (0) or < None >. Word counts
    are summed and then divided by the number of non-zero/non-< None > "word_count" articles. The
    resulting mean value is rounded to the second (2nd) decimal place and returned to the caller.

    The function maintains a count of the number of articles evaluated and a count of the total
    words accumulated from each article's "word_count" key-value pair.

    The function checks the truth value of each article's "word_count" before attempting to
    increment the count. If the truth vallue of the "word_count" is < False > the article is
    excluded from the count.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles

    Returns:
        float: mean word count rounded to the second (2nd) decimal place
    """
    article_count = 0
    word_total = 0

    for article in articles:
        if article.get("word_count") and article.get("word_count") != 0:
            article_count += 1
            word_total += article.get("word_count")
    return round(word_total / article_count, 2)


def convert_episode_values(episodes, none_values):
    """Converts select string values to either < int >, < float >, < list >, or < None >
    in the passed in list of nested dictionaries. The function delegates to the
    < utl.to_*() > functions the task of converting the specified strings to either
    an integer, float, list, or None.

    If a value is a member of < none_values > the value is replaced by < None >. Otherwise,
    various < utl.to_*() > functions are called as necessary in an attempt to convert
    certain episode values to more appropriate types per the "Type conversions" listed below.

    Type conversions:
        series_season_num (str) -> series_season_num (int | None)
        series_episode_num (str) -> series_episode_num (int | None)
        season_episode_num (str) -> season_episode_num (int | None)
        episode_prod_code (str) -> episode_prod_code (float | None)
        episode_us_viewers_mm (str) -> episode_us_viewers_mm (float | None)
        episode_writers (str) -> episode_writers (list | None)

    Parameters:
        episodes (list): nested episode dictionaries
        none_values (tuple): strings to convert to None

    Returns:
        list: nested episode dictionaries containing mutated key-value pairs
    """
    for episode in episodes:
        for key, value in episode.items():
            if value.lower().strip() in none_values:
                episode[key] = utl.to_none(value, none_values)
            elif key in ["series_season_num", "series_episode_num", "season_episode_num"]:
                episode[key] = utl.to_int(value)
            elif key in ["episode_prod_code", "episode_us_viewers_mm"]:
                episode[key] = utl.to_float(value)
            elif key == "episode_writers":
                episode[key] = utl.to_list(value, ", ")
            else:
                continue
    return episodes


def count_episodes_by_director(episodes):
    """Constructs and returns a dictionary of key-value pairs that associate each director with
    a count of the episodes that they directed. The director's name comprises the key and the
    associated value a count of the number of episodes they directed. Duplicate keys are NOT
    permitted.

    Format:
        {
            < director_name_01 >: < episode_count >,
            < director_name_02 >: < episode_count >,
            ...
        }

    Each director's episode count is incremented by < 1.0 > if, and only if, the director is
    the only person credited with directing the episode. Otherwise, if more than one person
    is credited with directing the episode each director is allocated a fraction of < 1.0 >.
    This value is calculated by dividing < 1.0 > by the number of directors credited with
    directing the episode.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that store counts of the number of episodes directed
              by each director
    """
    director_dict = {}
    for episode in episodes:
        # print(episode.get("episode_director"))
        directors = utl.to_list(episode.get("episode_director"), ", ")
        # print(directors)
        count = 1 / len(directors)
        for director in directors:
            if director in director_dict:
                director_dict[director] += count
            else:
                director_dict[director] = count
    return director_dict


def get_most_viewed_episode(episodes):
    """Identifies and returns a list of one or more episodes with the highest recorded
    viewership. Ignores episodes with no viewship value. Includes in the list only those
    episodes that tie for the highest recorded viewership. If no ties exist only one
    episode will be returned in the list. Delegates to the function < has_viewer_data >
    the task of determining if the episode includes viewership "episode_us_viewers_mm"
    numeric data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: episode(s) with the highest recorded viewership.
    """
    viewer_count = [0]
    top_episodes = []
    for episode in episodes:
        if has_viewer_data(episode):
            viewers = episode.get("episode_us_viewers_mm")
            max_viewers = max(viewer_count)
            if episode.get("episode_us_viewers_mm") > max_viewers:
                top_episodes = [episode]
                viewer_count = [viewers]
            elif viewers == max_viewers:
                top_episodes.append(episode)
                viewer_count.append(episode["episode_us_viewers_mm"])
    return top_episodes


def get_news_desks(articles, none_values):
    """Returns a list of New York Times news desks sourced from the passed in
    < articles > list. Accesses the news desk name from each article's "news_desk"
    key-value pair. Filters out duplicates in order to guarantee uniqueness. The
    list sorted alphanumerically before being returned to the caller.

    Delegates to the function < utl.to_none > the task of converting "news_desk"
    values that equal "None" (a string) to None. Only news_desk values that are "truthy"
    (i.e., not None) are returned in the list.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles
        none_values (tuple): strings to convert to None

    Returns:
        list: news desk strings (no duplicates) sorted alphanumerically
    """
    news_desks = []
    for article in articles:
        desk = utl.to_none(article.get("news_desk"), none_values)
        if desk:
            if desk not in news_desks:
                news_desks.append(desk)
    # print(sorted(news_desks))
    return sorted(news_desks)


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
        utl.write_json(CACHE_FILEPATH, cache)  # persist mutated cache
        return resource


def group_articles_by_news_desk(news_desks, articles):
    """Returns a dictionary of "news desk" key-value pairs that group the passed in
    < articles > by their parent news desk. The passed in < news_desks > list provides
    the keys while each news desk's < articles > are stored in a list and assigned to
    the appropriate "news desk" key. Each key-value pair is structured as follows:

    {
        < news_desk_name_01 >: [{< article_01 >}, {< article_05 >}, ...],
        < news_desk_name_02 >: [{< article_20 >}, {< article_31 >}, ...],
        ...
    }

    Each dictionary that represents an article is a "thinned" version of the New York Times
    original and consists of the following key-value pairs ordered as follows:

    Key order:
        web_url
        headline_main (new name)
        news_desk
        byline_original (new name)
        document_type
        material_type (new name)
        abstract
        word_count
        pub_date

    Parameters:
        news_desks (list): list of news_desk names
        articles (list): nested dictionary representations of New York Times articles

    Returns
        dict: key-value pairs that group articles by their parent news desk
    """
    articles_by_desk = {}
    for desk in news_desks:
        articles_by_desk[desk] = []
        for article in articles:
            if article.get("news_desk") == desk:
                articles_by_desk[desk].append(
                    {
                        "web_url": article.get("web_url"),
                        "headline_main": article.get("headline").get("main"),
                        "news_desk": article.get("news_desk"),
                        "byline_original": article.get("byline").get("original"),
                        "document_type": article.get("document_type"),
                        "material_type": article.get("type_of_material"),
                        "abstract": article.get("abstract"),
                        "word_count": article.get("word_count"),
                        "pub_date": article.get("pub_date"),
                    }
                )
    return articles_by_desk


def has_viewer_data(episode):
    """Checks the truth value of an episode's "episode_us_viewers_mm" key-value pair. Returns
    True if the truth value is "truthy" (e.g., numeric values that are not 0, non-empty sequences
    or dictionaries, boolean True); otherwise returns False if a "falsy" value is detected (e.g.,
    empty sequences (including empty or blank strings), 0, 0.0, None, boolean False)).

    Parameters:
        episode (dict): represents an episode

    Returns:
        bool: True if "episode_us_viewers_mm" value is truthy; otherwise False
    """
    if episode.get("episode_us_viewers_mm"):
        return True
    else:
        return False


def transform_droid(data, keys, none_values):
    """Returns a new "thinned" dictionary representation of a droid based on the passed in
     < data > dictionary with string values converted to more appropriate types.

    The new dictionary is constructed by mapping a subset of the < data > dictionary's
    key-value pairs to the new dictionary based on the passed in < keys >
    dictionary. The < keys > dictionary contains a nested "droid" dictionary that specifies
    the following features of the new dictionary to be returned to the caller:

     * the subset of < data > key-value pairs to be mapped to the new dictionary.
     * the order in which the < data > key-value pairs are mapped to the new dictionary.
     * the key names to be used in the new dictionary. Each key in < keys > corresponds to
       a key in < data >. Each value in < keys > represents the (new) key name to be used
       in the new dictionary.

     < data > values are converted to more appropriate types as outlined below under "Mappings".
     Strings found in < none_values > are converted to < None > irrespective of case. Type
     conversions are delegated to the various < utl.to_*() > functions. If a new key lacks a
     corresponding < data > value < None > is assigned.

    Each targeted < data > value is then mapped to the new key when assigning the new key-value
    pair to the new "droid" dictionary.

     Mappings (old key -> new key):
         url (str) -> url (str)
         name (str) -> name (str | None)
         model (str) -> model (str | None)
         manufacturer (str) -> manufacturer (str | None)
         create_year (str) -> create_date (dict | None)
         height (str) -> height_cm (float | None)
         mass (str) -> mass_kg (float | None)
         equipment (str) -> equipment (list | None)
         instructions (str) -> instructions (list | None)

     Parameters:
         data (dict): source data
         keys (dict): old key to new key mappings
         none_values (tuple): strings to convert to None

     Returns:
         dict: new dictionary representation of a droid
    """
    droid_dict = {}
    # keys = keys.get("droid")
    for key, value in keys.get("droid").items():
        # first check if key is in data
        if data.get(key):
            # pass through strings
            if key in ["url", "name", "model", "manufacturer"]:
                droid_dict[value] = utl.to_none(data.get(key), none_values)
            # convert to float
            elif key in ["height", "mass"]:
                droid_dict[value] = utl.to_none(utl.to_float(data.get(key)), none_values)
            # convert to year and era
            elif key in ["create_year"]:
                droid_dict[value] = utl.to_none(utl.to_year_era(data.get(key)), none_values)
            # convert to list
            elif key in ["equipment", "instructions"]:
                droid_dict[value] = utl.to_none(utl.to_list(data.get(key), "|"), none_values)
        # if key not in data create new key with value None
        else:
            droid_dict[value] = None
    return droid_dict


def transform_person(data, keys, none_values, planets=None):
    """Returns a new "thinned" dictionary representation of a person based on the passed in
    < data > dictionary with string values converted to more appropriate types.

    The new dictionary is constructed by mapping a subset of the < data > dictionary's
    key-value pairs to the new dictionary based on the passed in < keys >
    dictionary. The < keys > dictionary contains a nested "person" dictionary that specifies
    the following features of the new dictionary to be returned to the caller:

    * the subset of < data > key-value pairs to be mapped to the new dictionary.
    * the order in which the < data > key-value pairs are mapped to the new dictionary.
    * the key names to be used in the new dictionary. Each key in < keys > corresponds to
      a key in < data >. Each value in < keys > represents the (new) key name to be used
      in the new dictionary.

    < data > values are converted to more appropriate types as outlined below under "Mappings".
    Strings found in < none_values > are converted to < None > irrespective of case. Type
    conversions are delegated to the various < utl.to_*() > functions. If a new key lacks a
    corresponding < data > value < None > is assigned.

    Each targeted < data > value is then mapped to the new key when assigning the new
    key-value pair to the new "person" dictionary.

    Both the "homeworld" and "species" values require special handling.

    Retrieving a dictionary representation of the person's home planet is delegated to the
    function < get_swapi_resource() >. If the caller passes in a Wookieepedia-sourced
    < planets > list this function delegates to the function < utl.get_nested_dict() > the task
    of retrieving the Wookieepedia representation of the homeworld from < planets >.
    If the homeworld is found in < planets > the SWAPI and Wookieepedia dictionaries are
    combined. Cleaning the homeworld dictionary is delegated to the function < transform_planet() >.

    Likewise, retrieving a representation of the person's species is delegated to the function
    < get_swapi_resource() >. Cleaning the species dictionary is delegated to the function
    < transform_species() >.

    Mappings (old key -> new key):
        url (str) -> url (str)
        name (str) -> name (str | None)
        birth_year (str) -> birth_date (dict | None)
        height (str) -> height_cm (float | None)
        mass (str) -> mass_kg (float | None)
        homeworld (str) -> homeworld (dict | None)
        species (list) -> species (dict | None)
        force_sensitive (str) -> force_sensitive (str | None)

    Parameters:
        data (dict): source data
        keys (dict): old key to new key mappings
        none_values (tuple): strings to convert to None
        planets (list): Supplementary planet data

    Returns:
        dict: new dictionary representation of a person
    """
    person_dict = {}
    for key, value in keys.get("person").items():
        # if key in data
        if data.get(key):
            # print(key)
            # pass through strings
            if key in ["url", "name", "force_sensitive"]:
                person_dict[value] = utl.to_none(data.get(key), none_values)
            # convert to float
            elif key in ["height", "mass"]:
                person_dict[value] = utl.to_none(utl.to_float(data.get(key)), none_values)
            # convert birth date to year and era
            elif key in ["birth_year"]:
                person_dict[value] = utl.to_none(utl.to_year_era(data.get(key)), none_values)
            # special handling for species
            elif key in ["species"]:
                # only retrieve first url for species
                species = get_swapi_resource(data.get(key)[0])
                person_dict[value] = transform_species(species, keys, none_values)
            # special handling for homeworld
            elif key in ["homeworld"]:
                homeworld = get_swapi_resource(data.get(key))
                if planets:
                    wookie_homeworld = utl.get_nested_dict(planets, "name", homeworld.get("name"))
                    if wookie_homeworld:
                        homeworld.update(wookie_homeworld)
                person_dict[value] = transform_planet(homeworld, keys, none_values)
        # if key not in keys create new key with value None
        else:
            person_dict[value] = utl.to_none(data.get(key), none_values)
    return person_dict


def transform_planet(data, keys, none_values):
    """Returns a new "thinned" dictionary representation of a planet based on the passed in
    < data > dictionary with string values converted to more appropriate types.

    The new dictionary is constructed by mapping a subset of the < data > dictionary's
    key-value pairs to the new dictionary based on the passed in < keys >
    dictionary. The < keys > dictionary contains a nested "planet" dictionary that specifies
    the following features of the new dictionary to be returned to the caller:

    * the subset of < data > key-value pairs to be mapped to the new dictionary.
    * the order in which the < data > key-value pairs are mapped to the new dictionary.
    * the key names to be used in the new dictionary. Each key in < keys > corresponds to
      a key in < data >. Each value in < keys > represents the (new) key name to be used
      in the new dictionary.

    < data > values are converted to more appropriate types as outlined below under "Mappings".
    Strings found in < none_values > are converted to < None > irrespective of case. Type
    conversions are delegated to the various < utl.to_*() > functions. If a new key lacks a
    corresponding < data > value < None > is assigned.

    Each targeted < data > value is then mapped to the new key when assigning the new
    key-value pair to the new "planet" dictionary.

    Mappings (old key -> new key):
        url (str) -> url (str)
        name (str) -> name (str | None)
        region (str) -> region (str | None)
        sector (str) -> sector (str | None)
        suns (str) -> suns (int | None)
        moons (str) -> moons (int | None)
        orbital_period (str) -> orbital_period_days (float | None)
        diameter (str) -> diameter_km (int | None)
        gravity (str) -> gravity_std (float | None)
        climate (str) -> climate (list | None)
        terrain (str) -> terrain (list | None)
        population (str) -> population (int | None)

    Parameters:
        data (dict): source data
        keys (dict): old key to new key mappings
        none_values (tuple): strings to convert to None

    Returns:
        dict: new dictionary representation of a planet
    """
    planet_dict = {}
    # keys = keys.get("planet")
    for key, value in keys.get("planet").items():
        if data.get(key):
            # pass through strings
            if key in ["url", "name", "region", "sector"]:
                planet_dict[value] = utl.to_none(data.get(key), none_values)
            # convert to int
            elif key in ["suns", "moons", "population", "diameter"]:
                planet_dict[value] = utl.to_none(utl.to_int(data.get(key)), none_values)
            # convert to float
            elif key in ["orbital_period"]:
                planet_dict[value] = utl.to_none(utl.to_float(data.get(key)), none_values)
            # special handling for gravity
            elif key in ["gravity"]:
                planet_dict[value] = utl.to_none(
                    utl.to_gravity_value(data.get(key).split()[0]), none_values
                )
            # convert to list
            elif key in ["climate", "terrain"]:
                planet_dict[value] = utl.to_none(utl.to_list(data.get(key), ", "), none_values)
        # if key not in keys create new key with value None
        else:
            planet_dict[value] = None
    return planet_dict


def transform_species(data, keys, none_values):
    """Returns a new "thinned" dictionary representation of a species based on the passed in
    < data > dictionary with string values converted to more appropriate types.

    The new dictionary is constructed by mapping a subset of the < data > dictionary's
    key-value pairs to the new dictionary based on the passed in < keys >
    dictionary. The < keys > dictionary contains a nested "species" dictionary that specifies
    the following features of the new dictionary to be returned to the caller:

    * the subset of < data > key-value pairs to be mapped to the new dictionary.
    * the order in which the < data > key-value pairs are mapped to the new dictionary.
    * the key names to be used in the new dictionary. Each key in < keys > corresponds to
      a key in < data >. Each value in < keys > represents the (new) key name to be used
      in the new dictionary.

    < data > values are converted to more appropriate types as outlined below under "Mappings".
    Strings found in < none_values > are converted to < None > irrespective of case. Type
    conversions are delegated to the various < utl.to_*() > functions. If a new key lacks a
    corresponding < data > value < None > is assigned.

    Each targeted < data > value is then mapped to the new key when assigning the new
    key-value pair to the new "species" dictionary.

    Mappings (old key -> new key):
        url (str) -> url (str)
        name (str) -> name (str | None)
        classification (str) -> classification (str | None)
        designation (str) -> designation (str | None)
        average_lifespan (str) -> average_lifespan_yrs (int | None)
        average_height (str) -> average_height_cm (float | None)
        language (str) -> language (str | None)

    Parameters:
        data (dict): source data
        keys (dict): old key to new key mappings
        none_values (tuple): strings to convert to None

    Returns:
        dict: new dictionary representation of a planet
    """
    species_dict = {}
    # species_keys = keys.get("species")
    for key, value in keys.get("species").items():
        # if key in data
        if data.get(key):
            # pass through strings
            if key in ["url", "name", "classification", "designation", "language"]:
                species_dict[value] = utl.to_none(data.get(key), none_values)
            # convert to integer
            elif key in ["average_lifespan"]:
                species_dict[value] = utl.to_none(utl.to_int(data.get(key)), none_values)
            # convert to float
            elif key in ["average_height"]:
                species_dict[value] = utl.to_none(utl.to_float(data.get(key)), none_values)
        else:
            species_dict[value] = None
    return species_dict


def transform_starship(data, keys, none_values):
    """Returns a new "thinned" dictionary representation of a starship based on the passed in
    < data > dictionary with string values converted to more appropriate types.

    The new dictionary is constructed by mapping a subset of the < data > dictionary's
    key-value pairs to the new dictionary based on the passed in < keys >
    dictionary. The < keys > dictionary contains a nested "starship" dictionary that specifies
    the following features of the new dictionary to be returned to the caller:

    * the subset of < data > key-value pairs to be mapped to the new dictionary.
    * the order in which the < data > key-value pairs are mapped to the new dictionary.
    * the key names to be used in the new dictionary. Each key in < keys > corresponds to
      a key in < data >. Each value in < keys > represents the (new) key name to be used
      in the new dictionary.

    < data > values are converted to more appropriate types as outlined below under "Mappings".
    Strings found in < none_values > are converted to < None > irrespective of case. Type
    conversions are delegated to the various < utl.to_*() > functions. If a new key lacks a
    corresponding < data > value < None > is assigned.

    Each targeted < data > value is then mapped to the new key when assigning the new
    key-value pair to the new "starship" dictionary.

    Assigning crew members and passengers consitute separate operations.

    Mappings (old key -> new key):
        url (str) -> url (str)
        name (str) -> name (str | None)
        model (str) -> model (str | None)
        starship_class (str) -> starship_class (str | None)
        manufacturer (str) -> manufacturer (str | None)
        length (str) -> length_m (float | None)
        hyperdrive_rating (str) -> hyperdrive_rating (float | None)
        MGLT (str) -> max_megalight_hr (int | None)
        max_atmosphering_speed (str) -> max_atmosphering_speed_kph (int | None)
        crew (str) -> crew_size (int | None)
        crew_members (list) -> crew_members (list | None)
        passengers (str) -> max_passengers (int | None)
        passengers_on_board (list) -> passengers_on_board (list | None)
        cargo_capacity (str) -> cargo_capacity_kg (int | None)
        consumables (str) -> consumables (str | None)
        armament (list) -> armament (list | None)

    Parameters:
        data (dict): source data
        keys (dict): old key to new key mappings
        none_values (tuple): strings to convert to None

    Returns:
        dict: new dictionary representation of a planet
    """
    starship_dict = {}
    # starship_keys = keys.get("starship")
    for key, value in keys.get("starship").items():
        if data.get(key):
            # pass through strings
            if key in ["url", "name", "model", "starship_class", "manufacturer", "consumables"]:
                starship_dict[value] = utl.to_none(data.get(key), none_values)
            # convert to float
            elif key in ["length", "hyperdrive_rating"]:
                starship_dict[value] = utl.to_none(utl.to_float(data.get(key)), none_values)
            # convert to int
            elif key in ["MGLT", "max_atmosphering_speed", "crew", "passengers", "cargo_capacity"]:
                starship_dict[value] = utl.to_none(utl.to_int(data.get(key)), none_values)
            # convert to list
            elif key in ["crew_members", "passengers_on_board", "armament"]:
                starship_dict[value] = utl.to_none(utl.to_list(data.get(key), ","), none_values)
        else:
            starship_dict[value] = None
    return starship_dict


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    # 3.1 CHALLENGE 01

    assert utl.to_float("4") == 4.0
    assert utl.to_float("506,000,000.9999") == 506000000.9999
    assert utl.to_float("Darth Vader") == "Darth Vader"

    assert utl.to_int("506") == 506
    assert utl.to_int("506,000,000.9999") == 506000000
    assert utl.to_int("Ahsoka Tano") == "Ahsoka Tano"

    # 3.2 CHALLENGE 02

    assert utl.to_list("Use the Force") == ["Use", "the", "Force"]
    assert utl.to_list("X-wing|Y-wing", "|") == ["X-wing", "Y-wing"]
    assert utl.to_list([506, 507], ", ") == [506, 507]

    assert utl.to_none("", NONE_VALUES) == None
    assert utl.to_none("N/A ", NONE_VALUES) == None
    assert utl.to_none(" unknown", NONE_VALUES) == None
    assert utl.to_none("Yoda", NONE_VALUES) == "Yoda"
    assert utl.to_none(("41BBY", "19BBY"), NONE_VALUES) == ("41BBY", "19BBY")

    # 3.3 CHALLENGE 03
    clone_wars_episodes = utl.read_csv_to_dicts("data-clone_wars_episodes.csv")
    print(f"Total episodes: {len(clone_wars_episodes)}")

    # 3.4 CHALLENGE 04
    ## in a for loop check if the episode has viewer data using the has_viewer_data function
    ## increment a num_variable accumulator variable by 1 if the episode has viewer data
    ## print the num_variable accumulator variable
    num_episodes = 0
    for episode in clone_wars_episodes:
        if has_viewer_data(episode):
            num_episodes += 1

    print(num_episodes)
    print(f"Number of episodes with viewer data: {num_episodes}")

    # 3.5 CHALLENGE 05
    # apply convert_episode_values function to clone_wars_episodes
    clone_wars_episodes = convert_episode_values(clone_wars_episodes, NONE_VALUES)
    print(clone_wars_episodes[0])
    # write out json
    utl.write_json("stu-clone_wars-episodes_converted.json", clone_wars_episodes)

    # if USER is francisco, read fxt file and compare to stu file else skip
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-clone_wars-episodes_converted.json")
        stu = utl.read_json("stu-clone_wars-episodes_converted.json")
        assert stu == fxt

    # 3.5.2 get most viewed episode
    most_viewed_episode = get_most_viewed_episode(clone_wars_episodes)

    pp.pprint(f"Most viewed episode: {most_viewed_episode}")

    # 3.6 CHALLENGE 06
    director_episode_counts = count_episodes_by_director(clone_wars_episodes)
    # TODO Uncomment
    # Sort by count (descending), last name (ascending)
    director_episode_counts = {
        director: count
        for director, count in sorted(
            director_episode_counts.items(), key=lambda x: (-x[1], x[0].split()[-1])
        )
    }
    pp.pprint(f"director episode counts: {director_episode_counts}")
    # write to json as stu file
    utl.write_json("stu-clone_wars-director_episode_counts.json", director_episode_counts)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-clone_wars-director_episode_counts.json")
        stu = utl.read_json("stu-clone_wars-director_episode_counts.json")
        assert stu == fxt
    # 3.7 CHALLENGE 07
    articles = utl.read_json("data-nyt_star_wars_articles.json")
    # implement get news desks function
    news_desks = get_news_desks(articles, NONE_VALUES)
    pp.pprint(f"news desks: {news_desks}")
    # write to json
    utl.write_json("stu-nyt_news_desks.json", news_desks)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-nyt_news_desks.json")
        stu = utl.read_json("stu-nyt_news_desks.json")
        assert stu == fxt

    # 3.8 CHALLENGE 08
    # implement group articles by news desk function
    news_desk_articles = group_articles_by_news_desk(news_desks, articles)
    print(f"news desk articles: {news_desk_articles}")
    # write to json
    utl.write_json("stu-nyt_news_desk_articles.json", news_desk_articles)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-nyt_news_desk_articles.json")
        stu = utl.read_json("stu-nyt_news_desk_articles.json")
        assert stu == fxt

    # 3.9 CHALLENGE 09
    mean_word_counts = {}
    ignore = ("Business Day", "Movies")
    for desk in news_desk_articles:
        if desk not in ignore:
            mean_word_counts[desk] = calculate_articles_mean_word_count(news_desk_articles[desk])

    pp.pprint(f"mean word counts: {mean_word_counts.get('Obits')}")
    # 3.9.4 write to json
    utl.write_json("stu-nyt_news_desk_mean_word_counts.json", mean_word_counts)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-nyt_news_desk_mean_word_counts.json")
        stu = utl.read_json("stu-nyt_news_desk_mean_word_counts.json")
        assert stu == fxt
    # 3.10 CHALLENGE 10
    # 3.10.2 call get_nested_dict
    wookiee_planets = utl.read_csv_to_dicts("data-wookieepedia_planets.csv")
    wookiee_dagobah = utl.get_nested_dict(wookiee_planets, "name", "Dagobah")
    print(f"wookiee dagobah: {wookiee_dagobah}")
    # 3.10.4 write to json
    utl.write_json("stu-wookiee_dagobah.json", wookiee_dagobah)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-wookiee_dagobah.json")
        stu = utl.read_json("stu-wookiee_dagobah.json")
        assert stu == fxt
    # .3.10.6 wookiee_haruun_kal
    wookiee_haruun_kal = utl.get_nested_dict(wookiee_planets, "system", "Al'Har system")
    print(f"wookiee haruun kal: {wookiee_haruun_kal}")
    # 3.10.7 write to json
    utl.write_json("stu-wookiee_haruun_kal.json", wookiee_haruun_kal)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-wookiee_haruun_kal.json")
        stu = utl.read_json("stu-wookiee_haruun_kal.json")
        assert stu == fxt

    # 3.11 CHALLENGE 11
    assert utl.to_gravity_value("1 standard") == 1.0
    assert utl.to_gravity_value("5STANDARD") == 5.0
    assert utl.to_gravity_value("0.98") == 0.98
    assert utl.to_gravity_value("N/A") == "N/A"

    print(utl.to_year_era("1032BBY"))
    print(utl.to_year_era("19BBY"))
    print(utl.to_year_era("0ABY"))
    print(utl.to_year_era("Chewbacca"))
    assert utl.to_year_era("1032BBY") == {"year": 1032, "era": "BBY"}
    assert utl.to_year_era("19BBY") == {"year": 19, "era": "BBY"}
    assert utl.to_year_era("0ABY") == {"year": 0, "era": "ABY"}
    assert utl.to_year_era("Chewbacca") == "Chewbacca"

    # 3.12 CHALLENGE 12
    # create path to data-keys_mapping.json
    keys_path = Path("data-key_mappings.json").absolute()
    # print(keys_path)
    keys = utl.read_json(keys_path)
    # print(keys.get("planet"))
    swapi_tatooine = get_swapi_resource(SWAPI_PLANETS, {"search": "tatooine"})["results"][0]
    # print(swapi_tatooine.keys())
    # 3.12.4
    wookiee_tatooine = utl.get_nested_dict(wookiee_planets, "name", swapi_tatooine.get("name"))
    # print(wookiee_tatooine.keys())
    # print(f"wookiee tatooine: {wookiee_tatooine}")
    # merge swapi tattooine and wookie tattooine
    swapi_tatooine.update(wookiee_tatooine)
    # print(swapi_tatooine.keys())
    # use transform planet function
    tatooine = transform_planet(swapi_tatooine, keys, NONE_VALUES)
    # print(tatooine.keys())
    print(tatooine)
    # write to json
    utl.write_json("stu-tatooine.json", tatooine)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-tatooine.json")
        stu = utl.read_json("stu-tatooine.json")
        assert stu == fxt

    # 3.13 CHALLENGE 13
    # keys.get("droid")
    swapi_r2_d2 = get_swapi_resource(SWAPI_PEOPLE, {"search": "r2-d2"})["results"][0]
    wookiee_droids = utl.read_json("data-wookieepedia_droids.json")
    wookiee_r2_d2 = utl.get_nested_dict(wookiee_droids, "name", swapi_r2_d2.get("name"))
    swapi_r2_d2.update(wookiee_r2_d2)
    r2_d2 = transform_droid(swapi_r2_d2, keys, NONE_VALUES)
    print(r2_d2.keys())
    print(r2_d2)
    # write to json
    utl.write_json("stu-r2_d2.json", r2_d2)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-r2_d2.json")
        stu = utl.read_json("stu-r2_d2.json")
        assert stu == fxt

    # 3.14 CHALLENGE 14
    # get swapi dict
    swapi_human_species = get_swapi_resource(SWAPI_SPECIES, {"search": "human"})["results"][0]
    human_species = transform_species(swapi_human_species, keys, NONE_VALUES)
    # write to json
    utl.write_json("stu-human_species.json", human_species)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-human_species.json")
        stu = utl.read_json("stu-human_species.json")
        assert stu == fxt

    # 3.15 CHALLENGE 15
    # get swapi dict for anakin skywalker
    swapi_anakin = get_swapi_resource(SWAPI_PEOPLE, {"search": "anakin skywalker"})["results"][0]
    wookiee_people = utl.read_json("data-wookieepedia_people.json")
    wookiee_anakin = utl.get_nested_dict(wookiee_people, "name", swapi_anakin.get("name"))
    swapi_anakin.update(wookiee_anakin)
    # use transform person function
    anakin = transform_person(swapi_anakin, keys, NONE_VALUES, wookiee_planets)
    # write to json
    utl.write_json("stu-anakin_skywalker.json", anakin)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-anakin_skywalker.json")
        stu = utl.read_json("stu-anakin_skywalker.json")
        assert stu == fxt

    # create obi wan
    swapi_obi_wan = get_swapi_resource(SWAPI_PEOPLE, {"search": "obi-wan kenobi"})["results"][0]
    # swapi_obi_wan.get("homeworld")
    # swapi_obi_wan.get("species")
    wookiee_obi_wan = utl.get_nested_dict(wookiee_people, "name", swapi_obi_wan.get("name"))
    swapi_obi_wan.update(wookiee_obi_wan)
    # create person
    obi_wan = transform_person(swapi_obi_wan, keys, NONE_VALUES, wookiee_planets)
    # write to json
    utl.write_json("stu-obi_wan_kenobi.json", obi_wan)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-obi_wan_kenobi.json")
        stu = utl.read_json("stu-obi_wan_kenobi.json")
        assert stu == fxt

    # 3.16 CHALLENGE 16
    wookiee_starships = utl.read_csv_to_dicts("data-wookieepedia_starships.csv")
    wookiee_twilight = utl.get_nested_dict(wookiee_starships, "name", "Twilight")
    twilight = transform_starship(wookiee_twilight, keys, NONE_VALUES)
    # write to json
    utl.write_json("stu-twilight.json", twilight)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-twilight.json")
        stu = utl.read_json("stu-twilight.json")
        assert stu == fxt

    # 3.17 CHALLENGE 17
    # create padme
    params = {"search": "Padmé Amidala"}
    swapi_padme = get_swapi_resource(SWAPI_PEOPLE, params)["results"][0]
    wookiee_padme = utl.get_nested_dict(wookiee_people, "name", swapi_padme.get("name"))
    swapi_padme.update(wookiee_padme)
    padme = transform_person(swapi_padme, keys, NONE_VALUES, wookiee_planets)
    # write to json
    utl.write_json("stu-padme_amidala.json", padme)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-padme_amidala.json")
        stu = utl.read_json("stu-padme_amidala.json")
        assert stu == fxt

    # create c3po
    params = {"search": "C-3PO"}
    swapi_c_3po = get_swapi_resource(SWAPI_PEOPLE, params)["results"][0]
    wookiee_c_3po = utl.get_nested_dict(wookiee_droids, "name", swapi_c_3po.get("name"))
    swapi_c_3po.update(wookiee_c_3po)
    c_3po = transform_droid(swapi_c_3po, keys, NONE_VALUES)
    # write to json
    utl.write_json("stu-c_3po.json", c_3po)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-c_3po.json")
        stu = utl.read_json("stu-c_3po.json")
        assert stu == fxt

    # read jedi
    filepath = Path("data-jedi.json").absolute()
    jedi = utl.read_json(filepath)

    # unpack jedi list
    mace_windu, plo_koon, shaak_ti, yoda = jedi
    # create manifest
    passenger_manifest = [padme, c_3po, r2_d2, mace_windu, plo_koon, shaak_ti, yoda]

    assert board_passengers(1, passenger_manifest) == [padme]
    assert board_passengers(4, passenger_manifest) == [padme, c_3po, r2_d2, mace_windu]
    # pass passengers to twilight
    twilight["passengers_on_board"] = board_passengers(
        twilight.get("max_passengers"), [padme, c_3po, r2_d2]
    )

    # 3.18 CHALLENGE 18

    assert assign_crew_members(1, ("pilot",), (anakin, obi_wan, mace_windu)) == {"pilot": anakin}
    assert assign_crew_members(
        3, ("pilot", "copilot", "navigator"), (anakin, obi_wan, mace_windu)
    ) == {"pilot": anakin, "copilot": obi_wan, "navigator": mace_windu}
    # assign crew to twilight
    crew_positions = ("pilot", "copilot")
    personnel = (anakin, obi_wan)
    twilight["crew_members"] = assign_crew_members(twilight.get("crew_size"), crew_positions, personnel)
    # assign r2 instructions
    r2_d2["instructions"] = ["Power up the engines"]

    # 3.19 CHALLENGE 19
    planets = [transform_planet(wookiee_planets[i], keys, NONE_VALUES) for i in range(len(wookiee_planets))]
    # sort by name
    planets = sorted(planets, key=lambda x: x["name"], reverse=True)

    # write to json
    utl.write_json("stu-planets_sorted_name.json", planets)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-planets_sorted_name.json")
        stu = utl.read_json("stu-planets_sorted_name.json")
        assert stu == fxt

    # get naboo by diameter
    naboo = utl.get_nested_dict(planets, "diameter_km", 12120)
    # update instructions
    new_instructions = [f'Plot course for Naboo, {naboo.get("region")}, {naboo.get("sector")}']
    # update r2
    r2_d2["instructions"].extend(new_instructions)
    # sort planets by diameter_km and name
    planets_diameter_km = sorted(planets, key = lambda x: (-x["diameter_km"] if x["diameter_km"] else 0, x["name"]))
    # write to json
    utl.write_json("stu-planets_sorted_diameter.json", planets_diameter_km)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-planets_sorted_diameter.json")
        stu = utl.read_json("stu-planets_sorted_diameter.json")
        assert stu == fxt

    # 3.20 CHALLENGE 20
    # extend r2 instructions
    r2_d2["instructions"].append("Release the docking clamp")
    # write twilight to json
    utl.write_json("stu-twilight_departs.json", twilight)
    # compare to fxt
    if os.getenv("USER") == "francisco":
        fxt = utl.read_json("fxt-twilight_departs.json")
        stu = utl.read_json("stu-twilight_departs.json")
        assert stu == fxt


if __name__ == "__main__":
    main()
