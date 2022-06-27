# Combpy
A lightweight tool for cracking hashes with known values.

Sometimes developers rely on well-known parameters in generating Hashes for web applications. This tool came to help understand what combinations and separations were used to create the Hash. There is no need to explain the potential.

![ezgif-1-0b6c1902a8](https://user-images.githubusercontent.com/20946532/175826400-afb84e97-29bc-4d9c-ae0f-ea873f266f8b.gif)


## Example usage:
    python combpy.py -t 079b9b8877f36cae8f6561cde02894bc -a md5 -w admin@gmail.com,admin,ADMIN,19,1656265429


## Supported algorithms:
Since hashlib is "backed" by OpenSSL, all of the algorithms provided by that library are available, including:
- md5
- sha1
- sha224
- sha256
- sha384
- sha512

## Todo:
 - Add support with JSON Objects
