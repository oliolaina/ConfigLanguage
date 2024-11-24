import json
import re
import sys


def parse_json(data):
    output = []

    def convert_value(value):
        if isinstance(value, dict):
            return convert_dict(value)
        elif isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, (int, float)):
            return str(value)
        else:
            raise ValueError(f"Unsupported value type: {type(value)}")

    def convert_dict(d):
        entries = []
        for key, value in d.items():
            if not re.match(r'^[a-zA-Z][_a-zA-Z0-9]*$', key):
                raise ValueError(f"Invalid name: {key}")
            entries.append(f"{key} => {convert_value(value)}")
        return "table(\n" + ",\n".join(entries) + "\n)"

    for key, value in data.items():
        if not re.match(r'^[a-zA-Z][_a-zA-Z0-9]*$', key):
            raise ValueError(f"Invalid name: {key}")
        if key == "comment":
            output.append("C "+value)
        if isinstance (value, str) and value[0]==value[-1]=="|" and value[1:-1] in data:
            output.append(f"(def {key} {convert_value(data[value[1:-1]])})")
        else:
            output.append(f"(def {key} {convert_value(value)})")

    return "\n".join(output)


def main():

    input_file = "config3.json"
    if (len(sys.argv) >= 2):
        input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        #print(json_data)
        output = parse_json(json_data)
        print(output)

    except FileNotFoundError:
        print(f"Error: File not found: {input_file}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
