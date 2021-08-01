import requests
import time


def getValue(fromc, toc):
    #Request to get the current exchange rate, intraday, daily, weekly, monthly of a trade.
    urllist = ['https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + fromc + '&to_currency=' + toc + '&apikey=P61OB2NBUJFNKYL2',
               'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=' + fromc + '&to_symbol=' + toc + '&interval=5min&apikey=P61OB2NBUJFNKYL2',
               'https://www.alphavantage.co/query?function=FX_DAiLY&from_symbol=' + fromc + '&to_symbol=' + toc + '&apikey=P61OB2NBUJFNKYL2',
               'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=' + fromc + '&to_symbol=' + toc + '&apikey=P61OB2NBUJFNKYL2',
               'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=' + fromc + '&to_symbol=' + toc +'&apikey=P61OB2NBUJFNKYL2']
    #Information that i want from the json
    infolist = ['Time Series FX (5min)',  'Time Series FX (Monthly)', 'Time Series FX (Weekly)',  'Time Series FX (Daily)']

    r = requests.get(urllist[0])
    data = r.json()
    x = data['Realtime Currency Exchange Rate']
    exchange_rate = [x['5. Exchange Rate'], x['8. Bid Price'], x['9. Ask Price']]

    r = requests.get(urllist[1])
    data = r.json()
    x = data['Time Series FX (5min)']
    d = x.items()
    intraday = []
    for key, value in d:
        intraday.append(value)

    r = requests.get(urllist[2])
    data = r.json()
    x = data['Time Series FX (Daily)']
    d = x.items()
    daily = []
    for key, value in d:
        daily.append(value)

    r = requests.get(urllist[3])
    data = r.json()
    x = data['Time Series FX (Weekly)']
    d = x.items()
    weekly = []
    for key, value in d:
        weekly.append(value)

    r = requests.get(urllist[4])
    data = r.json()
    x = data['Time Series FX (Monthly)']
    d = x.items()
    monthly = []
    for key, value in d:
        monthly.append(value)

    for p in exchange_rate:
        print(p)
    for candle in intraday:
        print(candle)
    for candle in daily:
        print(candle)
    for candle in weekly:
        print(candle)
    for candle in monthly:
        print(candle)
def test():
    url = 'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=EUR&to_symbol=USD&interval=5min&apikey=P61OB2NBUJFNKYL2'
    r = requests.get(url)
    data = r.json()
    d = data['Time Series FX (5min)']
    print(d)
    x = d.items()
    for key, value in x:

        print(value)





def main():
    listExchange = [["USD", "EUR"], ["USD", "JPY"], ["USD", "CAD"], ["GBP" , "USD"], ["USD", "CHF"], ["AUD", "USD"]]
    #test()
    for x in listExchange:
        getValue(x[0], x[1])
        time.sleep(61)

if __name__ == "__main__":
    main()