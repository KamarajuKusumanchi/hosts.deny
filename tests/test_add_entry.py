from supplementary import add_entry

# To run the tests
# cd into the project directory
# python3 -m pytest


def test_subnet_mask():
    begin_ip_str = '218.64.0.0'
    end_ip_str = '218.65.127.255'

    got = add_entry.subnet_mask(begin_ip_str, end_ip_str)
    expected = '255.254.128.0'
    assert expected == got, \
        "Incorrect subnet mask. Expected = " + expected + ', got = ' + got
