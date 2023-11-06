import csv
from pathlib import Path


def calculate_shot_conversion_rate(goals, shots, precision=2):
    """Calculates the shot conversion rate (goals divided by shots). The number
    of decimal places to retain when rounding the quotient is specified by the
    < precision > argument. If the < try > block raises an exception (i.e., a
    ZeroDivisionError) the function returns 0.0.

    Parameters:
        goals (int): number of goals scored
        shots (int): number of shots taken
        precision (int): number of decimal places to retain

    Returns:
        float: shot conversion rate
    """

    pass  # TODO Implement


def clean_squad(squad):
    """Converts a player's "Squad" value (e.g. "es Spain") to a two-item tuple
    comprising the following items:

    1  Upper case two-letter country abbreviation (e.g., "ES")
    2. squad name (e.g., "Spain")

    Parameters:
        squad (str): comprises a two-letter country abbreviation and squad name

    Returns:
        tuple: "Squad" element converted to a two-item tuple
    """

    pass  # TODO Implement


def format_player_position(position):
    """Reformats player's position string by converting the comma (",") delimiter that
    separates multiple positions to a pipe (|), e.g., "MF,DF" -> "MF|DF". This change
    eliminates the need to surround the position string with double quotes when writing the
    value to a CSV file.

    Parameters:
        position (str): player's position string

    Returns:
        str: reformatted position string
    """

    pass  # TODO Implement


def get_multi_position_players(players, pos_idx):
    """Returns players who play multiple positions. Evaluates the "Pos" element
    for the presence of multiple positions (e.g., "DF", "FW", "GK", "MF").

    Parameters:
        players (list): nested list of player data
        pos_idx (int): index value of the "Pos" element

    Returns:
        list: nested list of players who play multiple positions
    """

    pass  # TODO Implement


def get_player_shooting_numbers(player, slice_):
    """Returns a player's shots, shots on target, and goals scored. All values
    are converted from strings to integers before being returned to the caller.

    Parameters:
        player (list): a list containing player data
        slice_ (slice): slice() instance required to access the shooting-related
                        elements in the player list.

    Returns:
        list: player's shooting statistics (shots, shots on target, and goals)
    """

    pass  # TODO Implement


def get_team(players, squad_idx, squad):
    """Returns members of a country's team.

    Parameters:
        players (list): nested list of player data
        squad_idx (int): index value of the "Squad" element
        squad (str): country/squad name

    Returns:
        list: team members who represent the < squad >
    """

    pass  # TODO Implement


def get_team_names(players, squad_idx):
    """Returns a list of team/squad names that correspond to the countries participating
    in the World Cup. Duplicate names are filtered out of the list returned to the caller.

    Parameters:
        players (list): nested list of player data
        squad_idx (int): index value of the "Squad" element

    Returns:
        list: countries represented by the players in the < players > list
    """

    pass  # TODO Implement


def get_team_shooting_numbers(team, slice_):
    """Returns a team's shot production: shots, shots on target, and goals. All values
    are converted from strings to integers.

    Parameters:
        team (list): nested list containing team/country player data
        slice_ (slice): slice() instance required to access the shooting-related
                        elements in the player list.

    Returns:
        tuple: team's shot production (shots, shots on target, and goals)
    """

    pass  # TODO Implement


def get_top_scorer(players, gls_idx):
    """Returns the top scorer from the < players > list. Filters out players
    that did not score a goal and excludes them from consideration. Ties between
    top scorers are accommodated.

    Parameters:
        players (list): nested list of player data
        gls_idx (int): index value of a nested list's "Gls" element

    Returns:
        list: nested list of one or more top scorers
    """

    pass  # TODO Implement


def read_csv(filepath, encoding="utf-8", newline="", delimiter=","):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list of lists,
    wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line of decoded
    text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted fields
    may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested "row" lists
    """

    with open(filepath, "r", encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)
        return data


def write_csv(filepath, data, headers=None, encoding="utf-8", newline=""):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list | tuple): sequence to be written to the target file
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, "w", encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point. Orchestrates workflow.

    Parameters:
        None

    Returns:
        None
    """

    # CHALLENGE 01

    # 1.1

    # 1.2

    # 1.3

    # 1.4
    # print(f"\n1.4 data[0] = {data[0]}")  # headers
    # print(f"\n1.4 data[-1] = {data[-1]}")  # last player
    # assert data[0] == ["Rk", "Player", "Pos", "Squad", "Age", "Born", "90s", "Gls", "Sh", "SoT"]
    # assert data[-1] == [
    #     "619",
    #     "Claudia Zornoza",
    #     "MF",
    #     "es Spain",
    #     "32",
    #     "1990",
    #     "0.4",
    #     "0",
    #     "0",
    #     "0",
    # ]

    # 1.5

    # CHALLENGE 02

    # 2.1
    # assert "MF|DF" == format_player_position("MF,DF")
    # assert "GK" == format_player_position("GK")

    # 2.2
    # assert ("NG", "Nigeria") == clean_squad("ng Nigeria")
    # assert ("ZA", "South Africa") == clean_squad("za South Africa")

    # CHALLENGE 03

    # 3.1

    # 3.2

    # 3.3

    # 3.4

    # CHALLENGE 04

    # 4.2

    # 4.3

    # CHALLENGE 05

    # 5.2

    # 5.3

    # 5.5

    # 5.6

    # CHALLENGE 06

    # 6.2

    # 6.3

    # 6.4
    # print(f"\n6.4 countries = {countries}")
    # assert len(countries) == 32

    # CHALLENGE 07

    # 7.2

    # 7.3

    # 7.4
    # print(f"\n7.4 top scorer(s) (n={len(top_scorers)}) = {top_scorers}")

    # CHALLENGE 08

    # 8.1-5

    # 8.6

    # CHALLENGE 09

    # 9.2 UNCOMMENT: built-in slice(< start >, < start >, < step >=None) object in action!
    # slice_ = slice(gls_idx, len(headers))  #  equivalent to slice(8, 11)

    # 9.3

    # 9.4
    # print(
    #     f"\n9.4 goals = {goals}",
    #     f"shots = {shots}",
    #     f"shots_on_target = {shots_on_target}",
    #     sep="\n",
    # )
    # assert goals == 1
    # assert shots == 10
    # assert shots_on_target == 4

    # CHALLENGE 10

    # 10.2-4

    # 10.5

    # 10.6

    # CHALLENGE 11

    # 11.2

    # 11.3-7

    # 11.8

    # CHALLENGE 12

    # 12.1-2

    # 12.3

    # 12.4 UNCOMMENT: sort by shots on target conversion rate (descending), squad name (ascending)
    # teams = sorted(teams, key=lambda x: (-float(x[-2]), x[0]))

    # 12.5


if __name__ == "__main__":
    main()
