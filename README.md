# Brok3

A simple price checking discord Bot, gets data from CoinGecko

## Commands

!cap <coin> - Get price and coin information on any coin in the CoinGeckoAPI

![image](https://user-images.githubusercontent.com/30761946/110569626-b3b19c00-818f-11eb-89e7-67c15d125e9f.png)
  
## Setup

1. Install the requirements (Discord.PY, CoinGeckoAPI)
```
pip install discord.py
pip install CoinGeckoAPI
```
2. Open main.py and replace the token variable.
3. You may have to replace the emojis inside the embeds, create your custom emoji in your own discord server then replace the emoji id.
4. Run it!

## Credits
Layout is inspired from the lamb0 discord bot.

## Disclaimer

If a token has the same coin id on CoinGecko, it might give the wrong coin, easily fixable by going in the ```find_by_symbol``` function and adding a override in there.

