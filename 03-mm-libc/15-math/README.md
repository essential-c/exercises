## Math Operations

Write a C program reading a `double` with `scanf` and asking the user if he wants this number to be floored or ceiled.
Next, the program performs the requested operation and displays the result. Output examples:

```console
$ ./math
Input a number:
12.4
Input 0 for ceil, 1 for floor
0
13.000000

$ ./math
Input a number:
45.87
Input 0 for ceil, 1 for floor
1
45.000000
```

To check the correctness of your program, use a [suitable environment](../../README.md) and write your solution in a file named **`math.c`**. In a terminal, with that file in the local directory, check with this command:

```console
$ check50 03-mm-libc/15-math
```

---

[← Previous exercise](../11-malloc4/README.md) | [Next exercise →](../16-strtol/README.md)
