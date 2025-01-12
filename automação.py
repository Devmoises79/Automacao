import pyautogui as pa
import time
import pyperclip


pa.PAUSE = 1


pa.press('win') #abre a janela do windows
pa.write('chrome') #escreve o nome do navegador
pa.press('ENTER') #entra no chrome
pa.write('youtube.com') #escreve o link do youtube
pa.press('enter') #entra no link
time.sleep(2) #espera 2 segundos
pa.click(x=550, y=200) #clica no campo de pesquisa

pa.write('curso em video') #escreve o que deseja pesquisar
pa.press('ENTER') #entra no link
time.sleep(2) #espera 2 segundos



