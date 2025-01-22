import webview
import time
import requests  # For sending CF value to Flask server
import pyautogui


url = "UrlHere"

# Python function to receive the CF value from JavaScript
def print_cf_value(cf):
    print(f"CF value found: {cf}")
    # Send the CF value to Flask server
    send_cf_to_server(cf)

# Function to send CF value to Flask server
def send_cf_to_server(cf):
    try:
        response = requests.post('http://127.0.0.1:5000/send_cf', json={'cf': cf})
        if response.status_code == 200:
            print(f"Successfully sent CF value {cf} to server")
        else:
            print(f"Failed to send CF value. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending CF value to server: {e}")

# Function to click using PyAutoGUI (for simulating right-click area)
def click_position(x, y):
    pyautogui.click(x, y)
    print(f"Clicked at position ({x}, {y}) using PyAutoGUI")

# JavaScript code to execute within the webview window
def execute_custom_js():
    js_code = """
    (function() {
        'use strict';
        var attemptCount = 0;  // Track the number of attempts

        function checkAndPrintCF() {
            var cfInput = document.querySelector("input[name^='cf-turnstile-response']");
            var cf = cfInput ? cfInput.value : null;
            console.log('cf value:', cf);

            if (cf) {
                console.log('CF value found:', cf);
                // Call the Python function to print the CF value
                if (window.pywebview) {
                    window.pywebview.api.print_cf_value(cf);
                }
                // Reload the page to repeat the process
                setTimeout(function() {
                    console.log('Reloading page to search again...');
                    window.location.reload();  // Reload the page
                }, 2000); // Wait 2 seconds before reloading
            } else {
                console.log('CF not found, searching again...');
                attemptCount++;  // Increment the attempt counter

                if (attemptCount >= 5) {
                    // If 5 attempts are reached, click using PyAutoGUI
                    console.log('Attempt limit reached, clicking...');
                    if (window.pywebview) {
                        window.pywebview.api.click_position(61, 362); // Call Python to click using PyAutoGUI
                    }
                    attemptCount = 0;  // Reset attempt counter
                    setTimeout(checkAndPrintCF, 2000);  // Continue searching after 2 seconds
                } else {
                    // Keep searching if attempt count is less than 5
                    setTimeout(checkAndPrintCF, 2000);  // Retry every 2 seconds if CF is not found
                }
            }
        }
        checkAndPrintCF();
    })();
    """
    return js_code

# Create a window with custom width and height for mobile-like size
def start_webview():
    print("Creating webview window with custom size (360x640)...")
    # Create the webview window
    window = webview.create_window("Custom Web Browser", url, width=191, height=390)

    # Expose the print_cf_value function to be called from JavaScript
    window.expose(print_cf_value)
    window.expose(click_position)

    # Start the webview, and after it starts, execute the JS
    def on_ready():
        print("Executing custom JS to check CF value...")
        window.evaluate_js(execute_custom_js())  # Execute the custom JS

    # Register the callback that will be triggered once the window is loaded
    window.events.loaded += on_ready

    # Start the webview
    webview.start()

# Entry point for script execution
if __name__ == "__main__":
    start_webview()
