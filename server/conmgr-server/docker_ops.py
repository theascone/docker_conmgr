import os
import docker

cli = docker.Client(base_url='unix://var/run/docker.sock')

filters = {'label':['com.conmgr.name']}

def getContainers():
    containers = cli.containers(all=True, filters=filters)
    containers_filtered = [x for x in containers if
        (not 'CONMGR_GROUP' in os.environ) or
        ('com.conmgr.group' in x['Labels'] and
         x['Labels']['com.conmgr.group'] == os.environ['CONMGR_GROUP'])]
    containers_transformed = [
        {
            'id': x['Id'],
            'running': x['State']=='running',
            'name': x['Labels']['com.conmgr.name'],
            'info': x['Labels'].get('com.conmgr.info', '')
        } for x in containers_filtered
    ]
    return containers_transformed

def startContainer(Id):
    containers = getContainers();
    containers_filtered = [x for x in containers if x['id'] == Id]
    print(containers_filtered)
    return containers_filtered and cli.start(container=containers_filtered[0]['id']) == None

def stopContainer(Id):
    containers = getContainers();
    containers_filtered = [x for x in containers if x['id'] == Id]
    print(containers_filtered)
    return containers_filtered and cli.stop(container=containers_filtered[0]['id']) == None
