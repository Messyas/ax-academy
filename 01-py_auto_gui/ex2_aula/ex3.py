# Melhoria 3: Fechar sem depender de atalhos de menu
# Problema: alt+a e depois s depende do idioma do Notepad/menu (PT/EN) e de como o Windows está configurado.
# É um dos trechos que mais quebra.
# Melhoria: usar Alt+F4 (padrão universal)

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
# verificando qual pasta existe.
home_path = Path.home()
desktop_path = home_path / "Documents"
if not desktop_path.is_dir():
    desktop_path = home_path / "Documentos"

time.sleep(1.0)

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
arquivo_txt = desktop_path / f"caso_rpa_notepad_{stamp}.txt"

pag.hotkey("ctrl", "s")
time.sleep(1.0)

# digita o caminho completo e confirma
pag.write(str(arquivo_txt))
time.sleep(0.2)
pag.press("enter")
time.sleep(1.0)

# Fechar Bloco de Notas
pag.hotkey("alt", "F4")
time.sleep(0.3)

print("Concluído.")
print("Arquivo TXT:", arquivo_txt)
