from seleniumpagefactory.Pagefactory import PageFactory

class BinanceHomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "buy_price": ("XPATH", "//div[@class='ask-light'])[last()]"),
        "sell_price": ("XPATH", "//div[@class='bid-light'])[1]"),
        "vol_24h": ("XPATH","//div[@class='tickerItemLabel' and text()='24h Volume(BTC)']/following-sibling::div")
    }

    def get_buy_price_value(self):
        return self.buy_price.get_text()

    def get_sell_price_value(self):
        return self.sell_price.get_text()

    def get_vol_24h_value(self):
        return self.vol_24h.get_text()