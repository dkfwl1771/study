case = input()
case = int(case)
case1 = case
i = 1
while case > 0:
    num1, num2 = map(int, input().split())
    middle_num=num1+num2
    cont_number=0
    if  num1 < 0 :
        if num2 < 0:
            cont_number=abs(num1)-abs(num2)+1
        else :
            cont_number=abs(num1)+abs(num2)+1
    else :
        cont_number=abs(num2)-abs(num1)+1

    answer = float(middle_num*(cont_number/2))
    print(int(cont_number/2))
    s_i = str(i)
    print("Scenario #"+s_i+":")
    answer = int(answer)
    print(answer)
    print()
    case = case-1
    i= i+1


