def com(card):
    global 梅
    global 菱
    global 愛
    global 黑
    goal = []
    com_梅 = []
    com_菱 = []
    com_愛 = []
    com_黑 = []
    if card == p2:
        print("\0", "--------------", "\n", "player2's turn", "\n",
              "--------------")
    if card == p3:
        print("\0", "--------------", "\n", "player3's turn", "\n",
              "--------------")
    if card == p4:
        print("\0", "--------------", "\n", "player4's turn", "\n",
              "--------------")
    if len(card) == 0:
        print("pass")
    for i in range(0, len(card)):
        if (card[i])[2] == "A":
            card[i] = (card[i])[0] + (card[i])[1] + "1"
        if (card[i])[2] == "J":
            card[i] = (card[i])[0] + (card[i])[1] + "11"
        if (card[i])[2] == "Q":
            card[i] = (card[i])[0] + (card[i])[1] + "12"
        if (card[i])[2] == "K":
            card[i] = (card[i])[0] + (card[i])[1] + "13"
        if (card[i])[0] == "梅":
            com_梅.append(card[i].split("梅花"))
        if (card[i])[0] == "菱":
            com_菱.append(card[i].split("菱形"))
        if (card[i])[0] == "愛":
            com_愛.append(card[i].split("愛心"))
        if (card[i])[0] == "黑":
            com_黑.append(card[i].split("黑桃"))
    for i in range(0, len(com_梅)):
        if int((com_梅[i])[1]) == int(梅[-1]) + 1 or int(
            (com_梅[i])[1]) == int(梅[0]) - 1:
            goal.append("梅花" + ((com_梅[i])[1]))
    for i in range(0, len(com_菱)):
        if int((com_菱[i])[1]) == int(菱[-1]) + 1 or int(
            (com_菱[i])[1]) == int(菱[0]) - 1:
            goal.append("菱形" + ((com_菱[i])[1]))
    for i in range(0, len(com_愛)):
        if int((com_愛[i])[1]) == int(愛[-1]) + 1 or int(
            (com_愛[i])[1]) == int(愛[0]) - 1:
            goal.append("愛心" + ((com_愛[i])[1]))
    for i in range(0, len(com_黑)):
        if int((com_黑[i])[1]) == int(黑[-1]) + 1 or int(
            (com_黑[i])[1]) == int(黑[0]) - 1:
            goal.append("黑桃" + ((com_黑[i])[1]))
    total = [com_梅, com_菱, com_愛, com_黑]
    if len(goal) > 0:
        for i in range(0, len(goal)):
            if int((goal[i])[2]) < 7:
                if (goal[i])[0] == "梅":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("梅花")
                    梅.append(kil[1])
                    print("我出:", kill)
                    break
                elif (goal[i])[0] == "菱":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("菱形")
                    菱.append(kil[1])
                    print("我出:", kill)
                    break
                elif (goal[i])[0] == "愛":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("愛心")
                    愛.append(kil[1])
                    print("我出:", kill)
                    break
                elif (goal[i])[0] == "黑":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("黑桃")
                    黑.append(kil[1])
                    print("我出:", kill)
                    break
            elif int((goal[i])[2]) > 7:
                if (goal[i])[0] == "梅":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("梅花")
                    梅.append(kil[1])
                    print("我出:", kill)
                    break
                elif (goal[i])[0] == "菱":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("菱形")
                    菱.append(kil[1])
                    print("我出:", kill)
                    break
                elif (goal[i])[0] == "愛":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("愛心")
                    愛.append(kil[1])
                    print("我出:", kill)
                    break
                elif (goal[i])[0] == "黑":
                    card.remove(goal[i])
                    kill = goal.pop(i)
                    kil = kill.split("黑桃")
                    黑.append(kil[1])
                    print("我出:", kill)
                    break

    else:
        total = [com_梅, com_菱, com_愛, com_黑]
        for i in range(0, len(com_梅)):
            com_梅.append((com_梅[0])[1])
            com_梅.pop(0)
        for i in range(0, len(com_菱)):
            com_菱.append((com_菱[0])[1])
            com_菱.pop(0)
        for i in range(0, len(com_愛)):
            com_愛.append((com_愛[0])[1])
            com_愛.pop(0)
        for i in range(0, len(com_黑)):
            com_黑.append((com_黑[0])[1])
            com_黑.pop(0)

        com_梅 = list(map(int, com_梅))
        com_梅.sort()
        com_菱 = list(map(int, com_菱))
        com_菱.sort()
        com_愛 = list(map(int, com_愛))
        com_愛.sort()
        com_黑 = list(map(int, com_黑))
        com_黑.sort()
        for o in range(0, 4):
            if len(card) == 0:
                break
            if len(total[o]) == 0:
                continue
            if int((total[o])[-1]) <= 10 and int((total[o])[-1]) >= 9:
                if card == p2:
                    bad_p2.append(word[o] + str((total[o])[-1]))
                    p2_point.append(p2_point[-1] + int((total[o])[-1]))
                    card.remove(word[o] + str((total[o])[-1]))
                if card == p3:
                    bad_p3.append(word[o] + str((total[o])[-1]))
                    p3_point.append(p3_point[-1] + int((total[o])[-1]))
                    card.remove(word[o] + str((total[o])[-1]))
                if card == p4:
                    bad_p4.append(word[o] + str((total[o])[-1]))
                    p4_point.append(p4_point[-1] + int((total[o])[-1]))
                    card.remove(word[o] + str((total[o])[-1]))
                break
            else:
                if card == p2 and len(card) != 0:
                    bad_p2.append(word[o] + str((total[o])[0]))
                    p2_point.append(p2_point[-1] + int((total[o])[0]))
                    card.remove(word[o] + str((total[o])[0]))
                if card == p3 and len(card) != 0:
                    bad_p3.append(word[o] + str((total[o])[0]))
                    p3_point.append(p3_point[-1] + int((total[o])[0]))
                    card.remove(word[o] + str((total[o])[0]))
                if card == p4 and len(card) != 0:
                    bad_p4.append(word[o] + str((total[o])[0]))
                    p4_point.append(p4_point[-1] + int((total[o])[0]))
                    card.remove(word[o] + str((total[o])[0]))
                (total[o]).pop(0)
                break

        print("蓋牌")
    梅 = list(map(int, 梅))
    菱 = list(map(int, 菱))
    愛 = list(map(int, 愛))
    黑 = list(map(int, 黑))
    梅.sort()
    菱.sort()
    愛.sort()
    黑.sort()


