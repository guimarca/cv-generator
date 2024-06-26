import json
import os.path
import uuid

FILES_PATH = "files"
SOURCE_DATA_PATH = "source_data"


def create_json(name: str, data: dict | list):
    json_str = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
    json_path = os.path.join(FILES_PATH, "json")
    if not os.path.exists(json_path):
        os.mkdir(json_path)
    with open(os.path.join(json_path, f"{name}.json"), "w") as f:
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
