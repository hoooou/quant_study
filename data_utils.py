import akshare as ak
import pandas as pd
def getStockInfo(stock_code):
    stock_info = ak.stock_individual_info_em(symbol=stock_code)
    stock_info = pd.DataFrame(stock_info)
    stock_info=stock_info.set_index("item").T
    return stock_info