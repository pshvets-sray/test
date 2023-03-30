# Data Technology Python Template

This is a cookiecutter template for bootstrapping a Python service within the [Arabeqsue organisation](https://github.com/arabesque-sray).

## Usage

Install cookiecutter:

```bash
python -m pip install cookiecutter
```

Run cookiecutter with this template:
```bash
python -m cookiecutter git@github.com:arabesque-sray/data-technology-python-template.git
```

Follow the prompts until the repo is created, see [cookiecutter.json](./cookiecutter.json) for the full list of arguments.

## Initialise

Create the repository under the [Arabesque organisation](https://github.com/arabesque-sray), and then initialise your new repo:

```bash
cd <repo-name>
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:arabesque-sray/<repo-name>.git
git push -u origin master
```

Once the repo is set-up, follow the [CI/CD User Guide](https://github.com/arabesque-sray/ops/blob/main/docs/cicd/user-guide.md#quickstart) to link the newly created repo into the existing CI/CD infrastructure.
