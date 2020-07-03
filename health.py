from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open('mylogs.txt','a') as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_physical=time()
    watersecs=2400
    eyessecs=1800
    exercisesecs=3000
    while True:
        if time()-init_water > watersecs:
            print("water drinking time.Enter 'drank' to stop alarm")
            musiconloop('water.mp3','drank')
            init_water=time()
            log_now('Drank water at')
        if time()-init_eyes > eyessecs:
            print("Eyes exercise time.Enter 'done' to stop alarm")
            musiconloop('eyes.mp3','done')
            init_eyes=time()
            log_now('Done eyes exercise at')
        if time()-init_physical > exercisesecs:
            print("normal exercise time.Enter 'done' to stop alarm")
            musiconloop('physical.mp3','done')
            init_physical=time()
            log_now('Done normal exercise at')
            
