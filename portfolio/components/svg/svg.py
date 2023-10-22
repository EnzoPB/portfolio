from django.conf import settings
from django.db.models.fields.files import FieldFile
from django_components import component
from django.contrib.staticfiles import finders
import os
@component.register('svg')
class Svg(component.Component):
    template_name = 'svg/svg.html'

    def get_context_data(self, src):
        if isinstance(src, FieldFile):
            src = src.path
        else:
            src = finders.find(src)

        if src is not None:
            with open(src, 'r') as f:
                svg_content = f.read()
        else:
            svg_content = ''

        return {
            'svg_content': svg_content
        }
