# SI 506 Week 10 Bonus Challenge

import json

from pathlib import Path


def read_json(filepath, encoding="utf-8"):
    """Reads a JSON document, decodes the file content, and returns a list or dictionary if
    provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, "r", encoding=encoding) as file_obj:
        return json.load(file_obj)


def write_json(filepath, data, encoding="utf-8", ensure_ascii=False, indent=2):
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
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point. Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 04

    # 1.0 create Path instance
    filepath = Path("data-nyt-articles-research.json").absolute()

    # 2.0 Get data
    articles = read_json(filepath)

    # 3.0 Implement nested loop, populate keyword_values dictionary
    # outer loop: loop over articles 
    # inner loop: loop over keywords in each article
    keyword_values = {}
    for article in articles:
        for keyword in article["keywords"]:
            # if name value is not a key in keyword_values
            # add it as the key and set the value to an empty list
            if keyword["name"] not in keyword_values:
                keyword_values[keyword["name"]] = []
            continue

    # 4.0 Write to file
    write_json("stu-nyt-keyword_values-v1.json", keyword_values)

    # CHALLENGE 05

    # 1.0-2.2 Paste nested loop below then modify.
    for article in articles:
        for keyword in article["keywords"]:
            # assign key and val to variables 
            keyword_name = keyword["name"]
            keyword_value = keyword["value"]
            if keyword_name not in keyword_values:
                keyword_values[keyword_name] = [keyword_value]
            elif keyword_value not in keyword_values[keyword_name]:
                keyword_values[keyword_name].append(keyword_value)   
            continue



    # 2.0 Implement nested loop, populate keyword_values

    # 3.0 sort dictionary keys and values
    keyword_values_sorted = {
        k: v for k, v in sorted(keyword_values.items(), key=lambda x: (x[0], x[1].sort()))
    }

    # 4.0 Write to file
    write_json("stu-nyt-keyword_values-v2.json", keyword_values_sorted)

   # CHALLENGE 06

    # 1.0-3.3 Paste nested loop below then modify.
    keyword_counts = {}

    for article in articles:
        for keyword in article["keywords"]:
            # assign key and val to variables 
            name = keyword["name"]
            value = keyword["value"]
            # if name is not in keyword_counts, create new key-value pair in keyword_counts 
            if name not in keyword_counts:
                keyword_counts[name] = {value: 1}
            # if name doesn't match existing keyword_counts key, create new key-value pair in keyword_counts
            elif name not in keyword_counts[name]:
                keyword_counts[name][value] = 1
            # final else, increment keyword_counts[name][value] by 1
            else:
                keyword_counts[name][value] += 1
            continue
        


    # 4.0 Sort dictionary items
    keyword_counts_sorted = {k: dict(sorted(v.items())) for k, v in sorted(keyword_counts.items())}

    # 5.0 Write to file
    write_json("stu-nyt-keyword_value_counts.json", keyword_counts_sorted)


if __name__ == "__main__":
    main()
