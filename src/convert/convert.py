#!/usr/bin/env python3
"""
Author : Brad Fulton <fultonbd@gmail.com>
Date   : 2025-11-12
Purpose: Binary, hex, decimal conveerter CLI

This module creates the Commanad Line Interface (CLI) that will perform
calculations to convert the following:
    base_2_to_base_10
    base_10_to_base_2
    base_16_to_base_2
    base_2_to_base_16
    base_16_to_base_10
    base_10_to_base_16

This program is based on information gleaned from chapter 2 of:
    Hyde, R. (2024). The Art of ARM Assembly, Volume 1: 64-Bit ARM Machine
    Organization and Programming. O'Reilly Media.

"""

import argparse
from typing import NamedTuple

from converters import (
    base_2_to_base_10,
    base_2_to_base_16,
    base_10_to_base_2,
    base_10_to_base_16,
    base_16_to_base_2,
    base_16_to_base_10,
)


class Args(NamedTuple):
    """Command-line arguments"""

    bin_8_bit_dec: bool
    bin_16_bit_dec: bool
    dec_bin_8_bit: bool
    dec_bin_16_bit: bool
    hex_bin: bool
    bin_8_bit_hex: bool
    bin_16_bit_hex: bool
    hex_dec: bool
    dec_hex: bool
    val: str


# --------------------------------------------------
def get_args(argv: list[str] | None = None) -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Binary, Hex, Decimal, Conversion Calculator",
        epilog="""
        This program is based on information gleaned from chapter 2 of:
            Hyde, R. (2024). The Art of ARM Assembly, Volume 1: 64-Bit ARM Machine
            Organization and Programming. O'Reilly Media.
        """,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # Create a mutually exclusive group
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-bd8",
        # Define using dashes, argparse automatically sets dest='bin_8_bit_dec'
        "--bin-8-bit-dec",
        help="Binary to Decimal (ie. input val = 11110000, input = 8 bits)",
        action="store_true",
    )

    group.add_argument(
        "-bd16",
        # Define using dashes, argparse automatically sets dest='bin_16_bit_dec'
        "--bin-16-bit-dec",
        help="Binary to Decimal (ie. input val = 1111000011110000, input = 16 bits)",
        action="store_true",
    )

    group.add_argument(
        "-db8",
        # Define using dashes, argparse automatically sets dest='dec_bin_8_bit'
        "--dec-bin-8-bit",
        help="Decimal to Binary (ie. input val = 0 - 255, output = 8 bits)",
        action="store_true",
    )

    group.add_argument(
        "-db16",
        # Define using dashes, argparse automatically sets dest='dec_bin_16_bit'
        "--dec-bin-16-bit",
        help="Decimal to Binary (ie. input val = 0 - 65535, output = 16 bits)",
        action="store_true",
    )

    group.add_argument(
        "-hb",
        # Define using dashes, argparse automatically sets dest='hex_bin'
        "--hex-bin",
        help="Hex to Binary (ie. input val = FFFF)",
        action="store_true",
    )

    group.add_argument(
        "-hd",
        # Define using dashes, argparse automatically sets dest='hex_dec'
        "--hex-dec",
        help="Hex to Decimal (ie. input val = FFFF)",
        action="store_true",
    )

    group.add_argument(
        "-bh8",
        # Define using dashes, argparse automatically sets dest='bin_8_bit_hex'
        "--bin-8-bit-hex",
        help="Binary to Hex (ie. input val = 11110000, input = 8 bits)",
        action="store_true",
    )

    group.add_argument(
        "-bh16",
        # Define using dashes, argparse automatically sets dest='bin_16_bit_hex'
        "--bin-16-bit-hex",
        help="Binary to Hex (ie. input val = 1111000011110000, input = 16 bits)",
        action="store_true",
    )

    group.add_argument(
        "-dh",
        # Define using dashes, argparse automatically sets dest='dec_hex'
        "--dec-hex",
        help="Decimal to Hex (ie. input val = 65535)",
        action="store_true",
    )

    # Required positional argument
    parser.add_argument(
        "val",
        help="Value to convert (ie. 11111111 or 255)",
        metavar="str",
        type=str,
    )

    args = parser.parse_args(argv)

    if args.bin_8_bit_dec or args.bin_8_bit_hex:
        try:
            validate_binary_string(args.val, size=8)
        except ValueError as ve:
            parser.error(f"{ve.args[0]}")

    if args.bin_16_bit_dec or args.bin_16_bit_hex:
        try:
            validate_binary_string(args.val, size=16)
        except ValueError as ve:
            parser.error(f"{ve.args[0]}")

    if args.hex_dec:
        try:
            validate_hex_string(args.val)
        except ValueError as ve:
            parser.error(f"{ve.args[0]}")

    if args.dec_bin_8_bit:
        try:
            validate_integer_string(args.val, 8)
        except ValueError as ve:
            parser.error(f"{ve.args[0]}")

    if args.dec_bin_16_bit or args.dec_hex:
        try:
            validate_integer_string(args.val, 16)
        except ValueError as ve:
            parser.error(f"{ve.args[0]}")

    # Note: These args must be returned in the same order as they are listed
    #       above under "Command-line arguments".
    return Args(
        args.bin_8_bit_dec,
        args.bin_16_bit_dec,
        args.dec_bin_8_bit,
        args.dec_bin_16_bit,
        args.hex_bin,
        args.bin_8_bit_hex,
        args.bin_16_bit_hex,
        args.hex_dec,
        args.dec_hex,
        args.val,
    )


