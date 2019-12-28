#/usr/bin/python
# -*- coding:utf-8 -*-
# 작성자 : 한석현


from matplotlib import pyplot as plt

def Ex1():
    x_val = [0, 1, 2, 3, 4]
    y_val = [0, 1, 4, 9, 4]
    plt.plot(x_val, y_val)
    plt.show()


def Ex2():
    x_values = [0, 1, 2, 3, 4, 5, 10]
    y_values_1 = [10, 12, 12, 10, 14, 22, 24]
    y_values_2 = [11, 14, 15, 15, 22, 21, 12]
    plt.plot(x_values, y_values_1, 'o')
    plt.plot(x_values, y_values_2)
    plt.show()


def Legend():
    plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
    plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
    plt.legend(['parabola', 'cubic'], loc=10)
    plt.show()

#loc=?
#0: best
#1: upper right
#2: upper left
#3: lower left
#4: lower right
#5: right
#6: center left
#7: center right
#8: lower center
#9: upper center
#10: center

def Legend2():
    plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label="parabola")
    plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], label="cubic")
    plt.legend() # 꼭 적어줘야 한다.
    plt.show()

def lineStyle():
#https://www.w3schools.com/colors/colors_names.asp
#https://www.w3schools.com/colors/colors_picker.asp
    
    # A circle:
    #plt.plot(x_values, y_values, marker='o')
    # A square:
    #plt.plot(x_values, y_values, marker='s')
    # A star:
    #plt.plot(x_values, y_values, marker='*')

    # Dashed:
    #plt.plot(x_values, y_values, linestyle='--')
    # Dotted:
    #plt.plot(x_values, y_values, linestyle=':')
    # No line:
    #plt.plot(x_values, y_values, linestyle='')

    x_values = [0, 1, 2, 3, 4, 5, 10]
    y_values_1 = [10, 12, 12, 10, 14, 22, 24]
    y_values_2 = [11, 14, 15, 15, 22, 21, 12]
    plt.plot(x_values, y_values_1, color='green', linestyle='--')
    plt.plot(x_values, y_values_2, color='#AAAAAA',  marker='o')
    plt.show()

def Title():
    #x
    hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #y
    happiness = [9.8, 9.9, 9.2, 8.6, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]

    #          X       Y
    plt.plot(hours, happiness)

    plt.xlabel('Time of day')
    plt.ylabel('Happiness Rating (out of 10)')

    plt.title('My Self-Reported Happiness While Awake')
    plt.show()

def Subplot():#다단 나누기
    x = [1, 2, 3, 4]
    y = [1, 2, 3, 4]

    # First Subplot
    plt.subplot(1, 2, 1)
    plt.plot(x, y, color='green')
    plt.title('First Subplot')

    # Second Subplot
    plt.subplot(1, 2, 2)
    plt.plot(x, y, color='steelblue')
    plt.title('Second Subplot')

    # Display both subplots
    plt.show()

def Subplot2():
    x = range(7)
    a = [0, 1, 2, 3, 4, 5, 6]
    b = [0, 1, 4, 9, 16, 25, 36]
    c = [0, 1, 8, 27, 64, 125, 216]

    plt.subplot(2,1,1)
    plt.plot(x, a)
    plt.subplot(2,2,3)
    plt.plot(x, b)
    plt.subplot(2,2,4)
    plt.plot(x, c)
    plt.show()

#subplot의 세부적인 위치는 plt.subplots_adjust()로 조절
#left — 왼쪽 마진, 기본값 0.125. y축 레이블이 표시될 공간을 확보
#right — 오른쪽 마진, 기본값 0.9. 그래프 이미지(figure)을 넉넉하게 
#       반대로 줄일 경우 항목 레이블(legend)를 위한 공간을 확보
#bottom — 아래쪽 마진, 기본값 0.1. 눈금이나 x 축 레이블이 표시될 공간을 확보
#top — 위쪽 마진, 기본값 0.9.
#wspace — 가로로 인접한 subplot 사이 공간, 기본값 0.2.
#hspace — 세로로 인접한 subplot 사이 공간, 기본값 0.2.
#
#ex)
#plt.subplots_adjust(wspace=0.35)
#plt.show()

def Axis():
# plt.axis() 안에 리스트를 넣어  x축, y축 각각의 최대값/최소값을 지정
# [x축 최소값, x축 최대값, y축 최소값, y축 최대값] 형태    

    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]
    plt.plot(x, y)
    plt.axis([0, 3, 2, 5])
    plt.show()

def Tick():
    #눈금
    # ax = plt.subplot()<==>  ax = plt.subplot(1, 1, 1) 동일함

    plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
    plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
    ax = plt.subplot()
    
    #특정 눈금만 표시
    ax.set_xticks([1, 2, 4])
    plt.show()

def Tick2():
    plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
    ax = plt.subplot()
    ax.set_yticks([0.1, 0.6, 0.8]) #y축특정눈금 표시
    ax.set_yticklabels(['10%', '60%', '80%'])
    plt.savefig('sample.png')
    plt.show()


# graphSize
# plt.figure() 안에 figsize=(width, height)를 직접 적어 넣으면 그래프 크기를 조정
# ex)
# plt.figure(figsize=(4, 10))

# delete
# plt.close('all')

# savefig():
# plt.savefig('sample.png')


if __name__ == '__main__':
    
#    Ex2()
#    Legend2()
#    lineStyle()
#    Title()
#    Subplot2()
    Tick2()
