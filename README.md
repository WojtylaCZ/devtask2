# Development task

## Requirements

- `docker` utility
- 2.9 GB of free disk space :) Read below.

## Getting started

Getting up and running is as easy as 1, 2, 3.

1. Build the docker image:  `docker build -t addressline .`
2. Run the docker image in **interactive** mode: `docker run -it -t addressline`
3. Input the address string to the interactive console.

## Usage

Interact with the interactive console of the running docker image.

## Solution

1. The key point of the solution is how to parse the address string. I was thinking and researching about the domain of this problem, I found the domain has not a straightfordward solution and there is no silver bullet. Possible solutions I considered:
    1. Write some logic to parse the string manually - using regexes, string parsing etc. Crazy idea. I believe this approach does not scale, especially when considering international addresses.
    2. Download databases of national addresses and to build infrastructure at top of that (for example using Elasticsearch). That could be an option for a production usage, but no much suitable for submission and sharing of the result.
    3. Use an external service/API, as Google Maps API for example. There could be an issue with Terms&Conditions, access to a paid service etc.
    4. I found there is this [Libpostal library](https://github.com/openvenues/libpostal). _"Library for parsing/normalizing street addresses around the world using statistical NLP and open data"_. _"The parser achieves very high accuracy on held-out data, currently 99.45% correct full parses (meaning a 1 in the numerator for getting every token in the address correct)."_ Based on OpenStreetMap.
    With [Python bindings pypostal](https://github.com/openvenues/pypostal).

2. I decided to use the **Libpostal** library to parse the address string. I guess you will say that I skipped the expected & the hardest part, on the other hand I'm curious what you think about this straightforward approach.
I do not like re-inventing wheel, I like to spend time on building solutions.
I also created public image [docker image](https://github.com/wojtylacz/pypostal-docker) with the python bindings **pypostal** installed.


## Development

### Codestyle:
Configuration file in [tox.ini](tox.ini)

To follow pep8 codestyle, see mistakes by:

`pycodestyle --show-pep8 addressline/*`

To auto apply the corrections, use:

`autopep8 -v --in-place --aggressive --aggressive  --recursive addressline/*`

### Tests
Tests are included and run when building the docker image.


## Assignment

### Addressline

An address provider returns addresses only with concatenated street names and numbers. Our own system on the other hand has separate fields for street name and street number.

**Input:** string of address

**Output:** string of street and string of street-number as JSON object

1. Write a simple program that does the task for the most simple cases, e.g.
   1. `"Winterallee 3"` -> `{"street": "Winterallee", "housenumber": "3"}`
   1. `"Musterstrasse 45"` -> `{"street": "Musterstrasse", "housenumber": "45"}`
   1. `"Blaufeldweg 123B"` -> `{"street": "Blaufeldweg", "housenumber": "123B"}`

2. Consider more complicated cases
   1. `"Am Bächle 23"` -> `{"street": "Am Bächle", "housenumber": "23"}`
   1. `"Auf der Vogelwiese 23 b"` -> `{"street": "Auf der Vogelwiese", "housenumber": "23 b"}`

3. Consider other countries (complex cases)
   1. `"4, rue de la revolution"` -> `{"street": "rue de la revolution", "housenumber": "4"}`
   1. `"200 Broadway Av"` -> `{"street": "Broadway Av", "housenumber": "200"}`
   1. `"Calle Aduana, 29"` -> `{"street": "Calle Aduana", "housenumber": "29"}`
   1. `"Calle 39 No 1540"` -> `{"street": "Calle 39", "housenumber": "No 1540"}`
   