def rule(card):
    if card == "0":
        kill = input("請輸入你要蓋哪張牌:")
        error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+", kill)
        while len(error) > 0 or kill == "" or int(kill) > len(player):
            kill = input('請輸入數字：')
            error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+", kill)
        while float(kill) > len(player):
            kill = input("你沒有這張牌,請重新選擇:")
        ans_1.append(kill)
        if len(player[int(kill) - 1]) == 4:
            player_point.append(int(player_point[-1]) + 10)
        elif (player[int(kill) - 1])[2] == "A":
            player_point.append(int(player_point[-1]) + 1)
        elif (player[int(kill) - 1])[2] == "J":
            player_point.append(int(player_point[-1]) + 11)
        elif (player[int(kill) - 1])[2] == "Q":
            player_point.append(int(player_point[-1]) + 12)
        elif (player[int(kill) - 1])[2] == "K":
            player_point.append(int(player_point[-1]) + 13)
        else:
            player_point.append(
                int(player[int(kill) - 1][2]) + int(player_point[-1]))
        bad_player.append(player[int(kill) - 1])
    else:
        ans_1.append(card)
        dre = player[int(card) - 1]
        deck.append(dre)
        if (player[int(card) - 1])[0] == "梅":
            if len(dre) == 3:
                梅.append(dre[2])
            else:
                梅.append("10")
        elif (player[int(card) - 1])[0] == "菱":
            if len(dre) == 3:
                菱.append(dre[2])
            else:
                菱.append("10")
        elif (player[int(card) - 1])[0] == "愛":
            if len(dre) == 3:
                愛.append(dre[2])
            else:
                愛.append("10")
        elif (player[int(card) - 1])[0] == "黑":
            if len(dre) == 3:
                黑.append(dre[2])
            else:
                黑.append("10")


