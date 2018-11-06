from . import ElementReader as Reader, BuildConfig as ConfigAPI, \
    ProjectContainer, ParseConfig


def _read_parsing_config(file) -> dict:
    print(f' _read_parsing_config(file={file}) -> HARDWIRED VALUES')
    return {
        file_type: 'file',
        folder_type: 'folder',
        import_type: 'import',
        git_attr: 'git',
        file_text: 'text',
        file_header: 'header',
        system_attr: 'system_attr',
        import_path: 'path',
        import_strategy: 'import_strategy'
    }


def from_xml(xml_file, config, parsing_config) -> ConfigAPI:
    print(f'STUBBED: import.xml(xml_file={xml_file}, config={config}, '
          f'parsing_config={parsing_config})')
    parsing_dict = _read_parsing_config(parsing_config)
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

