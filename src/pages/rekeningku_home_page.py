from seleniumpagefactory.Pagefactory import PageFactory

class RekeningkuHomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "buy_price": ("XPATH", "(((//tbody[@id='scroll-bottom'])[1]/tr)[1]/td)[1]"),
        "sell_price": ("XPATH", "(((//tbody[@id='scroll-bottom'])[2]/tr)[1]/td)[1]"),
        "vol_24h": ("XPATH", "//span[contains(text(),'Volume 24 Jam')]/following-sibling::b"),
        "price_24h": ("XPATH", "//span[contains(text(),'Harga Terakhir')]/following-sibling::b/span")
    }

    def get_buy_price_value(self):
        return self.buy_price.get_text()

    def get_sell_price_value(self):
        return self.sell_price.get_text()
    
    def get_vol_24h_value(self):
        return self.vol_24h.get_text()

    def get_price_24h_value(self):
        return self.vol_24h.get_text()
    
    # Request URL: https://api.rekeningku.com/v2/chart?t=2&f=1440&id=1