#轉成數字
def num(card):
    for i in range(0, len(card)):
        if card[i] == "J":
            card[i] = '11'
        if card[i] == "Q":
            card[i] = '12'
        if card[i] == "K":
            card[i] = '13'
        if card[i] == "A":
            card[i] = '1'


#轉成字母
def letter(card):
    for o in range(0, len(card)):
        if card[o] == "11":
            card[o] = "J"
        if card[o] == "12":
            card[o] = "Q"
        if card[o] == "13":
            card[o] = "K"
        if card[o] == "1":
            card[o] = "A"


import re
from random import shuffle

suit = ["黑桃", "愛心", "菱形", "梅花"]
order = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
黑桃 = []
梅花 = []
菱形 = []
愛心 = []
梅 = ["7"]
菱 = ["7"]
愛 = ["7"]
黑 = ["7"]
com_梅 = []
com_菱 = []
com_愛 = []
com_黑 = []
total = [com_梅, com_菱, com_愛, com_黑]
number = [梅, 菱, 愛, 黑]
word = ["梅花", "菱形", "愛心", "黑桃"]
goal = []
count = 0
t = 0
ans_1 = [0]
player_point = [0]
bad_player = []
p2_point = [0]
bad_p2 = []
p3_point = [0]
bad_p3 = []
p4_point = [0]
bad_p4 = []
player1 = []
player = []
p2 = []
p3 = []
p4 = []
deck = []
for i in suit:
    for j in order:
        deck.append(i + j)

shuffle(deck)
while len(deck) != 0:
    player1.append(deck.pop())
    a = deck.pop()
    p2.append(a)
    if a[2] == "7":
        p2.pop(-1)
    a = deck.pop()
    p3.append(a)
    if a[2] == "7":
        p3.pop(-1)
    a = deck.pop()
    p4.append(a)
    if a[2] == "7":
        p4.pop(-1)

for j in range(0, len(player1)):
    wash = player1[j]
    if wash[0] == "梅":
        player.append(player1[j])
        change = player[0].split("梅花")
        player.pop(0)
        ##############
        if change[1] == "7":
            continue
        梅花.append(change[1])
        num(梅花)
        梅花 = list(map(int, 梅花))
        梅花.sort()
        梅花 = list(map(str, 梅花))
        letter(梅花)

for j in range(0, len(player1)):
    wash = player1[j]
    if wash[0] == "菱":
        player.append(player1[j])
        change = player[0].split("菱形")
        player.pop(0)
        ################
        if change[1] == "7":
            continue
        菱形.append(change[1])
        num(菱形)
        菱形 = list(map(int, 菱形))
        菱形.sort()
        菱形 = list(map(str, 菱形))
        letter(菱形)

for j in range(0, len(player1)):
    wash = player1[j]
    if wash[0] == "愛":
        player.append(player1[j])
        change = player[0].split("愛心")
        player.pop(0)
        ###########
        if change[1] == "7":
            continue
        愛心.append(change[1])
        num(愛心)
        愛心 = list(map(int, 愛心))
        愛心.sort()
        愛心 = list(map(str, 愛心))
        letter(愛心)
for j in range(0, len(player1)):
    wash = player1[j]
    if wash[0] == "黑":
        player.append(player1[j])
        change = player[0].split("黑桃")
        player.pop(0)
        ############
        if change[1] == "7":
            continue
        黑桃.append(change[1])
        num(黑桃)
        黑桃 = list(map(int, 黑桃))
        黑桃.sort()
        黑桃 = list(map(str, 黑桃))
        letter(黑桃)
for i in range(0, len(梅花)):
    梅花[i] = "梅花" + 梅花[i]
    player.append(梅花[i])
