from seleniumpagefactory.Pagefactory import PageFactory


class TokocryptoHomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {
        "buy_price": ("XPATH", "(//div[@class='asks']/div/div/div[@class='gm-scroll-view']/div)[last()]"),
        "sell_price": ("XPATH", "(//div[@class='bids']/div/div/div[@class='gm-scroll-view']/div)[1]"),
        "interval_dropdown": ("XPATH","//div[@id='header-toolbar-intervals']/div/div/div"),
        "one_hari_interval_option": ("XPATH","//div[text()='1 hari']"),
        "canvas": ("XPATH","(//td[contains(@class,'chart-markup-table pane')])[1]"),
        "chart_container": ("XPATH","//div[@id='chart_container']"),
        "chart_iframe": ("XPATH","//iframe[contains(@id,'tradingview')]"),
        "volume_idr": ("XPATH","//div[text()='Volume Global 24 Jam']/following-sibling::div"),
        "price_idr": ("XPATH", "//div[text()='Perubahan 24jam']/following-sibling::div/span")
    }

    def get_buy_price_value(self):
        return self.buy_price.get_text()

    def get_sell_price_value(self):
        return self.sell_price.get_text()

    def change_interval(self):
        self.interval_dropdown.click()
        self.one_hari_interval_option.click()

    def click_canvas(self):
        self.canvas.click()

    def click_chart_container(self):
        self.chart_container.click()

    def get_volume_idr_value(self):
        return self.volume_idr.get_text()

    def get_price_idr_value(self):
        return self.price_idr.get_text()