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

### approxQuantile
```
rides.approxQuantile("distance", \
    probabilities=[0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 1.0], \
    relativeError=0.1)
[304.0, 304.0, 304.0, 4323.0, 5626.0, 9157.0, 92204.0, 92204.0, 92204.0]
rides.approxQuantile?
Signature: rides.approxQuantile(col, probabilities, relativeError)
Docstring:
Calculates the approximate quantiles of numerical columns of a
DataFrame.

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

### Spark function?
- decrypt
- sqrt

### Various Syntax
SELECT値の編集
```
riders.select(riders.id*2).show()
riders.select("student").withColumn("student_bool", col("student") == 1).show()
riders.select("student", (col("student") == 1).alias(""student_bool)).show()
riders.withColumn("home_block", col("home_block").cast("string")).show()
```
NULL値の操作
```
riders.dropna(how="any", subset=["sex", "ethnicity"]).show()
riders.fillna("UNKNOWN", subset=["sex", "ethnicity"]).show()
riders.na.fill({"sex":"UNKNOWN", "ethnicity":"NA"}).show()
```

### SQL Method
```
spark.sql("SHOW DATABASES").show()
spark.sql("USE duocar")
spark.sql("SHOW TABLES").show()
spark.sql("DESCRIBE riders").show()
spark.sql("SELECT * FROM riders LIMIT 10").show()

spark.sql("DROP TABLE IF EXISTS %s" % table_name)
```

#### Join

```
scientists.join(offices, scientists.office_id == offices.office_id, "inner").show()
```

##### Anti Join
```
# Use the value `left_anti` to return the rows in the left DataFrame that do
# not match rows in the right DataFrame:
scientists \
  .join(offices, scientists.office_id == offices.office_id, "left_anti") \
  .show()
```

### Left outer join
```
scientists \
  .join(offices, scientists.office_id == offices.office_id, "left_outer") \
  .show()
```
SparkのUNIONは、SQLのUNION ALL. SQLのUNIONにするには、distinctする必要がある

# Data Preperation for Training, Validation, Test

```
# Use the `randomSplit` DataFrame method to split a DataFrame into random
# subsets:
riders.count()
(train, validate, test) = riders.randomSplit(weights=[0.6, 0.2, 0.2], seed=12345)
(train.count(), validate.count(), test.count())
```

approx_count_distinct: サンプル利用、正確ではないが、早い

<data frame>.agg(count(..), ...)
 Sparkの場合、
<data frame>.select(count(..),..)でもよい。
  
- Skew
  - Positive Skew: Mean Mode Avg
  - Negative Skew: Mean Mode Avg
- Kurtosis: Steep or Flat

Use the `rollup` method to get subtotals
rollup(A, B)
B=nullでAだけでのaggregationが行われる(=subtotal)

## Pivoting data
```
# The following use case is common:
rides.groupBy("rider_student", "service").count().orderBy("rider_student", "service").show()

# The `crosstab` method can be used to present this result in a pivot table:
rides.crosstab("rider_student", "service").show()

# We can also use the `pivot` method to produce a cross-tabulation:
rides.groupBy("rider_student").pivot("service").count().show()

# We can also perform other aggregations:
rides.groupBy("rider_student").pivot("service").mean("distance").show()

rides.groupBy("rider_student").pivot("service").agg(mean("distance")).show()

# You can explicitly choose the values that are pivoted to columns:
rides.groupBy("rider_student").pivot("service", ["Car", "Grand"]).agg(mean("distance")).show()

# Additional aggregation functions produce additional columns:
rides.groupBy("rider_student").pivot("service", ["Car"]).agg(count("distance"), mean("distance")).show()

```
kde = k.. d.. Estimate
