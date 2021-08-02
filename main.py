import requests
import time


def getValue(fromc, toc):
    # Request to get the current exchange rate, intraday, daily, weekly, monthly of a trade.
    urllist = [
        'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=' + fromc + '&to_currency=' + toc + '&apikey=P61OB2NBUJFNKYL2',
        'https://www.alphavantage.co/query?function=FX_INTRADAY&from_symbol=' + fromc + '&to_symbol=' + toc + '&interval=5min&apikey=P61OB2NBUJFNKYL2',
        'https://www.alphavantage.co/query?function=FX_DAiLY&from_symbol=' + fromc + '&to_symbol=' + toc + '&apikey=P61OB2NBUJFNKYL2',
        'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=' + fromc + '&to_symbol=' + toc + '&apikey=P61OB2NBUJFNKYL2',
        'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=' + fromc + '&to_symbol=' + toc + '&apikey=P61OB2NBUJFNKYL2']
    # Information that i want from the json
    infolist = ['Realtime Currency Exchange Rate', 'Time Series FX (5min)', 'Time Series FX (Daily)', 'Time Series FX (Weekly)', 'Time Series FX (Monthly)']
    datalist = []  # 0.Exchange rate, 1. 5 Min, 2. Daily, 3. Weekly, 4. Monthly
    r = requests.get(urllist[0])
    data = r.json()
    x = data[infolist[0]]
    datalist.append([x['5. Exchange Rate'], x['8. Bid Price'], x['9. Ask Price']])
    for i in range(1, 5):
        r = requests.get(urllist[i])
        data = r.json()
        x = data[infolist[i]]
        d = x.items()
        tmp = []
        for key, value in d:
            tmp.append(value)
        datalist.append(tmp)
    return datalist


def main():
    listExchange = [["USD", "EUR"], ["USD", "JPY"], ["USD", "CAD"], ["GBP", "USD"], ["USD", "CHF"], ["AUD", "USD"]]
    # test()
    for x in listExchange:
        getValue(x[0], x[1])
        time.sleep(61)


if __name__ == "__main__":
    main()
