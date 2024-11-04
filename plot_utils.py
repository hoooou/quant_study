import plotly.graph_objects as go
def generate_pingjia(summary):
        evaluation=""
        if summary["总回报率"] > 20:
            evaluation += f"总回报率表现优异，说明投资策略的有效性很高；"
        elif summary["总回报率"] > 0:
            evaluation += f"总回报率表现良好，为正值，表明策略总体上有效；"
        elif summary["总回报率"] == 0:
            evaluation += f"总回报率为零，说明投资策略没有盈利或亏损，需进一步评估；"
        else:
            evaluation += f"总回报率为负，表明策略表现不佳，建议审视投资决策和策略；"

        if summary["最大回撤（百分比）"] < -5:
            evaluation += f"最大回撤（百分比）控制得当，风险管理良好，投资策略相对稳健；"
        elif summary["最大回撤（百分比）"] < -10:
            evaluation += f"最大回撤（百分比）在合理范围内，风险控制较好，但仍需关注市场波动；"
        elif summary["最大回撤（百分比）"] < -15:
            evaluation += f"最大回撤（百分比）较大，表明在市场波动中策略承受了一定的风险，需要加强风险管理；"
        else:
            evaluation += f"最大回撤（百分比）严重，需审视策略的风险控制和调整投资组合；"
        if summary["胜率"] > 60:
            evaluation += f"胜率表现优秀，超过60%，表明策略具有较高的盈利能力；"
        elif summary["胜率"] > 50:
            evaluation += f"胜率表现良好，略高于50%，显示出一定的优势；"
        elif summary["胜率"] >= 40:
            evaluation += f"胜率在40%-50%之间，表明策略表现一般，需考虑优化交易决策；"
        else:
            evaluation += f"胜率较低，低于40%，建议重新审视策略及其执行，以提高盈利能力；"
        if summary["夏普比率"] is None:
            evaluation += f"夏普比率未知，无法评估风险调整后的收益；"
        elif summary["夏普比率"] > 2:
            evaluation += f"夏普比率表现优异，超过2，表明每单位风险带来了相对较高的回报；"
        elif summary["夏普比率"] > 1:
            evaluation += f"夏普比率良好，超过1，说明策略的风险调整后收益较为合理；"
        elif summary["夏普比率"] > 0:
            evaluation += f"夏普比率略低，接近0，表明风险调整后收益一般，需关注风险控制；"
        else:
            evaluation += f"夏普比率为负，表明风险调整后的收益不理想，需重新审视投资策略；"
        if summary["交易次数"] < 10:
            evaluation += f"交易次数过少，可能无法充分捕捉市场机会，建议增加交易频率；"
        elif summary["交易次数"] < 50:
            evaluation += f"交易次数适中，策略在一定程度上活跃，仍可考虑适当增加交易；"
        elif summary["交易次数"] < 100:
            evaluation += f"交易次数较多，策略相对活跃，表现良好；"
        else:
            evaluation += f"交易次数非常高，策略非常活跃，但需注意控制交易成本；"
        if summary["总手续费"] < 1000:
            evaluation += f"总手续费较低，有助于提高净收益，表明交易成本控制得当；"
        elif summary["总手续费"] < 3000:
            evaluation += f"总手续费在合理范围内，建议继续关注交易成本，以优化整体收益；"
        else:
            evaluation += f"总手续费较高，可能影响整体盈利能力，需考虑减少交易频率或寻找更低手续费的交易平台；"

        if summary["索提诺比率"] is None:
            evaluation += f"索提诺比率未知，无法评估下行风险调整后的收益；"
        elif summary["索提诺比率"] > 2:
            evaluation += f"索提诺比率表现优异，超过2，表明每单位下行风险带来了相对较高的回报；"
        elif summary["索提诺比率"] > 1:
            evaluation += f"索提诺比率良好，超过1，说明策略的下行风险调整后收益较为合理；"
        elif summary["索提诺比率"] > 0:
            evaluation += f"索提诺比率略低，接近0，表明下行风险调整后的收益一般，需关注风险控制；"
        else:
            evaluation += f"索提诺比率为负，表明下行风险调整后的收益不理想，需重新审视投资策略；"
        if summary["卡尔玛比率"] is None:
            evaluation += f"卡尔玛比率未知，无法评估收益与最大回撤的关系；"
        elif summary["卡尔玛比率"] > 3:
            evaluation += f"卡尔玛比率表现优异，超过3，表明收益在考虑最大回撤后相当可观；"
        elif summary["卡尔玛比率"] > 2:
            evaluation += f"卡尔玛比率良好，超过2，表明收益与风险的关系较为理想；"
        elif summary["卡尔玛比率"] > 1:
            evaluation += f"卡尔玛比率略高于1，表明收益与最大回撤的平衡一般，需关注风险管理；"
        else:
            evaluation += f"卡尔玛比率低于1，表明在考虑最大回撤后，收益表现不理想，建议重新审视策略；"
        if summary["盈亏比"] is None:
            evaluation += f"盈亏比未知，无法评估盈利与亏损的关系；"
        elif summary["盈亏比"] > 2:
            evaluation += f"盈亏比表现优秀，超过2，表明每单位亏损带来了相对较高的盈利；"
        elif summary["盈亏比"] > 1:
            evaluation += f"盈亏比良好，超过1，说明盈利大于亏损，策略总体表现积极；"
        elif summary["盈亏比"] > 0:
            evaluation += f"盈亏比略高于0，表明盈利和亏损相当，需考虑优化交易策略；"
        else:
            evaluation += f"盈亏比为负，表明亏损大于盈利，建议重新审视策略及其执行；"
        if summary["溃疡指数"] is None:
            evaluation += f"溃疡指数未知，无法评估投资组合的下行风险；"
        elif summary["溃疡指数"] < 5:
            evaluation += f"溃疡指数表现良好，低于5，表明投资组合的下行风险较低；"
        elif summary["溃疡指数"] < 10:
            evaluation += f"溃疡指数在5到10之间，显示出一定的下行风险，需关注风险管理；"
        else:
            evaluation += f"溃疡指数高于10，表明下行风险较大，建议重新评估投资策略以降低风险；"
        if summary["净值R²"] is None:
            evaluation += f"净值R²未知，无法评估投资组合的表现与基准的相关性；"
        elif summary["净值R²"] > 0.8:
            evaluation += f"净值R²表现优异，超过0.8，表明投资组合的表现与基准高度相关；"
        elif summary["净值R²"] > 0.5:
            evaluation += f"净值R²良好，超过0.5，说明投资组合的表现与基准有一定的相关性；"
        elif summary["净值R²"] > 0.2:
            evaluation += f"净值R²较低，处于0.2到0.5之间，表明投资组合的表现与基准的相关性较弱；"
        else:
            evaluation += f"净值R²极低，低于0.2，表明投资组合的表现与基准几乎无关，需重新审视投资策略；"
        return evaluation.replace("；","；\n")
