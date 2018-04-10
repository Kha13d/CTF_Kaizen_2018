## Challenge Description:

Olympic City is looking into ways to improve connectivity. The following dump was found on the consultant’s laptop. Can you find what it says?

## Challenge Points:

100pt

## Challenge Solution:

The 'dump.txt' file look like a hex encoded text:

```shell
cat dump.txt | xxd -r -p
```

The output:

```
chr(102),chr(108),chr(97),chr(103),chr(58),chr(123),chr(73),chr(69),chr(69),chr(69),chr(95),chr(56),chr(48),chr(50),chr(46),chr(49),chr(53),chr(46),chr(52),chr(125)
```

It is CHR function using Python we find the Flag

### Flag: flag:{IEEE_802.15.4}
