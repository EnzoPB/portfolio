from django_components import component
from django.contrib.staticfiles import finders
import sys
@component.register('svg')
class Svg(component.Component):
    template_name = 'svg/svg.html'

    def get_context_data(self, src):
        src = finders.find(src)
        with open(src, 'r') as f:
            svg_content = f.read()

        return {
            'svg_content': svg_content
        }
