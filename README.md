# Judoka

[![PyPI](https://img.shields.io/pypi/v/judoka.svg)](https://pypi.org/project/judoka/)
[![Changelog](https://img.shields.io/github/v/release/eelkevdbos/judoka?include_prereleases&label=changelog)](https://github.com/eelkevdbos/judoka/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/eelkevdbos/judoka/blob/main/LICENSE)

Judoka is a command line utility that lets you define project scoped commands and call them through their alias. It lets you just do (= judo) your work.

## Installation

Install this library using `pip`:

    $ pip install judoka

## Usage

Create a `.judorc` file in your project root, like the example below:

```toml
greet = "cowsay 'Hi!'"

[frontend]
start = "npm run start"

[backend]
start = "docker compose up -d"
```

Then, just run any of the aliases:

```shell
$ judo greet
$ judo frontend:start
$ judo backend:start
```

Or, have a list of all the available commands in your project:

```shell
$ judo
```

You may also choose to include a `.judorc` file in your `$HOME` folder (`~/.judorc`). Commands defined in this file will always be loaded first and will be overwritten if an overlapping command was found.

## Shell completions

To install judo shell completions, execute `judo-completions [--apply] {bash|fish|zsh}` to get instructions on how to install completions for your shell of choice. By including the `--apply` option, the installation instructions will be applied for you. 

**Note:** Don't forget to reload your shell session after installation to load the completions.

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd judoka
    python -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
