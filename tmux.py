# tmux
# sudo apt-get install python3-tk python3-dev
# pip install PyAutoGUI
from pyautogui import write, press, hotkey, alert
from time import sleep

TIPOSDESESIONES = ['angular', 'react', 'node']

def tipoSesiones(tipo):
    hotkey('ctrl', 'a')
    write(f":rename-session {tipo}")
    press('enter')
    write("code .")
    press('enter')

def mongoBase():
    mongo = input("Usaras mongo? [s / n]").lower()
    if mongo == 's':
        write("mongodb-compass </dev/null &>/dev/null &")
        press('enter')

def configuracionSesion(tipo):
    if(tipo == TIPOSDESESIONES[0]):
        write("tmux split-window -v")
        press('enter')
        write("ng serve")
        press('enter')
    elif(tipo == TIPOSDESESIONES[1]):
        write("tmux split-window -v")
        press('enter')
        write("npm start")
        press('enter')
    elif(tipo == TIPOSDESESIONES[2]):
        write("tmux split-window -v")
        press('enter')
        write("postman </dev/null &>/dev/null &")
        press('enter')
        write("nodemon app")
        press('enter')


def main():
    print(f"Sessiones {TIPOSDESESIONES}")
    sesion = input("Que sesión\n").lower()
    if sesion in TIPOSDESESIONES:
        if sesion == TIPOSDESESIONES[2]:
            mongoBase()
        tipoSesiones(sesion)
        configuracionSesion(sesion)
    else:
        alert(f"Opciones {TIPOSDESESIONES}")


if __name__ == '__main__':
    main()