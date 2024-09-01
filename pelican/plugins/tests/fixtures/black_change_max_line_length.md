---
Category: note
Date: '2023-02-18'
Modified: '2023-07-12'
Slug: black-change-max-line-length
Status: published
Tags: black-formatter, code-formatting, maximum-line-length, code-quality, software-development, python, configuration-file, pyproject-toml, code-consistency, readability
Title: Black - Change Max Line Length
---
X::[[change_black_line_length]]

If you are a software developer or a code reviewer, you know how important it is to keep your code clean and consistent. One way to achieve this is by using a code formatter like Black. Black is a popular code formatter that automatically formats your code to a certain standard. One of the key features of Black is the ability to set the maximum line length. In this blog post, we will go over the steps you can take to change the maximum line length for Black.

## Why Change the Maximum Line Length?

The maximum line length is the number of characters that a line of code can have before it is considered too long. In most cases, lines of code that are too long can be difficult to read and can lead to errors. By setting the maximum line length, you can ensure that all lines of code in your project follow a consistent standard, making it easier for developers to read and review your code.

## How to Change the Maximum Line Length for Black?

The process of changing the maximum line length for Black is relatively easy. Here are the steps you can take:

### Step 1: Install Black

If you have not installed Black yet, you will need to install it first. You can install Black using pip, the Python package manager. To install Black, run the following command:

```sh
pip install black
```

### Step 2: Create a Configuration File

Once you have installed Black, you need to create a configuration file that specifies the maximum line length you want to use. You can create a configuration file by creating a file called pyproject.toml in the root directory of your project. The contents of the file should look like this:

```toml
[tool.black] line-length = 88
```
In the example above, we have set the maximum line length to 88 characters. You can set the maximum line length to any value you prefer.

### Step 3: Run Black

Now that you have created a configuration file, you can run Black to format your code. To run Black, you can use the following command:

```sh
black .
```

The command above will format all Python files in the current directory using the configuration specified in the pyproject.toml file.

Setting the maximum line length for Black is an important step in maintaining consistent and readable code. By following the steps outlined in this blog post, you can easily change the maximum line length for Black and ensure that your code is easy to read and review. Remember to choose a maximum line length that works for your project and be consistent in your coding style. Happy coding!

## The debate over the maximum line length
The concept of maximum line length is something that has been ingrained in the world of programming for a long time. In particular, the concept of a "maximum line length" has been used to set a hard limit on the number of characters that can be used in a single line of code. This concept has been widely adopted by various programming languages and tools, including Black - a popular code formatting tool for Python.

Black is an opinionated code formatter that automatically formats your code to adhere to a set of predefined rules. One of these rules is the maximum line length, which is set by default to 88 characters. This means that any line of code that exceeds 88 characters will be automatically reformatted by Black to fit within this limit. While this may seem like a relatively minor aspect of coding, it is a topic that has generated a lot of debate among developers.

The idea behind setting a maximum line length is to improve the readability of the code. The longer a line of code is, the harder it is to read and understand. This is especially true for code that is being viewed on a small screen, such as a laptop or a mobile phone. By limiting the number of characters per line, it is easier to see the entire line of code without having to scroll horizontally, which can be a major annoyance for developers.

The default line length of 88 characters in Black has generated a lot of controversy, with many developers arguing that it is too short. In fact, some developers have gone so far as to create forks of Black that allow for longer line lengths. There are a number of arguments in favor of increasing the maximum line length, including the fact that modern screens are larger and can display more characters, and that longer lines can help to reduce the number of lines of code required to perform a given task.

However, there are also a number of arguments in favor of keeping the line length limit at 88 characters. One of the main arguments is that longer lines can make it more difficult to understand the code. It can also lead to code that is difficult to maintain and modify in the future, as it becomes harder to track down errors or make changes to the code.

Ultimately, the decision of whether to increase the maximum line length in Black or any other code formatting tool is up to the individual developer or team. It is important to consider the specific needs of the project, as well as the preferences of the development team. If the code is being developed for a platform with a large screen or if the development team has a preference for longer lines, then increasing the maximum line length may be a good idea. However, if readability and maintainability are the top priorities, then keeping the line length limit at 88 characters may be the best approach.

To summarise: the debate over the maximum line length in code formatting tools like Black is not likely to be resolved anytime soon. There are valid arguments on both sides, and the decision ultimately depends on the specific needs of the project and the preferences of the development team. Regardless of which approach is taken, it is important to maintain consistency throughout the codebase to ensure readability and maintainability.