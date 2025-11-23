
from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        page = context.new_page()

        # Navigate to dashboard
        page.goto("http://localhost:8080/index.html")

        # Wait for animations/charts
        time.sleep(2)

        # Screenshot Dashboard
        page.screenshot(path="dashboard_view.png")
        print("Dashboard screenshot taken.")

        # Switch to Unit Economics
        page.click("#nav-unit")
        time.sleep(1)
        page.screenshot(path="unit_view.png")
        print("Unit Economics screenshot taken.")

        # Switch to Valuation Bridge
        page.click("#nav-valuation")
        time.sleep(1)
        page.screenshot(path="valuation_view.png")
        print("Valuation screenshot taken.")

        # Test Slider Logic (Back to Dashboard)
        page.click("#nav-dashboard")
        time.sleep(1)

        # Click Optimistic Button
        page.click("#btn-optimistic")
        time.sleep(1)
        page.screenshot(path="dashboard_optimistic.png")
        print("Optimistic Dashboard screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
