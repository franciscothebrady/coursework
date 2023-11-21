import json
from pathlib import Path
from datetime import datetime
import pprint

pp = pprint.PrettyPrinter(indent=2, sort_dicts=False, width=100)


def convert_published_date_value(data):
    """Converts the value in each article pub_date key.

    Assume the pub_date value is a string. Convert this value to a datetime object using the
    datetime.strptime() or the datetime.fromisoformat() function with the datetime string formatted as

    '< Year >-< Month >-< Day >T< Hour >:< Minute >:< Second >< %z UTC offset >".

    Hint: This function employs a nested for loop to interact with an article's key-value pairs.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.

    Returns:
        data (list): Updated list of dictionaries, with the value for pub_date key
              converted properly.
    """
    for article in data:
        for key, value in article.items():
            if key == "pub_date":
                article[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
    return data


def create_headline_url_list(data):
    """Creates a list of article headlines and urls.

    Hint: the comprehension expression is a list comprehension that iterates through the data
    and creates a new list of tuples containing the desired elements.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.

    Returns:
        list: A list of tuples, each containing the article's headline and url.
    """
    return [(article["headline"]["main"], article["web_url"]) for article in data]


def filter_articles(data, keys_to_exclude):
    """Filters each dictionary down to necessary information within the given < data >
    list based on the < keys_to_exclude > list.

    Hint: the comprehension expression is comprised of a dictionary comprehension
    nested within a list comprehension.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.
        keys_to_exclude (list): A list of key names to exclude from each article
                                dictionary.

    Returns:
        list: A list of dictionaries, each containing filtered information
              about a Technology themed New York Times article.
    """
    return [{k: v for k, v in article.items() if k not in keys_to_exclude} for article in data]


def format_author_name(person):
    """Reformats an author's name given an article's byline person dictionary. Employs
    a formatted string literal to return a string containing the author's last name and
    first name with the first letter of both names capitalized per the format specified
    below.

    Format: "< Last name >, < First name >"

    Parameters:
        person (dict): A dictionary containing information
                        about an article's byline person list.

    Returns:
        str: A string containing the author's name seperated by a single space.
    """
    return f"{person['lastname'].title()}, {person['firstname'].title()}"


def get_author_names(article):
    """Returns a list of article authors by employing a list comprehension. Delegates to
    the helper function < format_author_name() > the task of formatting each name added to the
    new list.

    Parameters:
        article (dict): A dictionary containing information about a technology-themed
        New York Times article.

    Returns:
        list: A list containing each author's first and last name, seperated by a single space.
    """
    return [format_author_name(person) for person in article["byline"]["person"]]


def get_organization_names(article):
    """Gets list of organizations mentioned in the 'keywords' section of the technology-themed New
    York Times article.

    Hint: the comprehension expression is a list comprehension looping over the article's keywords
    key. The loop variable must be named < keyword >.

    Parameters:
        article (dict): A dictionary containing information
                        about a technology-themed New York Times article.

    Returns:
        list: A list containing all the organization names present in the article (including repeated).
    """
    return [
        keyword["value"] for keyword in article["keywords"] if keyword["name"] == "organizations"
    ]


def get_news_by_location(data, location):
    """Filter articles based on the given location.

    Hint: the comprehension expression is a list comprehension which loops over the data and
    checks if the location is matching. Note that your loop variable for the outer loop must be
    < article >, and your loop variable for the inner loop must be < keyword >.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a technology-themed New York Times article.
        location (str): String representing the location of the article.

    Returns:
        list: A list containing the articles of the same, desired location.
    """
    return [
        article
        for article in data
        for keyword in article["keywords"]
        if keyword["name"] == "glocations" and location in keyword["value"]
    ]


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


def remove_empty_keywords_articles(data):
    """Removes articles which have empty lists as values for the 'keywords' key.

    Hint: the comprehension expression is a list comprehension looping over the data.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a Technology themed New York Times article.

    Returns:
        list: A list of dictionaries representing articles having keywords in them.
    """
    return [article for article in data if article["keywords"]]


def show_archival_status(data, active_year_threshold):
    """Classifies the article as active or archived depending on specified threshold.

    Hint: the comprehension expression implements an if-else in a list comprehension iterating
    through the data.

    Parameters:
        data (list): A list of dictionaries, each containing information
                     about a Technology themed New York Times article
                     with pub_date converted to datetime object.
        active_year_threshold (int): An integer representing the earliest year an article can be
                                     published in to be considered active.

    Returns:
        list: A list of tuples containing the article headline and its status.
    """
    return [
        (article["headline"]["main"], "Active")
        if article["pub_date"].year >= active_year_threshold
        else (article["headline"]["main"], "Archived")
        for article in data
    ]


def write_json(
    filepath,
    data,
    encoding="utf-8",
    ensure_ascii=False,
    indent=4,
    sort_keys=True,
    default=str,
):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding) as file_obj:
        json.dump(
            data,
            file_obj,
            ensure_ascii=ensure_ascii,
            indent=indent,
            sort_keys=sort_keys,
            default=default,
        )


