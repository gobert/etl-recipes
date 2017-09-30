# Apache Spark

1. Download the following dataset of [Open Recipes](https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json)
* Write an Apache Spark application in Python that reads the recipes json, extracts every recipe that has “Chilies” as one of the ingredients. Please allow for mispelling of the word for example Chiles as well as the singular form of the word.
* Add an extra field to each of the extracted recipes with the name difficulty. The difficulty field would have a value of "Hard" if the total of prepTime and cookTime is greater than 1 hour, "Medium" if the total is between 30 minutes and 1 hour, "Easy" if the total is less than 30 minutes, and "Unknown" otherwise.
* The resulting dataset should be saved as parquet file.
* Your Spark application could run in Stand-alone mode or it could run on YARN.
* Place your answer in a directory called "recipes-etl" in the root of this repository, with a README.md file that outlines the instructions to run your Spark Application.

## Requirements

1. Use Apache Spark version 1.6.1
2. Write well structured, documented, maintainable code.
3. Write unit tests to test the different components

Open Recipes archive courtesy of [Ed Finkler](https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json)
