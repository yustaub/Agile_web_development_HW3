import numpy as np
#定义 牌 结构体
#name 牌字符：2，3，, A
#value 牌字符在字符串中的索引
#suit 花色
cardType=np.dtype({'names':['name','suit','value'],'formats':['U10','U10','i4']})
#定义两副牌，每幅各有5张牌
cardsBlack = np.array([('b', 'b', 0)] * 5, dtype=cardType)  # 创建Data[10]
cardsWhite = np.array([('w', 'w', 0)] * 5, dtype=cardType)
#所有牌的值，其中10用T表示
CardValues="23456789TJQKA"
order_black = [0, 0, 0, 0, 0]
order_white = [0, 0, 0, 0, 0]
#把读入的字符串设置到數組中
def InitCards():
    for i in range(5):
        cardsBlack[i]['name']=str[3*i]
        cardsBlack[i]['suit']=str[3*i+1]
        cardsBlack[i]['value']=CardValues.find(cardsBlack[i]['name'])

        cardsWhite[i]['name']=str[3*i+15]
        cardsWhite[i]['suit']=str[3*i+16]
        cardsWhite[i]['value']=CardValues.find(cardsWhite[i]['name'])
#黑牌排序
def Sort_black():
    for i in range(4):
        min=i
        for j in range(i+1,5):
            if(cardsBlack[j]['value']<cardsBlack[min]['value']):
                min=j
        #swap
        tmp_name=cardsBlack[i]['name']
        tmp_value=cardsBlack[i]['value']
        tmp_suit=cardsBlack[i]['suit']

        cardsBlack[i]['name'] = cardsBlack[min]['name']
        cardsBlack[i]['value'] = cardsBlack[min]['value']
        cardsBlack[i]['suit'] = cardsBlack[min]['suit']

        cardsBlack[min]['name'] = tmp_name
        cardsBlack[min]['value'] = tmp_value
        cardsBlack[min]['suit'] = tmp_suit

#白牌排序
def Sort_white():
    for i in range(4):
        min=i
        for j in range(i+1,5):
            if(cardsWhite[j]['value']<cardsWhite[min]['value']):
                min=j
        #swap
        tmp_name=cardsWhite[i]['name']
        tmp_value=cardsWhite[i]['value']
        tmp_suit=cardsWhite[i]['suit']

        cardsWhite[i]['name'] = cardsWhite[min]['name']
        cardsWhite[i]['value'] = cardsWhite[min]['value']
        cardsWhite[i]['suit'] = cardsWhite[min]['suit']

        cardsWhite[min]['name'] = tmp_name
        cardsWhite[min]['value'] = tmp_value
        cardsWhite[min]['suit'] = tmp_suit
#两副牌进行排序
def Sortcard():
    Sort_black()
    Sort_white()

#查看黑牌的五张牌的牌值是否连续
def shunzi_black():
    if(cardsBlack[1]['value']-cardsBlack[0]['value']==1 and cardsBlack[2]['value']-cardsBlack[1]['value']==1
       and cardsBlack[3]['value']-cardsBlack[2]['value']==1 and cardsBlack[4]['value']-cardsBlack[3]['value']==1):
        return 1
    else:
        return 0
#查看白牌的五张牌的牌值是否连续
def shunzi_white():
    if (cardsWhite[1]['value'] - cardsWhite[0]['value'] == 1 and cardsWhite[2]['value'] - cardsWhite[1]['value'] == 1
        and cardsWhite[3]['value'] - cardsWhite[2]['value'] == 1 and cardsWhite[4]['value'] - cardsWhite[3]['value'] == 1):
        return 1
    else:
        return 0
#查看黑牌是否是同花色
def tonghua_black():
    for i in range(4):
        if(cardsBlack[i]['suit']!=cardsBlack[i+1]['suit']):
            return 0
    return 1
#查看白牌是否是同花色
def tonghua_white():
    for i in range(4):
        if(cardsWhite[i]['suit']!=cardsWhite[i+1]['suit']):
            return 0
    return 1
