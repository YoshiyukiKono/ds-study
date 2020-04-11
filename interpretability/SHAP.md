# SHAP（SHapley Additive exPlanations）

https://horomary.hatenablog.com/entry/2019/09/16/000110

SHAPは協力ゲーム理論におけるShapley値を利用して各説明変数の寄与を説明しようとするアプローチです。

シャープレイ値 は 協力ゲーム において”報酬（payout）”を各プレイヤーに対して公平に分配するためのアイデアです。
SHAPツールにおいては”報酬”とはモデルの予測値であり”プレイヤー”とは各特徴量にあたります。 
すなわち各特徴量に分配された報酬の大きさ＝寄与の大きさと考えるわけです。

背景理論の詳細: ”5.9 Shapley Values”および”5.10 SHAP (SHapley Additive exPlanations)”を参照

https://christophm.github.io/interpretable-ml-book/shapley.html


しかし、SHAPツールのpython実装ではjava scriptによるjupyter notebook上でのインタラクティブな操作を可能にしている
より完成度の高いモデル解釈ツールとなっています。

SHAPツールでは”特定のサンプルについての予測の解釈”を複数のサンプルについてそれぞれ行った結果をまとめてプロットできる
