

**Cloudflare Turnstile Automation**
This project was built for data scraping, specifically to work with the latest Cloudflare Turnstile challenge.

**What does it do?**
instance.py loads a Cloudflare Turnstile-protected webpage using pywebview.
If the Turnstile challenge is solved automatically, the script sends the cf_value to the Flask server (server.py).
If the challenge is not solved automatically, the script uses pyautogui to click on the Turnstile challenge.
**How to use:**
Run instance.py. If you need multiple cf_token values simultaneously, you can create multiple instances by copying the script.
Run server.py to start the Flask server.
**Notes:**
The pyautogui clicking mechanism is set up by measuring the coordinates on my own LCD screen. To make it work for you, you must place the Turnstile challenge in the same location on your screen or adjust the coordinates accordingly.
![cf](https://github.com/user-attachments/assets/171346ff-1b70-41b8-af20-fd800d109886)




