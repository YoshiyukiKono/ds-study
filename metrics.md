# Classification Performance Metrics

https://becominghuman.ai/understand-classification-performance-metrics-cad56f2da3aa


## Accuracy 正解率

## Precision/Recall

ソフトウェア・テストとの類比の比喩

### Precision 適合率

### Recall (sensitivity) 再現率

### Specificity

TN/(TN+FP)

## F1-Score / F-measure (F値)

F値は、２集団の母平均の比較（TODO）

## Confusion Matrix


||Positive|Negative|
|--|--|--|
|実際のクラス|||
|Positive|TP|FN|
|Negative|FP|TN|

* スパムメールの判定では、False Negativeが低いことが目指される（非スパムをスパムと判定することは問題だが、スパムをスパムと判定できなくても影響は低い）
* 医療における判定では、False Negativeが低いことが目指される（実在している症状を見逃すことは問題だが、実際には存在しない症状をPositiveと判定しても影響は低い）

## 多クラス分類の平均の取り方
### Micro-average マイクロ平均
### Macro-average マクロ平均

## 分類モデル比較
### ROC curve
### AUC (Area Under the Curve) Score

## Log-Loss

ロス値が高い：モデル構築の方向性が間違っている（要確認）

