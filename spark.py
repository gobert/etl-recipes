import json
from awesome_print import ap
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.sql.types import StructField, StructType, StringType, ArrayType, \
                              IntegerType, DataType
from models import Recipe

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def configure_spark(app_name, master):
    conf = SparkConf().setAppName(app_name).setMaster(master)
    sc = SparkContext(conf=conf)
    sc.addPyFile("./models.py")
    sql_context = SQLContext(sc)
    return sc, sql_context


def recipe_to_row(recipe):
    return Row(ingredients=" ".join(recipe.ingredients),
               description=recipe.description, name=recipe.name,
               url=recipe.url, image=recipe.image,
               recipe_yield=recipe.recipe_yield,
               date_published=recipe.date_published.strftime("%Y-%m-%d"),
               preparation_duration=recipe.preparation_duration,
               cooking_duration=recipe.cooking_duration)


def recipe_schema():
    return StructType([
        StructField('ingredients', StringType(), True),
        StructField('description', StringType(), True),
        StructField('name', StringType(), True),
        StructField('url', StringType(), True),
        StructField('image', StringType(), True),
        StructField('recipe_yield', StringType(), True),
        StructField('date_published', StringType(), True),
        StructField('preparation_duration', StringType(), True),
        StructField('cooking_duration', StringType(), True),
    ])


def run(sc, sql_context, output):
    recipes = sc.textFile("recipes.json")

    recipes = recipes.map(lambda line: json.loads(line))
    recipes = recipes.map(lambda recipe_json: Recipe(recipe_json))
    recipes = recipes.filter(lambda recipe: recipe.has_chili())
    rows = map(lambda recipe: recipe_to_row(recipe), recipes.collect())

    dataframe = sql_context.createDataFrame(rows, recipe_schema())
    dataframe.write.parquet(output)


if __name__ == '__main__':
    spark_master = sys.argv[1]
    sc, sql_context = configure_spark("SkillUpExercise", spark_master)
    run(sc, sql_context, "output")
