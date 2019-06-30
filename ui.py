""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    for line in table:
        for element in line:
            element.replace("\n", "").split(";")
    table.insert(0, title_list)
    trasponsed_table = list(map(list, zip(*table))) 
    longest_element_in_columns = []
    separator = "-"
    column_separator = " | "
    len_column_separator = len(column_separator)
    right_corner = "\\"
    left_corner = " /"
    correction_tag = 1
    line_separator = ""
    table_to_print = ""

    for columns in trasponsed_table:
        column = []
        for local_longest in columns:
            column.append(len(str(local_longest)))    
        longest_element_in_columns.append(max(column))


    width_of_table = len_column_separator * (len(title_list)) + sum(longest_element_in_columns) - correction_tag

    #Header & footer
    Top_bottom = left_corner + (separator * width_of_table) + right_corner

    #line_separator
    for i, element in enumerate(longest_element_in_columns):
        line_separator += column_separator + longest_element_in_columns[i] * separator

    #közértes
    for row in table:
        for i, element in enumerate(row):
            table_to_print += column_separator + element.center(longest_element_in_columns[i])
        table_to_print += column_separator + "\n" 
        table_to_print += line_separator + column_separator + "\n" 

    row_to_print = table_to_print
    table = (Top_bottom + "\n" + row_to_print)

    print(table)



def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(title + ":")
    for number, unit in enumerate(list_options):
        print("\t"+"(" + str(number+1) + ")", unit)
    print("\t"+"(0)", exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)

    for i in range(len(list_labels)):
        user_data = input(list_labels[i])
        inputs.append(user_data)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(message)
    # your code
