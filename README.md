# Differential_cryptoanalysis_table_script
This is my University work from cryptography course.
This is a script, which takes an subtitution, and creates a differential table for it.
A differential cryptanalysis attack is a method of abusing pairs of plaintext and corresponding ciphertext to learn about the secret key that encrypted them, or, more precisely, to reduce the amount of time needed to find the key. It’s what is called a chosen plaintext attack; the attacker has access to plaintext and corresponding ciphertext.
Creating a differential table is main part of this method.
## Exapmle:
For following substitution (5,8,1,13,10,3,4,2,14,15,12,7,6,0,9,11)
Script created following exel table, which can be used for differential cryptoanalysis:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|0|16|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
|1|0|0|0|2|2|0|4|0|0|0|8|6|0|0|2|0|0|
2|0|0|4|0|0|0|2|2|2|2|0|0|0|0|4|0|
3|0|0|0|2|4|2|0|0|4|0|0|2|0|2|0|0|
4|0|2|2|0|0|2|2|0|0|2|0|2|2|0|2|0|
5|0|2|0|0|2|0|0|0|2|0|2|2|2|0|0|4|
6|0|0|0|0|2|0|0|2|0|2|0|2|4|0|2|2|
7|0|0|2|0|2|0|4|0|0|2|0|0|0|4|0|2|
8|0|2|2|0|0|2|2|0|2|0|2|0|0|2|0|2|
9|0|0|2|0|0|0|0|2|2|2|0|2|4|0|0|2|
10|0|0|0|0|2|0|0|2|2|0|2|0|2|2|0|4|
11|0|2|0|0|0|4|0|2|0|0|2|0|2|0|4|0|
12|0|2|0|8|0|0|0|2|2|0|0|0|0|0|2|0|
13|0|0|2|2|0|4|0|0|0|4|2|2|0|0|0|0|
14|0|6|0|0|0|0|2|0|0|2|0|0|0|4|2|0|
15|0|0|2|2|2|2|0|4|0|0|0|4|0|0|0|0

