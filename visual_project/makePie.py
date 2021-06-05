import matplotlib.pyplot as plt
import pandas as pd
##############################################
plt.rc('font', family='NanumGothic')
##############################################
filename = 'NBALeagueChart.csv'
myframe = pd.read_csv(filename, encoding='utf-8')

# csv 파일에서 첫번째 항목 데이터만 가져오기
team = myframe['Team'][:1]
assist = int(myframe['Assists'][:1])
turnover= int(myframe['Turnovers'][:1])
steal = int(myframe['Steals'][:1])
block = int(myframe['Blocks'][:1])

# 라벨 항목 설정
labels = ['Assist', 'TurnOver', 'Steal', 'Block']
# 각 영역 비율 설정
ratio = [assist, turnover, steal, block]

title = team[0]

plt.figure()
plt.title(title)

# 파이차트 생성
plt.pie(ratio, labels=labels, shadow=False, startangle=90, autopct='%.1f%%')

savefile = 'Utah_Jazz_Pie.png'
plt.savefig(savefile, dpi=400)
plt.show()
