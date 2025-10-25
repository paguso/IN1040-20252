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

**Simulation** [problem2.cpp](./problem2.cpp) (python is too slow)

```sh
$ g++ -O3 problem2.cpp -o problem2
$ ./problem2 <nb_of_repetitions>
```



## Problem 4

### 4.1

**Simulation:** [problem4.py](./problem4.py)

```sh
$ python3 problem4.py <nb_repetitions> <max_nb_of_people>
```

**Conjecture:** The probability of the last person taking its own jacket is 0.5.

### 4.2

Consider the scenario as described for a group of $N > 1$ people. (For $N=1$ the problem is trivial). Then let 
- jackets/people be numbered $0,\ldots, N-1$.
- $X_i\in\{0,\ldots, N-1\}$ be the r.v. representing the jacket picked by person $i=0,\ldots, N-1$
- $[X_k = j]$ denote the event "Person $k$ picked jacket $j$"

**Conjecture:** For all $N > 1$,  $\mathbb{P}[X_{N-1}=N-1] = 1/2$.

The proof is by induction on $N$.

**Base.** For $N=2$, person #1 picks its own jacket iff person #0 picks its own jacket, and $\mathbb{P}[X_0=0] = 1/2$.

**Step.** Consider $N>2$.

- By the law of total probability

$$
\begin{equation*}
\begin{split}
\mathbb{P}[X_{N-1}=N-1] &=   \mathbb{P}[X_{N-1}=N-1 \cap X_0=0] \\
&+ \mathbb{P}[X_{N-1}=N-1 \cap X_0=N-1]  \\
&+ \mathbb{P}[X_{N-1}=N-1 \cap 0 < X_0 < N-1] \\
&= \mathbb{P}[X_{N-1}=N-1 | X_0=0]\cdot \mathbb{P}[X_0=0] \qquad(case\ 0)\\
&+ \mathbb{P}[X_{N-1}=N-1 | X_0=N-1]\cdot \mathbb{P}[X_0=N-1] \qquad(case\ 1)\\
&+ \mathbb{P}[X_{N-1}=N-1 \cap 0 < X_0 < N-1] \qquad(case\ 2)
\end{split}
\end{equation*}
$$

- In case 0, if $X_0=0$ then every other person will find and pick its own jacket. Thus 
$$
\mathbb{P}[X_{N-1}=N-1 | X_0=0]\cdot \mathbb{P}[X_0=0] = 1 \cdot \frac{1}{N} = \frac1N.
$$ 
- In case 1, if $X_0=N-1$ then of course person $N-1$ cannot have its own jacket. Thus
$$
\mathbb{P}[X_{N-1}=N-1 | X_0=N-1]\cdot \mathbb{P}[X_0=N-1] = 0 \cdot \frac{1}{N} = 0.
$$ 
- In case 2, suppose $X_0=k$, for some given $k\in\{1,\ldots, N-2\}$. After that, people with numbers #$i=1,\ldots,k-1$ will necessarily each take its own jacket and leave. Then we will eventually have a situation with $N-k$ people numbered $k,k+1,\ldots,N-1$ and $N-k$ jackets numbered $0,k+1,k+2,\ldots,N-1$. This scenario is equivalent to the original setting but with a smaller number $N'=N-k$ of people, sufficing to relabel people/jackets. The fact that the first remaining jacket (#0) is not the original jacket of the first remaining person (#$k$) is irrelevant since, in this situation, he/she will pick a jacket at random, just as he/she would if the game were just starting with each person's original jackets. Thus
$$
\begin{equation*}
\begin{split}
\mathbb{P}[X_{N-1}=N-1 \cap 0 < X_0 < N-1] 
&= \sum_{k=1}^{N-2} \mathbb{P}[X_{N-1}=N-1 | X_0 = k]\cdot\mathbb{P}[X_0=k]\\
&= \sum_{k=1}^{N-2} \frac12\cdot\mathbb{P}[X_0=k] \qquad (h.i.)\\
&= \frac12 \sum_{k=1}^{N-2} \mathbb{P}[X_0=k]\\
&= \frac12 \cdot (N-2) \cdot \frac1N \\ 
&= \frac{N-2}{2N}.
\end{split}
\end{equation*}
$$

- Summarising all three cases:

$$\mathbb{P}[X_{N-1}=N-1] = \frac1N + 0 + \frac{N-2}{2N} = \frac12.$$


## Problem 5

**Assumption:** $N$ is finite and known.

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
&= \mathbb{P}[OK | A=a]\mathbb{P}[A=a] + \mathbb{P}[OK | A=b]\mathbb{P}[A=b]\\ 
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