for i in range(0, len(菱形)):
    菱形[i] = "菱形" + 菱形[i]
    player.append(菱形[i])
for i in range(0, len(愛心)):
    愛心[i] = "愛心" + 愛心[i]
    player.append(愛心[i])
for i in range(0, len(黑桃)):
    黑桃[i] = "黑桃" + 黑桃[i]
    player.append(黑桃[i])

while len(player) != 0 or len(p2) != 0 or len(p3) != 0 or len(p4) != 0:
    print("\0", "--------------", "\n", "player1's turn", "\n",
          "--------------")
    print("\0", "梅花:", "\t", 梅, "\n", "菱形:", "\t", 菱, "\n", "愛心:", "\t", 愛,
          "\n", "黑桃:", "\t", 黑)
    print("\n", "目前點數:", player_point[-1])
    print("\0", "你已蓋的牌:", bad_player, "\n")
    for i in range(0, len(player)):
        if i == len(梅花) or i == len(梅花) + len(菱形) or i == len(梅花) + len(
                菱形) + len(愛心) or i == len(梅花) + len(菱形) + len(愛心) + len(黑桃):
            print("\n")
        print(i + 1, ':', end="")
        print(player[i], "\0", "\0", "\0", end="")
    print("\n")
    if len(player) != 0:
        ans = input("請輸入要出第幾張牌(蓋牌請輸入0):")
        while True:
            print("yes")
            try:
                print("number")
                int(ans)
                print('""')
                if ans == "":
                    raise
              
                ans = int(ans)
                print("yes")
                break
            except:
                ans = input("請重新輸入數字:")
                print("yes")

        if True:
            num(梅)
            梅 = list(map(int, 梅))
            梅.sort()
            梅 = list(map(str, 梅))
            num(菱)
            菱 = list(map(int, 菱))
            菱.sort()
            菱 = list(map(str, 菱))
            num(愛)
            愛 = list(map(int, 愛))
            愛.sort()
            愛 = list(map(str, 愛))
            num(黑)
            黑 = list(map(int, 黑))
            黑.sort()
            黑 = list(map(str, 黑))
            if int(ans) - 1 < len(梅花) and len(梅花) != 0:
                change = player[int(ans) - 1]
                a = change.split("梅花")
                if a[1] == "A":
                    a[1] = "1"
                if a[1] == "J":
                    a[1] = "11"
                if a[1] == "Q":
                    a[1] = "12"
                if a[1] == "K":
                    a[1] = "13"

                num(梅)
                num(菱)
                num(愛)
                num(黑)
                while int(a[1]) != int(梅[-1]) + 1 or int(
                        a[1]) != int(梅[0]) - 1:
                    if int(a[1]) == int(梅[-1]) + 1:
                        count += 1
                        break
                    if int(a[1]) == int(梅[0]) - 1:
                        count += 1
                        break
                    if int(a[1]) != int(梅[-1]) + 1 or int(
                            a[1]) != int(梅[0]) - 1:
                        ans = input("你現在還不能出這張牌,請輸入要出第幾張牌(蓋牌請輸入0):")
                        error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                           ans)
                        while len(error) > 0 or ans == "" or int(ans) > len(
                                player):
                            ans = input('請輸入數字：')
                            error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                               ans)
                        change = player[int(ans) - 1]
                        break
            elif int(ans) - 1 < len(梅花) + len(菱形) and len(菱形) != 0:
                change = player[int(ans) - 1]
                a = change.split("菱形")
                if a[1] == "A":
                    a[1] = "1"
                if a[1] == "J":
                    a[1] = "11"
                if a[1] == "Q":
                    a[1] = "12"
                if a[1] == "K":
                    a[1] = "13"
                while int(a[1]) != int(菱[-1]) + 1 or int(
                        a[1]) != int(菱[0]) - 1:
                    if int(a[1]) == int(菱[-1]) + 1:
                        count += 1
                        break
                    if int(a[1]) == int(菱[0]) - 1:
                        count += 1
                        break
                    if int(a[1]) != int(菱[-1]) + 1 or int(
                            a[1]) != int(菱[0]) - 1:
                        ans = input("你現在還不能出這張牌,請輸入要出第幾張牌(蓋牌請輸入0):")
                        error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                           ans)
                        while len(error) > 0 or ans == "" or int(ans) > len(
                                player):
                            ans = input('請輸入數字：')
                            error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                               ans)
                        break

            elif int(ans) - 1 < len(梅花) + len(菱形) + len(愛心) and len(愛心) != 0:
                change = player[int(ans) - 1]
                a = change.split("愛心")
                if a[1] == "A":
                    a[1] = "1"
                if a[1] == "J":
                    a[1] = "11"
                if a[1] == "Q":
                    a[1] = "12"
                if a[1] == "K":
                    a[1] = "13"
                while int(a[1]) != int(愛[-1]) + 1 or int(
                        a[1]) != int(愛[0]) - 1:
                    if int(a[1]) == int(愛[-1]) + 1:
                        count += 1
                        break
                    if int(a[1]) == int(愛[0]) - 1:
                        count += 1
                        break
                    if int(a[1]) != int(愛[-1]) + 1 or int(
                            a[1]) != int(愛[0]) - 1:
                        ans = input("你現在還不能出這張牌,請輸入要出第幾張牌(蓋牌請輸入0):")
                        error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                           ans)
                        while len(error) > 0 or ans == "" or int(ans) > len(
                                player):
                            ans = input('請輸入數字：')
                            error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                               ans)
                        break
            elif int(ans) - 1 < len(梅花) + len(菱形) + len(愛心) + len(黑桃) and len(
                    黑桃) != 0:
                change = player[int(ans) - 1]
                a = change.split("黑桃")
                if a[1] == "A":
                    a[1] = "1"
                if a[1] == "J":
                    a[1] = "11"
                if a[1] == "Q":
                    a[1] = "12"
                if a[1] == "K":
                    a[1] = "13"
                while int(a[1]) != int(黑[-1]) + 1 or int(
                        a[1]) != int(黑[0]) - 1:
                    if int(a[1]) == int(黑[-1]) + 1:
                        count += 1
                        break
                    if int(a[1]) == int(黑[0]) - 1:
                        count += 1
                        break
                    if int(a[1]) != int(黑[-1]) + 1 or int(
                            a[1]) != int(黑[0]) - 1:
                        ans = input("你現在還不能出這張牌,請輸入要出第幾張牌(蓋牌請輸入0):")
                        error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                           ans)
                        while len(error) > 0 or ans == "" or int(ans) > len(
                                player):
                            ans = input('請輸入數字：')
                            error = re.findall(r"[A-WY-Za-wy-z\u4e00-\u9fa5]+",
                                               ans)
                        break
        rule(ans)
        if player[int(ans_1[-1]) - 1][0] == "梅":
            player.remove(player[int(ans_1[-1]) - 1])
            梅花.pop()
        elif player[int(ans_1[-1]) - 1][0] == "菱":
            player.remove(player[int(ans_1[-1]) - 1])
            菱形.pop()
        elif player[int(ans_1[-1]) - 1][0] == "愛":
            player.remove(player[int(ans_1[-1]) - 1])
            愛心.pop()
        elif player[int(ans_1[-1]) - 1][0] == "黑":
            player.remove(player[int(ans_1[-1]) - 1])
            黑桃.pop()
        count = 0
    num(梅)
    梅 = list(map(int, 梅))
    梅.sort()
    梅 = list(map(str, 梅))
    letter(梅)
    num(菱)
    菱 = list(map(int, 菱))
    菱.sort()
    菱 = list(map(str, 菱))
    letter(菱)
    num(愛)
    愛 = list(map(int, 愛))
    愛.sort()
    愛 = list(map(str, 愛))
    letter(愛)
    num(黑)
    黑 = list(map(int, 黑))
    黑.sort()
    黑 = list(map(str, 黑))
    letter(黑)
    for i in range(0, len(梅)):
        if 梅[i] == "J":
            梅[i] = '11'
        if 梅[i] == "Q":
            梅[i] = '12'
        if 梅[i] == "K":
            梅[i] = '13'
        if 梅[i] == "A":
            梅[i] = '1'
    for i in range(0, len(菱)):
        if 菱[i] == "J":
            菱[i] = '11'
        if 菱[i] == "Q":
            菱[i] = '12'
        if 菱[i] == "K":
            菱[i] = '13'
        if 菱[i] == "A":
            菱[i] = '1'
    for i in range(0, len(愛)):
        if 愛[i] == "J":
            愛[i] = '11'
        if 愛[i] == "Q":
            愛[i] = '12'
        if 愛[i] == "K":
            愛[i] = '13'
        if 愛[i] == "A":
            愛[i] = '1'
    for i in range(0, len(黑)):
        if 黑[i] == "J":
            黑[i] = '11'
        if 黑[i] == "Q":
            黑[i] = '12'
        if 黑[i] == "K":
            黑[i] = '13'
        if 黑[i] == "A":
            黑[i] = '1'

    if len(p2) != 0:
        com(p2)
        goal = []
    if len(p3) != 0:
        com(p3)
        goal = []
    if len(p4) != 0:
        com(p4)
        goal = []
    num(梅)
    梅 = list(map(int, 梅))
    梅.sort()
    梅 = list(map(str, 梅))
    letter(梅)
    num(菱)
    菱 = list(map(int, 菱))
    菱.sort()
    菱 = list(map(str, 菱))
    letter(菱)
    num(愛)
    愛 = list(map(int, 愛))
    愛.sort()
    愛 = list(map(str, 愛))
    letter(愛)
    num(黑)
    黑 = list(map(int, 黑))
    黑.sort()
    黑 = list(map(str, 黑))
    letter(黑)
