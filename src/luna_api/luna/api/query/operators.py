from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from ..model.field import Field


class OperatorMeta(type):

    operators = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        mcs.operators[cls.symbol] = cls
        return cls

    @classmethod
    def create_operator(mcs, symbol, a, b):
        cls = mcs.operators[symbol]
        return cls(a, b)


class OperatorComparisonBase(object):

    symbol = None
    name = None

    def __and__(self, other: OperatorComparisonBase):
        return AndOperator(self, other)

    def __or__(self, other: OperatorComparisonBase):
        return OrOperator(self, other)


class ComparisonBase(OperatorComparisonBase):

    def __init__(self, a: typing.Union[OperatorComparisonBase, bool], b: typing.Union[OperatorComparisonBase, bool]):
        self.a = a
        self.b = b
    """
    def __repr__(self) -> typing.AnyStr:
        if isinstance(self.a, Field):
            a_str = f'{self.a.owner.__name__}.{self.a.name}'
        else:
            a_str = self.a
        if isinstance(self.b, Field):
            b_str = f'{self.b.owner.__name__}.{self.b.name}'
        else:
            b_str = self.b
        return f'{self.__class__.__name__}: {a_str} {self.symbol} {b_str}'
    """

class OperatorBase(OperatorComparisonBase):

    def __init__(self, field: typing.Union[Field, OperatorComparisonBase], other: typing.Any):
        self.field = field
        self.other = other

    def __repr__(self) -> typing.AnyStr:
        return f'{self.__class__.__name__}: {self.field.owner.__name__}.{self.field.name} {self.symbol} {self.other}'

    def process(self, obj):
        value = getattr(obj, self.field.name)
        return self._raw_process(value, self.other)

    def _raw_process(self, value, other):
        """"""


class EqualsOperator(OperatorBase, metaclass=OperatorMeta):

    symbol = '=='
    name = 'equals'

    def _raw_process(self, value, other):
        return value == other


class NotEqualsOperator(OperatorBase, metaclass=OperatorMeta):

    symbol = '!='
    name = 'notequals'

    def _raw_process(self, value, other):
        return value != other


class AndOperator(ComparisonBase, metaclass=OperatorMeta):

    symbol = '&'
    name = 'and'


class OrOperator(ComparisonBase, metaclass=OperatorMeta):

    symbol = '|'
    name = 'or'


class GreaterThanOperator(OperatorBase, metaclass=OperatorMeta):

    symbol = '>'
    name = 'greaterthan'


class LessThanOperator(OperatorBase, metaclass=OperatorMeta):

    symbol = '<'
    name = 'lessthan'


class GreaterThanEqualsOperator(OperatorBase, metaclass=OperatorMeta):

    symbol = '>='
    name = 'greaterthanequals'


class LessThanEqualsOperator(OperatorBase, metaclass=OperatorMeta):

    symbol = '<='
    name = 'lessthanequals'
