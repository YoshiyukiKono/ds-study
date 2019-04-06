# Step 1: Twits APIからメッセージ・データを獲得・保存する。
# 1. Tickerを特定する：固定リスト
#    1. read a local file.
#    2. iterate per ticker
# 2. 各Tickerを使って、APIからデータを獲得する (wget)
# 3. 獲得したデータをHDFSに保存する。(hdfs dfs -put)
