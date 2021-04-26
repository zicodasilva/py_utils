"""
Log utility file that encapsulates the default "logger" module.

NOTE: This module should be used for logging to stdout instead of "print".
The log level is configurable using the LOG_LEVEL environment variable.

Example:
    To get DEBUG logs:
        `export LOG_LEVEL="DEBUG" && python script.py`

@author: Zico da Silva
"""
import os
import logging

# Read the LOG_LEVEL environment varaible and set the logger level with this value.
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO").upper()
# Set up the logger output format.
logging.basicConfig(format="%(asctime)s.%(msecs)03d | %(levelname)s | %(name)s: %(message)s",
                    datefmt="%Y-%m-%dT%H:%M:%S",
                    level=LOG_LEVEL)


def logger(name: str) -> logging.Logger:
    """Creates a new logger.

    Args:
        name: Name of the module. This field is displayed in each log.

    Returns:
        The python module "logger" instance used to log to stdout.
    """
    return logging.getLogger(name)
