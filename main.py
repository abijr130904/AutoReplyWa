from playwright.sync_api import sync_playwright
import time
from ai_module import ai_response


def main():
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(channel="chrome", headless=False)

        page = browser.new_page()
        page.goto("https://web.whatsapp.com")

        print("Silakan scan QR Code WhatsApp Web...")
        time.sleep(15)  # waktu buat scan

        last_seen_msg = ""

        while True:
            try:
                # Ambil semua pesan masuk (message-in)
                messages = page.query_selector_all("div.message-in span.selectable-text")

                if messages:
                    last_msg = messages[-1].inner_text()

                    # Hanya balas jika ada pesan baru
                    if last_msg != last_seen_msg:
                        print("Pesan masuk:", last_msg)

                        # Dapatkan balasan AI
                        reply = ai_response(last_msg)
                        print("Balasan:", reply)

                        # Kirim balasan ke chat aktif
                        input_box = page.query_selector("div[contenteditable='true'][data-tab='10']")
                        input_box.click()
                        input_box.fill(reply)
                        input_box.press("Enter")

                        last_seen_msg = last_msg

            except Exception as e:
                print("Error:", e)

            time.sleep(5)  # cek setiap 5 detik


if __name__ == "__main__":
    main()
