"""
Data operations utility.
Mainly saving/loading data to/from disk and general operations on in-memory data storage containers  i.e. dictionaries etc.

@author: Zico da Silva
"""
import pickle
import cloudpickle
from typing import Any, Dict

def save_data(filename: str, data: Dict) -> None:
    """Saves dictionary as a pickle file to a user supplied destination directory.

    Args:
        filename: Full path to the directory and he filename for the pickle file.
        data: The data to be saved.
    """
    with open(filename, "wb") as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_data(filename: str) -> Dict:
    """Reads data from a pickle file.

    Args:
        filename: Full path to the pickle file.

    Returns:
        Read data into a dictionary.
    """
    with open(filename, "rb") as handle:
        return pickle.load(handle)

def save_sympy_functions(filename: str, data: Any) -> None:
    """Saves the lambdified sympy functions to a pickle file.

    Args:
        filename: Full path to the directory and he filename for the pickle file.
        data: The data to be saved.
    """
    with open(filename, "wb") as file:
        cloudpickle.dump(data, file)

def get_key(dict_data: Dict, value: Any) -> str:
    """Gets the key value in a dictionary based on the value.

    Args:
        dict_data: The input dictionary object.
        value: The value to be searched.

    Raises:
        ValueError: Value could not be found in dictionary.

    Returns: the key value.
    """
    for key, val in dict_data.items():
         if val == value:
             return key

    raise ValueError(f"Could not find key corresponding to value: {value}")
