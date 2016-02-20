# -*- coding: utf-8 -*-

from iprofile.settings.models.mixins import SettingsBase
from iprofile.settings.utils import GLOBAL_SETTINGS_FILE


class GlobalSettings(SettingsBase):
    base_section = 'profiles'
    default = {
        base_section: {
            'path': 'iprofiles',
            'active': None
        }
    }

    def __init__(self, *args, **kwargs):
        super(GlobalSettings, self).__init__(
            GLOBAL_SETTINGS_FILE, *args, **kwargs)


class ProfileSettings(SettingsBase):
    base_section = 'settings'
    default = {
        base_section: None
    }

    def __init__(self, path, *args, **kwargs):
        super(ProfileSettings, self).__init__(path, *args, **kwargs)
        self.read(ignore_errors=True)