#查看黑牌是否是炸弹
def boom_black():
    boom1=1
    boom2=1
    for i in range(3):#0-3
        if(cardsBlack[i]['value']!=cardsBlack[i+1]['value']):
            boom1=0
    for i in range(1,4):#1-4
        if(cardsBlack[i]['value']!=cardsBlack[i+1]['value']):
            boom2=0
    if(boom1 or boom2):#如果存在炸弹
        return 1
    else:
        return 0
#查看白牌是否是炸弹
def boom_white():
    boom1=1
    boom2=1
    for i in range(3):#0-3
        if(cardsWhite[i]['value']!=cardsWhite[i+1]['value']):
            boom1=0
    for i in range(1,4):#1-4
        if(cardsWhite[i]['value']!=cardsWhite[i+1]['value']):
            boom2=0
    if(boom1 or boom2):#如果存在炸弹
        return 1
    else:
        return 0
#查看黑牌的三张牌是否是相同值
def three_black():
    three1=1
    three2=1
    three3=3
    for i in range(2):
        if(cardsBlack[i]['value']!=cardsBlack[i+1]['value']):
            three1=0
    for i in range(1,3):
        if(cardsBlack[i]['value']!=cardsBlack[i+1]['value']):
            three2=0
    for i in range(2,4):
        if (cardsBlack[i]['value'] != cardsBlack[i + 1]['value']):
            three3 = 0
    if(three1 or three2 or three3):#如果存在三张牌相同
        return 1
    else:
        return 0
#查看白牌的三张牌是否是相同值
def three_white():
    three1 = 1
    three2 = 1
    three3 = 3

    for i in range(2):
        if (cardsWhite[i]['value'] != cardsWhite[i + 1]['value']):
            three1 = 0
    for i in range(1, 3):
        if (cardsWhite[i]['value'] != cardsWhite[i + 1]['value']):
            three2 = 0
    for i in range(2, 4):
        if (cardsWhite[i]['value'] != cardsWhite[i + 1]['value']):
            three3 = 0
    if (three1 or three2 or three3):  # 如果存在三张牌相同
        return 1
    else:
        return 0

#黑牌xxxoo或者ooxxx
def three_two_black():
    three1=1
    two1=1
    three2=1
    two2=1
    for i in range(2):
        if(cardsBlack[i]['value']!=cardsBlack[i+1]['value']):
            three1=0
    if(cardsBlack[3]['value']!=cardsBlack[4]['value']):
        two1=0
    for i in range(2,4):
        if (cardsBlack[i]['value'] != cardsBlack[i + 1]['value']):
            three2 = 0
    if(cardsBlack[0]['value']!=cardsBlack[1]['value']):
        two2=0
    if((three1 and two1) or (three2 and two2)):#如果存在xxxoo或者ooxxx
        return 1
    else:
        return 0
#白牌xxxooo或者ooxxx
def three_two_white():
    three1=1
    two1=1
    three2=1
    two2=1
    for i in range(2):
        if(cardsWhite[i]['value']!=cardsWhite[i+1]['value']):
            three1=0
    if(cardsWhite[3]['value']!=cardsWhite[4]['value']):
        two1=0
    for i in range(2,4):
        if (cardsWhite[i]['value'] != cardsWhite[i + 1]['value']):
            three2 = 0
    if(cardsWhite[0]['value']!=cardsWhite[1]['value']):
        two2=0
    if((three1 and two1) or (three2 and two2)):#如果存在xxxoo或者ooxxx
        return 1
    else:
        return 0
def two_black(index):#判断第index和第index+1个元素是否相等
    if(cardsBlack[index]['value']==cardsBlack[index+1]['value']):
        return 1
    else:
        return 0
#
def two_white(index):#判断第index和第index+1个元素是否相等
    if(cardsWhite[index]['value']==cardsWhite[index+1]['value']):
        return 1
    else:
        return 0
