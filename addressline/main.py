import json

from libpostal import get_street_housenumber


def get_json_result(data):
    return json.dumps(data, ensure_ascii=False)


def main():
    while True:
        try:
            user_input = input('Enter string of address:')
            result = get_street_housenumber(user_input)
            print(get_json_result(result))
        except (KeyboardInterrupt, EOFError):
            return


if __name__ == '__main__':
    main()
