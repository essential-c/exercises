import check50
import check50.c

@check50.check()
def exists():
    check50.exists("err.c")

@check50.check(exists)
def compiles():
    check50.c.compile("err.c", cc="gcc")

@check50.check(compiles)
def correct_output():
    check50.run("./err").stdout("This should work!").exit()
