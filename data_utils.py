import akshare as ak
import pandas as pd
def getValueFromDataFrame(df:pd.DataFrame,name):
    if name in df['name'].values:
        value = df.loc[df['name'] == name, 'value'].values[0]
    else:
        value = None  # 或者设定一个默认值
    return value
def getStockInfo(stock_code):
    stock_info = ak.stock_individual_info_em(symbol=stock_code)
    stock_info = pd.DataFrame(stock_info)
    stock_info=stock_info.set_index("item").T
    return stock_info