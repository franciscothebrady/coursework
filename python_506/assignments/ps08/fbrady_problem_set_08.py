# SETUP FOR PROBLEM SET 08

rank_1_avg_test = 25.38
rank_10_avg_test = 22.85

first_grand_central_book_title_test = "THE 6:20 MAN"
first_grand_central_book_score_test = 10

penultimate_grand_central_book_title_test = "LONG SHADOWS"
penultimate_grand_central_book_score_test = 15

grand_central_score_test = 125

# fmt: off
fiction_publishers_test = ['Ballantine', 'Mulholland', "St. Martin's", 'Bantam', 'Flatiron', 'Grand Central', 'Little, Brown', 'Doubleday', 'Harper Voyager', 'Viking', 'Morrow', 'Delacorte', 'Knopf', 'Scribner', 'Putnam', 'Berkley', 'Simon & Schuster', 'Minotaur', 'Zando', 'Atria/Emily Bestler', 'Tordotcom', 'Random House', 'Pamela Dorman', 'Del Rey', 'Atria', 'Penguin Press', "St. Martin's Griffin", 'Harper']
# fmt: on

fiction_publishers_scoreboard_test = {
    "Ballantine": 100,
    "Mulholland": 25,
    "St. Martin's": 45,
    "Bantam": 65,
    "Flatiron": 15,
    "Grand Central": 125,
    "Little, Brown": 85,
    "Doubleday": 70,
    "Harper Voyager": 10,
    "Viking": 35,
    "Morrow": 10,
    "Delacorte": 15,
    "Knopf": 45,
    "Scribner": 130,
    "Putnam": 50,
    "Berkley": 10,
    "Simon & Schuster": 15,
    "Minotaur": 25,
    "Zando": 40,
    "Atria/Emily Bestler": 40,
    "Tordotcom": 15,
    "Random House": 105,
    "Pamela Dorman": 15,
    "Del Rey": 15,
    "Atria": 35,
    "Penguin Press": 35,
    "St. Martin's Griffin": 10,
    "Harper": 15,
}

# PROBLEM SET 08

# Do not modify or remove this import statement
import json
from pathlib import Path
import pprint as pprint

pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)


def clean_book(book, desired_keys=None):
    """Accepts a dictionary representation of a book. Creates an empty dictionary.
    Loops through the keys and values of < book >.

    If < desired_keys > is not None, check if each key is in < desired_keys >.
    If it is, add that key and its value to the new dictionary. At the same time,
    call < convert_to_float > to make that value a float, if possible.

    If < desired_keys > is None, add each key and its value to the new dictionary
    while calling < convert_to_float > to make that value a float, if possible.

    Parameters:
        book (dict): dictionary representation of a book on the NYT bestsellers list
        desired_keys (list): represents which keys should still be in the cleaned book dictionary

    Returns:
        dict: a new, cleaned dictionary representation of the book with only the desired
                keys and "price" now a float
    """
    dict = {}
    for key, value in book.items():
        if desired_keys is not None:
            # only loop throuhg desired keys
            if key in desired_keys:
                dict[key] = convert_to_float(value)
        else:
            # all keys
            dict[key] = convert_to_float(value)
    return dict


def convert_to_float(value):
    """Implements error handling to check if the passed-in value is a NON-INTEGER
    that can be converted to a float.
    If possible, the non-integer value is converted and assigned back to its
    variable.

    Parameters:
        value (any): a value that may be able to be converted to a float. In this
                        case, these are the values from a single book dictionary.
    Returns:
        value (float|any): value will be float, if possible. Otherwise it will returned unchanged.
    """
    try:
        if isinstance(value, int) == False:
            return float(value)
        else:
            return value
    except:
        return value


def create_scoreboard(bestseller_lists):
    """Creates a new, empty dictionary. Given eight weeks of bestseller lists,
    this function calls < find_publishers > to find all unique publisher names
    from the lists. Then, using < score_publisher > assigns a "publisher name",
    "score" key-value pair to the new dictionary for each publisher. Returns the
    dictionary with publisher names and scores.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.

    Returns:
        dict: a "scoreboard" of each publisher that appears on the bestseller
                lists and their total scores based on the rankings of their
                books. The keys are strings of publisher's names and the
                values are integer scores.
    """
    scoreboard = {}
    publishers = find_publishers(bestseller_lists)
    for publisher in publishers:
        # create key-value pair for each publisher
        scoreboard[publisher] = score_publisher(bestseller_lists, publisher)
    return scoreboard


