# Resource

## Loughran and McDonald sentiment word lists
https://sraf.nd.edu/textual-analysis/resources/

https://drive.google.com/file/d/15UPaF2xJLSVz8DYuphierz67trCxFLcl/view

## Library

### Quantopian
https://en.wikipedia.org/wiki/Quantopian
Quantopian is a Boston-based company that aims to create a crowd-sourced hedge fund by letting freelance quantitative analysts develop, test, and use trading algorithms to buy and sell securities.[2][3][4]. Its primary competitors are other open source trading platforms mainly Numerai, QuantConnect, & WorldQuant.

### Alphalens
https://github.com/quantopian/alphalens
Alphalens is a Python Library for performance analysis of predictive (alpha) stock factors. 
Alphalens works great with the Zipline open source backtesting library, and Pyfolio which provides performance and risk analysis of financial portfolios.

The main function of Alphalens is to surface the most relevant statistics and plots about an alpha factor, including:

- Returns Analysis
- Information Coefficient Analysis
- Turnover Analysis
- Grouped Analysis

###  Pyfolio
https://github.com/quantopian/pyfolio
pyfolio is a Python library for performance and risk analysis of financial portfolios developed by Quantopian Inc. It works well with the Zipline open source backtesting library.

At the core of pyfolio is a so-called tear sheet that consists of various individual plots that provide a comprehensive image of the performance of a trading algorithm.

## Zipline
https://www.zipline.io/
Zipline is a Pythonic algorithmic trading library. 
It is an event-driven system for backtesting. 
Zipline is currently used in production as the backtesting and live-trading engine powering Quantopian – a free, 
community-centered, hosted platform for building and executing trading strategies.

## Turnover Analysis
Without doing a full and formal backtest, we can analyze how stable the alphas are over time. 
Stability in this sense means that from period to period, the alpha ranks do not change much. 
Since trading is costly, we always prefer, all other things being equal, that the ranks do not change significantly per period. 
We can measure this with the Factor Rank Autocorrelation (FRA).




## シャープ・レシオ （シャープ・レシオ） 
リスク（標準偏差）1単位当たりの超過リターン（リスクゼロでも得られるリターンを上回った超過収益）を測るもので、
この数値が高いほどリスクを取ったことによって得られた超過リターンが高いこと（効率よく収益が得られたこと）を意味します。

The last analysis we'll do on the factors will be sharpe ratio. 
Let's see what the sharpe ratio for the factors are. Generally, 
a Sharpe Ratio of near 1.0 or higher is an acceptable single alpha for this universe

```
negative       0.39000000
positive       4.17000000
uncertainty    3.05000000
litigious      1.97000000
constraining   1.92000000
interesting    3.49000000
```
超過リターンを標準偏差（＝リスク）で調整したもの。同じリスクを取るなら、シャープレシオの高い方がリターンが高い（効率的収益）

ベータは、ヒストリカルデータにより求められる。CAPM（＝無リスクリターン）に対する個別銘柄の特徴

アルファは、予測的。業種や、個別銘柄の特徴から得られる。
