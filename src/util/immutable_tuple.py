from collections import namedtuple

ConfigTupleBase = namedtuple('ConfigTupleBase',
                             ['git', 'sync', 'folder_hierarchy', 'metadata',
                              'auto_generate', 'execution', 'security'])

UnitTupleBase = namedtuple('UnitTupleBase',
                           ['name', 'element_type', 'meta', 'sync'])


class ImmutableConfig(ConfigTupleBase):
    """Immutable configuration file based on tuple"""

    def _replace(self, *args, **kwargs):
        raise Exception('Immutable object, cannot preform')


class ImmutableUnit(UnitTupleBase):
    """Immutable Unit attributes based on tuple"""

    def _replace(self, *args, **kwargs):
        raise Exception('Immutable object, cannot preform')
