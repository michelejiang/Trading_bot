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

def Monthlycalculate(datalist):
    #Monthly, we get a generic view
    point = 0.0
    cmin = 10.0000
    cmax = -1.0000
    i = 0
    s = 0
    for candle in datalist[4]:
        if i == 0: last = float(candle['4. close'])
        if i == 4: first = float(candle['1. open'])
        if i < 5: s += float(candle['4. close'])
        cmin = min(cmin, float(candle['4. close']))
        cmax = max(cmax, float(candle['4. close']))
        i+=1
    s /= 5
    if first > last: point += 0.25
    else: point -= 0.25
    if s > last: point -= 0.15
    else: point += 0.15
    diff = cmax - cmin
    if (last-cmin)/diff > 0.5: point += (last-cmin)/diff
    else: point -= (last-cmin)/diff
    return point

def Weeklycalculate(datalist):
    # Weekly, we get a generic view
    point = 0.0
    cmin = 10.0000
    cmax = -1.0000
    i = 0
    s = 0
    for candle in datalist[3]:
        if i == 0: last = float(candle['4. close'])
        if i == 4: first = float(candle['1. open'])
        if i < 5: s += float(candle['4. close'])
        cmin = min(cmin, float(candle['4. close']))
        cmax = max(cmax, float(candle['4. close']))
        i += 1
    s /= 5
    if first > last:
        point += 0.50
    else:
        point -= 0.50
    if s > last:
        point -= 0.40
    else:
        point += 0.40
    diff = cmax - cmin
    if (last - cmin) / diff > 0.5:
        point += 2*((last - cmin) / diff)
    else:
        point -= 2*((last - cmin) / diff)
    return point

def Dailycalculate(datalist):
    # Daily, we get a generic view
    point = 0.0
    cmin = 10.0000
    cmax = -1.0000
    i = 0
    s = 0
    for candle in datalist[2]:
        if i == 0: last = float(candle['4. close'])
        if i == 4: first = float(candle['1. open'])
        if i < 5: s += float(candle['4. close'])
        cmin = min(cmin, float(candle['4. close']))
        cmax = max(cmax, float(candle['4. close']))
        i += 1
    s /= 5
    if first > last:
        point += 0.70
    else:
        point -= 0.70
    if s > last:
        point -= 0.40
    else:
        point += 0.40
    diff = cmax - cmin
    if (last - cmin) / diff > 0.5:
        point += 2 * ((last - cmin) / diff)
    else:
        point -= 2 * ((last - cmin) / diff)
    return point

def intradailycalculate(datalist):
    point = 0.0
    cmin = 10.0000
    cmax = -1.0000
    i = 0
    s = 0
    for candle in datalist[1]:
        if i == 0: last = float(candle['4. close'])
        if i == 4: first = float(candle['1. open'])
        if i < 5: s += float(candle['4. close'])
        cmin = min(cmin, float(candle['4. close']))
        cmax = max(cmax, float(candle['4. close']))
        i += 1
    s /= 5
    if first > last:
        point += 0.10
    else:
        point -= 0.10
    if s > last:
        point -= 0.05
    else:
        point += 0.05
    diff = cmax - cmin
    if (last - cmin) / diff > 0.5:
        point += 0.3 * ((last - cmin) / diff)
    else:
        point -= 0.3 * ((last - cmin) / diff)
    return point

def main():
    listExchange = [["USD", "EUR"], ["USD", "JPY"], ["USD", "CAD"], ["GBP", "USD"], ["USD", "CHF"], ["AUD", "USD"]]
    # test()
    for x in listExchange:
        score = 0
        data = getValue(x[0], x[1])
        score = Monthlycalculate(data)
        score += Weeklycalculate(data)
        score += Dailycalculate(data)
        score += intradailycalculate(data)
        print(score)
        time.sleep(61)


if __name__ == "__main__":
    main()
