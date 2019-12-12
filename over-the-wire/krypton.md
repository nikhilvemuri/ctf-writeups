# Krypton

Krypton is a wargame about cryptography.
https://overthewire.org/wargames/krypton


## Krypton 0

The password is given to us, but in Base64 encoding:

`S1JZUFRPTklTR1JFQVQ=`

We can decrypt this with Python's base64 library:

```python
import base64
base64.b64decode("S1JZUFRPTklTR1JFQVQ=")
```

password1: `KRYPTONISGREAT`


## Krypton 1

Files for each level are stored in /krypton/.

Inside this level's directory, there is a file called krypton2 containing
the encrypted password, and a README telling us that it is in ROT13
encryption - meaning that each alphabet is shifted by 13. To get the
original password, just shift by 13 again (26 letters in alphabet):

`cat /krypton/krypton1/krypton2 | tr "[A-MN-Z]" "[N-ZA-M]"`

password2: `ROTTEN`


## Krypton 2


