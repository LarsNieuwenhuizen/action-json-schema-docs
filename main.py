import jsonschema2md
import json
import sys

class JsonSchemaDocGenerator:
    def __init__(self):
        self._json_schema_file: str = None
        self._examples_as_yaml: bool = True

    @property
    def examples_as_yaml(self) -> bool:
        return self._examples_as_yaml

    @examples_as_yaml.setter
    def examples_as_yaml(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("examples_as_yaml must be a boolean")

        self._examples_as_yaml = value

    @property
    def json_schema_file(self) -> str:
        return self._json_schema_file

    @json_schema_file.setter
    def json_schema_file(self, value: str):
        if not isinstance(value, str):
            raise TypeError("json_schema_file must be a string")

        self._json_schema_file = value

    def main(self) -> None:
        try:
            Parser = jsonschema2md.Parser(
                examples_as_yaml = self.examples_as_yaml,
                show_examples="all",
            )
            self.json_schema_file = sys.argv[1]

            with open(self.json_schema_file, "r") as f:
                md_lines = Parser.parse_schema(json.load(f))

            print("\n".join(md_lines))

            with open("docs/docs.md", "w") as f:
                f.write("\n".join(md_lines))

        except IndexError:
            print("Please provide a JSON schema file location")
            sys.exit(1)

        except (TypeError) as e:
            print("Json schema string must be a string")
            print(e)
            sys.exit(1)


generator = JsonSchemaDocGenerator()
generator.main()
