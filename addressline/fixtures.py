test_data = [
    {'input': 'Winterallee 3', 'output': {'street': 'Winterallee', 'housenumber': '3'}},
    {'input': 'Musterstrasse 45', 'output': {'street': 'Musterstrasse', 'housenumber': '45'}},
    {'input': 'Blaufeldweg 123B', 'output': {'street': 'Blaufeldweg', 'housenumber': '123B'}},

    {'input': 'Am Bächle 23', 'output': {'street': 'Am Bächle', 'housenumber': '23'}},
    {'input': 'Auf der Vogelwiese 23 b', 'output': {'street': 'Auf der Vogelwiese', 'housenumber': '23 b'}},

    {'input': '4, rue de la revolution', 'output': {'street': 'rue de la revolution', 'housenumber': '4'}},
    {'input': '200 Broadway Av', 'output': {'street': 'Broadway Av', 'housenumber': '200'}},
    {'input': 'Calle Aduana, 29', 'output': {'street': 'Calle Aduana', 'housenumber': '29'}},
    {'input': 'Calle 39 No 1540', 'output': {'street': 'Calle 39', 'housenumber': 'No 1540'}},

    {'input': 'An der Alster', 'output': {'street': 'An der Alster', 'housenumber': None}},
    {'input': 'Brandenburgische Str. 16', 'output': {'street': 'Brandenburgische Str.', 'housenumber': '16'}},
    {'input': 'Nad Královskou oborou 189/7', 'output': {'street': 'Nad Královskou oborou', 'housenumber': '189/7'}},
    {'input': 'foo', 'output': {'street': None, 'housenumber': None}},
    {'input': 'foo 123', 'output': {'street': 'foo', 'housenumber': '123'}},
    {'input': '', 'output': {'street': None, 'housenumber': None}},
    {'input': ' ', 'output': {'street': None, 'housenumber': None}},
    {'input': '122', 'output': {'street': None, 'housenumber': None}},
    {'input': 'ščšščěč 66', 'output': {'street': 'ščšščěč', 'housenumber': '66'}}
]
