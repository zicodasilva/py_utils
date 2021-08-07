"""
Data operations utility.
Mainly saving/loading data to/from disk and general operations on in-memory data storage containers  i.e. dictionaries etc.

@author: Zico da Silva
"""
import pickle
import cloudpickle
import dill
from typing import Any, Dict, List, Union
import pandas as pd
import numpy as np


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


def save_dill(filename: str, data: Any) -> None:
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


def series_to_supervised(data: Union[pd.DataFrame, np.ndarray, List], n_in=1, n_out=1, dropnan=True) -> pd.DataFrame:
    """
	Frame a time series as a supervised learning dataset.
	Args:
		data: Sequence of observations as a list or NumPy array.
		n_in: Number of lag observations as input (X).
		n_out: Number of observations as output (y).
		dropnan: Boolean whether or not to drop rows with NaN values.
	Returns:
        Pandas DataFrame of series framed for supervised learning.
	"""
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)

    return agg
