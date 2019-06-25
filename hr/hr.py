""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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

    options = ["Human resources manager",
               "List",
               "Add",
               "Remove",
               "Update",
               "Get oldest person",
               "Get persons closer to average",
               "Exit to main menu"]

    ui.print_menu(options[0], options[1:7], options[-1])
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    if option == "1":
        show_table(table)
    elif option == "2":
        add("persons.csv")
    elif option == "3":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to delete:")
        remove("persons.csv", choosen_ID)
    elif option == "4":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to update:")
        update("persons.csv", choosen_ID)
    elif option == "5":
        get_oldest_person(table)
    elif option == "6":
        get_persons_closest_to_average(table)
    elif option == "0":
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

    table = data_manager.get_table_from_file("hr/persons.csv")
    added_line = ui.get_inputs(["Name: ", "Birth year: "], "Please provide your data to add:")
    random_ID = common.generate_random("hr/persons.csv")
    added_line.insert(0, random_ID)
    added_line_helper = []
    added_line_helper.append(added_line)
    expanded_lines = table + added_line_helper
    data_manager.write_table_to_file("hr/persons.csv", expanded_lines)
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

    table = data_manager.get_table_from_file("hr/persons.csv")
    index_to_remove = common.index_list_of_list(id_, table)
    table.remove(table[index_to_remove])
    data_manager.write_table_to_file("hr/persons.csv", table)
    start_module()

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

    table = data_manager.get_table_from_file("hr/persons.csv")
    id_ = id_[0]
    update_data = ui.get_inputs(["Name: ", "Birth year: "], "Please provide data you would like to update:")
    index_to_update = common.index_list_of_list(id_, table)
    update_data.insert(0, id_)
    table[index_to_update] = update_data
    data_manager.write_table_to_file("hr/persons.csv", table)
    start_module()

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
