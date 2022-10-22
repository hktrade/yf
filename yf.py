from datetime import datetime
import json,os,sys
import requests
import yfinance as yf

# Youtube     : www.youtube.com/c/美股数据张老师
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"#7890

# symbol = '0700.HK'
# df = yf.download(symbol, start = '2022-06-01')

# print(df.keys(),len(df),df.tail(10))

symbol = 'TSLA' # day K or minute K or Week or Month
df = yf.download(symbol, start = '2022-06-01')

print(df.keys(),len(df),df.tail(10))

