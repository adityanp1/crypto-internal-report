from seleniumpagefactory.Pagefactory import PageFactory

class ZipmexHomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "popup_ok_button": "//div[@role='presentation']/div/div/button[contains(text(),'OK')",
        "buy_price": ("XPATH", "(//h6[contains(text(),'Order Book')]/following-sibling::div/div/div/div/div/div/div/div/div/span[@state='sell'])[last()]"),
        "sell_price": ("XPATH", "(//h6[contains(text(),'Order Book')]/following-sibling::div/div/div/div/div/div/div/div/div/span[@state='buy'])[1]"),
        "vol_24h": ("XPATH","//span[contains(text(),'Vol. 24 Jam')]/following-sibling::span")
    }

    def get_buy_price_value(self):
        return self.buy_price.get_text()

    def get_sell_price_value(self):
        return self.sell_price.get_text()

    def get_vol_24h_value(self):
        return self.vol_24h.get_text()
