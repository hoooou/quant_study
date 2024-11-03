import plotly.graph_objects as go
def plotResult(result):
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
    result.metrics_df['zh_name'] = result.metrics_df['name'].map(zh_names)
    # 调整列顺序，使 'zh_name' 列紧挨着 'name' 列
    df = result.metrics_df[['zh_name','name'] + [col for col in result.metrics_df.columns if col not in ['name', 'zh_name']]]
    return df

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
