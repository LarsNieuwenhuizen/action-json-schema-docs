import jsonschema2md
import json
import sys
import os

class JsonSchemaDocGenerator:
    def __init__(self):
        self._json_schema_dir: str = None
        self._documentation_dir: str = None
        self._examples_as_yaml: bool = True

    @property
    def documentation_dir(self) -> str:
        return self._documentation_dir

    @documentation_dir.setter
    def documentation_dir(self, value: str):
        if not isinstance(value, str):
            raise TypeError("documentation_dir must be a string")

        self._documentation_dir = value

    @property
    def examples_as_yaml(self) -> bool:
        return self._examples_as_yaml

    @examples_as_yaml.setter
    def examples_as_yaml(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("examples_as_yaml must be a boolean")

        self._examples_as_yaml = value

    @property
    def json_schema_dir(self) -> str:
        return self._json_schema_dir

    @json_schema_dir.setter
    def json_schema_dir(self, value: str):
        if not isinstance(value, str):
            raise TypeError("json_schema_dir must be a string")

        self._json_schema_dir = value

    def generateMarkdown(self, json_schema: str) -> None:
        try:
            Parser = jsonschema2md.Parser(
                examples_as_yaml = self.examples_as_yaml,
                show_examples="all",
            )
            self.json_schema = self.json_schema_dir + "/" + json_schema

            with open(self.json_schema, "r") as f:
                md_lines = Parser.parse_schema(json.load(f))


            with open("docs/" + json_schema + ".md", "w") as f:
                f.write("\n".join(md_lines))

        except IndexError:
            print("Please provide a JSON schema file location")
            sys.exit(1)

        except (TypeError) as e:
            print("Json schema string must be a string")
            print(e)
            sys.exit(1)

    def main(self) -> None:
        self.json_schema_dir = sys.argv[1]
        self.documentation_dir = sys.argv[2]

        if len(sys.argv) > 3:
            if sys.argv[3].lower() == "false":
                self.examples_as_yaml = False
            else:
                self.examples_as_yaml = True

        for json_schema in os.listdir(self.json_schema_dir):
            print(json_schema)
            if json_schema.endswith(".json"):
                self.generateMarkdown(json_schema)

generator = JsonSchemaDocGenerator()
generator.main()
