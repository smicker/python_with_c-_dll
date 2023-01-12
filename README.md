# Innovation_week_2023_group_7
Elaboration of github/github actions during the analytics innovation week 2023

# Installation
```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Branch 5-build-pipeline notes:
What I'm trying to do here is to mimic a project requiring a multi-stage build.
The idea is:
- to have some code written in c/c++, requiring a make build
- to have some python code (depending on the previous one), nothing to build here, but we might want to run some linters on it
- a set of unit tests, running against the python wrappers
- a docker that we build, installing the necessary dependencies and which would contain the built code (as an export)

The idea is to try to implement through actions (with an automatic trigger in case of pull request):
- build
- syntax check
- container build
- unit testing
