import mplfinance as mpf

def plot_candlestick_chart(data, title):
    ap = mpf.make_addplot(data['Volume'], panel=1, ylabel='Volume', color='purple')
    mpf.plot(data, type='candle', title=title, addplot=ap, volume=True, style='charles')

# Example usage:
plot_candlestick_chart(stock_data, title="AAPL Candlestick Chart with Volume")
