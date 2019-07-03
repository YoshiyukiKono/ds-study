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
F値は、適合率と再現率が同じように高い分類器を高く評価するが、いつもそれが望ましいわけではない。

モデル同士の性能を比較するのに使える。

* F値に関するメモ

https://qiita.com/conjugate_box/items/e568909df734cf0b200d

F値の利点は，おそらくだが，PrecisionとRecallという２つの指標を１つにまとめる所が大きい．(違うという意見もあるかもだけど，その議論は本記事の趣旨ではない)
例えば新しくモデルを提案としても，指標が2つある場合，どちらかは勝ってるけどどちらかは負けてる状況が生じうる．そこでF値は両者のスコアを用い，全体としての良さらしさを反映した何かのスカラを定義することで，モデルの優劣を議論しやすくできる．

また以下の性質により，F値は“全体としての良さらしさを反映”するのに好ましい性質を持っている．

F値は次の範囲に含まれる．

0≤F≤1

機械学習/統計モデルとしては，
- 1に近づく方がより良い精度
- 0に近づく方がより悪い精度
であることを意味し，特に予測誤り(FP+FN)が0の時に1に，真の正のラベル(TP)を全て間違えた場合に0になる．




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
複数の別々の評価の結果、TPやFPなどのレベルで合算して平均をとる

### Macro-average マクロ平均
複数の別々の評価の結果のメトリックス（適合率など）平均をとる。

クラスごとにデータの偏りがある場合は、マクロ平均を用いた方が、偏りの影響を考慮できる。

## 分類モデル比較

F値が使える。

### ROC curve

Receiver Operating Characteristic: 受信者動作特性曲線

偽陽性率に対する、真陽性率をプロットしたもの

http://kamiyacho.org/ebm/ce205.html

ＲＯＣ曲線は、スクリーニング検査等の精度の評価や従来の検査と新しい検査の比較に用いられる

どの範囲でカットオフポイント cut-off point を取るかを示すもの

カットオフポイントをどこに取るかで、ある状態にある者とない者を区別 する検査の能力を視覚的に示すことが可能となります。 
　ＲＯＣ曲線は、
 * 縦軸を真の陽性率、つまり 敏感度 、
 * 横軸を偽陽性率、つまり（１－特異度）
を尺度としてプロットしていきます。

まず、検査結果のどの値を異常、つまり所見ありと判断するかのカットオフ ポイントを決めます。
その値で陽性とされる有疾病者と非疾病者の割合より敏感度と偽陽性率を計算します。

同様にして他のカットオフポイントとした検査値での敏感度と偽陽性率を計算し、このようにして求めた値をグラフにプロットし曲線を描きます。

注意しなくてはならないのは、ここでいう偽陽性率は厳密な意味での偽陽性率（疾病がないにもかかわらず陽性となる割合）とは異なり、ＲＯＣ曲線においての定義であることです。 

このようにして描いた曲線より、どのカットオフポイントを採用するかは、 疾患の重症度や検査の位置づけ、その他種々の条件より決定されなくてはなりません。

しかし、カットオフポイントを偽陽性率の低い点（図のＡ点）にとると、 正常者で陽性となる者は減りますが、有疾病者を多く除いてしまい（つまり、敏感度が低い）、逆に敏感度を高める（図のＣ点）と偽陽性率は高くなってしまい ます。この関係を量的に求めるには一般に判別分析を用います。 

異なる検査の優劣を判定する場合は、この曲線がより左上方に位置するほど 優れていると判断します。
例えば、従来よりある検査のＲＯＣ曲線に比べて新し い検査の曲線が左上方にあれば、新しい検査はより精度が高く優れていると判断 され得るのです。

### AUC (Area Under the Curve) Score

https://oku.edu.mie-u.ac.jp/~okumura/stat/ROC.html

ROC曲線下の面積（Area under the curve，AUC）は分類器（分類のアルゴリズム）の性能の良さを表します。

0から1までの値をとり，完全な分類が可能なときの面積は1で，ランダムな分類の場合は0.5になります。

AUCの値は，TとFからランダムに1個ずつ選んだとき，Tの値がFの値以上になる確率です
（正確には，Tの値がFの値より大きくなる確率に，Tの値がFの値に等しくなる確率の半分を加えた値）。これは簡単に証明できます。

https://www.randpy.tokyo/entry/roc_auc

## Log-Loss - Logarithmic Loss

ロス値が高い：モデル構築の方向性が間違っている（要確認）

https://qiita.com/exp/items/1c6c9a3fae2d97bfa0c7

概要

分類モデルの性能を測る指標。

(このLog lossへの)入力は0~1の確率の値をとる。

この値を最小化したい。完璧なモデルではLog lossが0になる。

予測値が正解ラベルから離れるほどLog lossは増加する。

Accuracyとの違い

Accuracyは予測した値と正解が一致していた数のカウント。正解/不正解しかないのでいつも良い指標とは限らない（惜しかった、などが測れない）

### ラベルの予測との関係
Log Lossは実際のラベルからどのくらい違っていたのかを考慮できる
つまり、Log lossはモデルが間違ったラベルを、高い確信度で出力したときに、特に高くなる


一言でいうと、クロスエントロピー。0~1の予測値を入力してモデルの性能を測る指標を出力する。

## How to assess the performance of the model
https://towardsdatascience.com/the-complete-guide-to-classification-in-python-b0e34c92e455

With classification, it is sometimes irrelevant to use accuracy to assess the performance of a model.

Consider analyzing a highly imbalanced data set. For example, you are trying to determine if a transaction is fraudulent or not, but only 0.5% of your data set contains a fraudulent transaction. Then, you could predict that none of the transactions will be fraudulent, and have a 99.5% accuracy score! Of course, this is a very naive approach that does not help detect fraudulent transactions.

So what do we use?

Usually, we use sensitivity and specificity.

Sensitivity is the true positive rate: the proportions of actual positives correctly identified.

Specificity is the true negative rate: the proportion of actual negatives correctly identified.

Let’s give some context to better understand. Using the fraud detection problem, the sensitivity is the proportion of fraudulent transactions identified as fraudulent. The specificity is the proportion of non-fraudulent transactions identified as non-fraudulent.

Therefore, in an ideal situation, we want both a high sensitivity and specificity, although that might change depending on the context. For example, a bank might want to prioritize a higher sensitivity over specificity to make sure it identifies fraudulent transactions.

The ROC curve (receiver operating characteristic) is good to display the two types of error metrics described above. The overall performance of a classifier is given by the area under the ROC curve (AUC). Ideally, it should hug the upper left corner of the graph, and have an area close to 1.



