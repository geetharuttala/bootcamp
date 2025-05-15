import warnings

def use_deprecated():
    warnings.warn("This function is deprecated", DeprecationWarning)

use_deprecated()
