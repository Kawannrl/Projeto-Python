import serial
import time

porta = "COM5"
arduino = serial.Serial (porta, 9600, timeout = 1)
time.sleep (2)

while True:
    comando = input ("Digite 1 para ligar o 1° LED, 0 para desligar o 1° LED, 3 para ligar o 2° LED e 2  para desligar o 2° LED ou SAIR para encerrar o programa: ")
    if comando == '1':
        arduino.write (b'1')
        print ("1° LED Ligado!")
    elif comando == '0':
        arduino.write (b'0')
        print ("1° LED Desligado!")
    elif comando == '3':
        arduino.write (b'3')
        print ("2° LED Ligado!")
    elif comando == '2':
        arduino.write (b'2')
        print ("2° LED Desligado!")
    elif comando.lower () == 'sair':
        print ("Encerradno comunicação com o Arduíno")
        break
    else:
        print ("Comando Inválido!")
        
arduino.close ()