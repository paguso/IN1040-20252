# Homework 1

## Problem 1

Let 
- $X= \{x_0,\ldots, x_{51}\}$ denote the set of 52 distinct cards
- $x_i.val \in \{A=1, 2,..., 10, J=11, Q=12, K=13\}$ denote the numeric value of the card
- $x_i.suit \in \{C, D, H, S \}$ (Clubs ♣, Diamonds ♦, Hearts ♥, Spades ♠) denote the **suit** of the card $x_i$
 

### 1.1

- The probability space $\Omega = \{ E_0, \ldots, E_{N-1} \}$ is the set of all
$N=52!$ distinct permutations of $X$. 
- Each event (permutation) has the same probability $P=1/N=1/52!$

### 1.2

#### 1.2.a)

- Let $Y=(y_0, \ldots, y_{51})\in\Omega$ be a random permutation of $X$.
- There are 13 diamond cards among the 52 distinct cards, thus
- You can choose 13 among the 52 cards for the first position, then 12 among the remaining 51 for the second position, then 11 among the remaining 50 for the third position

$$
\begin{align*}
\mathbb{P}[y_0.suit = y_1.suit = y_2.suit = D] &= \mathbb{P}[\cap_{j=0}^3\  y_j.suit = D] \\
&= \frac{13}{52} \cdot \frac{12}{51} \cdot \frac{11}{50} \approx 0.0129\\
\end{align*}
$$


#### 1.2.b)

- There are 4 Aces and 48 non-aces cards. Thus

$$
\begin{align*}
\mathbb{P}[\cup_{j=0}^5\  y_j.val = A] 
&= 1-\mathbb{P}[\overline{\cup_{j=0}^5\  y_j.val = A}] \\
&= 1-\mathbb{P}[\cap_{j=0}^5\  y_j.val \neq A] \\
&= 1-(\frac{48}{52}\cdot\frac{47}{51}\cdot\frac{46}{50}\cdot\frac{45}{49}\cdot\frac{44}{48}) \approx 0.3412 
\end{align*}
$$

### 1.3

See [problem1.py](./problem1.py).

Usage:

```sh
$ python3 problem1.py <nb_of_repetitions>
```


## Problem 2

Let 
- $N = 10^8$
- $T = t_0 \cdots t_{N-1}$ be the sequence of chars typed by the monkey

Define the r.v's
- $X = \text{number of occurrences of the subword ``breno'' in } T$
- The indicator variables for $j=0\ldots N-5$
$$
I_j = \begin{cases}
1,\  \text{if } T[j:j+5] = \text{``breno''} \\
0,\  \text{else}
\end{cases}
$$

Then $X = \sum_{j=0}^{N-5} I_j$ and so 
$$
\begin{equation*}
\begin{split}
\mathbb{E}[X] &= \mathbb{E}[\sum_{j=0}^{N-5} I_j] \\
&= \sum_{j=0}^{N-5} \mathbb{E}[I_j] \\
&= \sum_{j=0}^{N-5} \mathbb{P}[T[j:j+5]=\text{``breno''}] \\
&= (10^8-4)\cdot\frac{1}{26^5} \approx 8.4165
\end{split}
\end{equation*}
$$

**Simulation** [problem2.cpp](./problem2.cpp)

```sh
$ g++ -O3 problem2.cpp -o problem2
$ ./problem2 <nb_of_repetitions>
```
