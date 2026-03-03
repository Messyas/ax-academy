import subprocess
import time
from pathlib import Path
from datetime import datetime
import pyautogui as pag
import pygetwindow as gw

# Abrir Bloco de Notas
subprocess.Popen(['notepad.exe'])

# Espera abrir
titulos_possiveis = ['Bloco de Notas', 'Notepad']
print('Aguardando o Notepad abrir... ')
while True:
    notepad_aberto = any(gw.getWindowsWithTitle(t)
        for t in titulos_possiveis)
    if notepad_aberto:
        print('Notepad está aberto. Saindo do bot.')
        break
    time.sleep(0.5)

# Escrever mensagem
agora = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
time.sleep(0.1)
mensagem = f"Estudo de caso RPA - Windows + PyAutoGUI + na Data: {agora}\n"
time.sleep(0.1)
pag.write(mensagem, interval=0.01)
time.sleep(0.3)

# Salvar no Documents do usuário
# verificando qual pasta existe.
home_path = Path.home()
desktop_path = home_path / "Documents"
if not desktop_path.is_dir():
    desktop_path = home_path / "Documentos"

time.sleep(0.3)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
time.sleep(1)
arquivo_txt = desktop_path / f"caso_rpa_notepad_{stamp}.txt"

#antes de salvar printa
time.sleep(1)

# Salvar a tela inteira em arquivo
pag.screenshot('notepad.png')
time.sleep(2)

pag.hotkey("ctrl", "s")
time.sleep(1.0)

# digita o caminho completo e confirma
pag.write(str(arquivo_txt))
pag.press("enter")

# garantir que salvou
time.sleep(1.5)

# Força a janela a ter foco
pag.press('alt')
time.sleep(0.5)

# fiz desmembrado pq hotkeys tava dando erro no meu note
pag.keyDown("alt")
pag.press("f4")
pag.keyUp("alt")

print("Concluído.")
print("Arquivo TXT:", arquivo_txt)