from botcity.core import DesktopBot

bot = DesktopBot()

# Procura um processo pelo nome ou PID
processo = bot.find_process("Calculator")

# Se encontrou, encerra
if processo:
    bot.terminate_process(processo)
    print("Processo encerrado.")
else:
    print("Processo não encontrado.")