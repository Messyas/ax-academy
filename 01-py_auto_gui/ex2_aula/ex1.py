# Altere o código que abre o notepad, escreve um texto, salva e fecha o notepad
# Melhoria 1: abrir o notepad usando outra estratégia
# Abrir o notepad sem Win+R (menos frágil)
# Problema: Win+R + digitação depende muito do foco na janela e do tempo.
# Melhoria: abrir direto com subprocess.Popen(['notepad.exe']). É mais confiável e mais simples.
import subprocess
import time
from pathlib import Path
from datetime import datetime
import pyautogui as pag

# Abrir Bloco de Notas
subprocess.Popen(['notepad.exe'])

time.sleep(1)

# Escrever mensagem
agora = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
mensagem = "Estudo de caso RPA - Windows + PyAutoGUI\n"
pag.write(mensagem, interval=0.01)
time.sleep(0.3)

# Salvar no Documents do usuário
desktop = Path.home() / "Documents"
stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
arquivo_txt = desktop / f"caso_rpa_notepad_{stamp}.txt"

pag.hotkey("ctrl", "shift", "s")
time.sleep(1.0)

# digita o caminho completo e confirma
pag.write(str(arquivo_txt))
time.sleep(0.2)
pag.press("enter")
time.sleep(1.0)

# Fechar Bloco de Notas
pag.hotkey("alt", "a")
pag.press("s")
time.sleep(0.3)

print("Concluído.")
print("Arquivo TXT:", arquivo_txt)