""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    options = ["Accounting manager",
               "List",
               "Add",
               "Remove",
               "Update",
               "Which year max",
               "Average amount",
               "Exit to main menu"]

    ui.print_menu(options[0], options[1:7], options[-1])
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    
    if option == "1":
        show_table(table)
    elif option == "2":
        add("items.csv")
    elif option == "3":
        remove(table, id_)
    elif option == "4":
        update(table, id_)
    elif option == "5":
        which_year_max(table)
    elif option == "6":
        avg_amount(table, year)
    elif option =="0":
        pass


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    table = data_manager.get_table_from_file("accounting/items.csv")
    added_line = ui.get_inputs(["Month: ","Day: ", "Year: ", "Type: ", "Amount: "], "Please provide your data to add:")
    random_ID = common.generate_random("accounting/items.csv")
    added_line.insert(0, random_ID)
    added_line_helper = []
    added_line_helper.append(added_line)
    expanded_lines = table + added_line_helper
    data_manager.write_table_to_file("accounting/items.csv", expanded_lines)
    start_module()

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