# --------------------------------------------------
def validate_binary_string(s: str, size: int) -> None:
    """
    Validates if a string contains only '0' or '1' and has a length of 8.
    Raises a ValueError if the conditions are not met.

    Note: This function was edited and enhanced from a Google AI example.
    """
    error_val = ""
    if len(s) != size:
        error_val += f"String must be exactly {size} characters long."

    for char in s:
        if char not in "01":
            error_val += " String must contain only '0' or '1' characters."
            break

    if len(error_val) > 0:
        raise ValueError(error_val)


# --------------------------------------------------
def validate_hex_string(s: str) -> None:
    """
    Validates if a string contains only these characters (0123456789ABCDEFabcdef)
    and has a length of 4.
    Raises a ValueError if the conditions are not met.

    Note: This function was edited and enhanced from a Google AI example.
    """
    error_val = ""
    if len(s) != 4:
        error_val += "String must be exactly 4 characters long."

    for char in s:
        if char not in "0123456789ABCDEFabcdef":
            error_val += (
                " String must contain only these characters: (0123456789ABCDEFabcdef)."
            )
            break

    if len(error_val) > 0:
        raise ValueError(error_val)


# --------------------------------------------------
def validate_integer_string(s: str, size: int) -> None:
    """
    Validates if a string is a valid positive integer between 0 and 255.
    """
    error_val = ""

    if size == 8 and int(s) > 255:
        error_val += "Decimal input must be between 0 and 255."
    elif size == 16 and int(s) > 65535:
        error_val += "Decimal input must be between 0 and 65535."

    if not s.isdigit():
        error_val += "String must be a positive integer value."

    if len(error_val) > 0:
        raise ValueError(error_val)


# --------------------------------------------------
def main(argv: list[str] | None = None) -> str:
    """Run program."""
    args = get_args(argv)

    is_bin_8_bit_dec = args.bin_8_bit_dec
    is_bin_16_bit_dec = args.bin_16_bit_dec
    is_dec_bin_8_bit = args.dec_bin_8_bit
    is_dec_bin_16_bit = args.dec_bin_16_bit
    is_hex_bin = args.hex_bin
    is_bin_8_bit_hex = args.bin_8_bit_hex
    is_bin_16_bit_hex = args.bin_16_bit_hex
    is_hex_dec = args.hex_dec
    is_dec_hex = args.dec_hex
    val = args.val

    return_val: str = ""

    if is_bin_8_bit_dec:
        return_val = str(base_2_to_base_10(val))
        print(return_val)
        return return_val
    elif is_bin_16_bit_dec:
        return_val = str(base_2_to_base_10(val))
        print(return_val)
        return return_val
    elif is_dec_bin_8_bit:
        return_val = base_10_to_base_2(int(val))
        print(return_val)  # Default stack size is 8.
        return return_val
    elif is_bin_8_bit_hex:
        return_val = base_2_to_base_16(val)
        print(return_val)
        return return_val
    elif is_bin_16_bit_hex:
        return_val = base_2_to_base_16(val)
        print(return_val)
        return return_val
    elif is_dec_bin_16_bit:
        return_val = base_10_to_base_2(int(val), stack_size=16)
        print(return_val)
        return return_val
    elif is_hex_bin:
        return_val = base_16_to_base_2(val)
        print(return_val)
        return return_val
    elif is_hex_dec:
        return_val = str(base_16_to_base_10(val))
        print(return_val)
        return return_val
    elif is_dec_hex:
        return_val = base_10_to_base_16(int(val))
        print(return_val)
        return return_val

    return "Error"


# --------------------------------------------------
if __name__ == "__main__":
    main()
