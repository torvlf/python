import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#######################################
plt.rc('font', family='NanumGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'boxPlotExam'
filename = '../data/tips.csv'
########################################

myframe = pd.read_csv(filename, encoding='utf-8', index_col=0)

print(myframe['time'].unique())
print('-'*30)

DINNER, LUNCH = 'Dinner', 'Lunch'

# for Dinner
frame01 = myframe.loc[myframe['time'] == DINNER, 'total_bill']
frame01.index.name = DINNER
print(frame01.head())
print('-'*30)

# for Lunch
frame02 = myframe.loc[myframe['time'] == LUNCH, 'total_bill']
frame02.index.name = LUNCH
print(frame02.head())
print('-'*30)

chartdata = [np.array(frame01), np.array(frame02)]
print(chartdata)
print('-'*30)

xtick_label = [DINNER, LUNCH]

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))

bplot1 = ax1.boxplot(chartdata, labels=xtick_label, patch_artist=True, vert=True)
ax1.set_title('상자 수염(noNotch)')

# print(type(bplot1))
# print(bplot1)

bplot2 = ax2.boxplot(chartdata, labels=xtick_label, patch_artist=True, vert=True, notch=True)
ax2.set_title('상자 수염(Notch)')

colors = ['pink', 'lightblue']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Dinner and Lunach Tip')
    ax.set_ylabel('Observation data')

cnt += 1

savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + '파일 저장 완료')
plt.show()