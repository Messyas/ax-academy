"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()
    #bot.driver_path = r"resources\chromedriver.exe"

    # Configure whether or not to run on headless mode
    bot.headless = False

    bot.browse("https://quotes.toscrape.com/")
    bot.wait(1000)

    # Clica no link Next para ir para a próxima página
    # proxima_pagina = bot.find_element("ul.pager li.next a", By.CSS_SELECTOR)
    proxima_pagina = bot.find_element("li.next a", By.CSS_SELECTOR)

    if proxima_pagina is None:
        print("Não foi possível localizar o link da próxima página.")
        bot.stop_browser()
        return

    proxima_pagina.click()
    bot.wait(2000)

    # Captura todas as citações da nova página
    citacoes = bot.find_elements("div.quote span.text", By.CSS_SELECTOR)

    if citacoes is None:
        print("Não foi possível localizar a terceira citação da próxima página.")
        bot.stop_browser()
        return

    print("Terceira citação da próxima página:")
    print(citacoes[2].text)

    bot.wait(3000)
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK.",
    #     total_items=0,
    #     processed_items=0,
    #     failed_items=0
    # )

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()