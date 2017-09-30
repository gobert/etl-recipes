# Technical Challenge for spark

Load some recipes from a file, select the recipes with chilies (singular, plural and with typo) and export them into a parquet file. This was a technical challenge to skill myself with Spark.

# Set-up
* Install python 2.7.14 like using pyenv: ```pyenv install 2.7.14```
* Install requirements like with pip ```pip install -r requirements.txt```

# Test
On top of each commit, all tests must pass:
```
py.test && rm -r **/*.pyc **/__pycache__
```

# Code quality
On top of each commit, no offense must be detected
```
pep8 -- .
```
