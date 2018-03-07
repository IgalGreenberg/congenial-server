class Server(object):
    """
    Attributes:
        name: A string
        role: A string
    """

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role
