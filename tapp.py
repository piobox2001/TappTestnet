import asyncio
from playwright.async_api import async_playwright

FAUCET_URL = "https://testnet.tapp.exchange/faucet"
TESTNET_ADDRESS = "your_testnet_aptos_address_here"  # Replace with your Aptos testnet wallet address

async def claim_tapp_faucet():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Change to True to run headless
        page = await browser.new_page()

        await page.goto(FAUCET_URL)

        # Wait for the address input field to appear (adjust selector if needed)
        await page.wait_for_selector('input[type="text"]')

        # Fill in your testnet address
        await page.fill('input[type="text"]', TESTNET_ADDRESS)

        # Click the faucet request button (adjust selector based on actual button text or class)
        await page.click('button:has-text("Request")')

        # Wait for a success confirmation or error message (adjust text accordingly)
        try:
            await page.wait_for_selector('text=Success', timeout=10000)
            print("Faucet claim successful!")
        except:
            print("No confirmation detected. Please check manually.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(claim_tapp_faucet())
