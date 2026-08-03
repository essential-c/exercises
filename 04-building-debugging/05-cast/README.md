## Type Casting

Complete the following code `cast.c` by writing the generic array printing function `array_print`:

```c
#include <stdio.h>

typedef enum {
    INT,
    CHAR,
    FLOAT
} array_type;

void array_print(void *ptr, int size, array_type type) {
    // complete here
}

int main(int argc, char **argv) {
    int int_tab[3] = {1, 2, 3};
    char char_tab[2] = {'a', 'b'};
    float float_tab[3] = {2.5, 1.1, 12.42};

    array_print(int_tab, 3, INT);
    array_print(char_tab, 2, CHAR);
    array_print(float_tab, 3, FLOAT);

    return 0;
}
```

The expected output is:

```console
[1, 2, 3]
[a, b]
[2.500000, 1.100000, 12.420000]
```

To check the correctness of your program, use a [suitable environment](../../README.md) and write your solution in a file named **`cast.c`**. In a terminal, with that file in the local directory, check with this command:

```console
$ check50 -l --ansi-log olivierpierre/comp26020-problems/2025-2026/week4-compilation/05-cast
```

---

[← Previous exercise](../04-makefile/README.md) | [Next exercise →](../06-preprocessor/README.md)
