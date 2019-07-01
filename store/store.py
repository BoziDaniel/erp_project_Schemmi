""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
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
    options = ["Store manager",
               "List",
               "Add",
               "Remove",
               "Update",
               "Get counts by manufacturers",
               "Average by manufacterer",
               "Exit to main menu"]

    ui.print_menu(options[0], options[1:7], options[-1])
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    if option == "1":
        show_table("games.csv")
    elif option == "2":
        add("games.csv")
    elif option == "3":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to delete:")
        remove("games.csv", choosen_ID)
    elif option == "4":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to update:")
        update("games.csv", choosen_ID)
    elif option == "5":
        get_counts_by_manufacturers("games.csv")
    elif option == "6":
        choosen_manufacturer = ui.get_inputs(["Manufacturer: "], "Average of games in stock: ")
        get_average_by_manufacturer("games.csv", choosen_manufacturer)
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
    table = data_manager.get_table_from_file("store/games.csv")
    ui.print_table(table, ["ID", "Title", "Manufacturer", "Price", "In_stock"])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    table = data_manager.get_table_from_file("store/games.csv")
    added_line = ui.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "In_stock: "], "Please provide your data to add:")
    random_ID = common.generate_random("store/games.csv")
    added_line.insert(0, random_ID)
    added_line_helper = []
    added_line_helper.append(added_line)
    expanded_lines = table + added_line_helper
    data_manager.write_table_to_file("store/games.csv", expanded_lines)
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

    table = data_manager.get_table_from_file("store/games.csv")
    index_to_remove = common.index_list_of_list(id_, table)
    table.remove(table[index_to_remove])
    data_manager.write_table_to_file("store/games.csv", table)
    start_module()

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    table = data_manager.get_table_from_file("store/games.csv")
    id_ = id_[0]
    update_data = ui.get_inputs(["Title: ","Manufacturer: ", "Price :", "In_stock: "], "Please provide data you would like to update:")
    index_to_update = common.index_list_of_list(id_, table)
    update_data.insert(0, id_)
    table[index_to_update] = update_data
    data_manager.write_table_to_file("store/games.csv", table)
    start_module()

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """
    table = data_manager.get_table_from_file("store/games.csv")
    manufacturers = []
    manufacturer_quantity = []
    result = {}
    for row in table:
        manufacturers.append(row[2])
    for manu in manufacturers:
        if manu in result:
            result[manu] += 1
        else:
            result.setdefault(manu, 1)
    
    return result
    
    

def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """
    table = data_manager.get_table_from_file("store/games.csv")
    games_in_stock = []
    for row in table:
        if manufacturer[0] in row:
            games_in_stock.append(row[4])
    average_by_manufacturer = common.my_sum(games_in_stock)/len(games_in_stock)

    return average_by_manufacturer

    
