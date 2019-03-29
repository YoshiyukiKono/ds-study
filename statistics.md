# Statistics

## Descriptive Statistics

discrete: integer
coninuous: rate
categorical: enumerated data type or nominal(no inferent oredering)

skewness: asymmetry

tri-modal

measures of central tendency 代表値: Mean and Median

categorical variable: カテゴリ変数 - バーチャート



### Summary Staistics

### Extremal Values 極値

## Inferential Statistics 推測統計

- Dependent: output
- Independent: input parameters

whereas independent variables are the input parameters we're testing for its effect on the output.
We must account for covariants.
These are input parameters that might also affect the result, but they're not being tested,
so they must be controlled, as far as possible, to avoid interference.

Linear regression is appropriate if observations for X are independent of one another.
Logistic regression is appropriate for a binary dependent variable.

## Matrices

dot product

## R
df = data.frame(x=1:7, y=1:7)

sum(df[ df$x > 3, "y" ])

with(df, sum(x) + sum(y))


