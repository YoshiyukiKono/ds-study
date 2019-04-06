# Step 2: 保存したtwitsのフォーマットを変更する。
#
# https://dev.classmethod.jp/cloud/aws/java-emr-run-hive-script/

DROP TABLE IF EXISTS twits_input;

CREATE EXTERNAL TABLE twits_input
(
    messages <ARRAY<STRUCT ticker ARRAY, sentiments ARRAY, BODY>>
)
ROW SERDE ...
LOCATION '${INPUT}';

DROP TABLE IF EXISTS twits_output;
 
CREATE EXTERNAL TABLE twits_output
(
    ticker string,
    sentiment string,
    body string
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION '${OUTPUT}';
 
FROM twits_input input
INSERT OVERWRITE TABLE twits_output
SELECT
input.yyyy,
input.mm,
input.dd,
input.remarks
WHERE input.yyyy = ${YYYY}
AND input.mm = ${MM}
exprode...;

# LATERAL VIEW EXPRODE
# Hiveで配列で保存されたカラムを展開して集計する
# https://qiita.com/eccyan/items/c0158bffcbdd04b9a5b9


