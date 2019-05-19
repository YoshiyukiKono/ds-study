# SpacyRで、Stats Tweetを分析

SparklyRでのHiveターブル集計

https://blog.cloudera.co.jp/rspark-with-cloudera-director-ee9ac5826f19

Dpryler

http://www.housecat442.com/?p=346

## 準備
SparklyRで接続

## データロード
```
table <- tbl(sc, "<Hive Table>")
table
```

テーブルに、ID, Sentiment, MessageBodyが入っているとする
```
counts_by_sentiment <- table %>% group_by(sentiment) %>% summarise(count=n()) %>% collect
counts_by_sentiment %>% tbl_df %>% print(n=nrow(.))

## # A tibble: 22 × 2
##     sentiment   cound
##    <int>   <double>
## 1   -1 54321
## 2    1 12345
## 3    0 ?????
```
こんな感じになればよい？

IDやID+Sentimentでも、Group Byする

```
counts_by_sentiment <- table %>% group_by(id, sentiment) %>% summarise(count=n()) %>% collect
```

## SpacyR

https://github.com/chezou/spacyr-sparklyr
```
#install.packages("spacyr")
library(spacyr)
spacy_initialize(python_executable="/home/cdsw/r_env/bin/python")

txt <- c(d1 = "spaCy excels at large-scale information extraction tasks.",
         d2 = "Mr. Smith goes to North Carolina.")

# process documents and obtain a data.table
parsedtxt <- spacy_parse(txt, lemma = FALSE)
entity_extract(parsedtxt)
```
```
entities <- tbl %>%
  select(text) %>%
  spark_apply(
    function(e) 
    {
      lapply(e, function(k) {
          spacyr::spacy_initialize(python_executable="/opt/cloudera/parcels/Anaconda/bin/python")
          parsedtxt <- spacyr::spacy_parse(as.character(k), lemma = FALSE)
          spacyr::entity_extract(parsedtxt)
        }
      )
    },
    names = c("doc_id", "sentence_id", "entity", "entity_type"),
    packages = FALSE)
```

```
#### Show results
entities %>% head(10) %>% collect()

grouped_entities <- entities %>% 
  group_by(entity_type) %>% 
  count() %>% 
  arrange(desc(n)) %>%
  collect()
  

grouped_entities

#### Plot the graph

library(ggplot2)

p <- entities %>%
  collect() %>% 
  ggplot(aes(x=factor(entity_type)))
p <- p + scale_y_log10()
p + geom_bar()

#### Show Top 10 persons for each document

persons <- entities %>% 
  filter(entity_type == "<?PERSON?>") %>%
  group_by(doc_id, entity) %>%
  select(doc_id, entity) %>%
  count() %>%
  arrange(doc_id, desc(n))

persons %>% 
  filter(doc_id == "text1") %>%
  head(10) %>%
  collect()

persons %>% 
  filter(doc_id == "text2") %>%
  head(10) %>%
  collect()
```

https://github.com/quanteda/spacyr
