import check50
import check50.c
import re

@check50.check()
def exists():
    check50.exists("factorial.c")
    with open("factorial.c") as f:
        sources_buf = f.read()
    return sources_buf

@check50.check(exists)
def compiles():
    check50.c.compile("factorial.c", cc="gcc")

@check50.check(compiles)
def output_correct():
    check50.run("./factorial 0").stdout("0! = 1").exit()
    check50.run("./factorial 1").stdout("1! = 1").exit()
    check50.run("./factorial 2").stdout("2! = 2").exit()
    check50.run("./factorial 3").stdout("3! = 6").exit()
    check50.run("./factorial 4").stdout("4! = 24").exit()
    check50.run("./factorial 5").stdout("5! = 120").exit()
    check50.run("./factorial 6").stdout("6! = 720").exit()
    check50.run("./factorial 10").stdout("10! = 3628800").exit()
    check50.run("./factorial 15").stdout("15! = 1307674368000").exit()
    check50.run("./factorial 17").stdout("17! = 355687428096000").exit()
    check50.run("./factorial 20").stdout("20! = 2432902008176640000").exit()

