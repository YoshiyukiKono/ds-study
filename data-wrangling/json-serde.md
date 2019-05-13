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
add jar hdfs:/tmp/json-serde-cdh5-shim-1.3.7.3.jar;

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

### Insert Overwrite New Table
```
create table twits_message (symbols STRING, sentiment STRING, body STRING) STORED AS TEXTFILE;
insert overwrite table twits_message select message.symbols, message.entities.sentiment, message.body from twits lateral view explode(messages) messages as message;
select symbols, sentiment, body from twits_message;
```

## 詳細化
sentimentの値を取り出せるよう構造体として定義
```
DROP TABLE IF EXISTS twits;
CREATE EXTERNAL TABLE twits (
	messages 
	ARRAY<
	    STRUCT<body: STRING,
	        symbols:ARRAY<STRUCT<symbol:STRING>>,
	        entities:STRUCT<sentiment:STRUCT<basic:STRING>>
	    >
	>
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe' 
STORED AS TEXTFILE
LOCATION '/tmp/twits';
```

sentimentがないメッセージを除いて、select (selectではうまくいくが、insert ... selectでは、なぜか上手くいかない)
```
select message.symbols, message.entities.sentiment.basic, message.body from twits lateral view explode(messages) messages as message where message.entities.sentiment is not null;
```

symbolを配列として受け取れるよう定義(JSON文字列はStructとして認識される。)
```
create table twits_message (symbols array<struct<symbol:string>>, sentiment STRING, body STRING) STORED AS TEXTFILE;
create table messages (symbols array<struct<symbol:string>>, sentiment STRING, body STRING) STORED AS TEXTFILE;
```

insertの時につけたnot null条件は上手く働かないので、２段階で、テーブルに格納
```
create table twits_message (symbols array<struct<symbol:string>>, sentiment STRING, body STRING) STORED AS TEXTFILE;
create table messages (symbols array<struct<symbol:string>>, sentiment STRING, body STRING) STORED AS TEXTFILE;

insert overwrite table twits_message select message.symbols, message.entities.sentiment, message.body from twits lateral view explode(messages) messages as message where message.entities.sentiment is not null;
insert overwrite table messages select symbols, sentiment, body from twits_message where sentiment is not null;
```

latelal view を使い、1行＝１シンボルに変換。全てのカラムは純粋に文字列のみになる。
```
select symbol.symbol, sentiment, body from messages lateral view explode(symbols) symbols as symbol;
```

## TODO

- DONE 現在のクエリを基本に扱いやすいデータに切り詰める:sentiment.basic
- DONE SympolでのGroupや、SentimentでのGroup

- ML利用データへ変換：Bulish -> 2, Bealish -> -2, 

- DONE NULLデータ除去など。

- DATAタグの付与（テキスト結合でよしとする？）


- Hive検索結果をテキストに吐き出す（どうやる？　質問１）
- Sparkで加工？　やりたくない？

- とにかく、BODYをファイルに書き出す（＝austin_book相当として、Spacyrで扱う

- HDFSからRのデータフレームにどうやって変換する？（難易度高）
- 本文の何をどう、分析するか？


### Hive to JSON
https://github.com/klout/brickhouse


https://codeday.me/jp/qa/20190211/256058.html

```
add jar hdfs:/tmp/brickhouse-0.7.1-SNAPSHOT.jar;
CREATE TEMPORARY FUNCTION to_json AS 'brickhouse.udf.json.ToJsonUDF';

SELECT to_json( named_struct( "symbols", symbols ,
            "sentiment", sentiment,
            "body", body ) )
   FROM twits_message;
```

#### Output
symbolsの扱いに課題：配列(String)が\u0002(START OF TEXT)で分割されている
```
"{""symbols"":""AAPL\u0002FB"",""sentiment"":""{\""basic\"":\""Bullish\""}"",""body"":""$FB $FB Zuck looking for the next bear to cuckold.  Easy $180 soon.   Will destroy $AAPL in it&#39;s sleep. $FB &gt; $AAPL""}"
"{""symbols"":""AAPL\u0002C\u0002ROKU\u0002BABA"",""sentiment"":null,""body"":""Lessons Learning From My Losing Swing-Trades: #Apple + #Citigroup $AAPL $C Also $BABA $ROKU https://talkmarkets.com/content/investing-ideas--strategies/lessons-learning-from-my-losing-swing-trades-apple--citigroup?post=215908""}"
"{""symbols"":""AAPL\u0002SPY"",""sentiment"":""{\""basic\"":\""Bearish\""}"",""body"":""$AAPL $SPY bearish macd cross. Rsi rejection""}"

```

#### ML想定フォーマット

This JSON file contains a list of objects for each twit in the 'data' field:

```
{'data':
  {'message_body': 'Neutral twit body text here',
   'sentiment': 0},
  {'message_body': 'Happy twit body text here',
   'sentiment': 1},
   ...
}
```

The fields represent the following:

- 'message_body': The text of the twit.
- 'sentiment': Sentiment score for the twit, ranges from -2 to 2 in steps of 1, with 0 being neutral.

ここでは、Ticker/Symbolは不要。

## 利用例
### HiveでJSONデータを処理するあれこれ(初級編)
https://qiita.com/unksato/items/42405305c28e5a788cd7
### HiveでJSONデータを処理するあれこれ(中級編)
Https://qiita.com/unksato/items/604edb73eb636dc8ada7

###  Hive posexplode関数を使った配列操作について (配列のインデックスを保持したまま処理を行う方法)
http://kakts-tec.hatenablog.com/entry/2017/04/25/234644


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

## Lateral View + explode

JSON処理した後に、配列（TICKER）を展開する。
https://qiita.com/daifuku_mochi2/items/35581b05c16bc3825f7e

## 組み込みUDF（未確認）

https://docs.microsoft.com/ja-jp/azure/hdinsight/hadoop/using-json-in-hive

## 正規表現
https://support.treasuredata.com/hc/ja/articles/215030588-Hive-%E6%96%87%E5%AD%97%E5%88%97%E9%96%A2%E6%95%B0
