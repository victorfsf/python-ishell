# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.cli import Save
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.core.utils import get_active_profile
from iprofile.core.utils import get_ipython_path
from iprofile.core.utils import get_profile_path
import click
import IPython
import os
import sys


@icommand(help=texts.HELP_SHELL, short_help=texts.HELP_SHELL)
@click.argument('name', required=False)
@click.argument('ipython_options', nargs=-1, required=False)
@click.option('--django', required=False, help=texts.HELP_DJANGO)
class Shell(ICommand):

    def run(self, **options):
        name = self.slugify_name(options) or get_active_profile()
        ipython_options = list(options.get('ipython_options', []))
        django_settings = options.get('django')

        if django_settings:
            import django
            os.environ.setdefault(
                'DJANGO_SETTINGS_MODULE',
                '{0}.settings'.format(django_settings)
            )
            sys.path.append('../{0}'.format(django_settings))
            django.setup()

        if not name:
            IPython.start_ipython(argv=ipython_options)
            return

        ipython_path, _, _ = get_ipython_path(name)
        profile_path = get_profile_path(name)

        if profile_path and not os.path.isdir(profile_path):
            self.red(texts.ERROR_PROFILE_DOESNT_EXIST_RUN.format(name))
            return

        if not ipython_path:
            Save.run(options)
            click.echo()
        IPython.start_ipython(
            argv=ipython_options + ['--profile-dir', ipython_path]
        )
