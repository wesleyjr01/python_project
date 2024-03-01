from .aux import aux_function
from ..bi.main import bi_function


def composite_function():
    return aux_function() + bi_function()
