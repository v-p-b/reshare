# REshare Python

This is the Python wrapper for the [REshare](https://github.com/v-p-b/reshare) reverse-engineering exchange format. 

## Installation

The package is available on PyPI:

```
pip install reshare==0.1.1
```

## Usage

```python
from reshare import *
from reshare.helpers import *

resh_export = ResharePy("my_project") # Convenience wrapper

# ... add RE knownledge to the export object ...

with open("reshare.json", "w") as out:
    out.write(json.dumps(resh_export.to_json_data(), indent=2))

# Time flies...

with open("reshare.json","r") as inp:
    data = json.load(inp)
    resh_import = Reshare.from_json_data(data)
    # ... parse RE data for your tool ...
```

### Helpers

While Python is a common denominator among reversing tools, the generated REshare classes aren't comfortable to work with:

* Reasonable defaults are not available
* Variant metadata is exposed

Wrapper classes with `...Py` suffix are provided that:

* Implement constructors with reasonable default values
* Hide variant internals
* Handle dynamically typed attribute assignment (in case of `ReshTypeSpec` for now)

