""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    options = ["Customer Relationship Management (CRM)",
               "List",
               "Add",
               "Remove",
               "Update",
               "Get longest name ID",
               "Get subscribed e-mails",
               "Exit to main menu"]
               
    ui.print_menu(options[0], options[1:7], options[-1])
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]

    if option == "1":
        show_table("customers.csv")
    elif option == "2":
        add("customers.csv")
    elif option == "3":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to delete:")
        remove("customers.csv", choosen_ID)
    elif option == "4":
        choosen_ID = ui.get_inputs(["ID: "], "Please provide the ID of the record you would like to update:")
        update("customers.csv", choosen_ID)
    elif option == "5":
        get_longest_name_id("customers.csv")
    elif option == "6":
        get_subscribed_emails("customers.csv")
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

    table = data_manager.get_table_from_file("crm/customers.csv")
    ui.print_table(table, ["ID", "Name: ", "E-mail: ", "Subscribed: "])


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    table = data_manager.get_table_from_file("crm/customers.csv")
    added_line = ui.get_inputs(["Name: ", "E-mail: ", "Subscribed: "], "Please provide your data to add:")
    random_ID = common.generate_random("crm/customers.csv")
    added_line.insert(0, random_ID)
    added_line_helper = []
    added_line_helper.append(added_line)
    expanded_lines = table + added_line_helper
    data_manager.write_table_to_file("crm/customers.csv", expanded_lines)
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

    table = data_manager.get_table_from_file("crm/customers.csv")
    index_to_remove = common.index_list_of_list(id_, table)
    table.remove(table[index_to_remove])
    data_manager.write_table_to_file("crm/customers.csv", table)
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

    table = data_manager.get_table_from_file("crm/customers.csv")
    id_ = id_[0]
    update_data = ui.get_inputs(["Name: ", "E-mail: ", "Subscribed: "], "Please provide data you would like to update:")
    index_to_update = common.index_list_of_list(id_, table)
    update_data.insert(0, id_)
    table[index_to_update] = update_data
    data_manager.write_table_to_file("crm/customers.csv", table)
    start_module()

    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    table = data_manager.get_table_from_file("crm/customers.csv")
    id_with_names = {}
    name = 1
    id = 0
    names = []
    longest_name_element_no = 0
    longest_names = []
    for line in table:
        id_with_names[line[id]] = line[name]
        names.append(line[name])
    for identication in names:
        if len(identication) > longest_name_element_no:
            longest_name_element_no = len(identication)
    for tag, person in id_with_names.items():
        if len(person) == longest_name_element_no:
            longest_names.append(person)
    last_alphabetical_name = max(longest_names)
    for tag, person in id_with_names.items():
        if len(person) == longest_name_element_no and person == last_alphabetical_name:
            return tag
            



# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