# Entry
def main():
    """Entry point for the program. Orchestrates the workflow.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0
    print("Problem 1:\n")

    # 1.1
    filepath = Path("data-nyt-articles-tech.json").resolve()

    # 1.2
    print(f"Filepath: {filepath}")
    nyt_tech_raw = read_json(filepath)

    pp.pprint(f"First 2 Records of nyt_tech_raw: {nyt_tech_raw[:2]}\n")

    # 1.4
    headline_url_list = create_headline_url_list(nyt_tech_raw)
    pp.pprint(f"Headline and URL List: {headline_url_list[0:10]}\n")

    # 1.5
    filename = "stu-headline-url-list.json"
    pp.pprint(f"Filename: {filename}")
    # 1.6
    write_json(filename, headline_url_list)
    # compare to fxt
    # fxt_headline_url_list = read_json(
    #     filepath=Path("fxt-headline-url-list.json").resolve()
    # )
    # stu_headline_url_list = read_json(
    #     filepath=Path("stu-headline-url-list.json").resolve()
    # )

    # assert stu_headline_url_list[0] == fxt_headline_url_list[0]

    # 2.0
    print("Problem 2:\n")

    keys_to_exclude = [
        "abstract",
        "web_url",
        "snippet",
        "lead_paragraph",
        "source",
        "document_type",
        "news_desk",
        "type_of_material",
    ]

    # 2.2
    nyt_tech_filtered = filter_articles(nyt_tech_raw, keys_to_exclude)

    pp.pprint(f"First Record of filtered_articles:\n")
    pp.pprint(nyt_tech_filtered[0])

    # 2.3
    ## write_json and compare to fxt file
    filename = "stu-nyt-tech-filtered.json"
    write_json(filename, nyt_tech_filtered)
    # 2.4
    # compare to fxt
    # fxt_filtered = read_json(filepath=Path("fxt-nyt-tech-filtered.json").resolve())
    # stu_filtered = read_json(filepath=Path("stu-nyt-tech-filtered.json").resolve())
    # assert stu_filtered[0] == fxt_filtered[0]

    # 3.0
    print("Problem 3:\n")
    # 3.2
    nyt_tech_cleaned = remove_empty_keywords_articles(nyt_tech_filtered)

    # 3.4
    nyt_tech = convert_published_date_value(nyt_tech_cleaned)
    # 3.5
    filename = "stu-nyt-tech-cleaned.json"
    # 3.6
    write_json(filename, nyt_tech)
    # compare to fxt
    # fxt_cleaned = read_json(filepath=Path("fxt-nyt-tech-cleaned.json").resolve())
    # stu_cleaned = read_json(filepath=Path("stu-nyt-tech-cleaned.json").resolve())
    # pp.pprint(f"First Record of cleaned_articles:\n")
    # pp.pprint(stu_cleaned[0])
    # pp.pprint("pub_date of first article:\n")
    # pp.pprint(stu_cleaned[0]["pub_date"])
    # assert stu_cleaned[0] == fxt_cleaned[0]
    # 4.0
    print("Problem 4:\n")

    tech_organizations = []
    for article in nyt_tech:
        # get org names
        org_names = get_organization_names(article)
        # check if org names is truthy
        if org_names:
            # if yes, check if not in tech_organizations and add to tech_organizations
            for org_name in org_names:
                if org_name not in tech_organizations:
                    tech_organizations.append(org_name)

    pp.pprint(f"Tech Organizations:\n")
    pp.pprint(tech_organizations)
    filename = "stu-unique-tech-organizations.json"
    # write to json
    write_json(filename, tech_organizations)
    # compare to fxt
    # fxt_unique_tech_orgs = read_json(
    #     filepath=Path("fxt-unique-tech-organizations.json").resolve()
    # )
    # stu_unique_tech_orgs = read_json(
    #     filepath=Path("stu-unique-tech-organizations.json").resolve()
    # )
    # assert stu_unique_tech_orgs == fxt_unique_tech_orgs

    print("Problem 5:\n")

    # 5.2
    calif_news = get_news_by_location(nyt_tech, "Calif")
    pp.pprint(f"California News:\n")
    pp.pprint(calif_news[0])
    # 5.3
    filename = "stu-nyt-calif-tech-articles.json"
    # 5.4
    # write to json
    write_json(filename, calif_news)
    # compare to fxt
    # fxt_calif_news = read_json(
    #     filepath=Path("fxt-nyt-calif-tech-articles.json").resolve()
    # )
    # stu_calif_news = read_json(
    #     filepath=Path("stu-nyt-calif-tech-articles.json").resolve()
    # )
    # assert stu_calif_news == fxt_calif_news

    # 6.0
    print("Problem 6:\n")

    # 6.2
    article_status = show_archival_status(nyt_tech, 2022)
    pp.pprint(f"Article Status:\n")
    pp.pprint(article_status)
    # 6.3
    filename = "stu-article-status.json"
    # 6.4
    # write to json
    write_json(filename, article_status)
    # compare to fxt
    # fxt_article_status = read_json(filepath=Path("fxt-article-status.json").resolve())
    # stu_article_status = read_json(filepath=Path("stu-article-status.json").resolve())
    # assert stu_article_status == fxt_article_status

    # 7.0
    print("Problem 7:\n")

    # 7.3
    unique_authors = []
    # 7.3.1-7.3.6
    for article in nyt_tech:
        authors = get_author_names(article)
        if authors:
            for author in authors:
                if author is not None and author not in unique_authors:
                    unique_authors.append(author)

    pp.pprint(f"Unique Authors:\n")
    pp.pprint(unique_authors)
    # 7.4
    filename = "stu-unique-authors.json"
    # 7.5
    # write to json
    write_json(filename, unique_authors)
    # compare to fxt
    # fxt_unique_authors = read_json(filepath=Path("fxt-unique-authors.json").resolve())
    # stu_unique_authors = read_json(filepath=Path("stu-unique-authors.json").resolve())
    # assert stu_unique_authors == fxt_unique_authors


if __name__ == "__main__":
    main()
