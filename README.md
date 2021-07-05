Obsidian: A Plugin for Pelican
============================

<!-- [![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/series/build)](https://github.com/pelican-plugins/series/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-series)](https://pypi.org/project/pelican-series/)
![License](https://img.shields.io/pypi/l/pelican-series?color=blue) -->

Obsidian is a pelican plugin that allows you to use the syntax used within Obsidian and when pelican then renders these posts it won't look weird or out of place.

Phrased differently, if you don't like that `#` is included in the name of the tag when you name it `#my-tag` and you think that internal pelican links are difficult to remember and would like to use `[[ my link ]]` as an internal link instead this plugin would be for you.

If the article doesn't exist it will return text only. That way, there is a possibility of clearly separating posts that should belong on the blog and linked as such vs posts that should only belong inside Obsidian.


Installation
------------

This plugin can be installed via:

    # not yet on pypi, but when it is you can install it with.
    pip install pelican-obsidian
    
    # meanwhile you can install using this repo.
    pip install git+git://github.com/jonathan-s/pelican-obsidian@main#egg=pelican-obsidian


Usage
-----
Install the plugin as described in the pelican documentation.

In the tags section you will be able to use `#` without that being reflected in the actual name of the tag. In other words.

```
Tags: #my-tag

# reflects as
my-tag in the html output.
```

The backlinks in Obsidian follows this format `[[ document | Actual link name ]]` The actual link name is optional.

To specify the location of an attachment the following syntax is used `![[ filename.jpg ]]`. They explain more about the syntax in the section on [how to embed files](https://help.obsidian.md/How+to/Embed+files)


Future features
---------------
- Embed files or sections as described [here](https://help.obsidian.md/How+to/Format+your+notes)
- Task list?
- Support .rst?
- don't generate links for drafts
- Apply the same linking for pages.


<!-- Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/series/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html -->

License
-------

This project is licensed under the MIT license.
