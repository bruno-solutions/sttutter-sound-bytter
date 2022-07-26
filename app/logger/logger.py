import logging
import time
import traceback
from typing import Union

import pydub

from configuration.configuration import Configuration


def timestamp():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))


class Logger(object):
    """
    Custom logger class
    """

    def __init__(self, log_file_path: str = Configuration().get('log_file_path'), log_to_console: bool = Configuration().get('log_to_console'), log_debug: bool = Configuration().get('log_debug'), log_warning: bool = Configuration().get('log_warning'), log_error: bool = Configuration().get('log_error')):
        self.log_to_console = log_to_console
        self.log_file_path = log_file_path
        self.log_debug = log_debug
        self.log_warning = log_warning
        self.log_error = log_error

        traceback.print_stack()
        logging.basicConfig(filename=self.log_file_path, filemode='w', level=logging.DEBUG if log_debug else logging.WARNING if log_warning else logging.ERROR, format="%(asctime)s [%(levelname)s] %(message)s")

    def separator(self, separator: Union[str, bool] = Configuration().get('log_file_separator'), length: int = 80, mode: str = ''):
        """
        Emit a log separator
        """
        if not separator or ('debug' == mode and not self.log_debug) or ('warning' == mode and not self.log_warning) or ('error' == mode and not self.log_error):
            return

        separator = ''.join([(separator if separator is str and separator != '' else Configuration().get('log_file_separator')) * length])

        if self.log_to_console:
            print(separator)

        if self.log_file_path is not None:
            logging.info(separator)

    def debug(self, message: str, separator: Union[str, bool] = False):
        """
        Log a debug message
        """
        if not self.log_debug:
            return

        self.separator(separator)

        message: str = message.lstrip()

        if self.log_to_console:
            if message.startswith('[download]'):
                print(f"\r{timestamp()} [DEBUG]: {message}", end='' if "100%" not in message else '\n', flush=True)
            else:
                print(f"{timestamp()} [DEBUG]: {message}")

        if self.log_file_path is not None:
            logging.debug(message)

    def warning(self, message: str, separator: Union[str, bool] = False):
        """
        Log a warning
        """
        if not self.log_warning:
            return

        self.separator(separator)

        message: str = message.lstrip()

        if self.log_to_console:
            print(f"{timestamp()} [WARNING]: {message}")

        if self.log_file_path is not None:
            logging.warning(message)

    def error(self, message: str, separator: Union[str, bool] = False):
        """
        Log an error
        """
        if not self.log_error:
            return

        self.separator(separator)

        message: str = message.lstrip()

        if self.log_to_console:
            print(f"{timestamp()} [ERROR]: {message}")

        if self.log_file_path is not None:
            logging.error(message)

    def properties(self, recording: pydub.AudioSegment, message: str = None):
        self.separator()

        if message is not None:
            self.debug(message)

        number_of_samples: int = len(recording.get_array_of_samples())
        number_of_samples_per_channel: int = number_of_samples // recording.channels
        duration: float = number_of_samples_per_channel / recording.frame_rate

        self.debug(f"Frame rate: {recording.frame_rate}")
        self.debug(f"Channels: {recording.channels} ({'monaural' if 1 == recording.channels else 'stereo'})")
        self.debug(f"Sample count: {number_of_samples}, per channel: {number_of_samples_per_channel}")
        self.debug(f"Duration: {(duration // 60):0.0f}:{(duration % 60):0.0f} or precisely {duration:f} seconds")
