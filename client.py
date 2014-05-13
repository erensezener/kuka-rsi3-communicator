"""
Author: Eren Sezener (erensezener@gmail.com)
Date: Month Day, 2014

Description: 

Status: Works correctly.

Dependencies:

Known bugs: -

"""
HEADER = '<Sen Type=\"ImFree\"><EStr>KRCnexxt - RSI Object ST_ETHERNET</EStr>'
FOOTER = '<Tech T21=\"1.09\" T22=\"2.08\" T23=\"3.07\" T24=\"4.06\" T25=\"5.05\" T26=\"6.04\" T27=\"7.03\" ' \
         'T28=\"8.02\" T29=\"9.01\" T210=\"10.00\"/><DiO>125</DiO><IPOC>0000000000</IPOC></Sen>'
DEFAULT_RKORR = '<RKorr X=\"0.0000\" Y=\"0.0000\" Z=\"0.0000\" A=\"0.0000\" B=\"0.0000\" C=\"0.0000\"/>'
DEFAULT_AKORR = '<AKorr A1=\"0.0000\" A2=\"0.0000\" A3=\"0.0000\" A4=\"0.0000\" A5=\"0.0000\" A6=\"0.0000\"/>'

def is_terminate_command(input_text):
    if input_text == 'q' or input_text == 'Q':
        return True
    else:
        return False


def process_text(input_text):  #TODO This is not robust at all, regex?
    text_without_spaces = input_text.replace(' ', '')  #get rid of the spaces
    string_list = text_without_spaces.split(',')
    if string_list[0] == 'r' or string_list[0] == 'a':
        coordinates = []
        for i in range(1, len(string_list)):
            coordinates.append(float(string_list[i]))
        return string_list[0], coordinates
    else:  # Erroneous command
        return None, []


def get_rkorr_string(command_list):
    command_list = map(lambda x: str(x), command_list)
    return '<RKorr X=\"' + command_list[0] + '\" Y=\"' + command_list[1] + '\" Z=\"' + command_list[2] + '\" A=\"' + \
           command_list[3] + '\" B=\"' + command_list[4] + '\" C=\"' + command_list[5] + '\" />'

def get_akorr_string(command_list):
    command_list = map(lambda x: str(x), command_list)
    return '<AKorr A1=\"' + command_list[0] + '\" A2=\"' + command_list[1] + '\" A3=\"' + command_list[2] + '\" A4=\"' + \
           command_list[3] + '\" A5=\"' + command_list[4] + '\" A6=\"' + command_list[5] + '\" />'


def create_command_string(type, command_list):
    if type == 'r':
        return HEADER + get_rkorr_string(command_list) + DEFAULT_AKORR + FOOTER
    elif type == 'a':
        return HEADER + DEFAULT_RKORR + get_akorr_string(command_list) + FOOTER



def run_client(connection):
    while True:
        input_text = raw_input("Please write the coordinates: ")
        type, command_list = process_text(input_text)
        if type is not None:
            string_to_send = create_command_string(type, command_list)
            print "Sending"
            print string_to_send
            connection.send(string_to_send)
        elif is_terminate_command(input_text):
            print "Terminating"
            return
        else:
            print "The command is not valid."