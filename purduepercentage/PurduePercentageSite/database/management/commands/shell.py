from django.core.management.commands.shell import Command as ShellCommand
import os


class Command(ShellCommand):
    shells = ShellCommand.shells.append('ptpython')

    def ptpython(self, _):
        try:
            # old ptpython
            from prompt_toolkit.contrib.repl import embed
        except ImportError:
            # new ptpython
            from ptpython.repl import embed

        history_filename = os.path.expanduser('~/.ptpython_history')
        embed(globals(), locals(), vi_mode=False)
