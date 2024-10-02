# 回帰モデル性能評価指標

各評価指標は、回帰モデルの予測精度を測るために使われます。それぞれの違いを簡潔に説明します。

1. **RMSE（Root Mean Squared Error, 平均二乗誤差の平方根）**  
   - 誤差の二乗平均の平方根を取ったもの。大きな誤差を強調するため、外れ値に敏感です。  
   - 数式：\[ \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y_i})^2} \]

2. **MAE（Mean Absolute Error, 平均絶対誤差）**  
   - 誤差の絶対値の平均。外れ値にあまり影響されません。  
   - 数式：\[ \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y_i}| \]

3. **MAPE（Mean Absolute Percentage Error, 平均絶対百分率誤差）**  
   - 実測値に対する誤差の割合の平均。データが0に近いときは不安定になります。  
   - 数式：\[ \text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left|\frac{y_i - \hat{y_i}}{y_i}\right| \times 100 \]

4. **決定係数（R², Coefficient of Determination）**  
   - モデルがどれだけデータを説明できているかを示す指標。1に近いほど精度が高い。0は説明できていないことを示し、負の値はモデルが不適切であることを意味します。  
   - 数式：\[ R^2 = 1 - \frac{\sum (y_i - \hat{y_i})^2}{\sum (y_i - \bar{y})^2} \]

**違い**:  
- RMSEは大きな誤差に敏感。外れ値を除いておくことが重要
- MAEは全体的な誤差の傾向を示す。  
- MAPEは誤差を百分率で表し、相対的な精度がわかるが、0に近い値には弱い。  
- 決定係数はモデルの説明力を示すが、誤差の大きさ自体はわからない。


### 重回帰分析の評価指標 (Evaluation Metrics for Multiple Regression)

1. **決定係数 (R², Coefficient of Determination)**  
   - モデルがデータの分散をどれだけ説明しているかを示す指標。1に近いほどモデルの説明力が高い。負の値はモデルが不適切であることを意味する。

2. **調整済み決定係数 (Adjusted R², Adjusted Coefficient of Determination)**  
   - 独立変数の数に応じて調整されたR²。過剰に複雑なモデルを避けるために使われ、独立変数が増えるとR²が上昇するのを補正する。

3. **RMSE（Root Mean Squared Error, 平均二乗誤差の平方根）**  
   - 誤差の大きさを測る指標。誤差が大きいほど値が大きくなり、外れ値に敏感。

4. **MAE（Mean Absolute Error, 平均絶対誤差）**  
   - 予測値と実測値の差の絶対値の平均を取った指標。外れ値の影響をRMSEよりも受けにくい。

5. **MAPE（Mean Absolute Percentage Error, 平均絶対百分率誤差）**  
   - 予測誤差を実測値に対する割合として示したもの。値が0に近い場合に不安定になりやすい。

### その他の重要指標

6. **AIC（Akaike Information Criterion, 赤池情報量基準）**  
   - モデルの良さと複雑さをバランスよく評価する指標。値が小さいほど良いモデルとされる。

7. **BIC（Bayesian Information Criterion, ベイズ情報量基準）**  
   - AICと同様にモデルの良さを評価するが、BICはモデルの複雑さに対してより厳しいペナルティを与える。
   - 
