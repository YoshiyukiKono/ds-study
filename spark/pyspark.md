# PySpark

Readable command.
- rides.show(5, vertical=True)
  - human readable
- head, take
  - not human readable

```Python
from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("yarn") \
    .appName("spark") \
    .getOrCreate()
rides = spark.read.csv("/duocar/raw/rides", sep=",", inferSchema=True, header=True)
rides.count()
len(rides.column)
rides.show(5, vertical=True)
rides.printSchema()
```

```R
library(sparklyr)
library(dplyr)

config <- spark_config()
config$spark.driver.host <- Sys.getenv("CDSW_IP_ADDRESS")
spark <- spark_connect(
  master = "local",
  app_name = "inspect",
  config = config
)

riders <- spark_read_csv(
  sc = spark,
  name = "riders",
  path = "/duocar/raw/riders/"
)
riders %>% 
  distinct(first_name, last_name) %>% 
  sdf_nrows()
```
