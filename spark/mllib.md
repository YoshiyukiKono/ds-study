# MLlib

VectorAssembler: Train DataとTest Dataにわける。
```
lr = LinearRegression
lr.explainParams()
- elasticNetParam

lr_model = lr.fit(train)

lr_model.coefficients
lr_model.interccept

y = x*coefficient + intercept

RMSE = SQRT(SUM((trueLabel - predLabel)^2)/NUM)

prediction = lr_model.transform(test)

evaluator = RegressionEvaluator(...)
evaluator.evaluate(predictions)

evaluator.setMetricName("rmse").evaluate(predictons)

pdf = predictions.sample(...)
plt.scatter(...data=pdf)
```


R2:1に近いほうがいい（大きいほうがいい）
RMSE:小さいほうがいい

dummy variable = one hot encoding: クラス（車の色）を、色毎の別のfeatureに変更する。
（Classificationのため、数値に変換する必要はあるが、計算できるものではないから）

# Area under ROC Curve　(AUC)

0.5はただのguess. 
0 は、いつも間違い
１は、いつも正解



ROC曲線(Receiver Operatorating Characteristic curve、受信者動作特性曲線)

(横軸：偽陽性率、縦軸：真陽性率）
偽陽性率（正解がクラスbのデータをクラスaと識別してしまった割合）が大きくなるように閾値を設定すれば、それはつまりクラスaに分類する判定を甘くすることを意味するため、真陽性率（正解がクラスaのデータをクラスaと識別できた割合）も自動的に上がります。つまり、このグラフは右下に下がることは決してなく、右に行くほど（偽陽性率が上がるほど）上に伸びる形をとります（真陽性率が上がる）。

極端に言えば、偽陽性率が1に近づくということは、なんでもかんでもクラスaに分類しているようなものなので、それは必然的に真陽性率も1に近づきますよね。

このようなことを考えると、良いモデルとは偽陽性率が低い時点で既に真陽性率が高い数値がでることという考えが直観的に理解できるのではと思います。

