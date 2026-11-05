def torre_de_hanoi(discatuais, pinorigem, pindestino, pinaux):
    mov = 0
    if discatuais == 1:
        print(f"Mova o disco 1 de {pinorigem} para {pindestino}")
        mov += 1

    else:
        mov += torre_de_hanoi(discatuais - 1, pinorigem, pinaux, pindestino)
        print(f"Mova o disco {discatuais} de {pinorigem} para {pindestino}")
        mov += 1
        mov += torre_de_hanoi(discatuais - 1, pinaux, pindestino, pinorigem)
    return mov















def uno():
    ie = input("i.e mille uno?: ").strip().lower()
    if ie == "sim":
        print("isso ai sumsumsumsumsumsumsumsumsumsum")
    elif ie == "uno":
        ver = input("turbo, sx, ep?: ").strip().lower()
        if ver == "turbo":
            print("vroooom ptssssss.")
        elif ver == "sx":
            print("ruuummmvvvvrrrrrraaaammmmmmmm")
        elif ver == "ep":
            print("ó? olha isso aqui contem 2 cavalinhos a mais 🧐")
    elif ie in ["ie", "i.e"]:
        points = input("spi ou mpi?(multi ou single): ").strip().lower()
        if points in ["spi", "single"]:
            print("vamooo ruuummmrrrrrararrararaaammmmmm")
        elif points in ["mpi", "multi"]:
            print("sai daqui seu fã de palio")
        else:
            print("era do uno zé")
    elif ie == "mille":
        poin = input("fire ou fiasa?: ").strip().lower()
        if poin == "fiasa":
            print("vrrrraaaaaammmmm")
        elif poin == "fire":
            print("sai daq seu modinha")
        else:
            print("era do uno zé")
    else:
        print("vaza daq")



def samsung():
    print("sum sum")
    sum = input("sum sum?").strip().lower()
    if sum == "sum":
        print("sumsumsum[...] Samsung")
    elif sum == "sim":
        print("era sum seu zé")
    elif sum == "nao":
        print("sumsumsumsumsumsumsumsumsumsumsum [...]")
    elif sum == "s":
        print("era sum seu zé")
    elif sum == "":
        print("era sum seu zé")
    else:
        print("vaza daq")


def calc():
    print("")
    print("calculadora simples pq sim")
    num = int(input("primeiro algarismo: "))
    nu = int(input("segundo algarismo: "))
    
    som = nu + num
    sub = num - nu
    mul = num * nu
    while True:
        try:
            op = input("qual operação?(* + - /): ")
            if op in ["*", "multiplicação", "multiplicacao", "multiplicacão"]:
                print(mul, " 🥺👍")
                break
            elif op in ["+", "adição", "adicao", "adiçao"]:
                print(som, " 🥺👍")
                break
            elif op in ["/", "divisão"]:
                try:
                    div = num / nu
                    print(div, " 🥺👍")
                    break  # Só sai do loop se a divisão der certo
                except ZeroDivisionError:
                    print("Dividir por zero não dá, né zé? 🧐")
            elif op in ["-", "subtracao", "subtração", "subtraçao"]:
                print(sub, " 🥺👍")
                break
            else:
                print("digita operação man")
        except ValueError:
            print("digita operação zé")


while True:
    print("=" * 30)
    print("== U.C.S.H. Rev2.7 by:kazer43 ==")
    print("=" * 30)
    try:
        print("digite qual função do codig usar")
        print("uno, calc, hanoi ou sumsum?(digite 'sair' para sair): ")
        fu = input("digite função: ")
        if fu == "uno":
            uno()
        elif fu == "calc":
            calc()
        elif fu == "sumsum":
            samsung()
        elif fu in ["hanoi", "torre de hanoi", "torre", "hanoi"]:
            print("torre de hanoi")
            e = int(input("Digite o numero de discos: "))
            if e <= 0:
                print("não tem como fazer com 0 discos ou menos, né zé? 🧐")
                continue
            total = torre_de_hanoi(e, 'A', 'C', 'B')
            print(f"Total de movimentos: {total}")
            print("")
        elif fu in ["sair", "sai"]:
            print("saindo...")
            break
        else:
            print("digite a funçao: ")
            raise ValueError
    except ValueError:
        print("")
        print("SEU TADINHO 🥹")
        print("")