def find_publishers(bestseller_lists):
    """Creates a list of the unique publisher names (no repeats) that appear
    throughout the weekly bestseller lists.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.

    Returns:
        list: list of strings; the names of all the publishers that have at least
            one book on a bestseller list for these 8 weeks.
    """
    publishers = []
    for list in bestseller_lists:
        for book in list["books"]:
            if book["publisher"] not in publishers:
                publishers.append(book["publisher"])
            continue
    return publishers


def get_average_price_by_rank(bestseller_lists, rank):
    """Given a list of bestseller lists and a rank, finds the average price of
    the books of that rank over the 8 weeks of lists. Includes duplicates of
    the same book if that book ranked in the same position multiple times over
    the eight weeks.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.
        rank (int): an integer 1-10 representing the rank of the books of interest
                    such as No. 1 bestsellers (1) or No. 5 bestsellers (5).

    Returns:
        float: the average price (rounded to nearest cent) for all books (including
                repeats) of the given rank over the eight weeks of lists
    """
    total_price = 0
    for list in bestseller_lists:
        for book in list["books"]:
            if book["rank"] == rank:
                total_price += book["price"]
    return round(total_price / 8, 2)


def get_books_by_publisher(bestseller_lists, publisher):
    """Given a publisher and eight weeks of bestseller lists, finds all of the
    books published by the publisher on those eight lists and returns the books
    as a list of dictionaries. Includes repeats if a book remained on the list for
    multiple weeks.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.
        publisher (str): the name of a book publisher that has a book on at least one
                        of the eight weekly bestseller lists.

    Returns:
        list : list of dictionaries, each representing a book published by the given
                publisher, includes repeats if a book remained on the list for
                multiple weeks
    """
    publisher_books = []
    for list in bestseller_lists:
        for book in list["books"]:
            if book["publisher"].lower() == publisher.lower():
                publisher_books.append(book)
    return publisher_books


def score_book(book):
    """Checks the rank of a book. If the book is rank 1-5, assigns a score
    of 15. If the book rank is 6-10, assigns a score of 10. Rank 11-15, score of 5.

    Parameter:
        book (dict): dictionary representation of a book on the NYT bestsellers list

    Returns:
        int: a score of 15, 10, or 5, depending on the rank of the book.
    """
    for key, value in book.items():
        if key == "rank":
            if value <= 5:
                return 15
            elif value > 5 and value <= 10:
                return 10
            elif value > 10 and value <= 15:
                return 5


def score_publisher(bestseller_lists, publisher):
    """Scores a publisher based on the rank of its books on the 8 weekly
    bestseller lists. Calls < get_books_by_publisher > to find the publisher's
    books, uses < score_book > to find the score for each book and adds that
    to the publisher score. This includes repeat books so that a publisher
    gets credit for a book remaining on the bestseller list for multiple
    weeks.

    Parameters:
        bestseller_lists (list): list of dictionaries, each dictionary represents
                                a weekly bestseller list and contains the key "books"
                                with a value that is a list of book dictionaries.
        publisher (str): the name of a book publisher that has a book on at least one
                        of the eight weekly bestseller lists.

    Returns:
        int: the total scores of all the publisher's books (including repeats) over
        the 8 weeks of bestseller lists
    """
    publisher_books = get_books_by_publisher(bestseller_lists, publisher)
    publisher_score = 0
    for book in publisher_books:
        publisher_score += score_book(book)
    return publisher_score


