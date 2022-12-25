from decouple import config
import interactions
import main
bot = interactions.Client(token=config("KEY"))


@bot.command(
    name="get_options_price",
    description="This is the first command I made!",
    options=[
        interactions.Option(
            name="strike",
            description="Strike price of the option",
            type=interactions.OptionType.INTEGER,
            required=True, ),

        interactions.Option(
            name="stock_price",
            description="Stock price",
            type=interactions.OptionType.NUMBER,
            required=True, ),
        interactions.Option(
            name="days",
            description="Days until expiration",
            type=interactions.OptionType.INTEGER,
            required=True, ),
        interactions.Option(
            name="volatility",
            description="Implied volatility for your option",
            type=interactions.OptionType.NUMBER,
            required=True, ),
        interactions.Option(
            name="type",
            description="call or put",
            type=interactions.OptionType.STRING,
            required=True, )

    ],
)
async def embed(ctx: interactions.CommandContext, strike: int, stock_price: float, days: int, volatility: float, type: str):
    option = main.get_price(stock_price, strike, days, volatility, type)
    embed=interactions.Embed(
        title="Options Data",
    )
    embed.set_author(name="Vandals Option Bot", icon_url="https://www.vandalcity.io/favicon.ico")
    embed.add_field(name="**Option Value**", value=f"{option['value']['option value']}")
    embed.add_field(name="**Intrinsic Value**", value=f"{option['value']['intrinsic value']}")
    embed.add_field(name="**Time Value (extrinsic)**", value=f"{option['value']['time value']}")
    embed.add_field(name="**Theta**", value=f"{option['greeks']['theta']}")
    await ctx.send(embeds=embed)


bot.start()
