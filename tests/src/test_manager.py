from src.manager import Generator


def test_generator():
    test = Generator('/Users/michael/prog/python/python3/project_creator/design/examples/hierarchy_config.xml')
    test.generate()