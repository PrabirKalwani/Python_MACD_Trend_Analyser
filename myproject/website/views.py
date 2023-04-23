from django.shortcuts import render
import requests
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as opy

def plot_macd(request):
    # Fetch the stock data using Alpha Vantage
    api_key = 'HEAH76RM55GB46KW'
    ticker = request.GET.get('ticker', 'AAPL')  # default to AAPL if ticker not provided
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey={api_key}&outputsize=full'
    response = requests.get(url)
    data = response.json()['Time Series (Daily)']
    df = pd.DataFrame.from_dict(data, orient='index', dtype=float)
    df.index = pd.to_datetime(df.index)

    # Calculate the MACD
    exp1 = df['4. close'].ewm(span=12, adjust=False).mean()
    exp2 = df['4. close'].ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=9, adjust=False).mean()
    histogram = macd - signal

    # Create the MACD plot using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=macd, name='MACD'))
    fig.add_trace(go.Scatter(x=df.index, y=signal, name='Signal'))
    fig.add_trace(go.Bar(x=df.index, y=histogram, name='Histogram'))
    fig.update_layout(title=f"MACD for {ticker}")

    # Convert the figure to HTML
    plot_html = opy.plot(fig, auto_open=False, output_type='div')

    # Render the HTML template with the plot embedded
    return render(request, 'website/predict.html', {'plot_html': plot_html})

def home(request):
    return render(request, 'website/home.html')

def learn(request):
    return render(request, 'website/learn.html')
def predict(request):
    if request.method == 'POST':
        # Get the form data
        ticker = request.POST['ticker']

        # Fetch the stock data using yfinance
        stock = yf.Ticker(ticker)
        df = stock.history(period="max")

        # Calculate the MACD
        exp1 = df['Close'].ewm(span=12, adjust=False).mean()
        exp2 = df['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        histogram = macd - signal

        # Create the MACD plot using Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=macd, name='MACD'))
        fig.add_trace(go.Scatter(x=df.index, y=signal, name='Signal'))
        fig.add_trace(go.Bar(x=df.index, y=histogram, name='Histogram'))
        fig.update_layout(title=f"MACD for {ticker}")

        # Convert the figure to HTML
        plot_html = opy.plot(fig, auto_open=False, output_type='div')

        # Render the HTML template with the plot embedded
        return render(request, 'website/predict.html', {'plot_html': plot_html})
    else:
        return render(request, 'website/predict.html')

def penant(request):
    return render(request, 'website/learn/penant.html')

def flag(request):
    return render(request, 'website/learn/flag.html')

def wedge(request):
    return render(request, 'website/learn/wedge.html')

def ascending(request):
    return render(request, 'website/learn/ascending.html')

def descending(request):
    return render(request, 'website/learn/descending.html')

def symmetrical(request):
    return render(request, 'website/learn/symmetrical.html')

def cup(request):
    return render(request, 'website/learn/cup.html')

def head(request):
    return render(request, 'website/learn/head.html')

def double(request):
    return render(request, 'website/learn/double.html')

def gaps(request):
    return render(request, 'website/learn/gaps.html')

def reliance(request):
    return render(request,'website/predict/Reliance.html')


def itc(request):
    return render(request,'website/predict/ITC.html')

def tata(request):
    return render(request,'website/predict/tata.html')