print("遊戲結束")
print("你蓋了", len(bad_player), "張牌", "\n", "共", player_point[-1], "點")
to = [bad_player, bad_p2, bad_p3, bad_p4]
total = [player_point[-1], p2_point[-1], p3_point[-1], p4_point[-1]]
tt = [player_point[-1], p2_point[-1], p3_point[-1], p4_point[-1]]
winner = ["player1", "player2", "player3", "player4"]
total.sort()
for i in range(1,4):
    for a in range(0,len(to[i])):
        c = list(to[i][a])
        if len(c) == 3:
            if c[2] == "1":
                to[i][a] = c[0]+c[1]+"A"
        if len(c) == 4:
            if c[2]+c[3] == "11" and len(c) == 4:
                to[i][a] = c[0]+c[1]+"J"
            elif c[2]+c[3] == "12" and len(c) == 4:
                to[i][a] = c[0]+c[1]+"Q"
            elif c[2]+c[3] == "13" and len(c) == 4:
                to[i][a] = c[0]+c[1]+"K"
c = 0
b = []
for i in tt:
    if i not in b:
        b.append(i)
if b == tt:
    for o in range(0, 4):
        for i in range(0, 4):
            if total[0] == tt[i] and c == 0:
                print("第一名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:",to[i])
                c += 1
            elif total[1] == tt[i] and c == 1:
                print("第二名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:",to[i])
                c += 1
            elif total[2] == tt[i] and c == 2:
                print("第三名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:",to[i])
                c += 1
            elif total[3] == tt[i] and c == 3:
                c += 1
                print("第四名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:",to[i])
for i in range(0, 4):
    a = tt.count(tt[i])
if b != tt:

        for i in range(0, 4):
            if total[0] == tt[i]:
                print("第一名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:", to[i])
            elif total[1] == tt[i]:
                print("第二名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:", to[i])
            elif total[2] == tt[i]:
                print("第三名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:", to[i])
            elif total[3] == tt[i]:
                print("第四名\t", winner[i], "共蓋了:", (tt[i]), "點\0蓋的牌:", to[i])
