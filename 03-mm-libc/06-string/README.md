## Standard Input and String Comparison

Write a C program that reads two strings from the standard input using `fgets`, and indicates if the strings are similar or not.
The program should behave as shown in the following execution and output examples:

```console
$ ./string
input string1:
test
input string2:
test
strings are similar

$ ./string
input string1:
hello world!
input string2:
goodbye
strings are different
```

To check the correctness of your program, use a [suitable environment](https://github.com/essential-c/devcontainer) and write your solution in a file named **`string.c`**. In a terminal, with that file in the local directory, check with this command:

```console
$ check50 03-mm-libc/06-string
```

---

[← Previous exercise](../04-malloc2/README.md) | [Next exercise →](../07-time/README.md)
