from wordcloud import WordCloud
import matplotlib.pyplot as plt

filename = 'steve.txt'
myfile = open(filename, 'rt', encoding='utf-8')
text = myfile.read()
print(type(text))
print('-'*30)

wordcloud = WordCloud()
wordcloud = wordcloud.generate(text)
print(type(wordcloud))
print('-'*30)

bindo = wordcloud.words_
print(type(bindo))
print(bindo)
print('-'*30)

# sorted() : 본체 리스트는 놔두고, 정렬한 새로운 리스트를 반환한다.
# bindo.items() : 정렬할 데이터
# key : 어떤 것을 기준으로 정렬할 것인가? 에 대한 기준
# reverse : 오름차순, 내림차순으로 정렬할지 지정 (False : 오름차순, True : 내림차순)
sortedData = sorted(bindo.items(), key=lambda x:x[1], reverse=True)
print(sortedData)
print('-'*30)

charData = sortedData[:10]
print(charData)
print('-'*30)

xtick = []
chart = []
for item in charData:
    xtick.append(item[0])
    chart.append(item[1])

plt.rc('font', family='NanumGothic')

mycolor = ['r', 'g', 'b', 'y', 'm', 'c', '#FFCC00', '#CCFFBB', '#05CEFF', '#1122CC']

plt.figure()
plt.bar(xtick, chart, color=mycolor)
plt.title('상위 빈도 top 10')

filename = 'wordCloudEx01_01.png'
plt.savefig(filename, dpi=400)
print(filename + '파일 저장')

plt.figure(figsize=(12,12))
plt.imshow(wordcloud)
plt.axis('off')
filename='wordCloudEx01_02.png'
plt.savefig(filename, dpi=400)
print(filename + '파일 저장')
