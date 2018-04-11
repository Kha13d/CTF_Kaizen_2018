## Challenge Description:

RSA is one of the strongest algorithms in history, combined with a massive key size it theoretically unbreakable, dude

## Challenge Points:

200pt

## Challenge Solution:

In this Challenge an RSA exponent (e) and modulus (n) is given and ciphertext (c).

All as a Hex number, we start with switching Hex to Decimal:

```
n = 47647552610849991581623686424393574412828853046763216104779659686338258908418098969172243993422261228448253602327312634239155223658496000000000000000000000000001
e = 65537
c = 820300114728129237419924110634789219857004146567907172220054986734484161696312148275727172778214900713787353071744964135115576008086912291654234356839087199969
```
Now attack the public key to find the privet key.

You can use [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) to find the privete key, or you use [Factordb](http://factordb.com/)

##### RSACTFTOOL:

```
python RsaCtfTool.py --createpub -n 47647552610849991581623686424393574412828853046763216104779659686338258908418098969172243993422261228448253602327312634239155223658496000000000000000000000000001 -e 65537 > pub.pub
python RsaCtfTool.py --publickey "pub.pub" -privete
```

##### Factordb:

python code: dec_sol.py

### Flag: SAFCSP{always_check_RSA_parameters_for_FIPS_compliance}
