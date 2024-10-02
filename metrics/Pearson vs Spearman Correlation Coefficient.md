### ピアソンとスピアマンの相関係数 (Pearson vs Spearman Correlation Coefficient)

1. **ピアソンの相関係数 (Pearson Correlation Coefficient)**  
   - **概要 (Overview):**  
     2つの変数間の**線形関係 (linear relationship)** を測る指標。-1から1の範囲で、1に近いほど強い正の相関、-1に近いほど強い負の相関、0は相関がないことを示す。  
   - **特徴 (Features):**  
     - 前提として、データは**正規分布 (normally distributed)** している必要がある。
     - 変数の関係は線形である必要がある。
     - **数式 (Formula):**  
       \[ r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}} \]

2. **スピアマンの順位相関係数 (Spearman's Rank Correlation Coefficient)**  
   - **概要 (Overview):**  
     2つの変数間の**単調関係 (monotonic relationship)** を測る指標。データの順位に基づいて相関を計算し、ピアソンのように-1から1の範囲で結果が得られる。  
   - **特徴 (Features):**  
     - データが**正規分布していなくても**使用可能。
     - **線形でない関係 (non-linear relationship)** でも、単調であれば適用可能。
     - **数式 (Formula):**  
       \[ r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)} \]  
       ここで、\( d_i \) は順位の差、\( n \) はデータの数。

### 違い (Key Differences):
- **線形 vs 単調 (Linear vs Monotonic):**  
  ピアソンは線形関係を測定、スピアマンは単調な関係を測定。
- **データの前提 (Data Assumptions):**  
  ピアソンは正規分布を前提とするが、スピアマンは非正規分布のデータにも対応可能。
