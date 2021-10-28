import pytest
import requests
#used pytest-responsemock

def for_test():
    return requests.get(
        'http://api.weatherapi.com/v1/current.json?key=e9a0950268484d07927114250212310&q=London&aqi=yes')


def test_me(response_mock):
    with response_mock(
            'GET http://api.weatherapi.com/v1/current.json?key=e9a0950268484d07927114250212310&q=London&aqi=yes -> 200 :City of London',
            bypass=False):
        result = for_test()

        assert result.ok
        assert result.content == b'City of London'
