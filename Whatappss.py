import pyautogui as pg
import time

time.sleep(5)

text = open('mensaje.txt','r')

a = 'Te quiero mucho'

for i in text:
  pg.write(a + ' ' + i )
  pg.press('Enter')