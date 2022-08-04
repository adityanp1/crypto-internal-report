from src.pages.tokocrypto_home_page import TokocryptoHomePage
import requests
import json
import time

class TokocryptoWorkFlow():

    def __init__(self,driver):
        self.tokocrypto_home_page = TokocryptoHomePage(driver)

    def get_buy_and_sell_prices(self):
        buy_price = self.tokocrypto_home_page.get_buy_price_value().split("\n")[0]
        sell_price = self.tokocrypto_home_page.get_sell_price_value().split("\n")[0]
        return [buy_price,sell_price]

    def change_range_for_graph(self,driver):
        driver.switch_to.frame(self.tokocrypto_home_page.chart_iframe)
        self.tokocrypto_home_page.interval_dropdown.click()
        time.sleep(5)
        self.tokocrypto_home_page.one_hari_interval_option.click()
        driver.switch_to.default_content()

    def get_last_day_volume(self):
        volume = self.tokocrypto_home_page.get_volume_idr_value()
        price = self.tokocrypto_home_page.get_price_idr_value()
        return [volume,price]

    def get_last_day_change_volume(self,name):
        url = "https://www.binance.info/api/v3/klines?symbol={}&interval=1d".format(name)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text)[-1][1]

