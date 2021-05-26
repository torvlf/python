import pandas as pd
from pandas import DataFrame

myencoding = 'utf-8'
chickenList = ['pelicana','nene','cheogajip','goobne']

# chickenList = ['pelicana']

newframe = DataFrame()

for onestore in chickenList:
    filename = onestore + '.csv'
    myframe = pd.read_csv(filename, index_col=0, encoding=myencoding)
    # 맨 앞에 5개만 출력할 때 .head()를 붙혀주면 된다.
    # print(myframe.head())
    # print('-'*30)

    newframe = pd.concat([newframe, myframe], axis=0, ignore_index=True)

print(newframe.info())

totalfile = 'allstore.csv'
newframe.to_csv(totalfile, encoding=myencoding)
print(totalfile + '파일이 저장됨')
