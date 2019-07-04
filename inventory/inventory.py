""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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

    options = ["Inventory manager",
               "List",
               "Add",
               "Remove",
               "Update",
               "Get available items",
               "Get average durability by manufacterers",
               "Exit to main menu"]

    ui.print_menu(options[0], options[1:7], options[-1])
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    if option == "1":
        show_table("inventory.csv")
    elif option == "2":
        add("inventory.csv")
    elif option == "3":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to delete:")
        remove("inventory.csv", choosen_ID)
    elif option == "4":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to update:")
        update("inventory.csv", choosen_ID)
    elif option == "5":
        get_available_items("inventory.csv")
    elif option == "6":
        get_average_durability_by_manufacturers("inventory.csv")
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

    table = data_manager.get_table_from_file("inventory/inventory.csv")
    ui.print_table(table, ["ID", "Name: ", "Manufacterer: ", "Purchase year: ", "Durability: "])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    table = data_manager.get_table_from_file("inventory/inventory.csv")
    added_line = ui.get_inputs(["Name: ", "Manufacterer: ", "Purchase year: ", "Durability: "], "Please provide your data to add:")
    random_ID = common.generate_random("inventory/inventory.csv")
    added_line.insert(0, random_ID)
    added_line_helper = []
    added_line_helper.append(added_line)
    expanded_lines = table + added_line_helper
    data_manager.write_table_to_file("inventory/inventory.csv", expanded_lines)
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

    table = data_manager.get_table_from_file("inventory/inventory.csv")
    index_to_remove = common.index_list_of_list(id_, table)
    table.remove(table[index_to_remove])
    data_manager.write_table_to_file("inventory/inventory.csv", table)
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

    table = data_manager.get_table_from_file("inventory/inventory.csv")
    id_ = id_[0]
    update_data = ui.get_inputs(["Name: ", "Manufacterer: ", "Purchase year: ", "Durability: "], "Please provide data you would like to update:")
    index_to_update = common.index_list_of_list(id_, table)
    update_data.insert(0, id_)
    table[index_to_update] = update_data
    data_manager.write_table_to_file("inventory/inventory.csv", table)
    start_module()

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    table = data_manager.get_table_from_file("inventory/inventory.csv")
    not_exceeded_items = []
    for row in table:
        if 2019 < int(row[-2]) + int(row[-1]):
            not_exceeded_items.append(row)
    #print(not_exceeded_items)
    return not_exceeded_items

def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    table = data_manager.get_table_from_file("inventory/inventory.csv")
    manufacturers = {}
    manufactorers_column = 2
    durability_column = -1
    for line in table:
        if line[2] not in manufacturers:
            manufacturers[line[manufactorers_column]] = line[durability_column]
        else:manufacturers[line[manufacturer]] += line[durability_column]
            #key legyen lista, első szám a sum durab, 2. h hány elemből jött


