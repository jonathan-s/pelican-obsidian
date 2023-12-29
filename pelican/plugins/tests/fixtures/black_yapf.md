---
Category: note
Date: '2023-02-23'
Modified: '2023-07-12'
Slug: black-vs-yapf
Status: published
Summary: The debate over the best Python code formatter continues. In this article, we dive deep into Black and yapf - their strong and weak points, and which one is right for you.
Tags: python, code-formatter, black, yapf, comparison, strong-points, weak-points, differences, usability, CICD, pipelines, automation, pre-commit-hooks, controversies
Title: Which Python Code Formatter Is Better - Black or Yapf?
---
X::[[black_formatter]]
X::[[black_keep_single_strings]]
X::[[change_black_line_length]]
X::[[black_formatter_avoid_destroying_git_blame]]
X::[[black]]
X::[[yapf]]


## Introduction

Python code formatters are tools used to format Python code according to a set of rules or conventions. These tools help to maintain consistent code formatting, improve code readability, and reduce the time spent on code review. Several code formatters are available in the Python community, and two of the most popular ones are Black and yapf. In this blog post, we will compare Black and yapf, highlighting their strong and weak points, differences, and evaluating their usability in CI/CD pipelines and other automation tools like pre-commit hooks. We will also address some controversies surrounding these tools.

## Overview of Black and yapf

[Black](https://github.com/psf/black) and [yapf](https://github.com/google/yapf) are open-source tools for code formatting in Python. Black was first released in 2018 and has gained popularity in the Python community since then. Black is designed to be opinionated, meaning that it enforces a strict set of rules for code formatting. On the other hand, yapf was first released in 2015 and is also popular among Python developers. Yapf is configurable, meaning that it allows users to customize the formatting rules to suit their preferences.

## Comparison of Black and yapf

This section will compare Black and yapf based on various criteria.

### 1.  Formatting rules

Black enforces a strict set of formatting rules that are non-configurable. The aim of these rules is to provide consistent code formatting and reduce the time spent on code review. Black aims to minimize the differences in formatting style among developers, which can cause confusion when working on large projects. Yapf, on the other hand, allows users to customize the formatting rules according to their preferences. Yapf provides a set of default rules, but users can modify them by specifying options in the configuration file.

### 2.  Speed

Black is known for its speed and can format code in a matter of seconds. Black achieves this speed by using a simple algorithm that focuses on making the smallest possible changes to the code. Yapf, on the other hand, is slower than Black but still relatively fast. Yapf's algorithm is more complex and focuses on making more significant changes to the code.

### 3.  Output readability

Both Black and yapf produce readable code output that is easy to understand. However, Black's output may sometimes be harder to read due to the strict formatting rules. Yapf's output, on the other hand, may be more readable due to the ability to customize the formatting rules.

### 4.  Integration with CI/CD pipelines and pre-commit hooks

Both Black and yapf can be integrated into CI/CD pipelines and pre-commit hooks. Black has an official pre-commit hook that can be easily installed and used. Yapf also has a pre-commit hook, but it is not officially supported by the yapf team. Both tools can also be integrated with CI/CD pipelines using various plugins.

### 5.  Community support

Both Black and yapf have active communities that contribute to their development and maintenance. However, Black has a larger community and is more widely used than yapf.

| Criteria                            | Black                           | yapf                                  |
|-------------------------------------|---------------------------------|---------------------------------------|
| Formatting rules                    | Enforces strict non-configurable rules| Allows customization of rules         |
| Speed                               | Fast                            | Slower than Black                      |
| Output readability                  | Sometimes harder to read due   | More readable due to customization    |
|                                     | to strict rules                 | of formatting rules                    |
| Integration with CI/CD pipelines    | Official pre-commit hook        | Pre-commit hook not officially         |
| and pre-commit hooks                | available                       | supported by yapf team                 |
| Community support                   | Active community                | Active community                       |
|                                     |                                 |                                       |

### 6.  Controversies

There have been some controversies surrounding Black and yapf. One of the main controversies surrounding Black is its strict formatting rules, which some developers find too restrictive. Some developers feel that Black's strict formatting rules can lead to unreadable code and may not be suitable for all projects. On the other hand, yapf's configurable formatting rules have also received criticism. Some developers feel that yapf's configurable formatting rules can lead to inconsistent code formatting, which can be confusing when working on large projects.

## References
- Black: [https://github.com/psf/black](https://github.com/psf/black)
- yapf: [https://github.com/google/yapf](https://github.com/google/yapf)