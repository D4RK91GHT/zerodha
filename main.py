from kite_trade import *

# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'

enctoken = "rd6h9K5zqjrBJ5CC4ulMABmvsLTnXYrgD7S42W6BPbDPssgAOHJT2ds19uyX+2Jd3E1TvAqChDvgoqlulCKRkrqcZE6RG4ddPPWHw7eGFNHt7eaMddWoEw=="
kite = KiteApp(enctoken=enctoken)

# Basic calls
# print(kite.margins())
# print(kite.orders())
# print(kite.positions())


# print(kite.instruments())
# print(kite.instruments("NSE"))
# print(kite.instruments("NFO"))

# print(kite.ltp("NSE:TCS"))
print(kite.ltp("NSE:SBIN"))
# print(kite.ltp(["NSE:NIFTY 50", "NSE:NIFTY BANK"]))
# print(kite.quote(["NSE:NIFTY BANK", "NSE:ACC", "NFO:NIFTY22SEPFUT"]))

# import time
# while True:
    # print(kite.quote(["NSE:SBIN"]))
    # time.sleep(1)

# Get Historical Data
# import datetime
# instrument_token = 9604354
# from_datetime = datetime.datetime.now() - datetime.timedelta(days=7)     # From last & days
# to_datetime = datetime.datetime.now()
# interval = "5minute"
# print(kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False))
