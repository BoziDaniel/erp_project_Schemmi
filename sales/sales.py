""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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

    options = ["Sales manager",
               "List",
               "Add",
               "Remove",
               "Update",
               "Get lowest price item ID",
               "Get item sold between",
               "Exit to main menu"]

    ui.print_menu(options[0], options[1:7], options[-1])
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    
    if option == "1":
        show_table(table)
    elif option == "2":
        add("sales.csv")
    elif option == "3":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to delete:")
        remove("sales.csv", choosen_ID)
    elif option == "4":
        update(table, id_)
    elif option == "5":
        get_lowest_price_item_id(table)
    elif option == "6":
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
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

    table = data_manager.get_table_from_file("sales/sales.csv")
    added_line = ui.get_inputs(["Title: ","Price: ", "Month: ", "Day: ", "Year: "], "Please provide your data to add:")
    random_ID = common.generate_random("sales/sales.csv")
    added_line.insert(0, random_ID)
    added_line_helper = []
    added_line_helper.append(added_line)
    expanded_lines = table + added_line_helper
    data_manager.write_table_to_file("sales/sales.csv", expanded_lines)
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

    table = data_manager.get_table_from_file("sales/sales.csv")
    index_to_remove = common.index_list_of_list(id_, table)
    table.remove(table[index_to_remove])
    data_manager.write_table_to_file("sales/sales.csv", table)
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

    # your code

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
