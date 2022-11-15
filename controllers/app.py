
import sys
import os
os.system('py -m pip install --upgrade pip')
os.system('py -m pip install pandas')
os.system('py -m pip install openpyxl')
import pandas as pd
import numpy as np
from statistics import mode
io = sys.argv[1]
sheets = ["Khánh", "Vĩ", "Đăng", "Nhi"]  # lấy 4 sheet nè
n_rows = 2000  # lấy 2000 hàng
use_cols = "A:G"  # lấy cột từ A đến GG
df = pd.read_excel(io, sheet_name=sheets, nrows=n_rows, usecols=use_cols)
cols = df[sheets[0]].columns
print(cols[0])
# for sheet in sheets:
#     df[sheet] = df[sheet].replace(to_replace = np.nan, value =0) # những nhãn chưa được gán sẽ mặc định bằng 0
# def most_common(List):
#     return (mode(List))
# def create_col_most_common(df, col, n_rows, sheets):
#     colResult = []
#     colLabelDetails = []
#     for i in range(n_rows):
#         label_details = [sheet + ": " + str(df[sheet][col][i]) for sheet in sheets]
#         colLabelDetails.append(label_details)
#         try:
#           tmp = most_common([int(df[sheet][col][i]) for sheet in sheets])
#         except:
#           tmp = set([df[sheet][col][i] for sheet in sheets]) # nếu không xác định được nhãn chung thì gắn các nhãn xuất hiện nhiều nhất
#         colResult.append(tmp)
#         #print("col:", col,"index:",i-2 , [int(df[sheet][col][i]) for sheet in sheets], "common:", tmp)
#     return colResult, colLabelDetails
# arr = []
# colResult = []
# colLabelDetails = []
# arr.append([text for text in df[sheets[0]][cols[0]]])
# for col in cols[1:]:
#     colResult, colLabelDetails = create_col_most_common(df, col, n_rows, sheets)
#     arr.append(colResult)
#     arr.append(colLabelDetails)
# columns = [col for col in cols for i in range(2)][1:]
# pd.DataFrame(arr, index = columns).T.to_excel("C:/Users/vohuy/Desktop/testapi2.xlsx")
