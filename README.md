# Axiom Schemas

This package is to be installed alongside Axiom to manage schemas. This allows schemas to change without triggering a new version of the base Axiom package.

## Installation

```shell
# Install the master branch (you will need to be a member of this repo)
pip install git+https://github.com/climate-resilient-enterprise/axiom-schemas.git
```

## Usage

Axiom Schemas is used internally by Axiom, however, if you need to access the schemas within elsewhere, it can be done using the following snippets.

```python
import axiom_schemas as axs

# List all available schemas
schemas = axs.list_schemas() # Returns a list of schema filenames

# Load the mrd-0.1.0 schema file for use in your own code
schema = axs.load_schema(schema='mrd-0.1.0.json')
```