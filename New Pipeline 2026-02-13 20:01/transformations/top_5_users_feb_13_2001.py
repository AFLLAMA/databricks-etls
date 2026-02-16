from pyspark import pipelines as dp
from pyspark.sql.functions import col, count, count_if
from utilities import utils

@dp.table
def top_5_user_types():
    return (
        spark.read.table("sample_users_feb_13_2001").orderBy("name").limit(5)
    )
