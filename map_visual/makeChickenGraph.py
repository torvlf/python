import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 하나로 묶어준 csv 파일을 호출
csv_file = '../crawling/allstoreModified.csv'
myframe = pd.read_csv(csv_file, index_col=0, encoding='utf-8')
print(myframe.info())
print('-'*30)

print(myframe['brand'].unique())
print('-'*30)

# groupby()를 사용해서 brand로 그룹핑
mygrouping = myframe.groupby(['brand'])['brand']
print(type(mygrouping))
print('-'*30)

chartdata = mygrouping.count()
print(type(chartdata))
print(chartdata)
print('-'*30)

mycolor = ['r', 'g', 'b', 'm']

print(chartdata.index)
print('-'*30)

brand_dict = {'cheogajip':'처갓집', 'goobne':'굽네', 'pelicana':'페리카나', 'nene':'네네'}

# list comprehension : 리스트를 쉽게 생성하기 위한 방법
newindex = [brand_dict[idx] for idx in chartdata.index]
chartdata.index = newindex

print(chartdata.index)
print('-'*30)

[f.name for f in fm.fontManager.ttflist if 'Nanum' in f.name]

# 유니코드 깨짐현상 해결
matplotlib.rcParams['axes.unicode_minus'] = False
# 나눔고딕 폰트 적용
plt.rcParams['font.family'] = 'NanumGothic'

# 원형 그래프
# figure() : 그래프를 그리기 위한 도화지
plt.figure()
# kind : 그래프 종류, legend : 범례, autopct : 보여줄 소숫점 자리
chartdata.plot(kind='pie', legend=False, title='브랜드별 총 매장 갯수', autopct='%1.2f%%', colors=mycolor)

filename = 'makeChickenGraph01.png'
plt.savefig(filename, dpi=400)
print(filename + '파일이 저장되었습니다.')


# 수평 그래프
plt.figure()
# title : 그래프 제목
chartdata.plot(kind='barh', legend=False, title='브랜드별 총 매장 갯수', rot=30, color=mycolor)

filename = 'makeChickenGraph02.png'
plt.savefig(filename, dpi=400)
print(filename + '파일이 저장되었습니다.')

# 그래프를 보여준다
# plt.show()


