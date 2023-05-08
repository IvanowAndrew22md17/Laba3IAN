x=int(input("Номер задачи: "))
a=0
b=0
c=0
d=0

#3.1
def f1():
    a = int(input("Введите количетво слов: "))
    b = []
    for i in range(a):
        b.append(str(input()))
    print(" ".join(b))
if x==1:
    f1()

#3.2
def f2():
    b =[]
    while (a := str(input())) != "stop":
        b.append(a)
    print(" ".join(b))
if x==2:
    f2()

#3.3
def f3():
    while (a := str(input())) != "stop":
        if "ф" in a or "Ф" in a:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
if x==3:
    f3() 

#3.4
def f4():
    e=0
    r=0
    while e != 3:
        from random import randint
        a = randint(1, 10)
        b = randint(1, 10)
        c = a + b
        print(a, "+", b, "=")
        d = int(input())
        if d==c:
            r = r + 1
            print("Правильно!")
        else:
            e = e + 1
            print("Ответ неверный")
    print("Игра окончена. Правильных ответов:", r)
if x==4:
    f4() 
if x< 0 or x > 4:
    print("Такой задачи нет(")