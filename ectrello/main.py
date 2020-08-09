
import click
import os


plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

help = """
The  ectrello Command Line Interface is a unified tool to manage your trello.\n
To see help text, you can run:

  ectrello --help\n
  ectrello <command> --help\n
  ectrello <command> <subcommand> help\n
"""

cli = MyCLI(help=help)

if __name__ == '__main__':
    cli()
