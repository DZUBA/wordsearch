"""This module is wordsearch application"""

import string
import sys
from random import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("VERT_NUM", help="paste number of vertical cells as int")
parser.add_argument("HORZ_NUM", help="paste number of horizontal cells as int")
parser.parse_args()


def table_generation():
    """returns table
    Create a table of random letters based on number of vertical and horizontal
    numbers from command line.

    Returns: Generated table of random letter
    """
    try:
        vertical_num = int(sys.argv[1])  # Check for int in vertical
        horizontal_num = int(sys.argv[2])  # Check for int in horizontal
    except ValueError:
        print 'Please enter an integer'  # Exit if args not int
    letters = string.ascii_lowercase  # Add letters
    table = []
    for i in range(vertical_num):
        """Generate table of random letters"""
        table_horizontal = "".join(choice(letters) for _ in range(horizontal_num))
        table.append(table_horizontal)
    return table


def puzzle():
    """Searching words from words.txt in table

    Returns: Print each finded word
    """
    table = table_generation()  # Call table from func table_generation
    with open("words.txt", "r") as text:
        """Open file with words and search them in generated table"""
        for line in text:
            for word in line.split():
                for i in table:
                    if word in i:  # Search word
                        print word
                    if word[::-1] in i:  # Search for backward words
                        print word

puzzle()
