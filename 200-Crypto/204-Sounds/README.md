## Challenge Description:

Olympic City intelligence officials recently picked up the following transmission. They think there is a hidden message.

## Challenge Points:

100pt

## Challenge Solution:

This was a fun challenge, when you run the sound you will know it is a morse code.

by using [Morsecode Scphillips](https://morsecode.scphillips.com/labs/audio-decoder-adaptive/) upload the wav file and let it decode the morse code:

```
7374656768696465207468652070617373776F72642069732070656163686573
```

This a hex string let's decode it:

```
echo '7374656768696465207468652070617373776F72642069732070656163686573' | xxd -r -p
```

and this is the decoded hex:

```
steghide the password is peaches
```

Now we can use Steghide with the password peaches to see what is inside the wav file:

```
steghide info sound.wav -p peaches
```

And there you go the flag is there

```
"sound.wav":
  format: wave audio, PCM encoding
  capacity: 171.2 KB
  embedded file "flag.txt":
    size: 66.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

Now to extract the flag 

```
steghide extract -sf sound.wav -p peaches 
```


#### Flag:  the flag is: morse_code_hex_and_stego_what_more_could_one_ask_for
