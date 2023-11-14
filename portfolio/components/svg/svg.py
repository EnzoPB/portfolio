from django.conf import settings
from django.db.models.fields.files import FieldFile
from django_components import component
from django.contrib.staticfiles import finders
import requests

# TODO: change the whole svg handling

@component.register('svg')
class Svg(component.Component):
    template_name = 'svg/svg.html'

    def get_context_data(self, src):
        svg_content = ''
        if isinstance(src, FieldFile):
            svg_content = requests.get(src.url).text
        else:
            src = finders.find(src)
            if src is not None:
                with open(src, 'r') as f:
                    svg_content = f.read()

        return {
            'svg_content': svg_content
        }
