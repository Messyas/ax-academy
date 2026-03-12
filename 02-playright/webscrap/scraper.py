import asyncio
import json
from playwright.async_api import async_playwright

URL_PORTAL = "https://news.ycombinator.com"
PAGS = 3
FILE = "noticias.json"


async def raspar_pagina(page, url):
    await page.goto(url)
    await page.wait_for_selector('.athing')

    noticias = []

    # .all -> devolver um lista de todas ou todos os links que possuem um determinado seletor DOM
    itens = await page.locator('.athing').all()

    for item in itens:
        link = item.locator('.titleline > a')
        titulo = await link.inner_text()  # pega o titulo da noticia
        l = await link.get_attribute('href')  # pega o link da noticia
        item_id = await item.get_attribute('id')  # pega o id da noticia
        score_l = page.locator(f'#score_{item_id}')  # pega o DOM que contem o score da noticia

        try:
            score_text = await score_l.inner_text(timeout=2000)
            score = int(score_text.replace('points', '').replace('point', ''))
        except Exception:
            score = 0

        noticias.append({
            'titulo': titulo,
            'link': l,
            'score': score,
        })

    return noticias


async def main():
    todas_noticias = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        url = URL_PORTAL

        for pagina in range(1, PAGS + 1):
            print(f'[Pagina {pagina}/{PAGS}] Acessando: {url}')
            noticias = await raspar_pagina(page, url)
            todas_noticias.extend(noticias)
            print(f'{len(noticias)} noticias coletadas.')

            if pagina < PAGS:
                more_link = page.locator('a.morelink')
                href = await more_link.get_attribute('href')
                url = f'{URL_PORTAL}/{href}'

        await browser.close()

    # pos-processamento
    # ordenar a lista de noticias
    todas_noticias.sort(key=lambda x: x['score'], reverse=True)
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(todas_noticias, f, ensure_ascii=False, indent=2)

    total = len(todas_noticias)
    print(f'Concluido\nTotal de {total} noticias salvas no arquivo.')
    print('Top 3 noticias mais votadas:')
    for n in todas_noticias[:3]:
        print(f"{n['score']} pts | {n['titulo'][:50]}")


if __name__ == '__main__':
    asyncio.run(main())