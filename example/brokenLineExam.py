################## import session ######################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#########################################################

################## common session #######################
plt.rc('font', family='NanumGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'brokenLineExam'
filename = '../data/주요발생국가주간동향(4월2째주).csv'
########################################################

############# 지정한 날짜에 대한 꺽은선 그래프 ################
data = pd.read_csv(filename, encoding='utf-8', index_col='국가')
print(data.columns)
print('-'*30)

print(data)
print('-'*30)

chartdata = data['4월06일']
print(type(chartdata))
print(chartdata)
print('-'*30)

# 꺽은선 그래프 그리기
plt.plot(chartdata, color='blue', linestyle='solid', marker='.')

# y축에서 보여줄 단위
YTICKS_INTERVAL = 50000

# chartdata내의 최대값보다 조금더 보여주기 위해서 최대값을 구한 것이다
maxlim = (int(chartdata.max()/YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL
print(maxlim)

# 0 부터 1100전까지 가는데 100씩 증가
values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)
print(values)

# y축에 보이는 숫자를 3자리씩 끊어서 ',' 를 삽입해준다
plt.yticks(values, ['%s' % format(val, ',') for val in values])

# 그래프 배경에 격자 생성
plt.grid(True)

# 그래프 x 축 라벨
plt.xlabel('국가명')

# 그래프 y 축 라벨
plt.ylabel('발생 건수')

# 그래프 제목
plt.title('4월 6일 코로나 발생 건수')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료 ')
######################################################

######### 날짜별 국가들의 코로나 확진 꺽은선 그래프 ###########
COUNTRY = ['스페인','프랑스','독일','중국','영국','이란']
WHEN = ['4월06일','4월07일','4월08일','4월09일','4월10일']

chartdata = data.loc[COUNTRY, WHEN]

# 행과 열을 변경하기 위해서 전치를 사용한다
chartdata = chartdata.T

print(chartdata)
print('-'*30)

chartdata.plot(title='Some Title', marker='.', rot=0, legend=True, figsize=(10,6))

plt.grid(True)
plt.xlabel('일자')
plt.ylabel('국가명')
plt.title('일자별 국가 코로나 발생 건수')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료 ')
#########################################################

################## 식당 총금액과 팁 정보 #####################
tipsfile = '../data/tips.csv'
myframe = pd.read_csv(tipsfile)
print(type(myframe))
print(myframe.columns)

# [:(행), [(열)]]을 의미
data_bill = myframe.loc[:, ['total_bill']]
data_tip = myframe.loc[:, ['tip']]

fig, ax1 = plt.subplots()
ax1.set_title('결제 금액과 tip(이중축)')

xrange = range(len(myframe))
color = 'tab:red'
ax1.set_ylabel('결제금액', color=color)
# plot: 2차원을 의미
# x축과 y축이 필요
# x축은 myframe의 갯수가 표시, y축은 결제 금액에 대한 값을 표시
ax1.plot(xrange, data_bill, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# twinx(): 기존에 사용하던 x축은 그대로 유지하면서 다른 y축에 새로운 값을 추가할 수 있다.(이중축)
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('팁(tip)', color=color)
ax2.plot(xrange, data_tip, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료 ')
########################################################
print('finished')