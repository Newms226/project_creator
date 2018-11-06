from . import ProjectContainer as Project, ElementWriter as Writer


def to_folder(destination, project: Project, writer: Writer) -> bool:
    print(f'STUBBED export.folder(destination={destination}, '
          f'project={project}, writer={writer})')
    pass  # TODO


def to_xml(destination, project: Project, writer: Writer) -> bool:
    print(f'STUBBED export.xml(destination={destination}, '
          f'project={project}, writer={writer})')
    pass  # TODO


def to_json(destination, project: Project, writer: Writer) -> bool:
    print(f'STUBBED export.json(destination={destination}, '
          f'project={project}, writer={writer})')
    pass  # TODO


def to_zip(destination, project: Project, writer: Writer, encryption=False) \
        -> bool:
    print(f'STUBBED export.zip(destination={destination}, project={project}, '
          f'writer={writer}, encryption={encryption})')
    pass  # TODO


def to_internet(destination, project: Project, protocol, writer: Writer,
                encryption=False) -> bool:
    print(f'STUBBED export.internet(destination={destination}, '
          f'project={project}, protocol={protocol}, writer={writer} '
          f'encryption={encryption})')
    pass  # TODO
