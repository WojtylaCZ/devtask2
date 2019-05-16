from postal.parser import parse_address


def get_street_housenumber(address):
    try:
        parsed_address = parse_address(address)
    except Exception:
        return {'street': None, 'housenumber': None}

    street = None
    housenumber = None
    for info in parsed_address:
        if info[1] == 'road':
            street_lowercase = info[0]
            index_original_street = address.lower().find(street_lowercase)
            street = address[index_original_street: index_original_street + len(street_lowercase)]
        elif info[1] == 'house_number':
            housenumber_lowercase = info[0]
            index_original_housenumber = address.lower().find(housenumber_lowercase)
            housenumber = address[index_original_housenumber: index_original_housenumber + len(housenumber_lowercase)]

    return {'street': street, 'housenumber': housenumber}
