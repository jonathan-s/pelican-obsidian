---
Category: note
Date: '2021-11-29'
Modified: 2023-08-12
Slug: black-code-formatter
Status: published
Summary: notes on using black formatter
Tags: black, python, pyqa, quality
Title: Black - The Code Formatter
citation_needed: false
---
![black logo](https://black.readthedocs.io/en/stable/_static/logo2-readme.png)
Black is a non-configurable code formatter.

## Install Black for Jupyter notebook
```sh
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
jupyter nbextension enable jupyter-black-master/jupyter-black
```

## Change the line length character limit in Black
To change the character limit for the Black Python formatter, you can add the following section to [pyproject.toml](https://www.python.org/dev/peps/pep-0518/) file:
```ini
[tool.black]
line-length = 119
```

- PEP8 recommends a line length of [79 characters](https://www.python.org/dev/peps/pep-0008/#maximum-line-length) (72 for docstrings)
- Black sets line lengths to [88 characters by default](https://black.readthedocs.io/en/stable/the_black_code_style.html?highlight=length#line-length)
- The Django docs recommend a maximum line length of [119 characters](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/) (79 for docstrings)

For info on how to configure black with vscode? See [[change_black_line_length|here]].

## Usages of black
- with tox
- in pre-commit hooks
- as an external tool in PyCharm

up::[[MOC_Python]]
X::[[black_keep_single_strings]]
X::[[black_change_max_line_length]]
X::[[black_formatter_avoid_destroying_git_blame]]
