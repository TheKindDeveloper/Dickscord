__title__ = "Dickscord"
__author__ = "KADIUM"
__license__ = "MIT"
__copyright__ = "Copyright 2023 KADIUM"

from .imports import *
from .Style import *
from .autocord import Dickcord
from .dickpc import pc
from .extra import Dickcord_extension
from .update import *

if __title__ == "Dickscord":
    update.__update__()
