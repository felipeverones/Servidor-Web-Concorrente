from threading import Thread
from time import sleep

def minha_funcao(arg):
    for i in range(arg):
        print("executando dentro de um outro thread...")
        sleep(1)
        
        
if __name__ == "__main__":
    thread = Thread(target = minha_funcao, args = (20, ))
    thread.start()
    for i in range(20):
        print("executando no thread principal...")
        sleep(0.5)
    print("for principal finalizou")
    thread.join()
    print("Thread finalizou...")
    
