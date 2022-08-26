from seleniumpagefactory.Pagefactory import PageFactory

class UpbitHomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "buy_price": ("XPATH", "(//tr[@class='down']/td[@class='upB']/a/div/strong)[last()]"),
        "sell_price": ("XPATH", "(//tr[@class='up']/td[@class='downB']/a/div/strong)[1]"),
        "vol_24h": ("XPATH", "//dt[text()='Vol. (24h)']/following-sibling::dd/strong)[1]")
    }

    def get_buy_price_value(self):
        return self.buy_price.get_text()

    def get_sell_price_value(self):
        return self.sell_price.get_text()

    def get_vol_24h_value(self):
        return self.vol_24h.get_text()


        # Request URL: https://crix-api-id.upbit.com/v1/crix/candles/days?code=CRIX.UPBIT.IDR-BTC&count=200&ciqrandom=1661246181397
