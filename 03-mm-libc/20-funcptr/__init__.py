import check50
import check50.c
import re

@check50.check()
def exists():
    check50.exists("funcptr.c")
    with open("funcptr.c") as f:
        sources_buf = f.read()
    return sources_buf

@check50.check(exists)
def compiles():
    check50.c.compile("funcptr.c", cc="gcc")

@check50.check(compiles)
def output_correct():
    check50.run("./funcptr")\
            .stdin("0")\
            .stdout("Emma Jones, 19")\
            .stdout("Amy Li, 20")\
            .stdout("Alice Brown, 25")\
            .stdout("Bob Smith, 28")\
            .stdout("John Smith, 31")\
            .stdout("Christopher Johnson, 35")\
            .stdout("David Brown, 42")\
            .exit()