def read_json(filepath, encoding="utf-8"):
    """Reads a JSON file and converts it to a Python dictionary.

    Parameters:
        filepath (str): a path to the JSON file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, "r", encoding=encoding) as file_obj:
        data = json.load(file_obj)
    return data


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
    """Program entry point.

    Parameters:
        None

    Returns:
        None
    """

    # PROBLEM 1
    filepath_young_adult = Path("data-young_adult_bestsellers.json").resolve()

    # TODO 1.2 & 1.3
    young_adult_bestsellers = read_json(filepath_young_adult)

    young_adult_bestsellers_week_1 = young_adult_bestsellers[0]

    print(f"\nYoung Adult Bestsellers Week 1: {young_adult_bestsellers_week_1}")

    # TODO 1.5 & 1.6
    filepath_fiction = Path("data-fiction_bestsellers.json").resolve()
    fiction_bestsellers = read_json(filepath_fiction)
    fiction_bestsellers_week_8 = fiction_bestsellers[-1]
    # pp.pprint(fiction_bestsellers_week_8)
    print(f"\nFiction Bestsellers Week 8: {fiction_bestsellers_week_8}")

    # PROBLEM 2

    assert convert_to_float("5") == 5
    assert convert_to_float("NYT Books of the Year") == "NYT Books of the Year"
    assert convert_to_float("24.57") == 24.57

    # PROBLEM 3

    keep_keys = [
        "rank",
        "rank_last_week",
        "isbns",
        "publisher",
        "description",
        "price",
        "title",
        "author",
    ]
    # TODO 3.3
    # use clean_book on each list of bestsellers
    for dict in young_adult_bestsellers:
        week_list = dict["books"]
        for i in range(len(week_list)):
            week_list[i] = clean_book(week_list[i], keep_keys)

    print(f"\nCleaned Young Adult Bestsellers Week 1: {young_adult_bestsellers_week_1}")

    filepath = "stu-clean_young_adult_bestsellers.json"
    write_json(filepath, young_adult_bestsellers)

    # PROBLEM 4

    # TODO 4.3
    rank_1_avg = get_average_price_by_rank(young_adult_bestsellers, 1)

    print(f"\nAverage Price of No. 1 Young Adult Books: ${rank_1_avg}")
    assert rank_1_avg == rank_1_avg_test

    # TODO 4.4
    rank_10_avg = get_average_price_by_rank(
        rank=10, bestseller_lists=young_adult_bestsellers
    )

    print(f"\nAverage Price of No. 10 Young Adult Books: ${rank_10_avg}")
    assert rank_10_avg == rank_10_avg_test

    # PROBLEM 5

    # TODO 5.3
    grand_central_books = get_books_by_publisher(fiction_bestsellers, "Grand Central")

    # TODO Uncomment and replace question marks with correct expressions
    # TODO 5.4

    for book in grand_central_books:
        print(f"\nTitle: {book['title']}")
        print(f"Rank: {book.get('rank')}")

    # PROBLEM 6

    # TODO Uncomment and replace "?first book title?" and "?penultimate book title?" with the correct expressions
    first_book_score = score_book(grand_central_books[0])
    # fmt: off
    print(f"\nFirst Grand Central Book: {grand_central_books[0].get('title')}; Score: {first_book_score}")
    # fmt: on
    assert grand_central_books[0]["title"] == first_grand_central_book_title_test
    assert first_book_score == first_grand_central_book_score_test

    penultimate_book_score = score_book(grand_central_books[-2])
    # fmt: off
    print(f"\nPenultimate Grand Central Book: {grand_central_books[-2].get('title')}; Score: {penultimate_book_score}")
    # fmt: on
    assert grand_central_books[-2]["title"] == penultimate_grand_central_book_title_test
    assert penultimate_book_score == penultimate_grand_central_book_score_test

    # PROBLEM 7

    # TODO 7.3

    # fmt: off
    grand_central_score = score_publisher(fiction_bestsellers, "Grand Central")
    # fmt: on

    print(f"\nGrand Central Publisher Score: {grand_central_score }")
    assert grand_central_score == grand_central_score_test

    # PROBLEM 8

    # TODO 8.3
    fiction_publishers = find_publishers(fiction_bestsellers)
    print(f"\nFiction Publishers: {fiction_publishers}")
    assert fiction_publishers == fiction_publishers_test

    # PROBLEM 9

    # TODO 9.3
    fiction_publishers_scoreboard = create_scoreboard(fiction_bestsellers)
    print(f"\nScoreboard of Fiction Publishers: {fiction_publishers_scoreboard}")
    assert fiction_publishers_scoreboard == fiction_publishers_scoreboard_test


# Do not modify or remove this if statement
if __name__ == "__main__":
    main()
