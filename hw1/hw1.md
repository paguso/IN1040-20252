# Homework 1

## Problem 1

Let 
- $X= \{x_0,\ldots, x_{51}\}$ denote the set of 52 distinct cards
- $x_i.val \in \{A=1, 2,..., 10, J=11, Q=12, K=13\}$ denote the numeric value of the card
- $x_i.suit \in \{C, D, H, S \}$ (Clubs ♣, Diamonds ♦, Hearts ♥, Spades ♠) denote the **suit** of the card $x_i$
 

### 1.1

- The probability space $\Omega = \{ E_0, \ldots, E_{n-1} \}$ is the set of all
$n=52!$ distinct permutations of $X$. 
- Each event (permutation) has the same probability $p=1/n=1/52!$

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
- $n = 10^8$
- $T = t_0 \cdots t_{n-1}$ be the sequence of chars typed by the monkey

Define the r.v's
- $X = \text{number of occurrences of the subword ``breno'' in } T$
- The indicator variables for $j=0\ldots n-5$

$$
I_j = \begin{cases}
1,\  \text{if } T[j:j+5] = \text{``breno''} \\
0,\  \text{else}
\end{cases}
$$

Then $X = \sum_{j=0}^{n-5} I_j$ and so 

$$
\begin{equation*}
\begin{split}
\mathbb{E}[X] &= \mathbb{E}[\sum_{j=0}^{n-5} I_j] \\
&= \sum_{j=0}^{n-5} \mathbb{E}[I_j] \\
&= \sum_{j=0}^{n-5} \mathbb{P}[T[j:j+5]=\text{``breno''}] \\
&= (10^8-4)\cdot\frac{1}{26^5} \approx 8.4165
\end{split}
\end{equation*}
$$

**Simulation** [problem2.cpp](./problem2.cpp) (python is too slow)

```sh
$ g++ -O3 problem2.cpp -o problem2
$ ./problem2 <nb_of_repetitions>
```


## Problem 3

**Assumption:** queries are **uniformly** distributed among nodes.

### 3.1

Let
- Queries be numbered $q=0,\ldots, n-1$
- Machines be numbered $s=0,..., m-1$

Define the r.v.s

$$
I_{qs} = \begin{cases}
1,\ \text{if query $q$ was served by machine $s$}\\
0,\ \text{otherwise}.
\end{cases},
$$

We assume that $I_{qs}\stackrel{iid}{\sim} Bernoulli(1/m)$. 

The number of queries served by machine $s$ is 

$$X_s=\sum_{q=0}^{n-1} I_{qs}.$$

Then

$$
\mathbb{E}[X_s] = \mathbb{E}\left[\sum_{q=0}^{n-1} I_{qs}\right]
= \sum_{q=0}^{n-1}\mathbb{E}[I_{qs}]
= \sum_{q=0}^{n-1}\frac1m = \frac{n}{m}.
$$

### 3.2

---

**Theorem  (Chernoff Bound)**. Let the r.v $X=\sum_{i=0}^{n-1}X_i$ be the sum of independent Bernoulli r.v's 
$X_i\sim Bernoulli(p_i)$, for $i=0\ldots n-1$. Let $\mu = \mathbb{E}[X] = \sum_{i=0}^{n-1}p_i$. Then

$$
\mathbb{P}[X \geq (1 + \delta)\mu)] \leq \exp\left\{-\frac{\delta^2\mu}{2+\delta}\right\}
\implies \mathbb{P}[X < (1 + \delta)\mu)] > 1-\exp\left\{-\frac{\delta^2\mu}{2+\delta}\right\}
, \text{for $\delta > 0$.}
$$
---

Setting $\delta = 1/2$ and $\mu = \mathbb{E}[X_q]= n/m$, and applying the Chernoff Inequality, we have

