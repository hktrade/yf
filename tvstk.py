from tradingview_ta import TA_Handler,Interval,Exchange
import os,sys,csv,json,time
import pandas as pd
import yfinance as yf
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
# (ex: 1m, 5m, 15m, 1h, 4h, 1d, 1W, 1M)
# ticker_info["ticker_rsi"] = val.get_analysis().indicators['RSI']
pd.set_option('display.max_rows', 5000) #https://tvdb.brianthe.dev/
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)

print(time.strftime('%H:%M:%S'))
df_all = pd.DataFrame({})
df = pd.read_csv('junxianshuju/today.csv', engine='python')
symbols = list(df['Symbol'])[0:50]
print(symbols)


index_lst = ['^IXIC', '^GSPC', '^DJI']
for sym in index_lst:
	dow_tk = yf.Ticker(sym)
	print(dow_tk.info)
	time.sleep(1)
print(yf.Ticker('AAPL').info)

df=pd.DataFrame({'symbol':[],'recommendation':[],'BUY':[],'SELL':[],'NEUTRAL':[]})

exch = ['amex', 'bats', 'nyse', 'NASDAQ']
if True:
	for symbol in symbols:
		time.sleep(2)
		symbol = symbol.lower()
		print('\n \t\t\t\t  hktrade.github.io \t',symbol.upper(),'\n')
		
		for my_ex in exch:
			try:
				my_sym = TA_Handler(
					symbol=symbol,
					screener='america',
					exchange=my_ex,
					interval='1d') #5m
				smm_dict = my_sym.get_analysis().summary
			except:
				# print('except\t\t\t',symbol);
				continue
			time.sleep(1)
			try:
				my_sym = TA_Handler(
					symbol=symbol,
					screener='america',

					exchange=my_ex,
					interval='5m') #5m
				smm_dict5 = my_sym.get_analysis().summary
				
				my_dict = my_sym.get_analysis().indicators
				print('\n Get real-time stk/fut data \n')
				df = pd.DataFrame([my_dict.keys(), my_dict.values()]).T
				df.columns = ['key', 'value']
				df = df.set_index('key')
				print(df.loc[['open','high','low','close','volume','change','MACD.macd','RSI','Stoch.K','Stoch.D']].value)

			except:
				# print('except\t\t\t',symbol);
				continue
		
			df = pd.DataFrame([smm_dict.keys(), smm_dict.values()]).T
			df.columns = ['key', 'value']
			df.at[0, ['key']] = symbol

			df5 = pd.DataFrame([smm_dict5.keys(), smm_dict5.values()]).T
			df5.columns = ['key', 'value']
			df5.at[0, ['key']] = symbol

			print(' 1 day')
			print(df)
			print('\n\n 5 m')
			print(df5)
			df_all = df_all.append({'symbol':symbol,'recommendation':df['value'].iloc[0],'BUY':df['value'].iloc[1],
			'SELL':df['value'].iloc[2],'NEUTRAL':df['value'].iloc[3]},ignore_index=True)

			df_all['BUY'] = df_all['BUY'].astype(int)
			df_all['SELL'] = df_all['SELL'].astype(int)
			df_all['NEUTRAL'] = df_all['NEUTRAL'].astype(int)
			df_all.to_csv('junxianshuju/cme_day.csv', index=False, mode='w',columns=['symbol','recommendation',
			'BUY','SELL','NEUTRAL'])
			df_all.to_csv('junxianshuju/cme_5m.csv', index=False, mode='w',columns=['symbol','recommendation',
			'BUY','SELL','NEUTRAL'])
			break
		
sys.exit()
