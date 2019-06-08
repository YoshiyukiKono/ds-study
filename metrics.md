# Classification Performance Metrics

https://becominghuman.ai/understand-classification-performance-metrics-cad56f2da3aa


## Accuracy 正解率

正解率（Accuracy）=（TP+TN）／（TP+FP+TN+FN）
TP（True Positive）とTN（True Negative）を足して、全部の合計で割ったもの

## Precision/Recall

ソフトウェア・テストとの類比の比喩

### Precision 適合率・精度

精度（Precision）＝TP／（TP+FP）

陽性であると予測したサンプルのうち、実際に陽性であるサンプルの割合

### Recall 検出率 / Sensitivity 感度・再現率 / Hit Rate ヒット率

真陽性率（True Positive Rate）＝TP／（TP+FN）

実際に陽性であるサンプルのうち、陽性であると判定されたサンプルの割合

### Specificity 特異度

TN/(TN+FP)
真陰性率（True Negative Rate）＝TN／（FP+TN）
実際に陰性であるサンプルのうち、陰性であると判定されたサンプルの割合。

## F1-Score / F-measure (F値)

F値は、２集団の母平均の比較（TODO）

調和平均
https://qiita.com/conjugate_box/items/e568909df734cf0b200d

```
F_1 = 2 / (1/precision + 1/recall) = 2 * (precision * recall) / (precision + recall) = TP / {TP + (FN + FP)/2}
```
F値は、適合率を再現率が同じように高い分類器を高く評価するが、いつもそれが望ましいわけではない。

## Confusion Matrix


|予測されたクラス|Positive|Negative|
|--|--|--|
|実際のクラス|||
|Positive|TP|FN|
|Negative|FP|TN|

## 適合率が高いことが望ましいケース
* スパムメールの判定では、False Positive(偽陽性)が低いことが目指される（非スパムをスパムと判定することは問題だが、スパムをスパムと判定できなくても影響は低い）。

* 他の例：子供に見せても安全なビデオを選ぶ。多くのよいビデオを排除（再現率が低い）しても、安全なビデオだけを選ぶ（適合率が高い）分類機の方が、再現率が高くても、少数の非常に危険がビデオが入り込む分類機よりも良い。

## 再現率が高いことが望ましいケース
* 医療判定（血液検査）では、False Negative（偽陰性）が低いことが目指される（実在している症状を見逃すことは問題だが、実在しない症状をPositiveと判定しても影響は低い）。

* 他の例：監視ビデオから万引き犯を検知する。再現率が99%あれば、適合率が30%しかなくても、警備員は偽陽性のアラートを受けるが、ほとんどすべての万引き犯を捕まえられる。

## 多クラス分類の平均の取り方
### Micro-average マイクロ平均
### Macro-average マクロ平均

## 分類モデル比較
### ROC curve
### AUC (Area Under the Curve) Score

## Log-Loss

ロス値が高い：モデル構築の方向性が間違っている（要確認）

