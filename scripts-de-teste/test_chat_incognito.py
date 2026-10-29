# Opens the public Nu Explica site in a fresh (incognito-equivalent) Edge context,
# opens the chat widget and prints the exact greeting text shown.
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://orgfarm-821eaec6c3-dev-ed.develop.my.site.com/nuexplica/"
OUT = Path(sys.argv[1])


def frames_report(page):
    rows = []
    for frame in page.frames:
        try:
            text = frame.locator("body").inner_text(timeout=2000)
        except Exception:
            text = "<sem acesso>"
        rows.append((frame.name, frame.url[:90], " ".join(text.split())[:300]))
    return rows


with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    context = browser.new_context(viewport={"width": 1280, "height": 900}, locale="pt-BR")
    page = context.new_page()
    page.goto(URL, wait_until="load", timeout=90000)
    page.wait_for_timeout(8000)

    print("== frames antes do clique")
    for row in frames_report(page):
        print(row)

    page.frame(name="embeddedMessagingFrame").get_by_text("Ask Me Anything").first.click(timeout=30000)
    print("clicou no botão do widget")

    greeting = ""
    for _ in range(30):
        page.wait_for_timeout(2000)
        for name, url, text in frames_report(page):
            if "Oi" in text:
                greeting = text
        if greeting:
            page.wait_for_timeout(20000)
            break
    page.screenshot(path=str(OUT / "3-chat-20s.png"))
    print("== frames depois do clique")
    for row in frames_report(page):
        print(row)
    browser.close()
