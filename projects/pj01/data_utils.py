"""Imported functions for PJ01."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Function 0.0."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Function 0.1."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Function 0.2."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(input_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Function 1.0."""
    # head returns entire table when int param >= the length.
    dict1: dict[str, list[str]] = {}
    
    for key in input_table:
        i = 0
        ls1 = []
        maximum: int
        if n >= len(input_table[key]):
            return input_table
        else:
            maximum = n

        while i < maximum:
            ls1.append(input_table[key][i])
            i += 1
        dict1[key] = ls1
    return dict1


def select(input_table: dict[str, list[str]], row_names: list[str]) -> dict[str, list[str]]:
    """Create a new dict from input dict with a select number of columns."""
    dict1 = {}

    for key in input_table:
        if key in row_names:
            dict1[key] = input_table[key] 

    return dict1
        

def count1(input_list: list[str]) -> dict[str, int]:
    """Creates a dictionary of the counts of each item in the input list."""
    dict1: dict[str, int] = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0}
    for key in input_list:
        if key in dict1:
            dict1[key] += 1
        else:
            dict1[key] = 1

    return dict1
        

def lists(input_table: dict[str, list[str]], input1: str, input2: str, input3: str) -> list[str]:
    """Creates a list."""
    list1 = []
    i = 0
    while i < len(input_table[input1]):
        if input_table[input1][i] == input2:
            list1.append(input_table[input3][i])
        i += 1
    return list1