## Santa's Forensics 101

We're given a file, X-MAS_Flag2.png. Running `file X-MAS_Flag2.png`, it
turns out that it's actually a zip archive. `exiftool X-MAS_Flag2.png`
shows that there's some data inside: `Zip File Name: hidden_data_dt/`.

`unzip X-MAS_Flag2.png` gives us the hidden folder, which has another file
in it: logo2.png, which is a picture of the X-MAS CTF logo. Running
`strings logo2.png` shows the flag at the bottom:
`X-MAS{W3lc0m3_t0_th3_N0rth_Pol3}`
