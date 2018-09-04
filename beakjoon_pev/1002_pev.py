import math
case = input()
case = float(case)
case1 = case
i = 0
while case > 0:
    x1, y1, r1, x2, y2, r2 = map(float, input().split())
    x = x1-x2
    y = y1-y2
    disx = math.pow(x,2)
    disy = math.pow(y,2)
    pow_distance = disx+disy
    dis1 = pow(r2+r1,2)
    dis2 = pow(r2-r1,2)
    if x1==x2 and y1==y2 and r1==r2:
        b = [-1]
        print(b[0])
    elif (dis2 == pow_distance) or (dis1 == pow_distance) or (pow_distance == 0 and dis1 == dis2):
        b = [1]
        print(b[0])
    elif dis1 < pow_distance or pow_distance < dis2 or (pow_distance == 0 and dis1 != dis2):
        b = [0]
        print(b[0])
    elif dis2 < pow_distance < dis1:
        b = [2]
        print(b[0])

    else:
        b = [-100]
        print(b[0])
    case = case-1

