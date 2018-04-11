## Challenge Description:

Detect and decode the PHP file found in the source code.

## Challenge Points:

300pt

## Challenge Solution:

On this challenge you can start your own php server and start testing the index.php page to find the flag.

For more info [PHP](https://secure.php.net/manual/en/features.commandline.webserver.php).


When you run the server 'Hello World' will show up and when you see the php code in index.php

```php
eval(base64_decode('ZXZhbChodG1sc3BlY2lhbGNoYXJzX2RlY29kZShiYXNlNjRfZGVjb2RlKGd6dW5jb21wcmVzcyhnenVuY29tcHJlc3MoZ3p1bmNvbXByZXNzKGd6dW5jb21wcmVzcyhiYXNlNjRfZGVjb2RlKCRjKSkpKSkpKSk7'));
```

Let's break it one by one and see what is happening!
At first we will decode string.

```php
echo (base64_decode('ZXZhbChodG1sc3BlY2lhbGNoYXJzX2RlY29kZShiYXNlNjRfZGVjb2RlKGd6dW5jb21wcmVzcyhnenVuY29tcHJlc3MoZ3p1bmNvbXByZXNzKGd6dW5jb21wcmVzcyhiYXNlNjRfZGVjb2RlKCRjKSkpKSkpKSk7'))
```

The output

```
eval(htmlspecialchars_decode(base64_decode(gzuncompress(gzuncompress(gzuncompress(gzuncompress(base64_decode($c))))))));
```

Let's see what the decodeing at the end will be:

```php
echo base64_decode(gzuncompress(gzuncompress(gzuncompress(gzuncompress(base64_decode($c))))));
```

We can see that $c will take a new value and a new $file will be created:

```
$c = file_get_contents('./0565d13d582a9f3bc664ef77b7fc74f8'); $file = file_get_contents('./8b99a1ff227a9353c98029a41d911612'); eval(base64_decode("$file")); 
```

And if you keep going it will repeate the same pattern.


Therefore, We should let it eval() everything and see the last result of $c

```php
$c = 'eJwB0gAt/3icAccAOP94nAG8AEP/eJyFzr0OgjAYheFb0tbEODhUlKbFfkT9ANsRjGB/1ISIwtVLjImjw1mf80YXVouIOd2zheDmXvL8bEg+ORLoyuvejxuSqHpsBzYFmzuF4ADrXqMPikgLVk9MoSkQQU1QFLieyd7No69rgm/N4Z/dXFL0jSpGwQqq0Q2AYFOsn8r6BtaxS3HzArvpf/bKn0LcJlw2FckIxAtnCugMz27yGk9LupvLz2cWqmPendbtPcE2GZtqwZbLN5w5U4Nq/l9bSBJkkFjUaPE=';
eval(base64_decode('ZXZhbChodG1sc3BlY2lhbGNoYXJzX2RlY29kZShiYXNlNjRfZGVjb2RlKGd6dW5jb21wcmVzcyhnenVuY29tcHJlc3MoZ3p1bmNvbXByZXNzKGd6dW5jb21wcmVzcyhiYXNlNjRfZGVjb2RlKCRjKSkpKSkpKSk7'));
echo $c;
``` 

And it look like a compressed base64 encoded something:

```php
$c = 'eJwB0gAt/3icAccAOP94nAG8AEP/eJyFzr0OgjAYheFb0tbEODhUlKbFfkT9ANsRjGB/1ISIwtVLjImjw1mf80YXVouIOd2zheDmXvL8bEg+ORLoyuvejxuSqHpsBzYFmzuF4ADrXqMPikgLVk9MoSkQQU1QFLieyd7No69rgm/N4Z/dXFL0jSpGwQqq0Q2AYFOsn8r6BtaxS3HzArvpf/bKn0LcJlw2FckIxAtnCugMz27yGk9LupvLz2cWqmPendbtPcE2GZtqwZbLN5w5U4Nq/l9bSBJkkFjUaPE=';
eval(base64_decode('ZXZhbChodG1sc3BlY2lhbGNoYXJzX2RlY29kZShiYXNlNjRfZGVjb2RlKGd6dW5jb21wcmVzcyhnenVuY29tcHJlc3MoZ3p1bmNvbXByZXNzKGd6dW5jb21wcmVzcyhiYXNlNjRfZGVjb2RlKCRjKSkpKSkpKSk7'));
echo base64_decode(gzuncompress(gzuncompress(gzuncompress(gzuncompress(base64_decode($c))))));
```

There you go the flag on the page.

### Other Way:

Use (get_defined_vars)[https://secure.php.net/manual/en/function.get-defined-vars.php] and it will returns an array of all defined variables.

```php
$c = 'eJwB0gAt/3icAccAOP94nAG8AEP/eJyFzr0OgjAYheFb0tbEODhUlKbFfkT9ANsRjGB/1ISIwtVLjImjw1mf80YXVouIOd2zheDmXvL8bEg+ORLoyuvejxuSqHpsBzYFmzuF4ADrXqMPikgLVk9MoSkQQU1QFLieyd7No69rgm/N4Z/dXFL0jSpGwQqq0Q2AYFOsn8r6BtaxS3HzArvpf/bKn0LcJlw2FckIxAtnCugMz27yGk9LupvLz2cWqmPendbtPcE2GZtqwZbLN5w5U4Nq/l9bSBJkkFjUaPE=';
eval(base64_decode('ZXZhbChodG1sc3BlY2lhbGNoYXJzX2RlY29kZShiYXNlNjRfZGVjb2RlKGd6dW5jb21wcmVzcyhnenVuY29tcHJlc3MoZ3p1bmNvbXByZXNzKGd6dW5jb21wcmVzcyhiYXNlNjRfZGVjb2RlKCRjKSkpKSkpKSk7'));
$arr = get_defined_vars();
print_r($arr);
```

#### Flag: $flag = "SAFCSP{FUN_WITH_PHP_BACKDOOR_0PHP}"
