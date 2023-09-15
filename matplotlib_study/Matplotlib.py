# 시각화 모듈
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [2,3,4,5]
plt.plot(x, y)
# plt.show()하면 이미지 보여주고 멈춤 창 닫으면 다음코드 실행
plt.show()
plt.bar(x, y)
plt.show()

# figure: 그래프의 틀
figure = plt.figure()
# add_subplot(row column index): 전체 틀 중 x축, y축을 제외한 그래프 부분
axes = figure.add_subplot(111)

x2 = np.array(x)
y2 = np.array([4,1,3,6])

axes.plot(x,y, color="red", linestyle="dashed", marker="^")
axes.plot(x2,y2, color="k", linestyle="dotted", marker="o")
plt.show()

x3 = np.array([5,6,7,8])
y3 = np.array([5,6,7,8])

x4 = np.array([1,2,3,4])
y4 = np.array([3,8,1,9])

figure = plt.figure()
axes1 = figure.add_subplot(221) #2행 2열에서 1번
axes1.plot(x, y)
axes2 = figure.add_subplot(222) #2행 2열에서 2번
axes2.plot(x2, y2)
axes3 = figure.add_subplot(223)
axes3.plot(x3, y3)
axes4 = figure.add_subplot(224)
axes4.plot(x4, y4)
plt.show()

figure = plt.figure()
axes = figure.add_subplot(111)
# 중첩 그래프
axes.bar(x, y)
axes.bar(x2, y2)
plt.show()

figure = plt.figure()
axes1 = figure.add_subplot(111)
axes2 = axes1.twinx()
axes1.bar(x, y, color="blue", label="bar")
axes2.plot(x2, y2, color="red", label="plot")
plt.show()