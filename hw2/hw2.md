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

* Let $T_i\geq 0$ be the r.v. representing the number of iterations an element $x_i$ stays in the sample, that is the ``lifetime'' of $x_i$ in the sample:
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


