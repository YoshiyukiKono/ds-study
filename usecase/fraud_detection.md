# Fraud Detection

## References

- Credit Card Fraud Detection using Autoencoders in Keras — TensorFlow for Hackers (Part VII)
   - https://medium.com/@curiousily/credit-card-fraud-detection-using-autoencoders-in-keras-tensorflow-for-hackers-part-vii-20e0c85301bd?source=search_post---------0
- Fraud Detection Under Extreme Class Imbalance
   - https://towardsdatascience.com/fraud-detection-under-extreme-class-imbalance-c241854e60c?source=search_post---------1
   
- How to Perform Fraud Detection with Personalized Page Rank
   - https://medium.com/sicara/fraud-detection-personalized-page-rank-networkx-15bd52ba2bf6
- Fraud Detection Systems — A Second look
   - https://medium.com/@deepeshn1988/fraud-detection-systems-a-second-look-a8f705624783
   
### ATM Fraud Detection with Kafka & KSQL ~ Stream Processing using Apache Kafka, KSQL & ElasticSearch 

https://medium.com/@deepeshn1988/fraud-detection-systems-a-second-look-a8f705624783

- ATMトランザクションのリアルタイム・ストリーミング・データから、不正に見えるトランザクションを検出する
- トランザクションが不正と思われるかどうかを判断するには、3つの重要な要素を使用します。
   - 前の取引と同じ口座番号…
   - …しかし、別の場所で
   - …前のものから10分以内

- 口座番号の連続する複数件のデータを入力とすることによって、正常と異常を区別できる可能性がある。
   - 場所（これには距離を測る方法が必要）
   - 時間（）
   - 購入品目（）
   - 購入平均
   - 上記の組み合わせ
- 口座番号以外のカットで、トランザクションをグループ化することも考えられる。

- KSQLによるリアルタイム処理

- アイディア
   - 過去のデータをつねにPCAなどで次元削減
   - RNNにより時系列の

### Healthcare Fraud Detection With Python

https://medium.com/better-programming/healthcare-fraud-detection-with-python-5a7a6738b5b2

- EDA(Explanatory Data Analysis 探索的データ解析)の重要性

### Patent Update: adbank’s AI ad fraud detection system

https://medium.com/adbank-blog/patent-update-adbanks-ai-ad-fraud-detection-system-c991b033e648

- 広告詐欺

### How to Choose Fraud Detection Software: Features, Characteristics, Key Providers

https://medium.com/gobeyond-ai/how-to-choose-fraud-detection-software-features-characteristics-key-providers-e7c12a90de9a

- False Positive 誤検知

- Gartner Groupの詐欺アナリストAvivah Litan による、詐欺の検出と防止に対する5層アプローチ。各レベルは、特定のタイプの顧客アクティビティと行動を表す。
   - レベル1: エンドポイント中心、ユーザー認証、トランザクションに使用しているデバイス、および位置情報。
   - レベル2: ナビゲーション中心。つまり、特定のセッション中の顧客の行動の異常を分析。
   - レベル3: チャネル中心、異常のアカウントアクティビティの分析を検討。
   - レベル4: 製品間、チャネル間、チャネルおよび銀行製品全体のエンティティの動作を監視。
   - レベル5: エンティティリンク分析 —さまざまなユーザーまたはトランザクション間の接続の評価。
 
 !(https://miro.medium.com/max/2562/0*JNjMwuc-0G1i35Jb.png)
 
 https://www.sas.com/content/dam/SAS/en_us/doc/whitepaper1/layered-approach-fraud-detection-prevention-106072.pdf
 
 - SAS不正防止ソリューション
    - エキスパートルール、数学モデル、対象の社会的設定の分析、テキスト分析、異常分析、その他の方法を組み合わせたハイブリッドアプローチ
 
- ソリューションは、チャネル全体の不正を識別して防止し、数百から数千の属性（ユーザーアクティビティ、デバイスデータ、または地理位置情報など）を使用
- 一般およびドメイン固有のブラックリストを選別してすべてのトランザクションをスコアリングできる必要がある。

### Reducing false positives in credit card fraud detection
https://www.sciencedaily.com/releases/2018/09/180920131513.htm

