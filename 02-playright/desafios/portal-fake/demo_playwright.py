from playwright.sync_api import sync_playwright

def main(): 
    query = 'tempo de manaus'
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context() #perfil anonimo temp
        #usuario existente:
        #content = browser.lauch_persistent_context('path_user'.temp, headless=False)
        page = content.new_page()
        
        page.goto('https://www.google.com/', wait_until='domcontentloaded')#quando todo o conteudo da pag for carregado
        
        try:
            page.locator('button:has-text("Aceitar tudo")').click(timeout=1000) #clicar no botão de aceitar cookies
        except:
            pass
        
        page.fill('//*[@id="APjFqb"]', query)   
        page.keyboard.press('Enter')
        page.wait_for_selector('#search', timeout=20000) #esperar o resultado da pesquisa carregar
        page.screenshot(path='hohoho.png', full_page=True)
        
        content.close()
        browser.close()
        
if __name__ == '__main__':
    main()  