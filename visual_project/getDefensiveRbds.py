import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
############################################
plt.rc('font', family='NanumGothic')
PNG = '.png'
CHART_NAME = 'Defensive_Rebounds_Chart'
filename = 'NBALeagueChart.csv'
############################################

# csv 파일 읽기
myframe = pd.read_csv(filename, encoding='utf-8')

# 데이터 타입 확인
print(type(myframe))

# 불러오는 데이터 확인
print(myframe)

# 경기당 평균 수비리바운드 갯수가 높은 순으로 팀명 정렬
teams = myframe.sort_values(by='Defensive Rebounds', axis=0, ascending=True)['Team']

# 경기당 평균 수비리바운드 갯수가 높은 순 정렬
defencerbds = myframe.sort_values(by='Defensive Rebounds', axis=0, ascending=True)['Defensive Rebounds']

# defencerbds 저장할 리스트
percentdata = []
percentdata = defencerbds

# 저장된 defencerbds 데이터 값을 내림차순으로 저장
ascendingpct = sorted(percentdata)

mycolor = ['salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque',
           'salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque',
           'salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque']

# 그래프를 설정 시작
plt.figure(figsize=(12,12))

# 수평 막대그래프 표현
plt.barh(teams, defencerbds, height=-0.7, align='center', color=mycolor,
         edgecolor='gray', linewidth=1, log=False)

# 수치 값 텍스트 표현
for idx, v in enumerate(teams):
    # 예시 : 20.0%
    ratioval = '%.1f' % (ascendingpct[idx])
    # 그래프의 에 비율 표시끝
    plt.text(ascendingpct[idx], v, ratioval + '개', fontsize=9,
             horizontalalignment='right', verticalalignment='center', color='black')

# 데이터축(x축) 정수에서 실수로 변환
plt.gca().xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1f'))

# 데이터축(x축) 최소값, 최대값 지정
plt.xlim(30, 40)

# x축 눈금 간격
plt.gca().xaxis.set_major_locator(mtick.MultipleLocator(0.5))

# 그래프 제목
plt.title('NBA 20-21 시즌 팀별 경기당 평균 수비 리바운드')

# 데이터축(x축) 라벨 설정
plt.xlabel('경기당 평균 수비 리바운드 성공횟수')

# 기준 축(y축) 라벨 설정
plt.ylabel('팀명')

savefile = CHART_NAME + PNG
plt.savefig(savefile, dpi=400)

plt.show()