print(123)

#입력
count = input("숫자를 입력하세요")
print(count)

print(3<5)

#int 정수/ float 실수
a = int(input("숫자를 입력하세요"))
b = float(input("숫자"))
print(a, b)

print(2*3)  
print(7/2)   #값
print(7//2)   #몫
print(7%2)   #나머지

print("문자열"+"입니당")
print("안녕"*3)

print(True and True)  #and는 둘다
print(True or False)
print(True and False)
print(True or True)    #둘중하나
print(not True)

game = 60
win = 30

print(game>=60 and win>=59)

fruit = ['apple','pineapple','berry'] #0번부터시작
print(fruit)

fruit.append('mango')
print(fruit)

fruit.sort() #정렬
print(fruit)

print(fruit.count("apple"))  #몇개있는지

print(fruit[0])

fruit[0]="사과"

print(fruit)