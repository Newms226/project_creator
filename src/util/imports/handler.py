import os
import os.path as paths
from src.logging_config import root_logger as log


def _get_resource_location() -> str:  # TODO!
    return '/Users/michael/prog/python/python3/src/resources'




def import_file(src, dest, src_type, dest_type, *options):
    def resource() -> str:
        """Extract the text from a resource"""
        log.debug(f'(src={src})')

        path_ = paths.join(_get_resource_location(), src)

        try:
            with open(path_) as f:
                to_return = f.read()
        except OSError as why:
            err = f"Failed to open '{path_}' Error_message:{why.args[0]}"
            log.error(err)
            raise OSError(err)  # TODO Error handling

        log.debug(f'RETURNED {to_return}')
        return to_return

    def variable_replace(contents:str):