$$
\begin{equation*}
\begin{split}
\mathbb{P}[X_q < 1.5\mu] &> 1 - \exp\left\{-\frac{\frac14}{2+\frac12}\mu\right\}\\
&= 1 - (e^{\frac nm})^{-\frac{1}{10}}
\end{split}
\end{equation*}
$$

Since $n\gg 120m\ln m$, we have

$$
\begin{equation*}
\begin{split}
\mathbb{P}[X_q < 1.5\mu] &> 
1 - (e^{\frac{120m\ln m}{m}})^{-\frac{1}{10}} \\
&= 1 - (e^{120\ln m})^{-\frac{1}{10}} \\
&= 1 - (e^{\ln m})^{-\frac{120}{10}} \\
&= 1 - m^{-12}. 
\end{split}
\end{equation*}
$$

### 3.3

We want to prove that the upper bound on the number of served queries hold for all machines simultaneously with high probability. That is
$$
\mathbb{P}[\forall q, X_q < 1.5\mu)] > 1 - m^{-c_2}
\iff \mathbb{P}[\exists q, X_q \geq 1.5\mu)] \leq m^{-c_2},
$$
for some constant $c_2$. By the union bound

$$
\begin{equation*}
\begin{split}
\mathbb{P}[\exists q, X_q \geq 1.5\mu] 
&\leq \sum_{q=0}^{m-1} \mathbb{P}[X_q \geq 1.5\mu] \\
&\leq \sum_{q=0}^{m-1} m^{-c_1} \qquad(3.2)\\
&= m\cdot m^{-c_1} = m^{-c_1+1}.
\end{split}
\end{equation*}
$$

By setting $c_2 = c_1 - 1$, we have the claim.

## Problem 4

### 4.1

**Simulation:** [problem4.py](./problem4.py)

```sh
$ python3 problem4.py <nb_repetitions> <max_nb_of_people>
```

**Conjecture:** The probability of the last person taking its own jacket is 0.5.

### 4.2

Consider the scenario as described for a group of $n > 1$ people. (For $n=1$ the problem is trivial). Then let 
- jackets/people be numbered $0,\ldots, n-1$.
- $X_i\in\{0,\ldots, n-1\}$ be the r.v. representing the jacket picked by person $i=0,\ldots, n-1$
- $[X_k = j]$ denote the event "Person $k$ picked jacket $j$"

**Conjecture:** For all $n > 1$,  $\mathbb{P}[X_{n-1}=n-1] = 1/2$.

The proof is by induction on $n$.

**Base.** For $n=2$, person #1 picks its own jacket iff person #0 picks its own jacket, and $\mathbb{P}[X_0=0] = 1/2$.

**Step.** Consider $n>2$.

- By the law of total probability

$$
\begin{equation*}
\begin{split}
\mathbb{P}[X_{n-1}=n-1] &=   \mathbb{P}[X_{n-1}=n-1 \cap X_0=0] \\
&+ \mathbb{P}[X_{n-1}=n-1 \cap X_0=n-1]  \\
&+ \mathbb{P}[X_{n-1}=n-1 \cap 0 < X_0 < n-1] \\
&= \mathbb{P}[X_{n-1}=n-1 | X_0=0]\cdot \mathbb{P}[X_0=0] \qquad(case\ 0)\\
&+ \mathbb{P}[X_{n-1}=n-1 | X_0=n-1]\cdot \mathbb{P}[X_0=n-1] \qquad(case\ 1)\\
&+ \mathbb{P}[X_{n-1}=n-1 \cap 0 < X_0 < n-1] \qquad(case\ 2)
\end{split}
\end{equation*}
$$

- In case 0, if $X_0=0$ then every other person will find and pick its own jacket. Thus 

$$
\mathbb{P}[X_{n-1}=n-1 | X_0=0]\cdot \mathbb{P}[X_0=0] = 1 \cdot \frac{1}{n} = \frac1n.
$$ 
- In case 1, if $X_0=n-1$ then of course person $n-1$ cannot have its own jacket. Thus

