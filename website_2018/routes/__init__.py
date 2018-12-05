from typing import Iterable, Text
from pkgutil import extend_path
from website_2018.util import import_subpackages

__path__: Iterable[Text] = extend_path(__path__, __name__)
packages = import_subpackages(__name__, __path__, globals())

__all__: Iterable[Text] = [name for name, fullname, module in packages]
