from seleniumpagefactory.Pagefactory import PageFactory

class IndodaxHomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "buy_price": ("XPATH", "//table[@id='sell_orders']/tbody/tr)[1]"),
        "sell_price": ("XPATH", "//table[@id='buy_orders']/tbody/tr)[1]"),
        "vol_24h": ("XPATH", "//span[text()='Vol 24h:']/following-sibling::strong[@class='vol_val']"),
        "interval_dropdown": ("XPATH", "//span[@class='timeframe-value']"),
        "one_day_options": ("XPATH", "//button[text()='1D']"),
        "graph_vol_24h": ("XPATH", "(//div[text()='Volume']/parent::div/parent::div/following-sibling::div/div/div)[1]/div")
    }

    def get_buy_price_value(self):
        return self.buy_price.get_attribute('price')

    def get_sell_price_value(self):
        return self.sell_price.get_attribute('price')

    def get_vol_24h_value(self):
        return self.vol_24h.get_text()
    
    # https://indodax.com/tradingview/history_v2?symbol=btcidr&tf=1&from=1661209113&to=1661209173
