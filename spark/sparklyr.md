# Sparklyr

* DataFrame : sdf_functions

* Feature transformers : ft_functions
  * ft_string_indexer
  * ft_one_hot_encoder

* Machine learning algorithms : ml_functions
  * ml_pipeline
  * ml_fit
 
 # Misc
 D3.js - Data Driven Documents Java Script
 
 
## CDSW R/Python/Scala? Invisible comment
#[//]: # (To include a comment that will not appear in the)
#[//]: # (output at all, you can use this curious syntax.)

## Data Analysis Objectives
- $ / revenue
- risk / cost

text file like json and csv is portable.

drawback is parque is hadoop-only.

you can use other languages without too much hustle.





# R Basics

## built-in R functions for tasks

- getwd() : pwd
- base::print.data.frame(file.info(list.files())) : ls

## Show what packages are loaded in this session of R:
- search()
- sessionInfo()

## Show the currently installed packages:
rownames(installed.packages())

## See if a particular package is installed:
"leaflet" %in% rownames(installed.packages())

# Sparklyr

- spark <- spark_connect(master = "yarn", app_name = "spark (yarn)")
- spark <- spark_connect(master = "local", app_name = "spark (local)", config = config)
- spark <- spark_connect(master = "local[*]", app_name = "spark (local)", config = config)

