# CV generation tool

Source data yml files should go inside `source_data`.

Outputs will be generated in the `output` folder: 

- `CV-[Name].html`
- `json`folder

**Tip**: To save the html CV as a pdf, print it with Chrome unchecking header and footer. 

## Setup:

You need python and [poetry](https://python-poetry.org/docs/#installation).

After cloning the repo, cd into the project's folder and run:

`poetry install`

## Usage:

Options: 

- `--html`: Generate the CV in html format sung [the template](cv_generator/assets/template.html)
- `--json`: Generate json files with the CV data
- `--full`: Include optional stuff (i.e.: driving licence). Corresponds to `fullCV` in html template
- `--filename`: Name of the yaml file under source_data you want to process (leave it blank to process all)

Examples:

```bash
cd cv_generator
poetry run python main.py --html --json [--full] [--filename cv-x.yml]
```

Build the example cv provided (cv-example.yaml):

```bash
cd cv_generator
poetry run python main.py --html --full --filename cv-example.yml
```

(Check out [`cv_generator/output/CV-John.html`](cv_generator/output/CV-John.html))
