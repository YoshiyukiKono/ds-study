# NLP

* Removing Stop words and signs (.!?...)
* Word Stemming = Lemmatizing
* Typo correction / Fuzzy matching

* Topic Model? = LDA
一緒に現れる単語をグループにする。Classification?


* Bag-of-Words
* TF-IDF
頻出～　要説明！

## n-gram

見出し語の切り出し方法:シークエンスはすべてN個の単語を持つ。

変換前
"I would like to meet you tomorrow"

変換後（n=2）
"I would", "would like", "like to"...

https://gihyo.jp/dev/serial/01/make-findspot/0006
転置インデックスを検索のためにつくる
漏れのない完全一致検索を可能にする（文字列の出現位置情報を利用）

### 形態素解析
構文解析を行ってから分かち書きを行う。

## Spark
 * CountVectorizer
