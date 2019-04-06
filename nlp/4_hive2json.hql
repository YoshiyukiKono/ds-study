# 4. Step 2で変換されたHiveテーブルのデータをRNNで利用するため、Json形式で出力する。
# https://codeday.me/jp/qa/20190211/256058.html
# https://github.com/klout/brickhouse

ad jar hdfs:/temp/brickhouse-<version number>.jar

SELECT to_json( named_struct( "field1", field1 ,
            "field2", field2,
            "field3", field3 ) )
   FROM mytable;
