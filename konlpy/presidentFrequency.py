import matplotlib.pyplot as plt
from PyKomoran import Komoran
import nltk
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator

plt.rc('font', family='NanumGothic')

class Visualization:
    def __init__(self, wordList):

        self.wordList = wordList
        self.wordDict = dict(wordList)


    # end of __init__

    def makeWordCloud(self):

        alice_color_file = '../wordcloud/alice_color.png'
        alice_coloring = np.array(Image.open(alice_color_file))

        fontpath = 'NanumGothic.ttf'

        wordcloud = WordCloud(background_color='black', font_path=fontpath, mask=alice_coloring, relative_scaling=0.2,
                              contour_width=2, contour_color='white')

        wordcloud = wordcloud.generate_from_frequencies(self.wordDict)

        image_colors = ImageColorGenerator(alice_coloring)

        wordcloud = wordcloud.recolor(color_func=image_colors, random_state=42)

        plt.imshow(wordcloud)
        plt.axis('off')

        filename = 'myWordCloud.png'
        plt.savefig(filename, dpi=400)
        print(filename + '파일 저장 완료')

    # end of makeWordCloud

    def makeBarChart(self):
        plt.figure(figsize=(12, 8))

        barcount = 10
        result = self.wordList[:barcount]

        # 차트 수치
        chartdata = []
        # 단어
        xdata = []

        for idx in range(len(result)):
            chartdata.append(result[idx][1])
            xdata.append(result[idx][0])

            #예시 : 10건
            value = str(chartdata[idx]) + '건'

            plt.text(x=idx, y=chartdata[idx] - 5, s=value, fontsize=8, horizontalalignment='center')
        # end of for

        mycolor = ['r','g','b','c','y','m','#05CCFF','#FFCC00','#CCFFBB','#11CCFF']

        plt.bar(x=range(barcount), height=chartdata, align='center', color=mycolor)
        plt.xticks(range(barcount), xdata, rotation='45')
        plt.title('상위 top ' + str(barcount) + ' 빈도 수')

        xlow, xhigh = -0.5, barcount - 0.5

        plt.xlim([xlow, xhigh])
        plt.ylim([0, 35])
        plt.xlabel('주요 키워드')
        plt.ylabel('빈도 수')

        filename = 'myBarChart.png'
        plt.savefig(filename, dpi=400)
        print(filename + '파일 저장 완료')

    # end of makeBarChart

# end of Visualization

filename = '문재인대통령신년사.txt'
ko_con_text = open(filename, encoding='utf-8').read()

komo = Komoran('STABLE')
# 사용자 사전을 등록
# komo.set_user_dic('사용자정의파일.txt')

tokens_ko = komo.nouns(ko_con_text)
# print(token_ko)
# print('-'*30)

stop_word_file = 'stopword.txt'
stop_file = open(stop_word_file, 'rt', encoding='utf-8')
stop_word = [word.strip() for word in stop_file.readlines()]
# print(stop_word)
# print('-'*30)

print(len(tokens_ko))
tokens_ko = [each_word for each_word in tokens_ko if each_word not in stop_word]
print(len(tokens_ko))

ko = nltk.Text(tokens=tokens_ko)
# tokens_ko 내에 있는 단어 중에서 빈도가 가장 많은 단어를 가져온다.
data = ko.vocab().most_common(500)
print(len(data))
# print(data)
print('-'*30)

wordlist = list()

for word, count in data:
    if(count >= 2 and len(word) >= 2):
        wordlist.append((word, count))

# 생성자 호출
visual = Visualization(wordlist)
# wordcloud 함수 호출
visual.makeWordCloud()
# makeBarChart 함수 호출
visual.makeBarChart()

print('finished')