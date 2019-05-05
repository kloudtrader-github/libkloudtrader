import libkloudtrader.equities.miscpaper as miscpaper
from libkloudtrader.defaults import ACCESS_TOKEN,ACCOUNT_NUMBER
from libkloudtrader.equities.trade import *
MISCPAPER_ACCESS_TOKEN='eCqH0Jcd9XphAbgf7Snt5FkNzI53'
MISCPAPER_ACCOUNT_NUMBER="VA81788104"
print(miscpaper.sell_preview('AAPL',1,MISCPAPER_ACCESS_TOKEN,MISCPAPER_ACCOUNT_NUMBER,duration='gtc',order_type='limit',price=210))
print(sell_preview('AAPL',1,'2HU89u9ikIX64eUcgrWqYaNEuxcS','6YA00005',duration='gtc',order_type='limit',price=210))