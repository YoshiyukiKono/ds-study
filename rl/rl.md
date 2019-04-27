# Reinforced Learning

## Foundations

### Monte Carlo Methods
### Temporal-difference Methods

## Value-Based Methods
### Q-Learning

#### ε-Greedy
（初めの内など）ランダムであることが効果的な内は、できるだけランダムにふるまう。

#### Bellman equation

#### Markov Decision Process
#### ExplorationとExploitationのバランス

#### Deep Q-network
DeepMindによる寄与（David Silver "Deep Reinforcement Learning" http://www0.ucl.ac.uk/.../deep_rl.pdf ）

* Experience Reply: 行動結果を蓄積するreplay memoryを用いる。連続するフレームは似ているため、学習結果(s, a, r, s')を一定サイズのメモリに格納
* Q-networkの固定(fixed target Q-network): ある段階で、Learning結果を固定する。
* 報酬のクリッピング: スコアを成功1、失敗-1に固定。

AlphaGoの特徴
* 価値関数(value network)と方策関数(policy network)を組み合わせている。
  * 勝率計算（モンテカルロ法）= 価値関数
  * 方策関数: 探索を行うべき手を減らし、望みが高い（＝価値が高い？）もののみ計算するために利用
* AlphaGo Zero: 教師データを使わない
  * https://deepmind.com/blog/alphago-zero-learning-scratch
* 完全ゲーム（お互いのプレイヤーがすべてのゲーム履歴を把握）


ポーカー（非完全情報ゲーム）をプレイするAI
* Librtatus
  * リスクと報酬をバランスさせる（ナッシュ均衡）
* DeepStack
  * ランダムに生成された局面を使用して強化学習（強化学習は使用していない、ともあるが）

## Policy-Based Methods
### Policy Gradient Methods
### Actor-Critic Methods

## Multi-Agent Reinforcement Learning
### Markov Game Theory

## Reference
* Deep Learning with Kearas by Antonio Gulli（日本版タイトル「直感Deep Learning」）より
 * https://github.com/oreilly-japan/deep-learning-with-keras-ja
 * https://github.com/PacktPublishing/Deep-Learning-with-Keras
