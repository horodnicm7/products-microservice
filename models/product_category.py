from enum import Enum


class ProductCategory(str, Enum):
    electronics = 'electronics'
    fashion = 'fashion'
    none = '*'
