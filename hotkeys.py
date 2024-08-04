import keyboard
from datetime import datetime, timedelta
import os

start = datetime.now() # 00:00:00
log = f"tempos_gravacao_{datetime.now().strftime('%H-%M-%S')}.txt"


def resetTime():
    global start
    start = datetime.now() # novo 00:00:00

def parseTimeDelta(time: timedelta):
    hours = int(time.seconds / 60 / 60) % 24
    minutes = int(time.seconds / 60) % 60
    seconds = time.seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"

def writeToLog():
    time = datetime.now() - start
    timeStr = parseTimeDelta(time)
    print(timeStr)
    writeToFile(timeStr)

def writeToFile(time):
    with open(log, "a") as file:
        file.write(time + "\n")

hotkeys = dict()

# Tenta ler o arquivo config, se não existir cria um padrão
try:
    file = open("config.txt", "r")
except:
    print("config.txt não existe, criando um...")
    with open("config.txt", "a") as file:
        file.write("RESET = CTRL + SHIFT + F12\n")
        file.write("WRITE-LOG = CTRL + F11")

with open("config.txt", "r") as file:
    for line in file.readlines():
        command = line.split('=')[0].strip()
        hotkey = line.split('=')[1].strip()
        hotkeys[command] = hotkey

if "WRITE-LOG" in hotkeys.keys():
    keyboard.add_hotkey(hotkeys["WRITE-LOG"], writeToLog)

if "RESET" in hotkeys.keys():
    keyboard.add_hotkey(hotkeys["RESET"], resetTime)

keyboard.wait()