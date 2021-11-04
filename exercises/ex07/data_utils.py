"""Utility functions."""

__author__ = "730318786"


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
    # establish empty dictionary
    dict1: dict = {}
    
    # create a dictionary with the column names [str] attached to the first 5 rows of column values 
    
    # loop through every column. copy column name into dict1.
    for key in input_table:
        dict1[key] = []
        # for every copied column. copy the first 5 vals. 
        
        for key in range(n):
            dict1[key].append(input_table)
    
    print(dict1)

    return dict1