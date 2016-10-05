import re
import sys


COMPONENT_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

component = '{{ cookiecutter.component }}'

if not re.match(COMPONENT_REGEX, component):
    print('ERROR: %s is not a valid Python module name!' % component)

    # exits with status 1 to indicate failure
    sys.exit(1)
