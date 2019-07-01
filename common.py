""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    special_characters = [33, 35, 36, 37, 38, 63, 64]
    while generated in table: #ezt lehet konkretizálni kell h ne nyűgösködjön vmi csöves spacere
        generated_in_list = []
        generated_in_list.append(str(chr(random.randrange(97, 123)))) #random lower letter from ascII decimal code
        generated_in_list.append(str(chr(random.randrange(65, 91))))  #random upper letter from ascII decimal code
        generated_in_list.append(str(chr(random.randrange(48, 58))))  #random number from ascII decimal code
        generated_in_list.append(str(chr(random.randrange(48, 58))))  #random number from ascII decimal code
        generated_in_list.append(str(chr(random.randrange(65, 91))))  #random upper letter from ascII decimal code
        generated_in_list.append(str(chr(random.randrange(97, 123)))) #random lower letter from ascII decimal code
        generated_in_list.append(str(chr(random.choice(special_characters)))) #random special character from ascII decimal code
        generated_in_list.append(str(chr(random.choice(special_characters)))) #random special character from ascII decimal code
        generated = str(''.join(generated_in_list)) #join the elements of generated in list to a string, same format as in csv files (sample:  "kH34Ju#&"  )
    return generated


def index_list_of_list(desired_element, table):
    for idx, list in enumerate(table):
        if desired_element in list:
            return idx
        return -1

def my_sum(array):
    summa = 0
    for item in array:
        summa += int(item)
    return summa