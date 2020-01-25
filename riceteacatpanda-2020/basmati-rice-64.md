## BASmati ricE 64 (forensics, 150)

**Description**: 

There's a flag in that bowl somewhere...

Replace all zs with _ in your flag and wrap in rtcp{...}.

(and a jpeg file)

---

`file`, `exiftool`, and `strings` don't show us anything significant. But:

```
$ steghide info rice-bowl.jpg

"rice-bowl.jpg":
  format: jpeg
  capacity: 3.3 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: (passphrase was blank)
  embedded file "steganopayload167748.txt":
    size: 21.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

`steghide extract -sf rice-bowl.jpg` gives us a file called
`steganopayload167748.txt`.

```
$ file steganopayload167748.txt

steganopayload167748.txt: ISO-8859 text
```

Taking out all lowercase characters in the challenge title gives us
"BASE64". From here, encoding the ISO-8859 text in base64 gives us the
flag.

`rtcp{s0m3t1m35_th1ng5_Ar3_3nc0D3d}`
