from datetime import datetime
from win10toast import ToastNotifier  # Módulo responsável pela notificação
import time


"""
   --- DESPERTADOR ---
   # feito por Douglas Costa
   # github: https://github.com/Douglas44
   # discord: $!doug_men!$#1750
   
"""

now = datetime.now()
hora = now.hour
minutos = now.minute
segundos = now.second

def main():   # Iniciando o programa #
    despertar_hora = 0
    despertar_minuto = 0
    now = datetime.now()
    hora = now.hour
    minutos = now.minute
    print(f"Horário atual: {hora}:{minutos}:{segundos}")
    while True:   # verificando caso dê erro #
        try:
            opcao = int(input("Deseja iniciar seu despertador[1 -- sim, 0 -- não]?: "))
            break
        except:
            print("Error! tente novamente...")
    while opcao:
        horario()
        despertar()
        while True:  # verificando caso dê erro #
            try:
                opcao = int(input("Deseja iniciar seu despertador[1 -- sim, 0 -- não]?: "))
                break
            except:
                print("Error! tente novamente...")
        if opcao == 0:
            print("Encerrando....")
            print(time.sleep(2))

def horario():    # hora e minuto para despertar #
    global despertar_hora, despertar_minuto

    while True:
        try:
            despertar_hora = int(input("Hora para despertar: "))
            despertar_minuto = int(input("Minuto para despertar: "))
            break
        except:
            print("Erro! tente novamente....")


def despertar():   # função para despertar quando atingir o horario #
    global despertar_hora, despertar_minuto, hora, minutos, segundos, tot

    print(f"Horário para despertar: --> {despertar_hora}:{despertar_minuto}")
    while True:
        now = datetime.now()
        hora = now.hour
        minutos = now.minute
        segundos = now.second

        if hora == despertar_hora:
            if minutos == despertar_minuto:
                notifier = ToastNotifier()
                notifier.show_toast('Despertador :)', 'O tempo chegou ao limite', duration=10)
                break
main()  # Chamando a função principal #

print(">>> VOLTE SEMPRE <<<")
input()
