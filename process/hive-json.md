# Json SerDe

## Twits
実際は１行

```
{
  "cursor" : {
    "since" : 159007802,
    "max" : 159000193,
    "more" : true
  },
  "messages" : [
    {
      "source" : {
        "id" : 2269,
        "title" : "StockTwits Web",
        "url" : "https://stocktwits.com"
      },
      "mentioned_users" : [

      ],
      "id" : 159007802,
      "created_at" : "2019-03-31T05:39:15Z",
      "symbols" : [
        {
          "watchlist_count" : 291210,
          "id" : 686,
          "symbol" : "AAPL",
          "title" : "Apple Inc.",
          "aliases" : [

          ],
          "is_following" : false
        },
        {
          "watchlist_count" : 207648,
          "id" : 7871,
          "symbol" : "FB",
          "title" : "Facebook",
          "aliases" : [
            "FBOOK"
          ],
          "is_following" : false
        }
      ],
      "entities" : {
        "chart" : {
          "large" : "https://charts.stocktwits.com/production/large_159007802.png",
          "original" : "https://charts.stocktwits.com/production/original_159007802.png",
          "thumb" : "https://charts.stocktwits.com/production/small_159007802.png",
          "url" : "https://charts.stocktwits.com/production/original_159007802.png"
        },
        "sentiment" : {
          "basic" : "Bullish"
        }
      },
      "body" : "$FB $FB Zuck looking for the next bear to cuckold.  Easy $180 soon.   Will destroy $AAPL in it&#39;s sleep. $FB &gt; $AAPL",
      "user" : {
        "id" : 493226,
...
```


```
add jar hdfs:/tmp/json-1.3.7.3.jar;
add jar hdfs:/tmp/json-serde-1.3.7.3.jar;
add jar hdfs:/tmp/json-serde-cdh5-shim-1.3.7.3AA.jar;

DROP TABLE IF EXISTS twits;
CREATE EXTERNAL TABLE twits (
	messages ARRAY<STRUCT<body: STRING>>
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' 
STORED AS TEXTFILE
LOCATION '/tmp/twits';

select messages from twits;

select message from twits lateral view explode(messages.body) messages as message;
```

```
DROP TABLE IF EXISTS twits;
CREATE EXTERNAL TABLE twits (
	messages 
	ARRAY<
	    STRUCT<body: STRING,
	        symbols:ARRAY<STRUCT<symbol:STRING>>,
	        entities:STRUCT<sentiment:STRING>
	    >
	>
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' 
STORED AS TEXTFILE
LOCATION '/tmp/twits';
```

```
select message.symbols, message.entities.sentiment, message.body from twits lateral view explode(messages) messages as message;
```

```
symbols,sentiment,body
"[{""symbol"":""AAPL""},{""symbol"":""FB""}]","{""basic"":""Bullish""}",$FB $FB Zuck looking for the next bear to cuckold.  Easy $180 soon.   Will destroy $AAPL in it&#39;s sleep. $FB &gt; $AAPL
"[{""symbol"":""AAPL""},{""symbol"":""C""},{""symbol"":""ROKU""},{""symbol"":""BABA""}]",NULL,Lessons Learning From My Losing Swing-Trades: #Apple + #Citigroup $AAPL $C Also $BABA $ROKU https://talkmarkets.com/content/investing-ideas--strategies/lessons-learning-from-my-losing-swing-trades-apple--citigroup?post=215908
"[{""symbol"":""AAPL""},{""symbol"":""SPY""}]","{""basic"":""Bearish""}",$AAPL $SPY bearish macd cross. Rsi rejection
```

```
create table twits_message (symbols STRING, sentiment STRING, body STRING) STORED AS TEXTFILE;
insert overwrite table twits_message select message.symbols, message.entities.sentiment, message.body from twits lateral view explode(messages) messages as message;
select symbols, sentiment, body from twits_message;
```



## 利用例
### HiveでJSONデータを処理するあれこれ(初級編)
https://qiita.com/unksato/items/42405305c28e5a788cd7
### HiveでJSONデータを処理するあれこれ(中級編)
Https://qiita.com/unksato/items/604edb73eb636dc8ada7

{ "a": "abc", "b": 123, "c": { "aa": "xyz", "bb": 987 }, "d": [1,2,3], "e": [ { "aaa": "ABC", "bbb": 12345 }, { "aaa": "XYZ", "bbb": 98765 } ] }


## OpenX

### AWS JSON SerDeライブラリ
Ja: https://docs.aws.amazon.com/ja_jp/athena/latest/ug/json.html#hivejson
En： https://docs.aws.amazon.com/athena/latest/ug/json.html#hivejson

#### Create Tables in Amazon Athena from Nested JSON and Mappings Using JSONSerDe
https://aws.amazon.com/blogs/big-data/create-tables-in-amazon-athena-from-nested-json-and-mappings-using-jsonserde/


https://github.com/rcongiu/Hive-JSON-Serde

https://github.com/rcongiu/Hive-JSON-Serde.git

json-serde-cdh5-shim

#### 

### Download json-serde JAR files with dependency
https://jar-download.com/?search_box=json-serde

## Misc

### Apache Json is recomended here
https://community.cloudera.com/t5/Batch-SQL-Apache-Hive/Create-Hive-Table-from-JSON-Files/td-p/64006

### Cannot validate serde : org.openx.data.jsonserde.jsonserde
https://stackoverflow.com/questions/26644351/cannot-validate-serde-org-openx-data-jsonserde-jsonserde

## Troubleshooting

ファイルが置いていない時（も）このエラー
Cannot validate serde : org.openx.data.jsonserde.jsonserde


