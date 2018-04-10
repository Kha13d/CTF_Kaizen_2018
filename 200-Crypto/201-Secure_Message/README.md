## Challenge Description:

Olympic City recently setup an encrypted messaging system. <p><p>Decrypt the message to get the flag.

## Challenge Points:

100pt

## Challenge Solution:

In this challenge we have a public key and the flag encrypted with an uknown praivet key,

Checking the pub key, we can know that RSA has been used for encryption.

Using OpenSSL to convert PEM to N and e:

```shell
openssl rsa -in olympic_city.pub -pubin -inform PEM -text -noout
```

Output:

```
Public-Key: (256 bit)
Modulus:
    00:cf:d7:43:c8:47:30:ec:66:5b:13:ac:d6:1f:e0:
    5b:27:1a:cc:01:fd:06:0b:d0:56:ee:23:51:50:a5:
    af:e6:cf
Exponent: 65537 (0x10001)

```

Since the key size for the RSA is small we can factor it to find the privet key or decrypt the cipher.

Using [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) to attack RSA.

```shell
python RsaCtfTool/RsaCtfTool.py --publickey olympic_city.pub --uncipherfile flag
```


#### Flag:   flag{t00_sma11_k3y}
