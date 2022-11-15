def text():
    print("1.Сколько байт и бит займёт слово?")
    print("2.Сколько символов в слове?")
    print("3.Сколько байт в символе?")
    if n==1:
        b=int(input("Сколько символов="))
        c=int(input("Сколько байт в одном символе="))
        a=b*c
        print(str(a) + "Байт")
    elif n==2:
        a=int(input("Сколько байт="))
        c=int(input("Сколько байт в ожном символе="))
        b=a/c
        print(str(b) + "Символов")
    elif n==3
        a=int(input("Сколько байт="))
        b=int(input("Сколько символов=")
        c=a/b
        print(str(c) + "Байт в одном символе")
    else:
        print("Введите данную цифру")
              
def zvyk():
    print("1.Размер аудиофайла")
    print("2.Частота")
    print("3.Время звучания")
    print("4.Разрядность регистра") 
    if n==1:
        D=int(input("Частота="))
        T=int(input("Время звучания="))
        I=int(input("Разряднсть регистра=")
        a=D*T*I/8
        print(str(a) + "Байт")
    elif n==2:
        A=int(input("Размер="))
        T=int(input("Время звучания="))
        I=int(input("Разряднсть регистра=")
        D=8*A/(T*I)
        print(str(D) + "Время звучания")
    elif n==3
        D=int(input("Частота="))
        T=int(input("Время звучания="))
        A=int(input("Размер=")
        I=8*A/(T*D)
        print(str(I) + "Разрядность регистра")
    elif n==4
        D=int(input("Частота="))
        A=int(input("Размер="))
        I=int(input("Разряднсть регистра=")
        T=A*8/(D*I)
        print(str(T) + "Время звучания")
    else:
        print("Введите данную цифру")
def izobr():
    print("1.a")
    print("2.b")
    print("3.C")
    if n==1:
        b=int(input("b="))
        c=int(input("c="))
        a=b*c
        print(a)
    elif n==2:
        a=int(input("a="))
        c=int(input("c="))
        b=a/c
        print(b)
    elif n==3
        a=int(input("a="))
        b=int(input("b="))
        c=a/b
        print(c)
    else:
        print("Введите данную цифру")
