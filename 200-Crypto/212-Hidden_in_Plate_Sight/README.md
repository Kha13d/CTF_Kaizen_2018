## Challenge Description:

Find the flag hidden in the image

## Challenge Points:

100pt

## Challenge Solution:

Check the file information:

```
file d3cryp4_k3y.jpg
```
The is a commnet encoded with base 64 on the image

```
d3cryp4_k3y.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "c3RlZ2hpZGUK", baseline, precision 8, 2048x1536, frames 3
```

Decode the comment:

```
echo "c3RlZ2hpZGUK" | base64 -d
```

and there is a hint:

```
steghide
```

Check the image using Steghide and the password of course is the plate

```
steghide info d3cryp4_k3y.jpg -p SDN7484U
```
The flag is there:

```
"d3cryp4_k3y.jpg":
  format: jpeg
  capacity: 48.4 KB
  embedded file "flag.txt":
    size: 37.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```
Extract the flag:

```
steghide extract -sf d3cryp4_k3y.jpg -p SDN7484U
```


#### Flag: c1a5d92b-fbe7-4fa8-ba59-0d637e6851ba

###### Not Sure about the flag!
