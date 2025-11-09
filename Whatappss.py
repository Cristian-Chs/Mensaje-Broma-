import pyautogui as pg
import time

time.sleep(5)

text = open('Broma.txt','r')

a = 'Mensaje de prueba'

for i in text:
  pg.write(a + ' ' + i )
  pg.press('Enter')