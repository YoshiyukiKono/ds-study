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
spark.stop()
```

## Pandas
```Python
import pandas as pd
pd.options.display.html.table_schema=True
rides.limit(5).toPandas()
```

```Python
# The `id` column represents a primary key variable.  It should be non-null and
# unique.
rides.select("id").show(10)

# Count the number of missing (null) values:
rides.select("id").filter(rides.id.isNull()).count()
rides.select("id").where(rides.id.isNull()).count()

# Count the number of distinct values:
rides.select("id").distinct().count()

# Count the number of non-missing and distinct values using Column functions:
from pyspark.sql.functions import count, countDistinct
rides.select(count("*"), count("id"), countDistinct("id")).show()

rides.createOrReplaceTempView("rides_view")

rides.groupby("service").count().toPandas().plot(x="service", y="count", kind="bar")


# Default DB is available without doing nothing! How to change database?
spark.sql("SELECT * FROM airlines").show()
spark.sql("SELECT * FROM duocar.drivers").show()
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

spark_disconnect(spark)
```
