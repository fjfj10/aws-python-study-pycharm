import pandas as pd
import numpy as np

#############################################[Series]################################################################
a = pd.Series({"a":1, "b":2, "c":3})

print(a)
# a의 인덱스는 key 값
print(a.index)

# a = np.arange(1, 5)
# np는 계산을 위한것 따라서 문자열로 넣으면 Object로 잡힘
# a = np.array(["a", "b", "c"])
a = np.array([1,2,3,4])
b = pd.Series(a)

print(b)
# 인덱스는 range로 나타남
print(b.index)
# index의 값만 들고와 보여준다
print(b.index.values)

#############################################[DataFrame]################################################################

a = {"a":[1,2,3,0], "b":[4,5,6,0], "c":[7,8,9,0], "d":[10,11,12,0]}
b = pd.Series(a)
c = pd.DataFrame(a, index=a.keys())
# Series는 key [value]로 나온다 index만 있다
print(b)
# DataFrame는 인덱스와 키의 행렬로 보여준다 index를 지정할거면 수를 맞춰야함 or 오류남
print(c)

print(c.index.values)
# DataFrame는 index와 column이 있다
print(c.columns)

a = pd.DataFrame({"a":(1,2,3), "b":1, "c":3})
# 부족한 부분은 이전 값을 복사하여 채워넣는다
print(a)
# 배열을 생성 후 인덱스와 칼럼을 바꿀 수 있다
a.index=["x", "y", "z"]
a.columns=["i", "j", "k"]
print(a)

# loc = location : key 값으로 찾는다
# iloc = index_location : index(번호=변경하기 전 가지는 번호)를 가지고 찾는다
print(a.loc["x"])
print(a.loc[a["j"] == 1])
print(a.iloc[2])

a = {"a":[1,2,3], "b":[4,5,6], "c":[7,8,9], "d":[10,11,12]}
b = pd.DataFrame(a)
print(b.describe())
print("------------------------")
# 결과는 Series 형태로 보여줌
# sum은 기본 열별로 합함
print(b.sum())
# axis는 행별로 합함
print(b.sum(axis=1))
print(b.min())
print(b.max())
# 평균
print(b.mean())
# 표준편차, 분산
print(b.std(), b.var())