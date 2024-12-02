from playwright.sync_api import sync_playwright

# This is the main function that runs the script
def run():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        
        # Navigate to a webpage
        # change it to google
        page.goto('https://example.com')
        
        # Take a screenshot of the page
        page.screenshot(path='test.png')
        
        # Close the browser
        browser.close()

# Call the function to execute
if __name__ == '__main__':
    run()

