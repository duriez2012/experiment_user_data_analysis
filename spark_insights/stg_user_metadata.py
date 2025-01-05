from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from pyspark.sql.functions import col, years, months
from pyspark.sql import SparkSession, Column

spark = (
    SparkSession.builder
    .appName("GoodNotesProcessStg")
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config(
        "google.cloud.auth.service.account.json.keyfile",
        "/Users/celinehocquette/PycharmProjects/interview_goodnotes/tduriez-interview-83a4159d10c7.json")
    .getOrCreate()
)

spark.table("iceberg_catalog.insights.raw_user_metadata").show()
