"""
Author: Eren Sezener (erensezener@gmail.com)
Date: Month Day, 2014

Description: 

Status: Works correctly.

Dependencies:

Known bugs: -

"""

def get_default_string():
    xml_file = open("ExternalData.xml", "r")
    default_command = xml_file.read()
    return default_command


def is_terminate_command(input_text):
    if input_text == 'q' or input_text == 'Q':
        return True
    else:
        return False


def process_text(input_text): #TODO This is not robust at all, regex?
    text_without_spaces = input_text.replace(' ', '') #get rid of the spaces
    string_list = text_without_spaces.split(',')
    if string_list[0] == 'r' or string_list[0] == 'a':
        coordinates = []
        for i in range(1, len(string_list)):
            coordinates.append(float(string_list[i]))
        return string_list[0], coordinates
    else: # Erroneous command
        return None, []


def modify_default_string(default_string, command_list):
    pass


def run_client(connection):
    default_string = get_default_string()
    while True:
        input_text = raw_input()
        validity, command_list = process_text(input_text)
        if validity is not None:
            string_to_send = modify_default_string(default_string, command_list)
            connection.send(string_to_send)
        elif is_terminate_command(input_text):
            break
        else:
            print "The command is not valid."