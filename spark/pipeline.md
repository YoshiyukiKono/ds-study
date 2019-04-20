# Pipeline

raw data -> SQL -> T transformer-> SI string indexer -> 1HE hot encoder -> VA vector assembler -> processed data

Pipeline encapsulate the process/
```
filterer

extractor

indexer

encoder

assembler

classifier

grid

evaluator: MulticlassClassificationEvaluator

validator: TrainValidationSplit(estimator=classifier, parammaps=grid, evaluator=..

stages = [filterer, extractor, indexer, encoder, assembler, validator]
pipeline = Pipline(stages)

--

RFormula = (SI, 1HE, VA)

Pipeline(SQL, SQL, RFormula)


```

## RFormula
http://mogile.web.fc2.com/spark/spark202/ml-features.html
RFormula は、特徴のカラムと、doubleあるいは文字列のカラムのベクトルを生成します。
Rで線形回帰のために公式が使われるように、文字列入力カラムはone-hotエンコードされ、数値カラムはdoubleにキャストされるでしょう。
ラベルのカラムが文字の種類の場合、それはStringIndexerを使ってまず二倍に変換されるでしょう。
データフレーム中にラベルのカラムが存在しない場合は、出力ラベルのカラムは公式内の指定された応答変数から生成されるでしょう。

http://m884.hateblo.jp/entry/20091112/1259855233

http://ill-identified.hatenablog.com/entry/2017/04/30/004258

http://cse.naro.affrc.go.jp/takezawa/r-tips/r/71.html


