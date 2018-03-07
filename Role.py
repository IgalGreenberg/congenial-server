class Role(object):
    """
    Attributes:
        name: A string
        Commands: A list
        iptables: A list
    """
    def __init__(self, name, commands, iptables):
        self.name = name
        self.commands = commands
        self.iptables = iptables

    def get_name(self):
        return self.name

    def get_commands(self):
        return self.commands

    def get_iptables(self):
        return self.iptables