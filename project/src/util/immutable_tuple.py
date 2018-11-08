from collections import namedtuple

ConfigTupleBase = namedtuple('ConfigTupleBase',
                             ['git', 'sync', 'folder_hierarchy', 'metadata',
                              'language', 'auto_generate', 'execution',
                              'security'])

UnitTupleBase = namedtuple('FileSystemUnitBase',
                           ['name', 'unit_type', 'git_track'])


class ImmutableConfig(ConfigTupleBase):
    """Immutable configuration file based on tuple"""

    def _replace(self, *args, **kwargs):
        raise Exception('Immutable object, cannot preform')


class ImmutableUnit(UnitTupleBase):
    """Immutable Unit attributes based on tuple"""

    def _replace(self, *args, **kwargs):
        raise Exception('Immutable object, cannot preform')
