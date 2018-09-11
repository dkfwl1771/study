def palindrome(n) : # if palindrome num return True
    i=0
    time=(str(n)).__len__()
    if(n==1):
        return False
    if(n<10):  # 2~9 num 
        return True  
    while i<time-1 :# 10 > i 
        if (str(n))[i]!=(str(n))[(-i)-1] : #first num and last num compare and second last scond num compare
            return False      
        i=i+1
    return True #if not false when last while number return true

def prime_num(n): #when prime num return true
    i = 2
    while i<n :
        if  n%i == 0:
            return False
        i=i+1
    return True

num = input()
caseLeng = num.__len__()
num = int(num)
while(num<=1004000) : #more bigger num than input num
    if (num<=0):
        break
    if (palindrome(num)): 
        if (prime_num(num)): 
            print(num)
            break
    num=num+1
        
