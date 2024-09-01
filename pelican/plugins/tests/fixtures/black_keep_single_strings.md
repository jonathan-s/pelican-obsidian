---
Category: note
Date: '2022-05-12'
Modified: '2023-07-12'
Slug: black-keep-single-quotes-strings
Status: published
Tags: black, single-string, quotation-mark
Title: Black - Keep Single Quotes for Strings
---

See: [Add --single-quote option · Issue #594 · psf/black · GitHub](https://github.com/psf/black/issues/594)

Currently, it requires everyone who uses single quotes to run black and then have a second tool (we use pre-commit double-quote-string-fixer) to ensure that single quotes are being used consistently.

From black documentation:
> If you are adopting *Black* in a large project with pre-existing string conventions (like the popular [“single quotes for data, double quotes for human-readable strings”](https://stackoverflow.com/a/56190)), you can pass `--skip-string-normalization` on the command line. This is meant as an adoption helper, avoid using this for new projects.

up::[[MOC_Software_Development]]