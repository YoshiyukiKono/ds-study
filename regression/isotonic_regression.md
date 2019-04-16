# Isotonic Regression

http://kasuya.ecology1.org/stats/isoreg1.html

isotonic回帰（isotonic regression）は、日本語では等調回帰とでもなるのだろう。k個の処理があるとき、
g1≦g2≦g3≦g4…（5以降省略、少なくとも一箇所では厳密な不等号が成り立つ）という制約のもとで、

ni（yi-gi）^2の合計

を最小化するgiの組をisotonic回帰という。ただし、yiはi番目の処理の目的変数の平均、niはi番目の処理のサンプル数である。
isotonic回帰は処理の数（ここではk個）だけの係数giの組である。

処理の順番に意味がなくて順番を入れ替えてもいいのなら（順序制約がない場合）、
isotonic回帰を考えてもあまり意味はないから、
処理を名義尺度と考えているあるいは傾向性仮説を考えている場合向けということになる。
