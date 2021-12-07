import pathlib
import subprocess
from functools import partial
from importlib import resources
from shutil import copy

import click


def rc_installer(rc_file, completion_file):
    judoka_homedir = pathlib.Path("~/.judo").expanduser()
    judoka_homedir.mkdir(exist_ok=True)

    with resources.path("judoka.completions", completion_file) as path:
        completion_target = copy(path, judoka_homedir)

    return f"echo 'source {completion_target}' >> {rc_file}"


def path_installer(install_path, completion_file):
    install_path.mkdir(exist_ok=True)

    with resources.path("judoka.completions", completion_file) as path:
        copy(path, install_path)


installers = {
    "bash": partial(
        rc_installer,
        rc_file=pathlib.Path("~/.bashrc").expanduser(),
        completion_file="judo.bash",
    ),
    "zsh": partial(
        rc_installer,
        rc_file=pathlib.Path("~/.zshrc").expanduser(),
        completion_file="judo.zsh",
    ),
    "fish": partial(
        path_installer,
        install_path=pathlib.Path("~/.config/fish/completions/").expanduser(),
        completion_file="judo.fish",
    ),
}


@click.command()
@click.argument("shell", type=click.Choice(["bash", "fish", "zsh"]))
@click.option("--apply/--no-apply", default=False)
def install(shell, apply=False):
    installer = installers.get(shell)

    if not installer:
        click.echo(f"No installer found for shell '{shell}'")
        exit(1)

    instruction = installer()
    if instruction:
        if not apply:
            click.echo("\nTo complete installation, execute the following command:\n")
            click.echo(instruction)
            click.echo("\nAlternatively, run with --force to automate installation.\n")
        else:
            subprocess.run(instruction, shell=True)
            click.echo(f"Shell completion was installed for you via: \n{instruction}")
    else:
        click.echo("Shell completion was installed")


if __name__ == "__main__":
    install()
