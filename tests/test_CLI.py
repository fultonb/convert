import sys

import pytest

from convert import main

"""
These test the command line interface flags using capsys, and monkeypatch:

    -bd8,  Binary to Decimal (ie. input val = 11110000, input = 8 bits)
    -bd16, Binary to Decimal (ie. input val = 1111000011110000, input = 16 bits)
    -db8,  Decimal to Binary (ie. input val = 0 - 255, output = 8 bits)
    -db16, Decimal to Binary (ie. input val = 0 - 65535, output = 16 bits)
    -hb,   Hex to Binary (ie. input val = FFFF)
    -hd,   Hex to Decimal (ie. input val = FFFF)
    -bh8,  Binary to Hex (ie. input val = 11110000, input = 8 bits)
    -bh16, Binary to Hex (ie. input val = 1111000011110000, input = 16 bits)
    -dh,   Decimal to Hex (ie. input val = 65535)

Note: Got this example by googling:
    testing a command line arguments example with pytest and importing the app file
"""


@pytest.mark.parametrize(
    "flag, val_to_convert, expected_val",
    [
        ("-bd8", "10101101", "173"),
        ("-bd16", "1010110100001100", "44300"),
        ("-db8", "123", "01111011"),
        ("-db16", "123", "0000000001111011"),
        ("-hb", "FF7F", "1111111101111111"),
        ("-hd", "FFFF", "65535"),
        ("-bh8", "11001100", "CC"),
        ("-bh16", "1100110011110011", "CCF3"),
        ("-dh", "345", "0159"),
    ],
)
def test_convert_hd_capsys(capsys, flag, val_to_convert, expected_val) -> None:
    """
    This is how you test CLI applications using capsys.
    """
    # Simulate command line arguments as a list (excluding script name)
    test_args = [flag, val_to_convert]

    # Call the main function directly with the simulated arguments
    result = main(test_args)

    # Capture the output
    captured = capsys.readouterr()
    expected_output = expected_val + "\n"

    # Assert the return value and the printed output
    assert captured.out == expected_output
    assert result == expected_val


@pytest.mark.parametrize(
    "flag, val_to_convert, expected_val",
    [
        ("-bd8", "10101101", "173"),
        ("-bd16", "1010110100001100", "44300"),
        ("-db8", "123", "01111011"),
        ("-db16", "123", "0000000001111011"),
        ("-hb", "FF7F", "1111111101111111"),
        ("-hd", "FFFF", "65535"),
        ("-bh8", "11001100", "CC"),
        ("-bh16", "1100110011110011", "CCF3"),
        ("-dh", "345", "0159"),
    ],
)
def test_convert_hd_monkeypatch(
    monkeypatch, capsys, flag, val_to_convert, expected_val
) -> None:
    """
    This is how you test CLI applications using monkeypatch with capsys.
    """
    # Mock sys.argv as a list of strings
    monkeypatch.setattr(sys, "argv", ["convert.py", flag, val_to_convert])

    # Call the main function without arguments, so it uses the mocked sys.argv
    main()

    # Capture the output
    captured = capsys.readouterr()
    expected_output = expected_val + "\n"

    # Assert the return value
    assert captured.out == expected_output
