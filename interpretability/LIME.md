# LIME (local interpretable model-agnostic explanations)

https://horomary.hatenablog.com/entry/2019/09/16/000110

アンサンブル木や深層ニューラルネットといった複雑なモデルを、より単純な解釈しやすいモデルである線形回帰で近似するというアプローチで解釈性の向上を目指す。

しかし、モデル全体を線形回帰で近似するというのは無理なので（可能ならそもそも複雑なモデルを使用する必要がない）、
対象とするサンプルの周囲のデータ空間からサンプリングと予測を繰り返し行うことで得られるデータセットを教師データとして線形回帰モデルを作成します。

対象サンプルの周囲のデータ空間でのみ有効な線形回帰モデルを獲得するゆえにLocal surrogate model (局所的な代理モデル) アプローチと言われます。

GitHub - marcotcr/lime: Lime: Explaining the predictions of any machine learning classifier

https://github.com/marcotcr/lime

LIMEまとめ：

正直なところモデルを解釈できるほどの情報量は得られません。

このツールの使い方としては、あまりにも予測がうまくいかないサンプルがあったときに適用してみるくらいのデバック的な使い方がよいと思います。
