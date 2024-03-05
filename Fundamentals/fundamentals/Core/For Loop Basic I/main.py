##Basic## 
for i in range(151): 
    print(i) 

##Multiples of five## 

for i in range (1,1001): 
    if (i%5==0) :
        print(i) 

##Counting, the Dojo Way##
        
for i in range(1,101): 
    if i%10==0:
        print("Coding Dojo")  
    elif i%5==0:
        print("Coding")
    else :
        print(i) 

##Whoa. That Sucker's Huge##
sum_of_odds = 0
for i in range(0, 500001):
    if i % 2 != 0:
        sum_of_odds += i

print(sum_of_odds)

##Countdown by Fours##
num = 2018

while num > 0:
    if num > 0:
        print(num)
    num -= 4

##Flexible counter##
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)