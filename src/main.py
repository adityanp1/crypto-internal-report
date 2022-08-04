from src.workflow.tokocrypto_work_flow import TokocryptoWorkFlow
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import time
import xlrd
import xlsxwriter



def init_driver():
    options = FirefoxOptions()
    # options.add_argument("--headless")
    web_driver = webdriver.Firefox(executable_path="/Users/aditya/Utilities/geckodriver",options=options)
    time.sleep(5)
    web_driver.maximize_window()
    return web_driver


def execute_price_work_flow_tokocrypto(driver,name,api_name,path,row):
    url = "https://www.tokocrypto.com/trade/{}".format(name)
    driver.get(url)
    tokocrypto_home_flow = TokocryptoWorkFlow(driver)
    tokocrypto_home_flow.change_range_for_graph(driver=driver)
    prices = tokocrypto_home_flow.get_buy_and_sell_prices()
    volume = tokocrypto_home_flow.get_last_day_volume()
    change = tokocrypto_home_flow.get_last_day_change_volume(api_name)

    outWorkbook = xlsxwriter.Workbook(path)
    outSheet = outWorkbook.add_worksheet(name)

    outSheet.write(0, 0, "Name")
    outSheet.write(0, 1, "Buy Price")
    outSheet.write(0, 2, "Sell Price")
    outSheet.write(0, 3, "Volume")
    outSheet.write(0, 4, "Volume 24h")
    outSheet.write(0, 5, "Volume price 24h")

    outSheet.write(row, 0, name)
    outSheet.write(row, 1, prices[0])
    outSheet.write(row, 2, prices[1])
    outSheet.write(row, 3, change)
    outSheet.write(row, 4, volume[0])
    outSheet.write(row, 5, volume[1])
    outWorkbook.close()
    print("done")


if __name__ == '__main__':
    driver = init_driver()
    execute_price_work_flow_tokocrypto(driver,"BTC_BIDR","BTCBIDR", "/Users/aditya/Documents/crypto_btc.xlsx",1)
    time.sleep(30)
    execute_price_work_flow_tokocrypto(driver, "ETH_BIDR", "ETHBIDR","/Users/aditya/Documents/crypto_eth.xlsx",1)
