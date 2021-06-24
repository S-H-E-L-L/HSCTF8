# Sneks

> https://www.youtube.com/watch?v=0arsPXEaIUY

Files attached: sneks.pyc, output.txt

First I used the uncompyle6 library to reverse obtain the .py file

```bash
uncompyle6 -o sneks.pyc
```

I know that the flag has to start with 'flag', so I ran the program and entered 'flag', and the 5 output numbers matched the first 5 numbers that are given in output.txt. This tells us that the output is independent of the length of the input string. It's straightforward from here, bruteforce for each letter and check which one matches the next number in output.txt.
Script used: desneks.py

Flag: flag{s3qu3nc35_4nd_5um5}