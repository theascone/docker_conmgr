# Conmgr
Utility to start and stop containers from a web frontend

This utility is used for allowing users without access to the docker daemon to start and stop specific containers.

It doesn't provide any kind of authentication,
so exposure behind a proxy providing password protection is strongly recommended.

## Launch
Use the docker-compose.yml.sample file provided in the root of the repository.

## Containers
If you want to enable users to start/stop a specific container using this utility,
then you have to label it with the key *com.conmgr.name*.

### Labels:
|Name             |Description        |Required   	|
|---	            |---	              |---	        |
|com.conmgr.name  |Container name   	|yes   	      |
|com.conmgr.info  |Short description  |no   	      |
|com.conmgr.group |Visibility group   |no   	      |

## Visibility Groups
If running multiple instances of conmgr, you might want to make a container only visible to one specific conmgr instance.
The conmgr-server has to be started with the environment variable *CONMGR_GROUP*.
This instance then will only list containers with the same visibility group specified in the label *com.conmgr.group*
