# Recommenders

Latent factor: User-Item Matrix と User-X Matrix Item-X Matrixの間の潜在的要因を仲介する

## ALS Recommenders

ALS(alternating least square)

## Model
Matrix Factorization Model

### Hyperparameters
- Rank: determines the complexity of a latent factor ALS model
- Lambda: used to prevent overfitting
- Alpha: used in trainimplicit method

### Metrics
- RMSE(Root Mean Square Error): 観測値と予測値の差。近づけば小さくなる。値そのものを対象とするため、Recomenderには向かない。（RecommenderはImplicit間接的Dataを用いるので、値そのものに意味はない〜値間の順序に意味がある）
- AUC: Area under the curve (Good model: > 0.9)
-- ROC Curve: Receiver Operating Characteristic





### Weighting
