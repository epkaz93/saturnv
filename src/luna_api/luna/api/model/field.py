from ..query import operators


class Field(object):

    def __init__(self):
        self._owner = None
        self._name = ''

    def __set_name__(self, owner, name):
        self._owner = owner
        self._name = name
        if not hasattr(self.owner, '__fields__'):
            self.owner.__fields__ = []
        self.owner.__fields__.append(self)

    @property
    def owner(self):
        return self._owner

    @property
    def name(self):
        return self._name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        return getattr(obj, f'_{self.name}')

    def __set__(self, obj, value):
        return setattr(obj, f'_{self.name}', value)

    #def in_(self, container):
    #    print('sup')

    def __eq__(self, other):
        return operators.EqualsOperator(self, other)

    def __ne__(self, other):
        return operators.NotEqualsOperator(self, other)

    def __lt__(self, other):
        return operators.LessThanOperator(self, other)

    def __gt__(self, other):
        return operators.GreaterThanOperator(self, other)

    def __le__(self, other):
        return operators.LessThanEqualsOperator(self, other)

    def __ge__(self, other):
        return operators.GreaterThanEqualsOperator(self, other)

    def __and__(self, other):
        return operators.AndOperator(self, other)

    def __or__(self, other):
        return operators.OrOperator(self, other)

