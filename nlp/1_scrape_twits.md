https://api.stocktwits.com/developers/docs/api#streams-symbol-docs

streams/symbol
Returns the most recent 30 messages for the specified symbol. Includes symbol object in response. 

```
curl -X GET https://api.stocktwits.com/api/2/streams/symbol/AAPL.json
```

# Shell File

```
# Step 1: Twits APIからメッセージ・データを獲得・保存する。
# 1. Tickerを特定する：固定リスト
#    1. read a local file.
#    2. iterate per ticker
# 2. 各Tickerを使って、APIからデータを獲得する (curl/wget)
# 3. 獲得したデータをHDFSに保存する。(hdfs dfs -put)
```
