"""
Data operations utility.
Mainly saving/loading data to/from disk and general operations on in-memory data storage containers  i.e. dictionaries etc.

@author: Zico da Silva
"""
import pickle
import cloudpickle
import dill
from typing import Any, Dict

def save_pickle(filename: str, data: Dict) -> None:
    """Saves dictionary as a pickle file to a user supplied destination directory.

    Args:
        filename: Full path to the directory and he filename for the pickle file.
        data: The data to be saved.
    """
    with open(filename, "wb") as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_pickle(filename: str) -> Dict:
    """Reads data from a pickle file.

    Args:
        filename: Full path to the pickle file.

    Returns:
        Read data into a dictionary.
    """
    with open(filename, "rb") as handle:
        return pickle.load(handle)

def save_dill(filename: str, data: Dict) -> None:
    """Saves dictionary as a pickle file to a user supplied destination directory using dill.

    Args:
        filename: Full path to the directory and he filename for the pickle file.
        data: The data to be saved.
    """
    with open(filename, "wb") as handle:
        dill.dump(data, handle, protocol=pickle.DEFAULT_PROTOCOL)

def load_dill(filename: str) -> Dict:
    """Reads data from a pickle file using dill.

    Args:
        filename: Full path to the pickle file.

    Returns:
        Read data into a dictionary.
    """
    with open(filename, "rb") as handle:
        return dill.load(handle)

def save_cloudpickle(filename: str, data: Any) -> None:
    """Saves the data that cannot be saved with the normal `pickle` module i.e. sympy functions and pyomo models.

    Args:
        filename: Full path to the directory and he filename for the pickle file.
        data: The data to be saved.
    """
    with open(filename, "wb") as file:
        cloudpickle.dump(data, file, protocol=pickle.DEFAULT_PROTOCOL)

def load_cloudpickle(filename: str) -> Dict:
    """Reads data using cloudpickle.

    Args:
        filename: Full path to the pickle file.

    Returns:
        Read data into a dictionary.
    """
    with open(filename, "rb") as handle:
        return cloudpickle.load(handle)

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
