from arduino_serial import Arduino
from banco_mysql import Banco
import time

PORTA = "COM5"
BAUDRATE = 9600
INTERVALO = 1.0

def principal ():
    arduino = Arduino (port = PORTA, baudrate = BAUDRATE)
    arduino.conexao_aberta ()
    bd = Banco ()
    bd.criar_tabela ()
    print ("Iniciando a leitura da Distância. Ctrl-C para parar")
    
    try:
        while True:
            #Enviando Requisição
            arduino.enviar ("REQ\n")
            
            #recebendo dados
            resposta = arduino.receber ()
            
            #imprimir o valor obtido
            print (f"Distância: {resposta} cm")
            
            #gravar bd
            bd.inserir_atualizar ("Kawann", 1, resposta)
            
            # time.sleep (INTERVALO)
            bd.listar ()
            
            #intervalo
            time.sleep (INTERVALO)
            
    except KeyboardInterrupt:
        print ("/nProgram interrompido pelo usuario!")
    except Exception as e:
        print (f"ERRO: {e}")
    finally:
        arduino.conexao_fechada ()
        print ("Conexão Fechada")

if __name__ == "__main__":
    principal ()