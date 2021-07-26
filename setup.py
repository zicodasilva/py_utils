from setuptools import setup, find_packages

setup(
    name="py_utils",
    version="1.1.0",
    description="A general shared utilities library for Python.",
    author="Zico da Silva",
    author_email="zicods7@gmail.com",
    url="https://github.com/zicodasilva/py_utils",
    packages=find_packages(),
    install_requires=["cloudpickle", "dill", "numpy", "sympy", "sklearn"]
)
