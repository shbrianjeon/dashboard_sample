# my_github_package/setup.py

from setuptools import setup, find_packages

setup(
    name='my_github_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'pandas',
        'numpy',
        'seaborn',
        'matplotlib',
        'plotly'
    ],
)
