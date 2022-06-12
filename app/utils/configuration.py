from app.utils.decorators import Singleton


class Configuration(object, metaclass=Singleton):
    def __init__(self, path='/code/app', env='dev'):
        with open('{path}/config-{env}.env'.format(path=path, env=env), 'r') as file:
            for line in file.readlines():
                entry = line.strip()

                if entry.startswith('#'):
                    continue

                first_equal_pos = entry.find('=')
                key = entry[: first_equal_pos].strip()
                value = entry[first_equal_pos + 1:].strip()

                self.__setattr__(key, value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)


# c = Configuration('../', 'dev')
# c1 = Configuration('../', 'dev')
# print(c)
# print(c1)
# print(c.DATABASE_USER)
# print(c1.DATABASE_USER)
