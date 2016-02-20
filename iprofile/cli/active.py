# -*- coding: utf-8 -*-

from iprofile import texts
from iprofile.core.decorators import icommand
from iprofile.core.models import ICommand
from iprofile.profiles.models import Profile
from slugify import slugify
import click


@icommand(help=texts.HELP_ACTIVE, short_help=texts.HELP_ACTIVE)
class Active(ICommand):

    def run(self, **options):
        name = self.settings.get('active')
        if not name or not slugify(name):
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
            return

        profile = Profile(name)
        if not profile.exists():
            self.red(texts.ERROR_NO_ACTIVE_PROFILE)
            return

        click.echo(texts.LOG_ACTIVE_PROFILE, nl=False)
        self.pgreen(profile.name)
