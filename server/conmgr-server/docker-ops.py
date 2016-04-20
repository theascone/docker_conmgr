from docker import Client

def getContainers():
    cli = Client(base_url='unix://var/run/docker.sock')
    containers = cli.containers(filters={'label':'com.conmgr.name'})
    print(containers)

def startContainer(Id):
    cli = Client(base_url='unix://var/run/docker.sock')
    containers = cli.containers(filters={'label':'com.conmgr.name'})
    print(containers)
    containers_filtered = [x for x in containers if x['Id'] == Id]
    print(containers_filtered)

    if containers_filtered:
        return cli.start(container=(head containers_filtered)['Id'])
    else return false

def stopContainer(Id):
    cli = Client(base_url='unix://var/run/docker.sock')
    containers = cli.containers(filters={'label':'com.conmgr.name'})
    print(containers)
    containers_filtered = [x for x in containers if x['Id'] == Id]
    print(containers_filtered)

    if containers_filtered:
        return cli.stop(container=(head containers_filtered)['Id'])
    else return false
