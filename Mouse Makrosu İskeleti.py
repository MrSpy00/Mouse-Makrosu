import mouse
import time

mouse_hareketleri = []
mouse.hook(mouse_hareketleri.append)

time.sleep(5)

mouse.unhook(mouse_hareketleri.append)
mouse.play(mouse_hareketleri)
