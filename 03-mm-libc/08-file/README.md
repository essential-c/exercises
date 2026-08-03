## File I/O
\label{sec:exercise-file-io}

Write a C program taking as command line parameter A) a file name `f` and B) a word `w`.
The program then creates the file `f-processed` which is a copy of `f` where all occurrences of the word `w` have been deleted.
Here is an example of execution:

```console
 cat sample-file-1
hello world
this is a test file containing the word hello several times
some lines do not contain that word
while others do: hello

 ./file sample-file-1 hello

 cat sample-file-1-processed
 world
this is a test file containing the word  several times
some lines do not contain that word
while others do: 
```

% TODO update URL
You can download `sample-file-1` here.

To check the correctness of your program, use a [suitable environment](../../README.md) and write your solution in a file named **`file.c`**. In a terminal, with that file in the local directory, check with this command:

```console
 check50 03-mm-libc/08-file
```

Make sure that `sample-file-1` is in the current directory alongside `file.c`.

---

[← Previous exercise](../05-malloc3/README.md) | [Next exercise →](../11-malloc4/README.md)
