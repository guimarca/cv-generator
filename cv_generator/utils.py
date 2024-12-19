import json
import os.path
import uuid

ASSETS_PATH = "assets"
SOURCE_DATA_PATH = "source_data"
OUTPUT_PATH = "output"
JSON_OUTPUT_PATH = os.path.join(OUTPUT_PATH, "json")


def create_json(name: str, data: dict | list):
    json_str = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
    if not os.path.exists(JSON_OUTPUT_PATH):
        os.mkdir(JSON_OUTPUT_PATH)
    with open(os.path.join(JSON_OUTPUT_PATH, f"{name}.json"), "w") as f:
        f.writelines(json_str.decode())


def protect_email(email: str) -> str:
    def insert_garbage(text: str) -> str:
        len_half = len(text) // 2
        part1, part2 = text[:len_half], text[len_half:]
        return f"<span style='display: none'>{str(uuid.uuid4())}</span>".join(
            [part1, part2]
        )

    username, domain = email.split("@")
    dname, ext = domain.split(".")
    domain = " (dot) ".join([insert_garbage(dname), ext])
    return " (at) ".join([insert_garbage(username), domain])
