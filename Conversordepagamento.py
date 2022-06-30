from time import sleep
import os

def clear():
    os.system("cls") #Ou Clear depende muito

print('》》Conversor de pagamento《《')
print(" ")

while True:
    print("---" * 15)
    modo = int(input('''Modo: 1)Mensal 2)Semanal 3)Hora :'''))
    print(" ")
    clear()
    if modo == 3:
        salario = float(input('》》Digite o valor por hora:'))
        hr = int(input('》》horas trabalhada:'))
        hrextra = int(input('》》hora extra:'))
        salahr = salario * hr
        extra = hrextra * 2
        total = salahr + extra
        clear()
        print(" ")
        print('Voce recebe R${:.2f} por hora, voce trabalhou {}hrs e fez {} horas extra'.format(salario, hr, hrextra))
        print(" ")
        print('Seu salario atualizado é R${:.2f}'.format(total))
        print("---" * 15)
        print(" ")

        cont = int(input('Realizar nova consulta? 1 para sim e 0 para não:'))
        if cont == 1:
            clear()
            continue
        else:
            print("---" * 15)
            print('Sistema encerrado!!!')
            sleep(2)
            clear()
            break

    if modo == 1:
        salario = float(input('》》Digite o valor por dia:'))
        extra = int(input('》》Hora extra:'))
        dia = salario * 24
        hrextra = extra * 2
        total = dia + hrextra
        clear()
        print(" ")
        print('Você recebe R${:.2f} por dia, fez {} hora extra'.format(salario, extra))
        print('Seu salário atualizado é R${:.2f}'.format(total))

        cont = int(input('Realizar nova consulta? 1 para sim 0 e para não:'))
        if cont == 1:
            clear()
            continue
        else:
            print("---" * 15)
            print('Sistema encerrado!!!')
            sleep(2)
            clear()
            break

    if modo == 2:
        salario = float(input('》》Digite o valor por semana:'))
        extra = int(input('》》Horas extra:'))
        sem = salario * 5
        hrextra = extra * 2
        total = sem + hrextra
        clear()
        print(" ")
        print('Você recebe R${:.2f} por dia e fez {} hora extra'.format(salario, hrextra))
        print('Seu salario atualizado é R${:.2f}'.format(total))

        cont = int(input('Realizar nova consulta? 1 para sim e 0 para não:'))
        if cont == 1:
            clear()
            continue
        else:
            print("---" * 15)
            print('Sistema encerrado!!!')
            sleep(2)
            clear()
            break

    else:
        print('Código Inválido! tente novamente.')
        print("---" * 15)
        print(" ")
        sleep(2)
        clear()
        continue
