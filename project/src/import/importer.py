from . import ElementReader as Reader, BuildConfig as ConfigAPI, \
    ProjectContainer


def from_xml(xml_file, config, reader: Reader) -> ConfigAPI:
    print(f'STUBBED: import.xml(xml_file={xml_file}, config={config}, '
          f'reader={reader})')
    pass  # TODO


def from_json(json_file, config, reader: Reader) -> ConfigAPI:
    print(f'STUBBED import.json(json_file={json_file}, config={config}, '
          f'reader={reader})')
    pass  # TODO


def from_folder(folder_root, config, metadata, reader: Reader) -> ConfigAPI:
    print(f'STUBBED import.folder(folder_root={folder_root}, config={config}, '
          f'metadata={metadata}, reader={reader})')
    pass  # TODO


def from_project(project: ProjectContainer, config, metadata, reader: Reader) \
        -> ConfigAPI:
    print(f'STUBBED import.project(project={project}, config={config}, '
          f'metadata={metadata}, reader={reader})')
    pass  # TODO
