################## import session ######################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#########################################################

################## common session #######################
plt.rc('font', family='NanumGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'histogramExam'
filename = '../data/tips.csv'
########################################################

############# 지정한 날짜에 대한 히스토그램 ################
tips = pd.read_csv(filename, encoding='utf-8')
print(tips.columns)
print('-'*30)

print(tips)
print('-'*30)

# 배열 혹은 배열들로 구성된 스퀀스를 입력 받고 데이터를 넣고자 하는 x축 위치를 설정
x= tips['total_bill']
print(type(x))

# 해당 막대의 영역을 얼마나 채우는지 결정해주는 변수
num_bins = 50

# 그래프 그릴 수 있는 도화지 생성
fig, ax = plt.subplots()

# hist(): 히스토그램 그래프를 만드는 method
# density: 확률밀도를 성정하기 위해 가중치 데이터를 정규화한다.
# density=False: 데이터를 정규화시키지 않는다.
n, bins, patches = ax.hist(x, num_bins, density=True, edgecolor='lightblue', linewidth=1)

# 그래프의 타이틀과 x,y축 라벨링
ax.set_title('히스토그램')
ax.set_xlabel('Frequency')
ax.set_ylabel('total bill')

# 평균
mu = x.mean()
print('mu :', mu)

# 표준 편차
sigma = x.std()
print('sigma :', sigma)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()


cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료 ')
######################################################

############### Human_Histogram ######################
humanfile = '../data/human_height.csv'
human = pd.read_csv(humanfile, encoding='utf-8')

fig, axes = plt.subplots(nrows=1, ncols=2)
giant = human['giant']
dwarf = human['dwarf']

axes[0].hist(giant, range=(210, 290), bins=20, alpha=0.6)
axes[1].hist(dwarf, range=(100, 180), bins=20, alpha=0.6)

axes[0].set_title('거인국의 키')
axes[1].set_title('소인국의 키')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료')


fig, axes = plt.subplots()
axes.hist(giant, bins=20, alpha=0.6, label='Giant')
axes.hist(dwarf, bins=20, alpha=0.6, label='Dwarf')
axes.legend()

axes.set_title('Giant & Dwarf Height')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료')
#######################################################

################# Men & Women Histogram ###############

fig, axes = plt.subplots()

man = human['man']
woman = human['woman']

x = np.array([man,woman]).T

# shape는 형상
print(x.shape)
print(type(x.shape))

axes.hist(x, bins=num_bins, density=False, histtype='bar', stacked=True, label=['men', 'women'])
axes.legend()
axes.set_title('Men & Women Histogram')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료')

#######################################################
print('finished')