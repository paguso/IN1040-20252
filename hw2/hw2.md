# Homework 2

## Problem 1

*Note*: the following analyses are for elements arriving after the reservoir is full, i.e. $x_i$ with $i\geq k$ (0-based indexing)

### 1.1

* Let $R_i$ denote the reservoir (array) immediately after processing element $x_i$.
* We have that $x_i\in R_{i+t}$ for $t\geq 0$ iff
    1. $x_i$ is stored in some position $j$ of the reservoir, i.e. $R_i[j]=x_i$; and
    2. For all $q=1\ldots t$, $x_{i+q}$ is **not** stored in position $j$, i.e. $R_{i+q}[j]\neq x_{i+q}$.

Then

1. $Pr[R_i[j] = x_i] = p \cdot \frac1k$
2. $Pr[R_{i+q}[j] \neq x_{i+q}] = 1 - Pr[R_{i+q}[j]=x_{i+q}] = (1-\frac pk)$

and thus

$$
\begin{split}
Pr[x_i\in R_{i+t}] &= Pr [\cup_{j=0}^{k-1}(x_i \text{ inserted in position } j \cap x_i \text{ not replaced by } x_{i+1}\ldots x_{i+t})]\\
&= 
\sum_{j=0}^{k-1}Pr[R_i[j] = x_i \wedge R_{i+1}[j]\neq x_{i+1} \wedge \ldots \wedge R_{i+t}[j]\neq x_{i+t} ]\\
&= 
k \cdot \frac pk \cdot\left( 1 - \frac pk\right) ^t\\
&= 
p\left( 1 - \frac pk\right) ^t.
\end{split}
$$


### 1.2

* Let $T_i\geq 0$ be the r.v. representing the number of iterations an element $x_i$ stays in the sample, that is the **"lifetime"** of $x_i$ in the sample:
    * $T_i=0$ means that $x_i$ is not kept. Thus $Pr[T_i=0]=(1-p)$;
    * $T_i=1$ means that $x_i$ is inserted but already removed by $x_{i+1}$;
    * etc

* The probability of $x_i$ staying in the sample for exactly $t>0$ iterations is obtained similarly to 1.1 as

$$
\begin{split}
Pr[T_i = t] &= Pr [\cup_{j=0}^{k-1}(x_i \text{ inserted in position } j \cap x_i \text{ not replaced by } x_{i+1}\ldots x_{i+t-1} \cap x_i\text{ replaced by } x_{i+t})]\\
&= 
\sum_{j=0}^{k-1}Pr[R_i[j] = x_i \wedge R_{i+1}[j]\neq x_{i+1} \wedge \ldots \wedge R_{i+t-1}[j]\neq x_{i+t-1} \wedge R_{i+t}[j]=x_{i+t} ]\\
&= 
k \cdot \frac pk \cdot\left( 1 - \frac pk\right)^{t-1}\cdot \frac pk\\
&= 
\frac{p^2}k\left( 1 - \frac pk\right)^{t-1}.
\end{split}
$$

Thus

$$
\begin{split}
E[T_i] &= \sum_{t=0}^\infty t\Pr[T_i=t] \\
&= 
\sum_{t=1}^\infty t\Pr[T_i=t] \\
&= 
\sum_{t=1}^\infty t\cdot \frac{p^2}k\left( 1 - \frac pk\right)^{t-1} \\
&= 
\frac{p^2}{k}\sum_{t=1}^\infty t\cdot\left( 1 - \frac pk\right)^{t-1}.
\end{split}
$$

Let $c:=(1-\frac  pk)$ and consider the sum $S:=\sum_{t=1}^\infty t\cdot c^{t-1}$. 

$$
\begin{split}
S-cS &= (1c^0 + 2c + 3c^2 + \cdots) - (1c + 2c^2 + 3c^3 + \cdots) \Rightarrow \\
S(1-c) &= 1 + c + c^2 + c^3 + \cdots \Rightarrow \\
S(1-c) &= \frac{1}{1-c} \Rightarrow \\
S &= \frac{1}{(1-c)^2} = \frac{1}{(1-1+\frac pk)^2} = \frac{k^2}{p^2}.
\end{split}
$$

Therefore

$$
E[T_i] = \frac{p^2}{k}\cdot\frac{k^2}{p^2} = k.
$$

### 1.3

- The lifetime of an element will be $>T$ (for any $T\geq 0$) iff it is inserted in its iteration and kept at least by the following $T$ iterations

$$Pr[\text{lifetime }> T] = p (1-p/k)^T.$$

- The probability that any element in the reservoir has lifetime greater than $T$ is then bounded as

$$Pr[\text{ $\exists$ element older than } T] \leq \sum_{j=0}^{k-1} Pr[\text{element at position $j$ older than $T$}] = kp(1-p/k)^T.$$

- We want

$$Pr[\text{ $\exists$ element older than } T] = kp(1-p/k)^T \leq \delta.$$

- Solving for $\delta$:

