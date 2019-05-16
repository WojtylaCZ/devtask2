from libpostal import get_street_housenumber
from fixtures import test_data


class TestLibpostal:
    def test_street_housenumber(self):
        for data in test_data:
            result = get_street_housenumber(data['input'])
            assert result['street'] == data['output']['street']
            assert result['housenumber'] == data['output']['housenumber']
