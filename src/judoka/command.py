from functools import reduce
import operator
import subprocess
import typing as t

from click import (
    argument,
    command,
    Command,
    Context,
    MultiCommand,
)


class Hub(MultiCommand):
    _config: t.Optional[dict]
    _configresolver: t.Optional[t.Callable[[], dict]]

    def __init__(
        self,
        *args,
        config: t.Optional[t.Mapping] = None,
        configresolver: t.Optional[t.Callable[[], t.Mapping]] = None,
        **kwargs,
    ):
        self._config = config
        self._configresolver = configresolver
        super().__init__(*args, **kwargs)

    @property
    def config(self):
        if not self._config and self._configresolver:
            self._config = self._configresolver()

        return self._config

    def list_commands(self, ctx: Context) -> t.List[str]:
        commands = []

        for key, value in self.config.items():
            if type(value) is str:
                # if value is str, consider the key the name of the command
                commands.append(key)
            elif type(value) is dict:
                # if the value is a dict, consider the key a namespace
                # all keys within the dict are the names of the commands
                for name in value.keys():
                    commands.append(f"{key}:{name}")

        commands.sort()

        return commands

    def get_command(self, ctx: Context, cmd_name: str) -> t.Optional[Command]:
        if cmd_name not in self.list_commands(ctx):
            return None

        args = self.get_command_args(cmd_name)
        if type(args) == list:
            args = " ".join(args)

        @command(name=cmd_name)
        @argument("shell_args", nargs=-1)
        def _command(shell_args):
            process = subprocess.Popen(
                args + " " + " ".join(shell_args),
                shell=True,
            )
            process.wait()
            process.kill()

        return _command

    def get_command_args(self, cmd_name):
        try:
            args = reduce(
                operator.getitem,
                cmd_name.split(":"),
                self.config,
            )
        except KeyError:
            args = []
        return args
