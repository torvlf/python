import pandas as pd
import matplotlib.pyplot as plt

filename = 'pusanHospitalExcel.csv'
myframe = pd.read_csv(filename, encoding='utf-8')

# pandas에서 String type은 object라고 한다
# print(myframe.info())
# print('-'*30)

# describe() : 숫자인 컬럼만 통계 수치를 보여준다.(옵션을 설정하면 그외 컬럼들도 할 수 있다)
print(myframe.describe())
print('-'*30)

# 컬럼 정보 확인
# print(myframe.columns)
# print('-'*30)

# instit_kind 종류 확인
# print(myframe['instit_kind'].unique())
# print('-'*30)

mygrouping = myframe.groupby(['instit_kind'])['instit_kind']

# print(type(mygrouping))
# print('-'*30)

chartdata = mygrouping.count()

# print(type(chartdata))
# print(chartdata)
# print('-'*30)

# 종류의 수가 1000보다 큰 것
newdata = chartdata[chartdata > 1000]
print(newdata)
print('-'*30)

plt.rcParams['font.family'] = 'NanumGothic'

plt.figure(figsize=(10,10))

newdata.plot(kind='pie', legend=True, autopct='%6.3f%%')

savefilename = 'getHospitalInfo01.png'
plt.savefig(savefilename, dpi=400)
print(savefilename + '파일 저장 완료')

mycolor = ['r', 'g', 'b', 'm']
plt.figure(figsize=(10,10))

newdata.plot(kind='bar', legend=False, title='부산 지역 병의원 현황 top 4', color=mycolor, rot=0)

savefilename = 'getHospitalInfo02.png'
plt.savefig(savefilename, dpi=400)
print(savefilename + '파일 저장 완료')