#得到黑牌的等级（同花顺最高，离牌最低）
def get_black_level():
    level=9
    order_black=[0,0,0,0,0]
    #level 9
    # 同花顺  9
    if (shunzi_black() and tonghua_black()):
        order_black[0]=cardsBlack[4]['value']
        return level,order_black
    #level 8
    # 4張牌相同（炸弹）
    level-=1
    if(boom_black()):#如果黑牌是炸弹
        #如果有4张相同的牌，位置为1的牌一定在炸弹序列中
        order_black[0]=cardsBlack[1]['value']
        return level,order_black
    #level 7
    #三张牌相同，另外两张也相同 xxxoo or oooxx
    level-=1
    if(three_two_black()):
        #比较三张相同的值即可，位置为2的元素一直都在3个相同的值中
        order_black[0]=cardsBlack[2]['value']
        return level,order_black
    #level 6
    #五张牌的花色相同 按照散排规则比较大小
    level-=1
    if(tonghua_black()):
        for i in range(5):
            #order中是从大到小排列的牌值，用于判别大小
            order_black[i]=cardsBlack[4-i]['value']
        return level,order_black
    #level 5
    #五张相连的牌。 比较最大的牌点数。若大小都相同，则为平局
    level-=1
    if(shunzi_black()):
        order_black[0]=cardsBlack[4]['value']#按最大的值比较
        return level,order_black
    #level 4
    #有三张同样大小的牌片。 比较三张大小一样的牌的牌点数大小
    level-=1
    if(three_black()):
        order_black[0]=cardsBlack[2]['value']
        return level,order_black
    #level 3
    #有两个对子牌。 比较大对子的大小，若相同，比较小对子的大小，
    # 若还相同，比较单张牌的大小，若还相同，则为平局
    #abbcc bbacc bbcca
    level-=1
    #abbcc
    two1=0
    two2=0
    two3=0
    if(two_black(1) and two_black(3)):
        two1=1
        tmp=cardsBlack[0]['value']
    #bbacc
    if(two_black(0) and two_black(3)):
        two2=1
        tmp=cardsBlack[2]['value']
    #bbcca
    if (two_black(0) and two_black(2)):
        two3 = 1
        tmp = cardsBlack[4]['value']
    if(two1 or two2 or two3):
        order_black[0]=cardsBlack[3]['value']#大对子的值
        order_black[1]=cardsBlack[1]['value']#小对子的值
        order_black[2]=tmp
        return level,order_black
    #level 2
    #有两张同样大小的牌片。 比较两张大小一样的牌的牌点数，
    # 如果相同，依次比较剩余的三张牌大小。若大小都相同，则为平局
    level-=1
    #aabcd baacd bcaad bcdaa
    #aabcd
    two1=0;two2=0;two3=0;two4=0
    if(two_black(0)):
        two1=1
        i = 0;t1 = 4;t2 = 3;t3 = 2
    #baacd
    elif(two_black(1)):
        two2=1
        i = 1;t1 = 4;t2 = 3;t3 = 0
    #bcaad
    elif(two_black(2)):
        two3=1
        i = 2;t1 = 4;t2 = 1;t3 = 0
    elif(two_black(3)):
        two4=1
        i = 3;t1 = 2;t2 = 1;t3 = 0
    if(two1 or two2 or two3 or two4):
        order_black[0]=cardsBlack[i]['value']
        order_black[1]=cardsBlack[t1]['value']
        order_black[2] = cardsBlack[t2]['value']
        order_black[3] = cardsBlack[t3]['value']
        return level,order_black
    #level 1
    #不符合其他任何规则的五张牌。 比较最大一张牌的大小，如果相同，
    #比较第二大的牌的牌点数，如果五张牌的牌点数都相同，则为平局
    level-=1
    for i in range(5):
        order_black[i]=cardsBlack[4-i]['value']
    return level,order_black
