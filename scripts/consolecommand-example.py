
@basket.command(name="consolecommand", description="console command test", usage="consoletest", aliases=["consoleCommand-consoletest"])
async def consoletest(ctx):
    print("This is a command that can be executed in the console.")
    print("You can create this commands by adding consoleCommand-{commandname} in the commands aliases.")
    print("")
    print("Any command that has that in the aliases will be able to be executed in the console and in discord so prints will be better.")
    print("FYI: Arguments currently are not possible.")