from pandas import DataFrame

import data_utils
import plot_utils

def printResult(df: DataFrame):
    import pandas as pd
    
    # 假设 result.metrics_df 已经存在，并且包含您的数据
    # 中文名称映射字典
    zh_names = {
        'trade_count': '交易次数',
        'initial_market_value': '初始市值',
        'end_market_value': '期末市值',
        'total_pnl': '总盈亏',
        'unrealized_pnl': '未实现盈亏',
        'total_return_pct': '总回报率',
        'annual_return_pct': '年化总回报率',
        'total_profit': '总盈利',
        'total_loss': '总亏损',
        'total_fees': '总手续费',
        'max_drawdown': '最大回撤（现金）',
        'max_drawdown_pct': '最大回撤（百分比）',
        'win_rate': '胜率',
        'loss_rate': '亏损率',
        'winning_trades': '盈利交易次数',
        'losing_trades': '亏损交易次数',
        'avg_pnl': '每笔交易平均盈亏',
        'avg_return_pct': '每笔交易平均回报率',
        'avg_trade_bars': '每笔交易平均K线数',
        'avg_profit': '每笔交易平均盈利',
        'avg_profit_pct': '每笔交易平均盈利率',
        'avg_winning_trade_bars': '盈利交易的平均K线数',
        'avg_loss': '每笔交易平均亏损',
        'avg_loss_pct': '每笔交易平均亏损率',
        'avg_losing_trade_bars': '亏损交易的平均K线数',
        'largest_win': '最大盈利交易',
        'largest_win_pct': '最大盈利交易（百分比）',
        'largest_win_bars': '最大盈利交易的K线数',
        'largest_loss': '最大亏损交易',
        'largest_loss_pct': '最大亏损交易（百分比）',
        'largest_loss_bars': '最大亏损交易的K线数',
        'max_wins': '最大连续盈利交易次数',
        'max_losses': '最大连续亏损交易次数',
        'sharpe': '夏普比率',
        'sortino': '索提诺比率',
        'calmar': '卡尔玛比率',
        'profit_factor': '盈亏比',
        'ulcer_index': '溃疡指数',
        'upi': '溃疡表现指数',
        'equity_r2': '净值R²',
        'std_error': '标准误差',
        'annual_std_error': '年化标准误差',
        'annual_volatility_pct': '年化波动率（百分比）'
    }
    
    # 在 DataFrame 中新增“zh_name”列
    df['zh_name'] = df['name'].map(zh_names)
    # 调整列顺序，使 'zh_name' 列紧挨着 'name' 列
    df = df[['zh_name', 'name'] + [col for col in df.columns if col not in ['name', 'zh_name']]]
    
    # 增加总结评价逻辑
    summary={}
    for key, name in zh_names.items():
        summary[name]=data_utils.getValueFromDataFrame(df,key)
    print(plot_utils.generate_pingjia(summary))
    new_order = [i for i in range(39)]  # 默认顺序
    # 手动修改顺序，例如将第1行和第39行对调
    new_order = [5, 10, 11,25,28,32,34]+[i for i in new_order if i not in [5, 10, 11,25,28,32,34]]
    df_reordered = df.iloc[new_order]
    return df_reordered
