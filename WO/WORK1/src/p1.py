#  Downloading the following - https://playwright.dev/python/docs/introduction

from playwright.sync_api import sync_playwright
from datetime import datetime, timezone

# Target and userAgent
url = "https://www.coingecko.com/"
uA = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"


# Actual Code here
def m_F1():
    """ALl operations will be in this function"""
    with sync_playwright() as p:
        # Launch broser
        br1 = p.chromium.launch()

        # Create a new page
        page1 = br1.new_page(user_agent=uA)

        # Visit the page specified
        page1.goto(url)

        # Create sreenshot - wih current date time
        c_d = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        page1.screenshot(path=f"clicks/{c_d}-s1.png", full_page=True)

        # Close the browser
        br1.close()
