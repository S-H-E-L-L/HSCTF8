# Seeded Randomizer

> There are at least two types of randomizers in Java, one that is purely random and one that is seeded (that is pseudorandom). Please fix this code to output the correct flag (note the flag format, and a sample has been provided).

Files attached: SeededRandomizer.java

There's a comment in the file that says that the seed is between 0 and 1000, and a sample function that shows how random number generation works on java. It's pretty simple from here, just iterate from 0 to 1000, set the seed as that number, and use random number generation with that seed. Out of the 1000 outputs, one should be correct. You could add an extra statement that checks if the string starts with flag, or dump the entire output in a text editor, and use ctrl+f to search for 'flag'.

Flag: flag{s33d3d_r4nd0m1z3rs_4r3_c00l}