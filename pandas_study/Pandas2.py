import pandas as pd
import numpy as np

##########################[CSV 파일 불러오기]##########################
# pandas에서 불러올 때 기본 UTF-8, encoding이 안맞으면 오류남
data = pd.read_csv("books_data.csv", encoding="euc-kr")
print(data)
print(data.columns)
print(data.loc[data["도서명"] == "퇴사 후 독립출판 책 만들기"])

import csv
# 데이터를 배열 형태로 가지고 옴
f = open("books_data.csv", "r", encoding="euc-kr")
csvData = csv.reader(f)
i = 0
for data in csvData:
    if i < 10:
        print(data)
    else:
        break
    i += 1
