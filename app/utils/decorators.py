class Singleton(type):
    _instances = {}

    def __call__(cls, path, env):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(path, env)
        return cls._instances[cls]
