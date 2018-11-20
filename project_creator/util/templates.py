from string import Template
from ast import literal_eval
from project_creator.logging_config import root_logger as log


def parse_template(template_path, string_args: str,
                   delimiters=(', ', '=')) -> str:

    def _parse_string_args() -> dict:
        d = {}
        for pair in string_args.split(delimiters[0]):
            log.debug(f'found {pair}')

            k, v = pair.split(delimiters[1])
            log.debug(f'turned {pair} into k={k} & v={v}')

            d[k] = literal_eval(v)
            log.debug(f'current dictionary={d}')

        log.debug(f'RETURNED {d}')
        return d

    log.debug(f'(template_path={template_path}, string_args={string_args}, '
              f'delimiters={delimiters})')

    with open(template_path) as f:
        template = Template(f.read())
        log.debug(f'Parsed template as {template.template}')

    to_return = template.safe_substitute(_parse_string_args())
    log.debug(f'RETURNED {to_return}')

    return to_return
