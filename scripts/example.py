
@basket.command(name="example", description="Example custom script.", usage="example")
async def example(basket):
    exampleEmbed = discord.Embed(
        title="Example Embed",
        description="""
        An example embed to display what you can do in scripts.
        Check `scripts/example.py` to see the code!
        ** **
        Ghost scripts are all created in python using discord.py so you can use any feature from discord.py.
        """,
        color=__embedcolour__
    )
    exampleEmbed.add_field(name="Variables", value="""
    **\_\_embedtitle\_\_** : Theme's embed title.
    **\_\_embedcolour\_\_** : Theme's embed colour.
    **\_\_embedfooter\_\_** : Theme's embed footer.
    **\_\_embedimage\_\_** : Theme's embed image url.
    **\_\_embedfooterimage\_\_** : Theme's embed footer image url.
    
    **\_\_embedemoji\_\_** : Theme's global emoji.
    **\_\_deletetimeout\_\_** : Config delete timeout (seconds).
    """)
    exampleEmbed.set_thumbnail(url=__embedimage__)
    exampleEmbed.set_footer(text=__embedfooter__, icon_url=__embedfooterimage__)

    await basket.send("Hello World!", embed=exampleEmbed)
    