# convert

This module is a Binary, Hex, Decimal, Conversion Calculator. 
It creates a Commanad Line Interface (CLI) that will perform calculations to convert the following:
```
    base_2_to_base_10
    base_10_to_base_2
    base_16_to_base_2
    base_2_to_base_16
    base_16_to_base_10
    base_10_to_base_16
```

The commands for the CLI are:
```
    -bd8,  Binary to Decimal (ie. input val = 11110000, input = 8 bits)
    -bd16, Binary to Decimal (ie. input val = 1111000011110000, input = 16 bits)
    -db8,  Decimal to Binary (ie. input val = 0 - 255, output = 8 bits)
    -db16, Decimal to Binary (ie. input val = 0 - 65535, output = 16 bits)
    -hb,   Hex to Binary (ie. input val = FFFF)
    -hd,   Hex to Decimal (ie. input val = FFFF)
    -bh8,  Binary to Hex (ie. input val = 11110000, input = 8 bits)
    -bh16, Binary to Hex (ie. input val = 1111000011110000, input = 16 bits)
    -dh,   Decimal to Hex (ie. input val = 65535)
```

This program is based on information gleaned from chapter 2 of:
    Hyde, R. (2024). The Art of ARM Assembly, Volume 1: 64-Bit ARM Machine
    Organization and Programming. O'Reilly Media.

###### Commands to run code:
```Code
$ cd your_uv_project/convert
$ uv run pytest -sv
$ uv run pytest tests/test_CLI.py -sv
$ uv run src/convert/convert.py -hd ffff
               or
$ chmod 744 src/convert/convert.py
$ ./src/convert/convert.py -hd ffff

```
Bring up help menu:
```
$ uv run src/convert/convert.py -h
               or
$ ./src/convert/convert.py -h
usage: convert.py [-h] [-bd8 | -bd16 | -db8 | -db16 | -hb | -hd | -bh8 | -bh16 | -dh] str

Binary, Hex, Decimal, Conversion Calculator

positional arguments:
  str                   Value to convert (ie. 11111111 or 255)

options:
  -h, --help            show this help message and exit
  -bd8, --bin-8-bit-dec
                        Binary to Decimal (ie. input val = 11110000, input = 8 bits)
  -bd16, --bin-16-bit-dec
                        Binary to Decimal (ie. input val = 1111000011110000, input = 16 bits)
  -db8, --dec-bin-8-bit
                        Decimal to Binary (ie. input val = 0 - 255, output = 8 bits)
  -db16, --dec-bin-16-bit
                        Decimal to Binary (ie. input val = 0 - 65535, output = 16 bits)
  -hb, --hex-bin        Hex to Binary (ie. input val = FFFF)
  -hd, --hex-dec        Hex to Decimal (ie. input val = FFFF)
  -bh8, --bin-8-bit-hex
                        Binary to Hex (ie. input val = 11110000, input = 8 bits)
  -bh16, --bin-16-bit-hex
                        Binary to Hex (ie. input val = 1111000011110000, input = 16 bits)
  -dh, --dec-hex        Decimal to Hex (ie. input val = 65535)

        This program is based on information gleaned from chapter 2 of:
            Hyde, R. (2024). The Art of ARM Assembly, Volume 1: 64-Bit ARM Machine
            Organization and Programming. O'Reilly Media.
```
## License
[MIT](/LICENSE)
