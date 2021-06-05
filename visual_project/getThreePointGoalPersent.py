import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
############################################
plt.rc('font', family='NanumGothic')
PNG = '.png'
CHART_NAME = '3Point_Goal_Chart'
filename = 'NBALeagueChart.csv'
############################################

# csv 파일 읽기
myframe = pd.read_csv(filename, encoding='utf-8')

# 데이터 타입 확인
print(type(myframe))

# 불러오는 데이터 확인
print(myframe)

# 3점 득점 성공률 높은 순으로 팀명 정렬
teams = myframe.sort_values(by='3Point Field Goal Persent', axis=0, ascending=True)['Team']

# 3점 득점 성공률 높은 순 정렬
threegp = myframe.sort_values(by='3Point Field Goal Persent', axis=0, ascending=True)['3Point Field Goal Persent']

# threegp 저장할 리스트
percentdata = []
percentdata = threegp

# 저장된 threegp 데이터 값을 내림차순으로 저장
ascendingpct = sorted(percentdata)

mycolor = ['salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque',
           'salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque',
           'salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque']

# 그래프를 설정 시작
plt.figure(figsize=(12,12))

# 수평 막대그래프 표현
plt.barh(teams, threegp, height=-0.7, align='center', color=mycolor,
         edgecolor='gray', linewidth=1, log=False)

# 수치 값 텍스트 표현
for idx, v in enumerate(teams):
    # 예시 : 20.0%
    ratioval = '%.1f%%' % (ascendingpct[idx])
    # 그래프의 에 비율 표시끝
    plt.text(ascendingpct[idx], v, ratioval, fontsize=9,
             horizontalalignment='right', verticalalignment='center', color='black')

# 데이터축(x축) 정수에서 실수로 변환
plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

# 데이터축(x축) 최소값, 최대값 지정
plt.xlim(33, 42)

# x축 눈금 간격
plt.gca().xaxis.set_major_locator(mtick.MultipleLocator(0.5))

# 그래프 제목
plt.title('NBA 20-21 시즌 팀별 3점 득점 성공률')

# 데이터축(x축) 라벨 설정
plt.xlabel('3점골 성공확률')

# 기준 축(y축) 라벨 설정
plt.ylabel('팀명')

savefile = CHART_NAME + PNG
plt.savefig(savefile, dpi=400)

plt.show()