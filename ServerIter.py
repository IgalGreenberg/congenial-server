from Server import Server
from Role import Role

Roles = {} # empty dictionary
Servers = {} # empty dictionary


a = Role("db",[], [])

Roles["db"] = Role("db",
              ["install mysql", "install mysql_client"],
              ["configure iptable"])
Roles["web"] = Role("web",
              ["install apache", "install php"],
              ["configure iptable", "configure iptables"])

Servers["Server1"] = Server("Server1", "db")
Servers["server2"] = Server("Server2", "web")
Servers["server3"] = Server("Server3", "web")

def buildServers(pServers, pRoles):
    for k, v in pServers.items():
        role = pRoles[v.get_role()]
        print(v.get_name())
        for c in role.get_commands():
            print(c)
        for ip in role.get_iptables():
            print(ip)


buildServers(Servers, Roles)