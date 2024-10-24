import os.path

from jinja2 import Environment, select_autoescape, FileSystemLoader

from cv_generator.utils import ASSETS_PATH, OUTPUT_PATH

env = Environment(
    loader=FileSystemLoader(ASSETS_PATH), autoescape=select_autoescape(["html"])
)


def get_output_name(cv: dict) -> str:
    return f"CV-{cv['general']['fullName'].split(' ')[0]}"


def generate_html(cv: dict, full=False):
    t = env.get_template("template.html")
    output_path = f"{os.path.join(OUTPUT_PATH, get_output_name(cv))}.html"
    t.stream(**cv, fullCV=full).dump(output_path)
    print(
        f"html done! file://{os.path.join(os.path.abspath(os.getcwd()), output_path)}\n"
    )
