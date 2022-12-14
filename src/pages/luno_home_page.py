from seleniumpagefactory.Pagefactory import PageFactory

class LunoHomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "buy_price": ("XPATH", "(//luno-orderbook/div/div/luno-spread/preceding-sibling::luno-orderbook-entry/div/span/span)[last()]"),
        "sell_price": ("XPATH", "(//luno-orderbook/div/div/luno-spread/following-sibling::luno-orderbook-entry/div/span/span)[1]"),
        "vol_24h": ("XPATH", "//div[@data-original='24h Volume']/following-sibling::div")
    }

    def get_buy_price_value(self):
        return self.buy_price.get_text()

    def get_sell_price_value(self):
        return self.sell_price.get_text()

    def get_vol_24h_value(self):
        return self.vol_24h.get_text()
    
    # Request URL: https://ajax.luno.com/ajax/1/udf/history?symbol=XBTIDR&resolution=1D&from=1632787200&to=1661299200&countback=330&currencyCode=XBTIDR
