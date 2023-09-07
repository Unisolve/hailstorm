# Scaling attention

## Our summary

The quality of attention degrades when the token size gets beyond 8K. This paper
introduces LongNet, a proposal to scale transformers to 1,000,000,000 tokens.
The core of LONGNET is dilated attention, which reduces the computation complexity 
from quadratic to linear.

## URL

https://arxiv.org/pdf/2307.02486.pdf

## Primary Organsation

Microsoft

## Authors' abstract

Scaling sequence length has become a critical demand in the era of large language
models. However, existing methods struggle with either computational complexity
or model expressivity, rendering the maximum sequence length restricted. To
address this issue, we introduce LONGNET, a Transformer variant that can scale
sequence length to more than 1 billion tokens, without sacrificing the performance
on shorter sequences. Specifically, we propose dilated attention, which expands
the attentive field exponentially as the distance grows. LONGNET has significant
advantages: 1) it has a linear computation complexity and a logarithm depen-
dency between any two tokens in a sequence; 2) it can be served as a distributed
trainer for extremely long sequences; 3) its dilated attention is a drop-in replace-
ment for standard attention, which can be seamlessly integrated with the existing
Transformer-based optimization. Experiments results demonstrate that LONGNET
yields strong performance on both long-sequence modeling and general language
tasks. Our work opens up new possibilities for modeling very long sequences, e.g.,
treating a whole corpus or even the entire Internet as a sequence. Code is available
at https://aka.ms/LongNet.
