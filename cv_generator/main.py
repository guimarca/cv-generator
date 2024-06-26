import argparse
import os.path

import yaml

from cv_generator.cv_html import generate_html
from cv_generator.cv_json import generate_json
from cv_generator.utils import SOURCE_DATA_PATH


def main(
    format_json: bool, format_html: bool, full: bool, cv_file_name: str = "cv.yml"
):
    with open(f"{os.path.join(SOURCE_DATA_PATH, cv_file_name)}") as f:
        cv = yaml.load(f, Loader=yaml.FullLoader)

    if format_json:
        print("Generating json ...")
        generate_json(cv)

    if format_html:
        print(f"Generating html (full={full}) ...")
        generate_html(cv, full)

    print("Finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate CV or CV data in different formats"
    )
    parser.add_argument(
        "--json", action="store_const", const=True, help="Build json data files for web"
    )
    parser.add_argument("--html", action="store_const", const=True, help="Build html")
    parser.add_argument(
        "--full",
        action="store_const",
        const=True,
        default=False,
        help="Add all sections",
    )
    parser.add_argument(
        "--filename",
        default="cv.yml",
        help=f"CV yaml file name (should be in {SOURCE_DATA_PATH} folder)",
    )
    args = parser.parse_args()
    main(args.json, args.html, args.full, args.filename)
