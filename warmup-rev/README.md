# Warmup rev

> Time to get warmed up!

File attached: WarmupRev.java

This one was actually quite fun to solve. 

The warm function first splits the string according to the first occurrance of the letter l, into a and b
for ex: t = halola
a = hal, t1 = ola
Then it further splits t1 into b and c on the occurrance of the letter l
b = ol
c = a
Then it outputs c + b + a
So in this example, output = aolhal
Cold is simpler, it will just cut the string from the middle and swap it
for ex: yeehaw = hawyee

It's easy to figure out c, as it's the string until the first occurrance of l. Now we have to figure out a and b, and there are 20 something different combinations of a and b, one of which is correct and will give the correct flag. I've calculated all the different varations (by splitting the string accordingly, like b being the first character, a being the rest of the string, then b being the first two characters, a being the rest of the string, and so on) and proceed to reverse each of these and output them on the screen. One of them gives the correct flag.
Script used: warmup.py

![Alt text](screenshot.png?raw=true "warmuprev")

Flag: flag{1ncr34s3_1n_3nth4lpy_0f_5y5}