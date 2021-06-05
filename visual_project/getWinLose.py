import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
############################################
plt.rc('font', family='NanumGothic')
PNG = '.png'
CHART_NAME = 'WinLose_Chart'
filename = 'NBALeagueChart.csv'
matplotlib.rcParams['axes.unicode_minus'] = False
############################################

# csv 파일 읽기
myframe = pd.read_csv(filename, encoding='utf-8')

# 데이터 타입 확인
print(type(myframe))

# 불러오는 데이터 확인
print(myframe)

# 필드 득점 성공률 높은 순으로 팀명 정렬
teams = myframe.sort_values(by='Wins', axis=0, ascending=True)['Team']

# 경기 승리 횟수
wins = myframe.sort_values(by='Wins', axis=0, ascending=True)['Wins']

# 경기 패배 횟수
losses = myframe.sort_values(by='Wins', axis=0, ascending=True)['Losses']

mycolor = ['salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque',
           'salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque',
           'salmon','springgreen','aqua','lemonchiffon','thistle','lightblue','pink','violet','greenyellow','bisque']

#그래프를 설정 시작
plt.figure(figsize=(12,12))

# 막대 그래프 갯수
index = np.arange(len(teams))

# 수평 막대그래프 양쪽으로 표현
plt.barh(index, wins, color='lightcoral', label='승')
plt.barh(index, -(losses), color='cornflowerblue', label='패')

# 자동 방식을 이용한 레전드 작성
plt.legend()

# 기준 축(y축) 표시
plt.yticks(index, teams, rotation=15)

# 데이터축(x축) 범위 설정
plt.xlim(-72, 72)

# # 수치 값 텍스트 표현
# for idx, v in enumerate(teams):
#     # 예시 : 20.0%
#     ratioval = '%d' % (wins[idx])
#     # 그래프의 에 비율 표시끝
#     plt.text(wins[idx], v, ratioval + '승', fontsize=9,
#              horizontalalignment='right', verticalalignment='center', color='black')

# 그래프 제목
plt.title('NBA 20-21 시즌 팀별 승패')

# 데이터축(x축) 라벨 설정
plt.ylabel('팀명')

# 기준 축(y축) 라벨 설정
plt.xlabel('팀별 승패')

savefile = CHART_NAME + PNG
plt.savefig(savefile, dpi=400)

plt.show()