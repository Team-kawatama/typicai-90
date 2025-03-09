N,L=map(int,input().split())
K = int(input())
A = list(map(int,input().split()))
A.append(L) #最後のピースの判定
def split(pieces,minW):
    can = 0
    side = 0 #前のピースをどこで切ったか
    for i in range(N+1):
        if (A[i]-side)>=minW:
            side = A[i]
            can+=1
    if (can > pieces):
        return True
    else:
        return False

'''
めぐる式二分探索

特徴：ある1箇所で真偽値の切り替わる関数があるとき、
初期値を「確実に偽(right)」な位置と「確実に真(left)」な位置に配置する

その中央値をとり、それが「偽」ならば「偽の位置(right)」を動かす
「真」ならば「真の位置(left)」を動かす

それを差(right-left)が1まで繰り返す

↑真偽値の切り替わる地点の左側と右側が分かる

今回だと条件を満たさないといけないため「真(left)側」である
計算量は探索値に関わらずO(logN)
'''
left = 0
right = L
while right - left > 1:
    med = (left+right)//2
    if (split(K,med)):
        left = med
    else:
        right = med
print(left)
