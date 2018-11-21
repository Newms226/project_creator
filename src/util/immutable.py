
def read_only_properties(*attrs):

    def class_rebuilder(cls):
        """The class decorator"""

        class NewClass(cls):
            """This is the overwritten class"""
            def __setattr__(self, name, value):
                if name not in attrs:
                    pass
                elif name not in self.__dict__:
                    pass
                else:
                    raise AttributeError("Can't modify {}".format(name))

                super().__setattr__(name, value)

            def __delattr__(self, name):
                if name not in attrs:
                    pass
                elif name not in self.__dict__:
                    pass
                else:
                    raise AttributeError("Can't modify {}".format(name))

                super().__delattr__(name)

        return NewClass

    return class_rebuilder
