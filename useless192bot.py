import discord
from discord.ext import commands

TOKEN = "{}"
client = discord.Client()

bot = commands.Bot(command_prefix="$")

# Try to use cog

@bot.command(name="hello")
async def response_hello(ctx):
    response = "Hello World! FUCK the cheat sheet, I am the cheat bot"
    await ctx.send(response)


@bot.command(name="content")
async def response_content(ctx):
    response = "content"
    await ctx.send(response)

# @bot.command(name="simple")
# # async def
@bot.command()
async def simple(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 3:
        await ctx.send('You need to input 3 args as P(present amount), i(interest rate) and n(period of time)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))

        res = arg_list[0] * (1+arg_list[1]*arg_list[2])
        await ctx.send(res)


@bot.command()
async def compound(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 3:
        await ctx.send('You need to input 3 args as P(present amount), i(interest rate) and n(period of time)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))

        res = arg_list[0] * ((1+arg_list[1])**arg_list[2])
        await ctx.send(round(res, 4))

@bot.command()
async def effectiveRate(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 3 args as r(nominal annual interest rate) and m(number of compounding periods per year)')
    else:
        arg_list = []
        for arg in args:
            if "%"in arg:
                arg_list.append(float(arg.strip("%")))
            else:
                arg_list.append(float(arg))
        r = arg_list[0] *arg_list[1]
        res = (1 + r/arg_list[1]) ** arg_list[1] -1
        await ctx.send("effective rate is {}%".format(round(res, 4)))
        await ctx.send(arg_list[0])
        await ctx.send(arg_list[0] / arg_list[1])
        await ctx.send(arg_list[1])


#continuous compounding
@bot.command()
async def continuous(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 3:
        await ctx.send('You need to input 3 args as P(current amount), i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))

        res = arg_list[0] * (2.71828 ** (arg_list[1] * arg_list[2]))
        await ctx.send(round(res, 4))

# @bot.command()
# async def continuous(ctx, *args):
#     # await ctx.send('You passed {}'.format(','.join(args)))
#     if len(args) != 3:
#         await ctx.send('You need to input 3 args as P(current amount), i(norminal interest) and n(Time range)')
#     else:
#         arg_list = []
#         for arg in args:
#             arg_list.append(float(arg))
#
#         res = arg_list[0] * (2.71828 ** (arg_list[1] * arg_list[2]))
#         await ctx.send(round(res, 3))


@bot.command(name="P/F")
async def PresentFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        N = arg_list[1]
        res = 1 /(1 + i) ** N
        await ctx.send("(P/F, i, N) = {}".format(round(res, 4)))


@bot.command(name="F/P")
async def CompundFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        N = arg_list[1]
        res = (1 + i) ** N
        await ctx.send("(F/P, i, N) = {}".format(round(res, 4)))


@bot.command(name="A/F")
async def SinkFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        N = arg_list[1]
        res = i / ((1+ i) ** N -1)
        await ctx.send("(A/F, i, N) = {}".format(round(res, 4)))

@bot.command(name="F/A")
async def UniformFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        N = arg_list[1]
        res = ((1+ i) ** N -1) / i
        await ctx.send("(F/A, i, N) = {}".format(round(res, 4)))


@bot.command(name="A/P")
async def CapitalFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        N = arg_list[1]
        res = (i * (1 + i) ** N ) / ((1+i) ** N -1)
        await ctx.send("(A/P, i, N) = {}".format(round(res, 4)))


@bot.command(name="P/A")
async def SeriesFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        N = arg_list[1]
        res = ((1+i) ** N) -1 / (i * (1 + i) ** N)
        await ctx.send("(P/A, i, N) = {}".format(round(res, 4)))


@bot.command(name="P/G")
async def ArithmeticFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 2:
        await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        N = arg_list[1]
        single_payment = ((1+i) ** N - i * N - 1) / (i ** 2 * (1 + i) ** N)
        uniform_series_factor = (1/i - N /( (1+i)**N - 1))
        await ctx.send("The single payment(P/G, i, N) = {}" \
                       "The Uniform series factor (A/G, i, N) = {}".format(round(single_payment, 4),round(uniform_series_factor, 4)))

@bot.command(name="q1")
async def GeometricFactor(ctx, *args):
    # await ctx.send('You passed {}'.format(','.join(args)))
    if len(args) != 3:
        await ctx.send('You need to input 3 args as i(norminal interest), g, and n(Time range)')
    else:
        arg_list = []
        for arg in args:
            arg_list.append(float(arg))
        i = arg_list[0]
        g = arg_list[1]
        N = arg_list[2]
        i_zero = (1+i)/(1+g) - 1
        factor = ((1+i_zero)**N -1) / (i_zero*(1+i_zero)**N)*(1/1+g)
        # i_zero = ((1+i) ** N - i * N - 1) / (i ** 2 * (1 + i) ** N)
        # uniform_series_factor = (1/i - N /( (1+i)**N - 1))
        await ctx.send("The I_zero is {}" \
                       "The Geometric gradient factor (P/A,g, i, N) = {}".format(round(i_zero, 4),round(factor, 4)))
# @bot.command()
# async def ArithmeticFactor(ctx, *args):
#     # await ctx.send('You passed {}'.format(','.join(args)))
#     if len(args) != 2:
#         await ctx.send('You need to input 2 args as i(norminal interest) and n(Time range)')
#     else:
#         arg_list = []
#         for arg in args:
#             arg_list.append(float(arg))
#         i = arg_list[0]
#         N = arg_list[1]
#         res = (1/i - N /( (1+i)**N - 1))
#         await ctx.send("(A/G, i, N) = {}".format(round(res, 3)))

bot.run(TOKEN)