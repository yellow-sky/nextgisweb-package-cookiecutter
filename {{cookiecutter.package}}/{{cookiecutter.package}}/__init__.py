{% set amd_pkg = cookiecutter.amd_package -%}
{% set component_class = '%sComponent' % cookiecutter.component.title().replace('_', '') -%}

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from nextgisweb.component import Component, require

from .model import Base
from .util import COMP_ID


class {{ component_class }}(Component):
    identity = COMP_ID
    metadata = Base.metadata

    def initialize(self):
        pass
    
    @require('resource')
    def setup_pyramid(self, config):
        from . import view, api
        view.setup_pyramid(self, config)
        api.setup_pyramid(self, config)
        
    settings_info = (
        #dict(key='any_key', desc=u"Any key description"),
    )

    
def pkginfo():
    return dict(components=dict(
        {{ cookiecutter.component }}='{{ cookiecutter.package }}'))


def amd_packages():
    return (
        ('{{ amd_pkg }}', '{{ cookiecutter.package }}:amd/{{ amd_pkg }}'),
    )
