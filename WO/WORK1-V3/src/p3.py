# This is p2.py code which has been made into a function to get screenshots

from playwright.sync_api import sync_playwright
from datetime import datetime, timezone

# Target and userAgent
urls = [
    "https://www.coingecko.com/",
    "https://www.coinwatch.com/",
    "https://www.meanbitches.com/",
]
uA = "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"


def m_F3():
    """All operations will be in this function"""
    with sync_playwright() as p:
        # Launch browser
        br1 = p.chromium.launch()

        # Create a new browser context
        context_config = {
            "record_video_dir": "clicks/",
            "user_agent": uA,
            "locale": "de-DE",
            "timezone_id": "Europe/Berlin",
        }
        context = br1.new_context(**context_config)

        # Loop through the URLs
        for index, url in enumerate(urls):
            # Create a new page
            page1 = context.new_page()

            # Start recording video
            c_d = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            context.video.start_recording(path=f"clicks/{c_d}-video{index+1}.webm")

            # Visit the page specified
            page1.goto(url)

            # Stop recording video
            context.video.stop_recording()

            # Create screenshot
            page1.screenshot(path=f"clicks/{c_d}-s{index+1}.png", full_page=True)

            # Close the page
            page1.close()

        # Close the context
        context.close()

        # Close the browser
        br1.close()


m_F3()
