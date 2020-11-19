# Convolution
## Notation
- input shape: $n_h\times n_w$
- convolution kernel shape: $k_h \times k_w$
- padding shape: $p_h\times p_w$
- stride stap: $s_h\times s_w$
## Padding
In many cases, we will want to set  $𝑝_ℎ=𝑘_ℎ−1$  and  $𝑝_𝑤=𝑘_𝑤−1$  to give the input and output the same height and width. 

If $p_h$ is even, we pad $p_h/2$ rows on both sides of the height. But if $p_h$ is odd, one possibility is to pad  $\lceil 𝑝_ℎ/2 \rceil$  rows on the top of the input and  $\lfloor 𝑝_ℎ/2\rfloor$  rows on the bottom. We will pad both sides of the width in the same way.

That is why, usually, we use shape 1, 3, 5 or 7 for convolution kernel.

## Stripe
Taking stripe and padding into consideration, the output shape shape be

$$\lfloor (n_h - k_h + p_h +s_h)/s_h \rfloor \times \lfloor (n_w - k_w + p_w +s_w)/s_w \rfloor$$

If we set  $𝑝_ℎ=𝑘_ℎ−1$, $𝑝_𝑤=𝑘_𝑤−1$ and Going a step further, if the input height and width are divisible by the strides on the height and width, then the output shape will be $(n_h/s_h) \times (n_w/s_w)$

## Conclusion
Padding make output shape bigger and stripe make output shape smaller.

By default, $p_h=p_w=0$ and $s_h=s_w=1$.

## Reference
- [Padding and Stride](https://d2l.ai/chapter_convolutional-neural-networks/padding-and-strides.html)
