import matplotlib.pyplot as plt

# 输入与输出数据集
input_value = range(1, 6)
squares = [i ** 2 for i in range(1, 6)]

# 设置样式，生成图表
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_value, squares, linewidth=3)

# set title and axis label
ax.set_title('squares', fontsize=24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('squares of value', fontsize=14)

# set tick刻度
ax.tick_params(axis="both", labelsize=14)

plt.show()
