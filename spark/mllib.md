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
