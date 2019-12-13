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

The README tells us that krypton3 contains the password, encrypted using
keyfile.dat. But we don't have access to keyfile.dat - instead we're given
a binary which can use it to encrypt any plaintext file we provide. (Note:
the binary makes an output file, so to work in a place with write
permissions, we have to make a directory in /tmp/ and work there)

We know that this is a Caesar cipher, in other words a generalized version
of ROT13: instead of 13, the shift can be anything between 0-25.

Using `encrypt` on a plaintext file containing `abcd` outputs ciphertext
`MNOP`. So we can just take a shortcut and use `tr` again:

`cat krypton3 | tr "[M-ZA-L]" "[A-Z]"` to shift the ciphertext alphabets 12 places
backward to get the original text. (Alternatively, `cat krypton3 | tr
"[A-Z]" "[O-ZA-N]"` produces the same output, but by shifting the ciphertext
alphabets 14 places forward.)

password3: `CAESARISEASY`
