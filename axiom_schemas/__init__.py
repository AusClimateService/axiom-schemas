"""Entrypoint for the schemas package."""
import os
import sys
import glob
import pkgutil as pu
import json
from importlib.metadata import version

# Version handle
__version__ = version('axiom_schemas')


def load_schema(filename):
    """Load the schema.

    Args:
        filename (str): Internal path to the schema.
    
    Returns:
        dict : Schema dictionary.
    """
    return json.loads(pu.get_data('axiom_schemas', f'schemas/{filename}').decode('utf-8'))


def list_schemas():
    """List the available schemas.

    Returns:
        list : List of schema files available for loading.
    """
    # Get the path to the installed directory
    d = os.path.dirname(sys.modules['axiom_schemas'].__file__)

    # List everything in the schemas folder
    schemas = sorted(glob.glob(os.path.join(d, 'schemas/*.json')))

    # Just return the basenames
    return [os.path.basename(s) for s in schemas]