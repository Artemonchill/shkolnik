import math
def text():
    print("1.Сколько байт и бит займёт слово?")
    print("2.Сколько символов в слове?")
    print("3.Сколько байт в символе?")
    n=int(input())
    if n==1:
        b=int(input("Сколько символов="))
        c=int(input("Сколько байт в одном символе="))
        if b<=0 or c<=0:
            print ("Введите нормально")
            text()
        else:
            a=b*c
            print(str(a) + "Байт")
    elif n==2:
        a=int(input("Сколько байт="))
        c=int(input("Сколько байт в ожном символе="))
        if a<=0 or c<=0:
            print ("Введите нормально")
            text()
        else:
            b=a/c
            print(str(b) + "Символов")
    elif n==3:
        a=int(input("Сколько байт="))
        b=int(input("Сколько символов="))
        if a<=0 or b<=0:
            print ("Введите нормально")
            text()
        else:
            c=a/b
            print(str(c) + "Байт в одном символе")
    else:
        print("Введите данную цифру")
              
def zvyk():
    print("1.Размер аудиофайла")
    print("2.Частота")
    print("3.Время звучания")
    print("4.Разрядность регистра")
    n=int(input())
    if n==1:
        D=int(input("Частота="))
        T=int(input("Время звучания="))
        I=int(input("Разряднсть регистра="))
        if I<=0 or T<=0 or D<=0:
            print ("Введите нормально")
            zvyk()
        else:
            a=D*T*I/8
            print(str(a) + "Байт")
    elif n==2:
        A=int(input("Размер="))
        T=int(input("Время звучания="))
        I=int(input("Разряднсть регистра="))
        if I<=0 or T<=0 or A<=0:
            print ("Введите нормально")
            zvyk()
        else:
            D=8*A/(T*I)
            print(str(D) + "Время звучания")
    elif n==3:
        D=int(input("Частота="))
        T=int(input("Время звучания="))
        A=int(input("Размер="))
        if T<=0 or D<=0 or A<=0:
            print ("Введите нормально")
            zvyk()
        else:
            I=8*A/(T*D)
            print(str(I) + "Разрядность регистра")
    elif n==4:
        D=int(input("Частота="))
        A=int(input("Размер="))
        I=int(input("Разряднсть регистра="))
        if I<=0 or D<=0 or A<=0:
            print ("Введите нормально")
            zvyk()
        else:
            T=A*8/(D*I)
            print(str(T) + "Время звучания")
    else:
        print("Введите данную цифру")
def izobr():
    print("1.Объём видеопамяти")
    print("2.Глубина цвета")
    print("3.Разрешение экрана")
    print("4.Колличество цветов")
    n=int(input())
    if n==1:
        I=int(input("Глубина цвета="))
        X=int(input("Колличество пикселей по горизонтали="))
        Y=int(input("Колличество пикселей по вертикали="))
        if I<=0 or X<=0 or Y<=0:
            print ("Введите нормально")
            izobr()
        else: 
            V=I*X*Y
            print(V)
    elif n==2:
        K=int(input("Колличество цветов="))
        if K<=0:
            print ("Введите нормально")
            izobr()
        else:
            I=math.log(I,2)
            print(I)
    elif n==3:
        V=int(input("Объём видеопамяти="))
        I=int(input("b="))
        if V<=0 or I<=0:
            print ("Введите нормально")
            izobr()
        else:
            X=V/I
            print(X)
    elif n==4:
        I=int(input("Глубина цвета="))
        if I<=0:
            print ("Введите нормально")
            izobr()
        else:
            K=2**I
            print(K)        
    else:
        print("Введите данную цифру")
def menu1():
    print("1.Текстовые задачи")
    print("2.Звуковые задачи")
    print("3.Графические задачи")
    a=int(input("Что вам нужно?"))
    if a==1:
        text()
    elif a==2:
        zvyk()
    elif a==3:
        izobr()
    else:
        print("Введи нормально")
while 1 > 0:
    menu1()