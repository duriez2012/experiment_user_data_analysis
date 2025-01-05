from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType
from pyspark.sql.functions import col, years, months
from pyspark.sql import SparkSession, Column

spark = (
    SparkSession.builder
    .appName("GoodNotesIngestRaw")
    .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .config(
        "google.cloud.auth.service.account.json.keyfile",
        "/Users/celinehocquette/PycharmProjects/interview_goodnotes/tduriez-interview-83a4159d10c7.json")
    .getOrCreate()
)

GCS_BUCKET = "gs://tduriez_interview_goodnotes"
USER_METADATA_FILE = f"{GCS_BUCKET}/user_data/user_metadata_sample.csv"
USER_INTERACTIONS_FILE = f"{GCS_BUCKET}/user_data/user_interactions_sample.csv"

user_metadata_df = (
    spark.read
    .option("multiline","true")
    .option("header", True)
    .option("inferSchema", True)
    .csv(USER_METADATA_FILE)
)

user_metadata_df.printSchema()

user_metadata_df.writeTo("iceberg_catalog.insights.raw_user_metadata") \
  .using("iceberg") \
  .partitionedBy("country") \
  .tableProperty("write.format.default", "parquet") \
  .tableProperty("format-version", "2") \
  .createOrReplace()