$$
\mathbb{P}[X_{n-1}=n-1 | X_0=n-1]\cdot \mathbb{P}[X_0=n-1] = 0 \cdot \frac{1}{n} = 0.
$$ 
- In case 2, suppose $X_0=k$, for some given $k\in\{1,\ldots, n-2\}$. After that, people with numbers #$i=1,\ldots,k-1$ will necessarily each take its own jacket and leave. Then we will eventually have a situation with $n-k$ people numbered $k,k+1,\ldots,n-1$ and $n-k$ jackets numbered $0,k+1,k+2,\ldots,n-1$. This scenario is equivalent to the original setting but with a smaller number $n'=n-k$ of people, modulo some relabelling of people/jackets. The fact that the first remaining jacket (#0) is not the original jacket of the first remaining person (#$k$) is irrelevant since, in this situation, he/she will pick a jacket at random, just as he/she would if the game were just starting with each person's original jackets. Thus

$$
\begin{equation*}
\begin{split}
\mathbb{P}[X_{n-1}=n-1 \cap 0 < X_0 < n-1] 
&= \sum_{k=1}^{n-2} \mathbb{P}[X_{n-1}=n-1 | X_0 = k]\cdot\mathbb{P}[X_0=k]\\
&= \sum_{k=1}^{n-2} \frac12\cdot\mathbb{P}[X_0=k] \qquad (i.h.)\\
&= \frac12 \sum_{k=1}^{n-2} \mathbb{P}[X_0=k]\\
&= \frac12 \cdot (n-2) \cdot \frac1n \\ 
&= \frac{n-2}{2n}.
\end{split}
\end{equation*}
$$

- Summarising all three cases:

$$\mathbb{P}[X_{n-1}=n-1] = \frac1n + 0 + \frac{n-2}{2n} = \frac12.$$


## Problem 5

**Assumption:** $n$ is finite and known.

In this case, let's say the number in the paper you picked is $A=k$. Let $B$ be the number in the other piece of paper. There are $n-1$ possibilities for $B$, of which, $k-1$ are smaller than $k$, and $n-k$ are greater than $k$. 
Thus, as a strategy, you can pick a number $T$ uniformily at random in $\{1,\ldots,k-1,k+1,\ldots,n\}$ and call:
- $A < B$ (the number you chose is the smallest), if  $T > k$; or else
- $B < A$ (the number you chose is the greatest),  if $T < k$.

You are basically simulating the choice of the other paper. 

Now, suppose Emilio had written two given numbers $a < b$. You could have chosen any of the two papers at random, that is $A=a$ or $A=b$, each with equal $0.5$ probability. The probability of the call being right is thus 

$$
\begin{equation*}
\begin{split}
\mathbb{P}[OK] &= \mathbb{P}[OK \cap A=a] + \mathbb{P}[OK \cap A=b]\\
&= \mathbb{P}[OK | A=a]\cdot\mathbb{P}[A=a] + \mathbb{P}[OK | A=b]\cdot\mathbb{P}[A=b]\\ 
&= \frac12\left( \mathbb{P}[OK | A=a] + \mathbb{P}[OK | A=b]\right) \\ 
\end{split}
\end{equation*}
$$

$\mathbb{P}[OK | A=a]$ means "the probability of being right given you had chosen the smallest of the two numbers". In this case you'd have picked $T$ uniformly at random in $1,\ldots,a-1,a+1,\ldots,n$ and you'd have guessed right only if $T>a$, which would have happened with probability $\frac{n-a}{n-1}$.
Similarly $\mathbb{P}[OK | A=b] = \frac{b-1}{n-1}$. Thus

$$
\mathbb{P}[OK]  = \frac12\left( \frac{n-a}{n-1} + \frac{b-1}{n-1}\right)
= \frac12\left( \frac{(n-1)+(b-a)}{n-1} \right) = \frac12 + \frac{b-a}{2(n-1)} > \frac12.
$$