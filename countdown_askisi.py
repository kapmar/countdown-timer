#ftiakse ena function me onoma countdown to opoio tha dexetai 1 argument seconds to opoio tha dinei o xristis
#sti sunexeia otan kaleitai auto to function tha ektupwnei tous arithmous apo to ton arithmo pou edwse o xristis os to 1 me 1 deuterolepto diafora
#telos tha ektupwnei ti leksi "finished" otan teliosei.
#SIMANTIKO-------- EAN O XRISTIS DOSEI OTIDIPOTE ALLO EKTOS APO THETIKO ARITHMO TO PROGRAMMA NA TOU LEEI OTI EKANE LATHOS KAI PREPEI NA TO TREKSEI KSANA

import time
def countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds-= 1
        time.sleep(1)
    print("teleiwsame")

xronos = input("posa theleis na metrisume anapoda: ")
if xronos.isdigit():
    xronos_int = int(xronos)
    countdown(xronos_int)
else:
    print("vale numero")