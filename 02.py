'''
！！模範解答と違います！！

模範解答はbit全探索を用いた全探索です
個人的に、全探索嫌じゃね？

bit全探索はとっても有用
二進数に直したら001 010 011 100 101...となるのを利用して
n個において 選ぶ/選ばない を探索できるアルゴリズム
'''
N=int(input())

def kakko(open_,opened=0,retu = ""):
    if open_ == 0 and opened == 0: #即ち終わりを意味する
        print(retu)
    else:
        if (open_ != 0):
            kakko(open_-1,opened+1,retu+"(") #開く方が優先順位が高いのでこっちから
        if (opened != 0):
            kakko(open_,opened-1,retu+")")
#()とならないといけないのでNが奇数の場合は不可能　それ以外は可能
if (N%2 == 1):
    print()
else:
    kakko(N//2)
