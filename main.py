from discord.ext import commands
from pycoingecko import CoinGeckoAPI

import discord

client = discord.Client()
bot = commands.Bot(command_prefix='!')
cg = CoinGeckoAPI()
coin_list = cg.get_coins_list()

token = ''


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='cap')
async def cap(ctx, coin):
    symbol = coin.lower()

    coin_id = find_by_symbol(coin_list, symbol)

    if coin_id:

        data = cg.get_coin_by_id(coin_id, localization='false', tickers='false', market_data='true',
                                 community_data='false', developer_data='false', sparkline='false')

        # pictures and whatever
        name = data['name']
        image = data['image']['large']
        thumb = data['image']['thumb']

        # all-time highs
        usd_ath = str(data['market_data']['ath']['usd'])
        btc_ath = str(data['market_data']['ath']['btc'])
        eth_ath = str(data['market_data']['ath']['eth'])

        # market data
        market_cap = "{:,}".format(data['market_data']['market_cap']['usd'])
        circulating = "{:,}".format(int(data['market_data']['circulating_supply']))
        volume = "{:,}".format(data['market_data']['total_volume']['usd'])
        current_price = "{:,}".format(data['market_data']['current_price']['usd'])
        btc_value = "{:,}".format(data['market_data']['current_price']['btc'])
        eth_value = "{:,}".format(data['market_data']['current_price']['eth'])

        # price changes

        day_price_change = round(data['market_data']['price_change_percentage_24h_in_currency']['usd'], 2)
        week_price_change = round(data['market_data']['price_change_percentage_7d_in_currency']['usd'], 2)
        monthly_price_change = round(data['market_data']['price_change_percentage_30d_in_currency']['usd'], 2)

        # price movement emojis
        up_emoji = "<:up_bot:811071234313551923>"
        down_emoji = "<:down_bot:811071183709143070>"

        day_price_emoji = None
        week_price_emoji = None
        month_price_emoji = None

        if day_price_change > 0:
            day_price_emoji = up_emoji
        else:
            day_price_emoji = down_emoji

        if week_price_change > 0:
            week_price_emoji = up_emoji
        else:
            week_price_emoji = down_emoji

        if monthly_price_change > 0:
            month_price_emoji = up_emoji
        else:
            month_price_emoji = down_emoji

        embed = discord.Embed(color=0x5ba0d0)
        embed.add_field(name="Coin Information",
                        value="<:bitcoin:811023744881000469> BTC: " + btc_value +
                              "\n<:eth:811065950060675072> ETH: "
                              + eth_value + "\n:dollar: USD: " + current_price +
                              "\n:moneybag: Market Cap: " + market_cap + "\n:dizzy: Circulating: " + circulating +
                              "\n:money_mouth: Volume: " +
                              volume,
                        inline=False)
        embed.add_field(name="Price Changes",
                        value=day_price_emoji + "24H: " + str(day_price_change) + "%\n" + week_price_emoji +
                        "7D: " + str(week_price_change) + "%\n" + month_price_emoji + "30D: " +
                        str(monthly_price_change) + "%\n", inline=True)
        embed.add_field(name="ATH", value="<:bitcoin:811023744881000469> BTC: " + btc_ath +
                                          "\n <:eth:811065950060675072> ETH: " + eth_ath + "\n:dollar: USD: " +
                                          usd_ath,
                        inline=True)

        embed.set_thumbnail(url=image)
        embed.set_author(name=str(name).capitalize(),
                         icon_url=thumb)

        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid coin symbol provided, please try again.")

    return None


def find_by_symbol(api_response, symbol):
    if symbol == "surf":
        return "surf-finance"
    if symbol == "mir":
        return "mirror-protocol"
    try:
        for entry in api_response:
            if entry["symbol"] == symbol:
                return entry["id"]
    except ValueError:
        return False


if __name__ == '__main__':
    bot.run(token)