def plotMy(stock_name,dataframe):
    print(stock_name)
    # 新增需要的列
    # 检查并新增需要的列
    if 'Open' not in dataframe.columns:
        dataframe['Open'] = dataframe['开盘']
    if 'High' not in dataframe.columns:
        dataframe['High'] = dataframe['最高']
    if 'Low' not in dataframe.columns:
        dataframe['Low'] = dataframe['最低']
    if 'Close' not in dataframe.columns:
        dataframe['Close'] = dataframe['收盘']
    if 'Volume' not in dataframe.columns:
        dataframe['Volume'] = dataframe['成交量']

    # 创建交互式蜡烛图
    fig = go.Figure(data=[go.Candlestick(
        x=dataframe.index,
        open=dataframe['Open'],
        high=dataframe['High'],
        low=dataframe['Low'],
        close=dataframe['Close'],
        hovertext=[
            f"{stock_name}<br>" +
            f"日期: {date.strftime('%Y年%m月%d日')}<br>" +
            f"开盘: {open_price}<br>" +
            f"最高: {high_price}<br>" +
            f"最低: {low_price}<br>" +
            f"收盘: {close_price}"
            for date, open_price, high_price, low_price, close_price in zip(
                dataframe.index,
                dataframe['Open'],
                dataframe['High'],
                dataframe['Low'],
                dataframe['Close']
            )
        ],
        hoverinfo="text"  # 只显示 hovertext
    )])

    # 设置图表标题和标签
    fig.update_layout(
        title='交互式蜡烛图',
        xaxis_title='日期',
        yaxis_title='价格',
        xaxis=dict(
            showspikes=True,
            spikecolor="blue",
            spikemode="across",
            spikethickness=1
        ),
        yaxis=dict(
            showspikes=True,
            spikecolor="blue",
            spikethickness=1
        ),
        hovermode="x unified"
    )

    # 显示图表
    fig.show()
def plotChart(result):
    import matplotlib.pyplot as plt
    result.portfolio['syl']=result.portfolio['market_value']/result.portfolio.iloc[0]["cash"]-1
    chart = plt.subplot2grid((3, 2), (0, 0), rowspan=3, colspan=2)
    chart.plot(result.portfolio.index, result.portfolio['syl'])
