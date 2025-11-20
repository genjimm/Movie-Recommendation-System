import os
import sys
from pyspark.sql import SparkSession

def main():
    # 当前 driver 使用的 Python 解释器
    driver_py = sys.executable
    print("Driver sys.executable =", driver_py)

    # 强制 PySpark worker & driver 都用同一个 python
    os.environ["PYSPARK_PYTHON"] = driver_py
    os.environ["PYSPARK_DRIVER_PYTHON"] = driver_py
    print("Env PYSPARK_PYTHON      =", os.environ["PYSPARK_PYTHON"])
    print("Env PYSPARK_DRIVER_PYTHON =", os.environ["PYSPARK_DRIVER_PYTHON"])

    spark = (
        SparkSession.builder
        .appName("WinSparkTest")
        .master("local[1]")               # 单线程，先把环境跑通
        .config("spark.ui.port", "4050")
        .config("spark.driver.memory", "512m")
        # 再用 Spark 自己的配置锁死 python 路径（双保险）
        .config("spark.pyspark.python", driver_py)
        .config("spark.pyspark.driver.python", driver_py)
        .getOrCreate()
    )

    sc = spark.sparkContext
    print("Spark version:", spark.version)
    print("Python exec used by Spark (sc.pythonExec) =", sc.pythonExec)

    rdd = sc.parallelize(range(1000))
    total = rdd.count()
    s = rdd.sum()

    print("RDD count =", total)
    print("RDD sum   =", s)

    spark.stop()

if __name__ == "__main__":
    main()
