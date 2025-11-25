"""
This file contains converter functions to convert base10, base 2, and base 16
numbers.
"""


# --------------------------------------------------
def base_2_to_base_10(base_2_val: str) -> int:
    """
    The input argument base_2_val = 8 bits or 1 byte (11111111)
                 or               = 16 bit or 2 bytes (1111000011110000)

    The binary value 11001010 represents the following:
    (1 x 2⁷) + (1 x 2⁶) + (0 x 2⁵) + (0 x 2⁴) + (1 x 2³) + (0 x 2²) + (1 x 2¹) + (0 x 2⁰)
    (1 x 128) + (1 x 64) + (0 x 32) + (0 x 16) + (1 x 8) + (0 x 4) + (1 x 2) + (0 x 1)
    = 128 + 64 + 0 + 0 + 8 + 0 + 2 + 0
    = 128 + 64 + 8 + 2
    = 202
    """
    base_10_val: int = 0
    reverse_num: str = base_2_val[::-1]
    for i, n in enumerate(reverse_num):
        base_10_val += int(n) * 2**i

    return base_10_val


# --------------------------------------------------
def is_odd(num: int) -> bool:
    if num % 2 == 1:
        return True
    return False


# --------------------------------------------------
def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


# --------------------------------------------------
def pop_stack(stack: list[str], stack_size: int = 8) -> str:
    """
    Pops values from stack and fills in empty preceding values with zero.
    """
    return_val = ""
    # Default stack size for binary is 8 characters.
    stack = stack[:stack_size]

    for _ in range(len(stack)):
        return_val += stack.pop()

    # Fill empty spaces on the left side of the string with zeros (0).
    return return_val.zfill(stack_size)


# --------------------------------------------------
def base_10_to_base_2(base_10_val: int, stack_size: int = 8) -> str:
    """
    The even/odd, divide-by-2 algorithm, comprising the following steps:
    1. If the number is even, emit a 0. If the number is odd, emit a 1.
    2. Divide the number by 2 and throw away any fractional component or remainder.
    3. If the quotient is 0, the algorithm is complete.
    4. If the quotient is not 0 and is odd, insert a 1 before the current string.
       If the number is even, prefix your binary string with 0.
    5. Go back to step 2 and repeat.
    """
    my_stack: list[str] = []

    if is_even(base_10_val):
        my_stack.append("0")
    else:
        my_stack.append("1")

    quotient: int = base_10_val // 2
    if quotient == 0:
        # return values after popping them from the stack.
        return pop_stack(my_stack, stack_size)
    else:
        remainder = str(quotient % 2)  # Remainder will be 1 or 0.
        my_stack.append(remainder)

    while quotient != 0:
        quotient = quotient // 2
        remainder = str(quotient % 2)  # Remainder will be 1 or 0.
        my_stack.append(remainder)

    return pop_stack(my_stack, stack_size)


# --------------------------------------------------
def _hex_to_decimal(val: str) -> int | str:
    """
    Converts hex string, containing only 1 value, to a single decimal integer.
    Ex. "B" = 11
    """
    # fmt: off
    hex = {
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13,  "E": 14, "F": 15,
    }
    # fmt: on

    default_value = "Must use one of the following values: (0123456789ABCDEFabcdef)."
    return hex.get(val.upper(), default_value)


# --------------------------------------------------
def _hex_to_binary(val: str) -> str:
    """
    Converts hex string, containing only 1 value, to a  4 bit binary string.
    """
    # fmt: off
    hex = {
        "0": '0000', "1": '0001', "2": '0010', "3": '0011', "4": '0100', "5": '0101', 
        "6": '0110', "7": '0111', "8": '1000', "9": '1001', "A": '1010', "B": '1011',
        "C": '1100', "D": '1101',  "E": '1110', "F": '1111',
    }
    # fmt: on

    default_value = "Must use one of the following values: (0123456789ABCDEFabcdef)."
    return hex.get(val.upper(), default_value)


# --------------------------------------------------
def _binary_to_hex(val: str) -> str:
    """
    Converts a 4 bit binary string to a single hex value.
    Ex: "1111" = F
    """
    # fmt: off
    hex = {
        '0000': "0" , '0001': "1", '0010': "2", '0011': "3", '0100': "4", '0101': "5", 
        '0110': "6", '0111': "7", '1000': "8", '1001': "9", '1010': "A", '1011': "B",
        '1100': "C", '1101': "D",  '1110': "E", '1111': "F",
    }
    # fmt: on

    default_value = "Binary val must consist of 4 ones (1) or zeros (0)."
    return hex.get(val.upper(), default_value)


# --------------------------------------------------
def extract_chunks(text: str, chunk_size: int = 4) -> list[str]:
    """
    Extracts character chunks from a string. Default chunk size is 4.
    ex. extract_chunks("1111111111111111") = ['1111', '1111', '1111', '1111']

    Note: This function was edited and enhanced from a Google AI example.
    """
    chunks: list[str] = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i : i + chunk_size])

    return chunks


# --------------------------------------------------
def base_16_to_base_2(base_16_val: str) -> str:
    """
    Converts a base 16 string value into a base 2 string value.

    """
    base_2_val = ""

    for val in base_16_val:
        base_2_val += str(_hex_to_binary(val))

    return base_2_val


# --------------------------------------------------
def base_2_to_base_16(base_2_val: str) -> str:
    """
    Converts a base 2 string value into a base 16 string value.

    The base 2 value must consist of multiples of 4, binary values.
    Ex. "1010", or "11110000", "111101010000", "1010111101010000".

    To convert a binary (base 2) number to a hex number (base 16):
    1. Separate the binary value into groups of 4 bits.
    2. Look up these binary values and substitute the appropriate hexadecimal digits.
    """
    if len(base_2_val) % 4 != 0:
        raise ValueError("The length of the input string must be divisible by 4.")
    base_16_val = ""

    four_bit_vals = extract_chunks(base_2_val)
    for binary_val in four_bit_vals:
        base_16_val += str(_binary_to_hex(binary_val))

    return base_16_val


# --------------------------------------------------
def base_16_to_base_10(base_16_val: str) -> int:
    """
    The input arguement base_16_val = 4 bits (FFFF).

    The hex number 1,234 is equal to this:
    (1 x 16³) + (2 x 16²) + (3 x 16¹) + (4 x 16⁰)
    (1 x 4,096) + (2 x 256) + (3 x 16) + (4 x 1)
    or
    4,096 + 512 + 48 + 4 = 4,660
    """
    base_10_val: int = 0
    reverse_num: str = base_16_val[::-1]
    for i, n in enumerate(reverse_num):
        base_10_val += _hex_to_decimal(n) * 16**i

    return base_10_val


# --------------------------------------------------
def base_10_to_base_16(base_10_val: int) -> str:
    """
    To convert a decimal (base 10) number to a hex number (base 16):
    1. Convert decimal number (base 10) to a binary number (base 2)
    2. Convert binary number (base 2) to a hex number (base 16)
    """
    base_16_val: str = ""

    base_2_val = base_10_to_base_2(base_10_val, stack_size=16)
    base_16_val = base_2_to_base_16(base_2_val)

    """ reverse_num: str = base_16_val[::-1]
    for i, n in enumerate(reverse_num):
        base_10_val += hex_to_decimal(n) * 16**i """

    return base_16_val
