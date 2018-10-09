import argparse
import json
import jsonschema
import sys


SCHEMA_FILE = "message_schema.json"


def validate_message_text(message):
    '''
    Test that the given message text matches the schema.

    Throws an exception with detail of the errors if any are found.

    Returns otherwise
    '''
    with open(SCHEMA_FILE, "r", encoding="utf-8") as read_schema:
        schema = json.load(read_schema)

    jsonschema.validate(message, schema)
    return True



def validate_message_file(message_file):
    '''
    Validate the message contained in the file
    '''
    with open(message_file, "r", encoding="utf-8") as in_file:
        return validate_message_text(json.load(in_file))


def main():
    '''
    Main entry point, handle argument parsing
    '''
    parser = argparse.ArgumentParser(
        description='Validate Pioneer Burn message.')
    parser.add_argument("-f", "--file", help="File containing message.")
    args = parser.parse_args()
    try:
        validate_message_file(args.file)
    except jsonschema.exceptions.ValidationError as err:
        print("Error with message:")
        print(err)
        sys.exit(1)

    print ("Message is valid!")


if __name__ == "__main__":
    main()
