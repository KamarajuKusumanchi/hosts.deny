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


def test_no_country():
    ip = '193.169.252.228'
    country = get_country(ip)
    assert country is None, \
        'Expected country to be None for ' + ip + '. But instead got ' + \
        country + '.'