$$
\begin{split}
kp(1-p/k)^T &\leq \delta \Rightarrow \\
(1-p/k)^T &\leq \delta/kp\Rightarrow \\
\log_{(1-p/k)}(1-p/k)^T &\geq \log_{(1-p/k)}(\delta/kp)\Rightarrow \qquad(0< 1-p/k <1)\\
T &\geq \log_{(1-p/k)}(\delta/kp)
\end{split}
$$

### 1.4

Not sure about what is intended. As $\delta$ gets smaller, we'd typically need $T$ to be increasingly larger than the expected lifetime $k$. Other than that, I see no obvious algebraic relation between the derived bound for $T$ and $k$, as I guess it would be desirable. Sorry :-(


## Problem 2

### Bloom Filter (BF)

- Let $BF_A$ and $BF_B$ be two BFs representing sets $A$ and $B$, respectively. Suppose both bitvectors have length $m$ and use the same $k$ hash functions.
- Let $BF_A[i]$ denote the $i$-th bit of $BF_A$.

#### 1. $A\cup B$

Let $BF_{A\cup B}$ be a BF of length $m$ using the same $k$ hash functions as $BF_A$ and $BF_B$ s.t.

$$BF_{A\cup B}[i] = BF_A[i] \lor BF_B[i].$$

By construction, the positions set in $BF_{A\cup B}$ are exactly those which are set in either $BF_A$ or $BF_B$ (or both). Thus $BF_{A\cup B}$ is exactly the same bitvector that we would obtain by inserting the elements of $A\cup B$, in any order, in a blank bitvector.

The guarantees provided by the combined BF are therefore similar to those of the original BFs, however taking into account the overall number of elements. In particular, the false positive rate of a BF is known to be $PFP(k,m,n) = (1-e^{-kn/m})^k$, where $n$ is the size (cardinality) of the represented set. 

For example, suppose $A$ and $B$ have roughly the same size $n$, and let us estimate the ratio 

$$
\varphi:=\frac{PFP(k,m,2n)}{PFP(k,m,n)} = \frac{(1-e^{-2kn/m})^k}{(1-e^{-kn/m})^k}.
$$

Let $x:=-kn/m$. We have $(1-e^{2x}) = -(e^{2x}-1) = -[(e^x + 1)(e^x - 1)]$. And thus

$$
\varphi = \left(\frac{-[(e^x+1)(e^x-1)]}{-(e^x-1)}\right )^k = (e^x+1)^k = (1 + e^{-kn/m})^k.
$$

So, had we adjusted $BF_A$ to approximately $PPF(k,m,n)=1\%$ false-positive rate, which could have been done with 10bits per element ($m=10n$) and $k=10$, the false positive rate of the combined BF would be $\varphi\approx 23$ times higher ($PFP(k,m,2n)\approx 23\%$)! This exemplifies how tricky can be the parametrization of these sketches.

#### 2. $A\cap B$

We can obtain a BF for $A\cap B$ similarly by having a bitvector of same size $m$, with the same hash functions, and setting 

$$BF_{A\cap B}[i] = BF_A[i] \wedge BF_B[i].$$

By construction, the positions set in $BF_{A\cap B}$ are exactly those which are set in both $BF_A$ and $BF_B$. However, the bitvector obtained this way is not necessarity identical to that obtained by inserting only the elements of $A\cap B$ in a blank bitvector with the same hash functions.

- Any element of $A\cap B$ will set the same bits in $BF_A$ and $BF_B$, and therefore they will all also be set in $BF_{A\cap B}$ $\implies$ true positives OK!
- All negatives of $BF_{A\cap B}$ are indeed true negatives. A false negative would be an element in $A\cap B$ whose hashed positions are not all set in $BF_{A\cap B}$, despite being all set in $BF_A$ and $BF_B$, but this contradicts the bitwise-and construction.
- However, the false positives are not necessarily the same. $BF_{A\cap B}$ can introduce new false positives compared to the BF created directly from $A\cap B$. 

An element $x$ will be a false positive in $BF_{A\cap B}$ iff $x\not\in A\cap B$ and $BF_{A\cap B}[h_q(x)]=1$ for all $q=0\ldots k-1$. Given a position $j$, we have

$$
\begin{split}
Pr[BF_{A\cap B}[j] = 1] &= Pr[BF_{A}[j] = 1 \wedge BF_B[j]=1] \\
&= Pr[BF_A[j] = 1] \cdot  Pr[BF_B[j]=1] \\
&\approx (1-e^{-ka/m})(1-e^{-kb/m}),
\end{split}
$$

where $a=|A|$ and $b=|B|$. Hence, the false-positive rate of $BF_{A\cap B}$ is given by

$$
Pr[\land_{q=0}^{k-1} BF_{A\cap B}[h_q(x)] = 1\ |\ x \not\in A\cap B]  
\approx ((1-e^{-ka/m})(1-e^{-kb/m}))^k.
$$

As before, if $a=b=n$ then the false positive rate of the merged BF would be $(1-e^{kn/m})^{2k}$, which is the square of the original false positive rate.

