# Spark

Readable command.
- rides.show(5, vertical=True)
  - human readable
- head, take
  - not human readable

```Python
rides = spark.read.csv("/duocar/raw/rides", sep=",", inferSchema=True, header=True)
rides.show(5, vertical=True)
rides.printSchema()
```
