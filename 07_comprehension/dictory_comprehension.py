tea_prices_inr = {
        "masala_chai":20,
        "lemon_tea": 10,
        "ginger_tea":30
        }

tea_prices_usd = {tea:price*80 for tea, price in tea_prices_inr.items() }

print(tea_prices_usd)
