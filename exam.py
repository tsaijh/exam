Answer = [0]*80
Question = range(1,81)
Option = ['A','B','C','D']
Number = 1
while Number in Question:
    while Number in Question:
        while Number in Question:
            what = input('輸入第%d題答案'%Number)
            if what in Option:
                Answer[Number-1] = what
                Number+=1
            else:
                try:
                    if int(what) in Question:
                        Number = int(what)
                    else:
                        break
                except:
                    print('請再次輸入答案')
        try:
            Number = input('確認交卷請按0，繼續作答請輸入題號')
            if int(Number) in Question:
                Number = int(Number)
                continue
        except:
            break
    counter = 1
    QuestionNumber = 0
    for check in Answer:
        if check==0:
            QuestionNumber = counter
            print('第%d題沒寫'%QuestionNumber)
        counter+=1
        Number = QuestionNumber
correctans = [0]*80
Number = 1
while Number in Question:
    while Number in Question:
        while Number in Question:
            what = input('輸入第%d題正確答案'%Number)
            if what in Option:
                correctans[Number-1] = what
                Number+=1
            else:
                try:
                    if int(what) in Question:
                        Number = int(what)
                    else:
                        break
                except:
                    print('請再次輸入答案')
        try:
            Number = input('確認不輸答案請按0，繼續請輸入題號')
            if int(Number) in Question:
                Number = int(Number)
                continue
        except:
            break
    counter = 1
    QuestionNumber = 0
    for check in correctans:
        if check==0:
            QuestionNumber = counter
            print('第%d題沒寫正確答案'%QuestionNumber)
        counter+=1
        Number = QuestionNumber       
score = 0
f = open('新寫的國考.txt','w')
f.close()
f = open('新寫的國考.txt','a')
for counter in range(1,81):
    if Answer[counter-1]!=correctans[counter-1]:
        C = '第%d答案寫%s，正確答案為%s'%(counter,Answer[counter-1],correctans[counter-1])
        f.writelines(C)
        f.write('\n')
        score+=1
wrong = '錯%d題'%score
f.write('\n')
f.writelines(wrong)
score = 100-score*1.25
S = '分數為%d分'%score
f.write('\n')
f.writelines(S)
f.write('\n')
f.write('\n')
blank = [5,11,17,23,29,35,41,47,53,59,65,71,77,83,89]
for i in blank:
    Answer.insert(i,'_')
    correctans.insert(i,'_')
f.writelines(Answer)
f.write('\n')
f.writelines(correctans)
f.close()
