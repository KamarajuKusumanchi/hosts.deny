from sshfilter import get_country

# To run the tests
# cd into the project directory
# python3 -m pytest


def test_get_country():
    ip = '67.158.225.229'
    got = get_country(ip)
    expected = 'US'
    assert expected == got, \
        'Unexpected country for ' + ip + '. Expected ' + expected + \
        ' but got ' + got + '.'
