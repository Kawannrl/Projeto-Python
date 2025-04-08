import serial
import time
from banco import Banco

porta = "COM4"
arduino = serial.Serial(porta, 9600, timeout = 1)
time.sleep(2)

aluno = "Kawann"
led = 1
banco = Banco()
banco.criar_tabela()

while True:
    estado = banco.ler_estado (aluno)
    if estado.upper () == "LIGADO":
        arduino.write (b"1")
    else:
        arduino.write (b"0")
    #comando = input ("Digite 1 para ligar o LED e 0 para desligar o LED ou SAIR para encerrar o programa: ").upper()
    #match comando:
    #    case "1":
    #        #arduino.write (b'1')
    #        estado = "Ligado"
    #        banco.inserir_ou_atualizar_estado(aluno, led, estado)
    #        print("LED Ligado!")
    #    case "0":
    #        #arduino.write (b'0')
    #        estado = "Desligado"
    #        banco.inserir_ou_atualizar_estado(aluno, led, estado)
    #        print("LED Desligado!")
    #    case "2":
    #        banco.listar_estados ()
    #    case "SAIR":
    #        print("Encerrando comunicação com o Arduíno")
    #        break
        
arduino.close()