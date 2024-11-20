import os.path
import yaml

from jinja2 import Environment, select_autoescape, FileSystemLoader

from cv_generator.utils import ASSETS_PATH, OUTPUT_PATH

env = Environment(
    loader=FileSystemLoader(ASSETS_PATH), autoescape=select_autoescape(["html"])
)


def get_output_name(cv: dict) -> str:
    return f"CV-{cv['general']['fullName'].split(' ')[0]}"

def load_language_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def load_translations(language):
    try:
        return load_language_file(os.path.join(f'{ASSETS_PATH}/languages', f'{language}.yml'))
    except FileNotFoundError:
        print(f"Language file not found: {language}.yml, using default language: en")
        return load_language_file(os.path.join(f'{ASSETS_PATH}/languages', 'en.yml'))


def generate_html(cv: dict, full=False, lang='en'):
    translations = load_translations(lang)
    t = env.get_template("template.html")
    output_path = f"{os.path.join(OUTPUT_PATH, get_output_name(cv))}.html"
    t.stream(**cv, fullCV=full, translations=translations).dump(output_path)
    print(
        f"html done! file://{os.path.join(os.path.abspath(os.getcwd()), output_path)}\n"
    )
