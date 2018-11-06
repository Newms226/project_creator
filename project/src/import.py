from . import BuildConfig as ConfigAPI


def from_xml(xml_file) -> ConfigAPI:
    print(f'STUBBED: import.xml(xml_file={xml_file}')
    pass  # TODO


def from_json(json_file) -> ConfigAPI:
    print(f'STUBBED import.json(json_file={json_file})')
    pass  # TODO


def from_config(config_, hierarchy, hierarchy_type=None) -> ConfigAPI:
    """Import a config.py & hierarchy as separate entities

    Args:
        config_: a python configuration file
        hierarchy: a folder/file hierarchy
        hierarchy_type: the type of the folder_hierarchy. (xml, json, etc.)
            If none, method will attempt to determine the type by itself.
    """
    print(f'STUBBED config(config={config_}, hierarchy={hierarchy} '
          f'hierarchy_type={hierarchy_type}')
    pass  # TODO
