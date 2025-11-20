from pyspark.sql import SparkSession

def main():
    # 创建本地 SparkSession
    spark = SparkSession.builder \
        .appName("LocalSparkQuickCheck") \
        .master("local[*]") \
        .config("spark.ui.port", "4050") \
        .getOrCreate()

    # 简单 DataFrame 测试
    df = spark.createDataFrame(
        [(1, "A"), (2, "B"), (3, "C")],
        ["id", "label"]
    )
    print("Row count:", df.count())
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()
