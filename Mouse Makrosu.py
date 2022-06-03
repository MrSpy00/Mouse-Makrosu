import mouse
import time
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.CYAN)
print("Mouse Makrosu Başlıyor...")
time.sleep(1.4)
süre = int(input("Mouse Makrosu kaç saniye olsun ---> "))

mouse_hareketleri = []
mouse.hook(mouse_hareketleri.append)


time.sleep(süre/4)
print("Sürenin"+str(süre/4)+"Bitti")
time.sleep(süre/4)
print("Sürenin"+str(süre/2)+"Bitti")
time.sleep(süre/4)
print("Sürenin"+str(süre/3)+"Bitti")
time.sleep(süre/4)
print("Sürenin"+str(süre/1)+"Bitti")


mouse.unhook(mouse_hareketleri.append)
time.sleep(1)
print(Fore.GREEN)
print("Mouse kaydı başlatılıyor..")
time.sleep(2)
mouse.play(mouse_hareketleri)
print("İyi Günler Dilerim..")
time.sleep(1)
exit()