### Flajolet-Martin

- We assume a simple implementation in which we keep an integer $R := \max_i\{z(h(x_i))\}$, where $h(x_i)\in[2^L]$ is the $L$-bit hash value of element $x_i$, and $z(\cdot)$ denotes the number of leading (most significant) zeroes in the binary representation of its argument. Then $F_0(X)$ is estimated as $2^R$.
- Because $R\in[L]$, it takes $\lg L$ bits. Assuming the universe has size $U\leq 2^L$, this implemetation of FM takes $\Theta(\lg L) = \Theta(\lg\lg U)$ bits of space.
- Let $R_A$ be the $R$-value maintained by $FM_A$, and  likewise for $R_B$.

#### 1. $A\cup B$

Because $R$ is the max of a set and $\max(A\cup B)=\max\{\max(A), \max(B)\}$, it follows that we can merge $FM_A$ and $FM_B$ into $FM_{A\cup B}$ by having $R_{A\cup B}:=\max\{R_A, R_B\}$. This sketch is indistinguishable from the one obtained by inserting the elements in $A\cup B$ from scratch in a blank FM-sketch (with the same hash function), which would have $R=\max_{A\cup B}\{z(h(x))\}=\max\{\max_A\{z(h(x))\}, \max_B\{z(h(x))\}\}=\max\{R_A, R_B\}$. The approximation guarantees are therefore the same. Notice that, in this case, the estimate given by $FM_{A\cup B}$ will be the maximum of the two original estimates.


#### 2. $A\cap B$

The inclusion-exclusion principle purports that 

$$
|A\cup B| = |A| + |B| - |A\cap B| \implies 
|A\cap B| = |A| + |B| - |A\cup B|.
$$

It is therefore possible to estimate $F_0(A\cap B)$ from $FM_A$ and $FM_B$ (and $FM_{A\cup B}$). Following this rationale, $FM_{A\cap B}.query()$ should return $2^{R_A} + 2^{R_B} - 2^{R_{A\cup B}}$. But since $R_{A\cup B}=\max\{R_A, R_B\}$, that estimate reduces to $2^{\min\{R_A, R_B\}}$. This could suggest that a merge operation of $FM_A$ and $FM_B$ into $FM_{A\cap B}$ should be implemented by having $R_{A\cap B}:=\min\{R_A, R_B\}$.
However, this construction is limited by the amount of information that can be recovered from $R$ alone, and is not equivalente to a FM-sketch built directly from $A\cap B$, which would have $R=\max_{A\cap B}\{z(h(x))\}\neq\min\{\max_A\{z(h(x))\}, \max_B\{z(h(x))\}\}$.

A less memory-efficient implementation is more amenable to intersection-merges. Instead of keeping $R$, one can maintain a bit mask $Z$ of size $L$, initially set to 0, and on each update set 

$$
Z[z(h(x)] = 1,
$$

that is, we record in $B$ all the distinct observed values of $z(h(x))$. The estimate is then given by $2^{\max\{i | Z[i] = 1\}}$. We could then build $FM_{A\cap B}$ by having $Z_{A\cap B} = Z_{A} \& Z_B$, where $\&$ stands for bitwise-and. This way the merged sketch would be the same as that obtained by inserting the values in $A\cap B$ from scratch, albeit with slightly worse $\Theta(\lg U)$-space.


## Problem 3

Let 
- $X = x_0, x_1, x_2, \ldots, x_{n-1}$ be the stream s.t. each $x_i$ is a $m$-bit value
- $D(X)$ denote the set of distinct elements of $X$
- $F_0(X) = |D(X)|$ denote the number of distinct elements of $X$
- $x_{ij}$, for $j=0\ldots m-1$, denote the $j$-th order bit of $x_i$.
- $X_{(j)}$ denote the substream composed only of elements whose $j$-th order bit equals 1

Then the value we want is

$$
\begin{split}
S &:= \sum_{x_i\in D(X)} x_i \\
&= \sum_{x_i\in D(X)} \sum_{j=0}^{m-1}2^jx_{ij} \\
&= \sum_{j=0}^{m-1} \left(2^j \cdot \sum_{x_i\in D(X)}x_{ij}\right) \\
&= \sum_{j=0}^{m-1} \left(2^j \cdot \sum_{x_i\in D(X_{(j)})}x_{ij}\right) \\
&= \sum_{j=0}^{m-1} 2^j F_0(X_{(j)}). 
\end{split}
$$

This formula implies counting, for each bit order $j=0\ldots m-1$, the number distinct elements with the $j$-th order bit equal to 1. We can thus keep a set of $m$ $F_0$-estimators $E=(E_0,\ldots, E_{m-1})$ and update them on each new element arrival as

```
update(E, x_i):
    for j = 0 ... m-1 :
        if x_i[j] == 1 :
            update(E_j, x_i)
```

Then, according to the formula above, the query would be 

```
query(E):
    s = 0
    for j = 0 ... m-1 : 
        s = s + (2^j * query(E_j)
    return s
```


