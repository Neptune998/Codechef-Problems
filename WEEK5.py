from operator import itemgetter
list1, list2, list3 = [], [], []
a = input()
while True:

    if a == "Courses":
        a = input()
        while a != "Students":
            list1.append(a.split("~"))
            a = input()
    elif a == "Students":
        a = input()
        while a != "Grades":
            list2.append(a.split("~"))
            a = input()
    elif a=="Grades":
        a = input()
        while a != "EndOfInput":
            list3.append(a.split("~"))
            a = input()
    elif a == 'EndOfInput':
        break
    else:
        break
for i in range(len(list3)):
    if list3[i][4] == "A":
        list3[i][4] = 10
    elif list3[i][4] == "AB":
        list3[i][4] = 9
    elif list3[i][4] == "B":
        list3[i][4] = 8
    elif list3[i][4] == "BC":
        list3[i][4] = 7
    elif list3[i][4] == "C":
        list3[i][4] = 6

    elif list3[i][4] == "CD":
        list3[i][4] = 5
    else:
        list3[i][4] = 4

cnt = 1
sm = []
temp = 0
avg = 0

for i in range(len(list2)):
   temp = 0
   for j in range(len(list3)):
      if list2[i][0] == list3[j][3]:
         temp += list3[j][4]
         cnt += 1


   if cnt>=1:
       cnt-=1
   if cnt==0:
       avg=temp
   else:
       avg = temp/cnt
       ("%.2f"%avg)

   sm.append(avg)

   cnt=1

list4 = []
for i in range(len(list2)):

    list4.append(list2[i])

for i in range(len(list2)):
    list4[i].append(str(sm[i]))
list4.sort()
#print(list4)
for i in list4:
    print('~'.join(i))