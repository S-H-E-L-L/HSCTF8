# Aptenodytes Forsteri

> Here's a warmup cryptography challenge. Reverse the script, decrypt the output, submit the flag.

Files attached: aptenodytes-forsteri.py, output.txt

Taking a look at the given program, we notice that each character is being shifted by 18 characters. Which is basically the Caesar cipher. I move over to a Caesar decipher website and decipher it keeping the shift of 8.

![Alt text](screenshot.png?raw=true "aptenodytes-forsteri")

Flag: flag{QWERTYUIOP}