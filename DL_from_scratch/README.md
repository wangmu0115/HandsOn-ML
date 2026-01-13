
1957 年 Frank Rosenblatt 首次提出了感知机 **perceptron** 算法，是神经网络的起源算法。感知机接收多个输入信号，输出一个信号，信号的取值为 `0` 和 `1`，分别表示不传递和传递信号，下图展示了两个输入和一个输出的感知机示例，$w_1$和$w_2$是权重。

当信号综合超过某个界限值 $\theta$，称为阈值时，神经元被激活

$$
y = \begin{cases}
0,& b+w_1x_1+w_2x_2 \leqslant \theta \\
1,& b+w_1x_1+w_2x_2 > \theta
\end{cases}
$$

感知机的每个输入都对应有一个权重，权重越大对应该权重的信号就越重要。




perceptron <font color="grey">感知机</font>

$$
y = \begin{cases}
1,& b+w_1x_1+w_2x_2 > 0\\
0,& b+w_1x_1+w_2x_2 \leqslant 0
\end{cases} \tag{1}
$$


### 神经网络
