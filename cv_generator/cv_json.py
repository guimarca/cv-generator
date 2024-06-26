from cv_generator.utils import create_json, protect_email


def generate_contact(cv: dict) -> dict:
    contact = cv["personal"]["public"].copy()
    contact["email"] = protect_email(contact["email"])
    return contact


def generate_description(cv: dict) -> dict:
    general = cv["general"].copy()
    general.pop("communicationSkills", None)
    desc = []
    for sentence in general["description"].strip().split("."):
        if not sentence:
            continue
        desc.append(sentence.strip() + ".")
    general.pop("description", None)
    general["text"] = desc
    return general


def generate_positions(cv: dict) -> list[dict]:
    positions = []
    for position in cv["positions"]:
        if position.get("avoidable") is True:
            continue
        pos = position.copy()
        pos["date"] = {"from": pos.pop("from", ""), "to": pos.pop("to", "")}
        pos["description"] = pos["description"].strip()
        positions.append(pos)
    return positions


def generate_json(cv: dict):
    create_json("conferences", cv["academia"]["conferences"])
    create_json("contact", generate_contact(cv))
    create_json("description", generate_description(cv))
    create_json("devProjects", cv["developmentProjects"])
    create_json("education", cv["education"])
    create_json("journalRefereeing", cv["academia"]["journalRefereeing"])
    create_json("otherPublications", cv["academia"]["otherPublications"])
    create_json("positions", generate_positions(cv))
    create_json("publications", cv["academia"]["publications"])
    create_json("teaching", cv["academia"]["teaching"])
    print("json done!\n")