#得到白牌的等级（同花顺最高，离牌最低）
def get_white_level():
    level=9
    order_white=[0,0,0,0,0]
    #level 9
    # 同花顺  9
    if (shunzi_white() and tonghua_white()):
        order_white[0]=cardsWhite[4]['value']
        return level,order_white
    #level 8
    # 4張牌相同（炸弹）
    level-=1
    if(boom_white()):#如果黑牌是炸弹
        #如果有4张相同的牌，位置为1的牌一定在炸弹序列中
        order_white[0]=cardsWhite[1]['value']
        return level,order_white
    #level 7
    #三张牌相同，另外两张也相同 xxxoo or oooxx
    level-=1
    if(three_two_white()):
        #比较三张相同的值即可，位置为2的元素一直都在3个相同的值中
        order_white[0]=cardsWhite[2]['value']
        return level,order_white
    #level 6
    #五张牌的花色相同 按照散排规则比较大小
    level-=1
    if(tonghua_white()):
        for i in range(5):
            #order中是从大到小排列的牌值，用于判别大小
            order_white[i]=cardsWhite[4-i]['value']
        return level,order_white
    #level 5
    #五张相连的牌。 比较最大的牌点数。若大小都相同，则为平局
    level-=1
    if(shunzi_white()):
        order_white[0]=cardsWhite[4]['value']#按最大的值比较
        return level,order_white
    #level 4
    #有三张同样大小的牌片。 比较三张大小一样的牌的牌点数大小
    level-=1
    if(three_white()):
        order_white[0]=cardsWhite[2]['value']
        return level,order_white
    #level 3
    #有两个对子牌。 比较大对子的大小，若相同，比较小对子的大小，
    # 若还相同，比较单张牌的大小，若还相同，则为平局
    #abbcc bbacc bbcca
    level-=1
    #abbcc
    two1=0
    two2=0
    two3=0
    if(two_white(1) and two_white(3)):
        two1=1
        tmp=cardsWhite[0]['value']
    #bbacc
    if(two_white(0) and two_white(3)):
        two2=1
        tmp=cardsWhite[2]['value']
    #bbcca
    if (two_white(0) and two_white(2)):
        two3 = 1
        tmp = cardsWhite[4]['value']
    if(two1 or two2 or two3):
        order_white[0]=cardsWhite[3]['value']#大对子的值
        order_white[1]=cardsWhite[1]['value']#小对子的值
        order_white[2]=tmp
        return level,order_white
    #level 2
    #有两张同样大小的牌片。 比较两张大小一样的牌的牌点数，
    # 如果相同，依次比较剩余的三张牌大小。若大小都相同，则为平局
    level-=1
    #aabcd baacd bcaad bcdaa
    #aabcd
    two1=0;two2=0;two3=0;two4=0
    if(two_white(0)):
        two1=1
        i = 0;t1 = 4;t2 = 3;t3 = 2
    #baacd
    elif(two_white(1)):
        two2=1
        i = 1;t1 = 4;t2 = 3;t3 = 0
    #bcaad
    elif(two_white(2)):
        two3=1
        i = 2;t1 = 4;t2 = 1;t3 = 0
    elif(two_white(3)):
        two4=1
        i = 3;t1 = 2;t2 = 1;t3 = 0
    if(two1 or two2 or two3 or two4):
        order_white[0]=cardsWhite[i]['value']
        order_white[1]=cardsWhite[t1]['value']
        order_white[2] = cardsWhite[t2]['value']
        order_white[3] = cardsWhite[t3]['value']
        return level,order_white
    #level 1
    #不符合其他任何规则的五张牌。 比较最大一张牌的大小，如果相同，
    #比较第二大的牌的牌点数，如果五张牌的牌点数都相同，则为平局
    level-=1
    for i in range(5):
        order_white[i]=cardsWhite[4-i]['value']
    return level,order_white


if __name__=='__main__':

    str = input("请输入牌组：")
    print('你输入的牌组是：',str)
    print('白牌:%s' % cardsWhite)
    print('黑牌%s' % cardsBlack)
    if(str):
        InitCards() #把读入的字符串设置到数组中
        Sortcard() #将两副牌都排好序
        #分别得到黑牌白牌的等级
        level_black=get_black_level()
        level_white=get_white_level()
        #比较两副牌
        if(level_black>level_white):#黑牌赢
            print('black wins!!!')
        elif(level_black<level_white):#白牌赢
            print('white win!!!')
        else:#等级相同，比较order数组
            i=0
            for i in range(5):
                if(order_black[i]>order_white[i]):
                    print('black wins!!!')
                    break
                elif(order_black[i]<order_white[i]):
                    print('white wins!!!')
                    break
            if(i==4):
                print('Tie')




    # Sort_black()
    # print(cardsBlack)
    # print(three_black())
    # print(level_black)
