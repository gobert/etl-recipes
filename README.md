# Technical Challenge for spark

Load some recipes from a file, select the recipes with chilies (singular, plural and with typo) and export them into a parquet file. This was a technical challenge to skill myself with Spark.

# Set-up
* Install python 2.7.14, like using pyenv: ```pyenv install 2.7.14```
* Install requirements, like with pip ```pip install -r requirements.txt```
* [Install Spark 1.6.1](https://spark.apache.org/downloads.html)
* [Add package pySpark](https://stackoverflow.com/a/29498104/1483163)
* Ensure NLTK dependencies are up to date: ```python -c "import nltk;nltk.download()"```
* Download input dataset in the project folder, like with wget: ```wget https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json .```

# Run me
**Local mode**
```
python spark.py local
```

**In Standalone**
1. Start services
  ```
  sbin/start-master.sh -h 127.0.0.1  # start spark master
  sbin/start-slave.sh spark://127.0.0.1:7070 # add exeutor to master
  ```
2. Launch application with ```spark-submit```. For instance, on my local installation:
  ```
  ~/sys/spark-1.6.1-bin-hadoop2.4/bin/spark-submit spark.py spark://localhost:7077
  ```

**Over YARN**
```
~/sys/spark-1.6.1-bin-hadoop2.4/bin/spark-submit spark.py yarn-client
```

# Test
On top of each commit, all tests must pass:
```
py.test && rm -r **/*.pyc **/__pycache__
```

# Code quality
On top of each commit, no offense must be detected:
```
pep8 -- .
```
