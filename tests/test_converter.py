import pytest
from converters import (
    _binary_to_hex,
    _hex_to_binary,
    _hex_to_decimal,
    base_2_to_base_10,
    base_10_to_base_2,
    base_10_to_base_16,
    base_16_to_base_2,
    base_16_to_base_10,
    extract_chunks,
    is_even,
    is_odd,
    pop_stack,
)


def test_reverse_string() -> None:
    num: str = "11001010"
    result: str = num[::-1]
    expected: str = "01010011"
    assert result == expected


@pytest.mark.parametrize(
    "base_2_val, expected",
    [
        ("11001010", 202),
        ("11111111", 255),
        ("10111101", 189),
        ("1111111111111111", 65535),
    ],
)
def test_base_2_base_10(base_2_val: str, expected: int) -> None:  # type: ignore
    assert base_2_to_base_10(base_2_val) == expected


@pytest.mark.parametrize(
    "num, expected",
    [
        (5, True),
        (50, False),
        (0, False),
    ],
)
def test_is_odd(num: int, expected: bool) -> None:
    assert is_odd(num) == expected


@pytest.mark.parametrize(
    "num, expected",
    [
        (6, True),
        (67, False),
        (0, True),
    ],
)
def test_is_even(num: int, expected: bool) -> None:
    assert is_even(num) == expected


def test_pop_stack() -> None:
    stack: list[str] = ["1", "0", "0", "1", "1", "0"]
    result: str = pop_stack(stack)
    expected: str = "00011001"
    assert result == expected


@pytest.mark.parametrize(
    "base_10_val, sz, expected",
    [
        (25, 8, "00011001"),
        (255, 8, "11111111"),
        (2, 8, "00000010"),
        (65535, 16, "1111111111111111"),
    ],
)
def test_base_10_to_base_2(base_10_val: int, sz: int, expected: str) -> None:
    assert base_10_to_base_2(base_10_val, stack_size=sz) == expected


@pytest.mark.parametrize(
    "val, expected",
    [
        ("0", 0),
        ("D", 13),
        ("d", 13),
        ("F", 15),
        ("Z", "Must use one of the following values: (0123456789ABCDEFabcdef)."),
    ],
)
def test_get_hex_value(val: str, expected: int) -> None:
    assert _hex_to_decimal(val) == expected


@pytest.mark.parametrize(
    "val, expected",
    [
        ("0", "0000"),
        ("D", "1101"),
        ("d", "1101"),
        ("F", "1111"),
        ("Z", "Must use one of the following values: (0123456789ABCDEFabcdef)."),
    ],
)
def test_hex_to_binary(val: str, expected: str) -> None:
    assert _hex_to_binary(val) == expected


@pytest.mark.parametrize(
    "val, expected",
    [
        ("0000", "0"),
        ("1101", "D"),
        ("1111", "F"),
        ("Z", "Binary val must consist of 4 ones (1) or zeros (0)."),
    ],
)
def test_binary_to_hex(val: str, expected: str) -> None:
    assert _binary_to_hex(val) == expected


@pytest.mark.parametrize(
    "val, expected",
    [
        ("0000", "0000000000000000"),
        ("0FD0", "0000111111010000"),
        ("0fd0", "0000111111010000"),
        ("0022", "0000000000100010"),
        ("Z", "Must use one of the following values: (0123456789ABCDEFabcdef)."),
    ],
)
def test_base_16_to_base_2(val: str, expected: str) -> None:
    assert base_16_to_base_2(val) == expected


@pytest.mark.parametrize(
    "base_16_val, expected",
    [
        ("1234", 4660),
        ("FFFF", 65535),
        ("ffff", 65535),
        ("BEEF", 48879),
    ],
)
def test_base_16_base_10(base_16_val: str, expected: int) -> None:  # type: ignore
    assert base_16_to_base_10(base_16_val) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("1100101011111111", ["1100", "1010", "1111", "1111"]),
        ("1111111111111111", ["1111", "1111", "1111", "1111"]),
    ],
)
def test_extract_chunks(text: str, expected: list[str]) -> None:  # type: ignore
    assert extract_chunks(text) == expected


@pytest.mark.parametrize(
    "base_10_val, expected",
    [
        (2, "0002"),
        (4660, "1234"),
        (65535, "FFFF"),
        (65535, "FFFF"),
        (48879, "BEEF"),
    ],
)
def test_base_10_base_16(base_10_val: int, expected: int) -> None:  # type: ignore
    assert base_10_to_base_16(base_10_val) == expected
