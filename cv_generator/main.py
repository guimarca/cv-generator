import argparse
import glob
import os.path

import yaml

from cv_generator.cv_html import generate_html
from cv_generator.cv_json import generate_json
from cv_generator.utils import SOURCE_DATA_PATH


def main(
    format_json: bool, format_html: bool, full: bool, cv_file_name: str | None = None, lang: str = 'en'
):
    if not cv_file_name:
        cv_filenames = glob.glob(f"{os.path.join(SOURCE_DATA_PATH, "*.y*ml")}")
    else:
        cv_filenames = [os.path.join(SOURCE_DATA_PATH, cv_file_name)]

    for filename in cv_filenames:
        print(f"-> Processing source file: {filename} ...\n")
        with open(filename) as f:
            cv = yaml.load(f, Loader=yaml.FullLoader)

        if format_json:
            print("Generating json ...")
            generate_json(cv)

        if format_html:
            print(f"Generating html ({full=}) ...")
            generate_html(cv, full, lang)

    print("Finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate CV or CV data in different formats"
    )
    parser.add_argument(
        "--json", action="store_const", const=True, help="Build json data assets for web"
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
        help=f"Single CV yaml file name (should exist in {SOURCE_DATA_PATH} folder)",
    )
    parser.add_argument('--lang', type=str, default='en', help="Language for the CV template")
    args = parser.parse_args()
    main(args.json, args.html, args.full, args.filename, args.lang)
