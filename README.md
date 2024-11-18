# CV Generation Tool

Source data YAML files should go inside the `source_data` folder.

Outputs will be generated in the `output` folder:

- `CV-[Name].html`
- `json` folder

> [!TIP]
> To save the HTML CV as a PDF, print it using Chrome and uncheck the header and footer options.

## Setup

> [!IMPORTANT]
> You need Python and [Poetry](https://python-poetry.org/docs/#installation).

After cloning the repository, navigate to the project's folder and run:

```bash
poetry install
```

## Usage

### Options:

- `--html`: Generate the CV in HTML format using [the template](cv_generator/assets/template.html).
- `--json`: Generate JSON files with the CV data.
- `--full`: Include optional details (e.g., driving license). Corresponds to `fullCV` in the HTML template.
- `--filename`: Specify the name of the YAML file under `source_data` you want to process (leave blank to process all).
- `--lang`: Specifies the language for the generated template (default is English)

### Examples:

Generate the CV with HTML and JSON outputs:

```bash
cd cv_generator
poetry run python main.py --html --json [--full] [--filename cv-x.yml]
```

Build the example CV provided (`cv-example.yml`):

```bash
cd cv_generator
poetry run python main.py --html --full --filename cv-example.yml
```

Check the generated file: [`cv_generator/output/CV-John.html`](cv_generator/output/CV-John.html)
