# MaxScale Setup with Docker Compose and Python Script

This README.md provides instructions for setting up a MaxScale environment using Docker Compose, configuring MaxScale with example.cnf, and interacting with MaxScale using a Python script.

## Docker Compose Setup

The provided Docker Compose configuration sets up two MariaDB database servers (`db1` and `db2`) and a MaxScale instance (`maxscale`). The servers are configured to use MariaDB version 10.3.

### Prerequisites

Ensure you have Docker and Docker Compose installed on your system.

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)


### Usage

1. Clone this repository: https://github.com/Olakunleabiola/maxscale-docker

    ```bash
    git clone https://github.com/Olakunleabiola/maxscale-docker
    ```

2. Navigate to the cloned directory:

    ```bash
    cd /testing/maxscale-docker/maxscale
    ```

3. Run Docker Compose to start the containers:

    ```bash
    docker-compose up -d
This will start three containers: db1, db2, and maxscale

    ```

## MaxScale Configuration with example.cnf

The provided `example.cnf` file configures MaxScale to implement sharding with MariaDB servers. It includes server configurations, server monitoring, service definitions, and listener configurations.


### Configuration Overview

The `example.cnf` file consists of sections for server configuration, server monitoring, sharded service definition, listener configuration, service definitions, and listener definitions.


### Usage

1. Copy the provided `example.cnf` file to the MaxScale configuration directory.

2. Update the configuration file according to your environment, including server addresses, ports, and authentication credentials.

3. Restart MaxScale to apply the new configuration:

    ```bash
    systemctl restart maxscale

    ```

## Python Script for Interacting with MaxScale

The provided Python script (`main.py`) allows you to interact with MaxScale instances and perform various queries on specified databases using the `mysql.connector` library.


### Prerequisites

Before running the script, ensure you have Python installed on your system. Install the `mysql.connector` library using pip:

```bash
pip install mysql-connector-python
python3 main.py

MaxScale configuration files are located in the maxscale.cnf.d directory.
Modify the configuration files according to your requirements.

Database Initialization:
SQL scripts for initializing databases db1 and db2 are placed in the sql/db1 and sql/db2 directories respectively.
You can place your initialization SQL scripts in these directories.

Important Notes
The database servers (db1 and db2) are configured with specified username and password.
This setup is for demonstration purposes and not recommended for production use without proper security configurations.
MaxScale serves as the database proxy and load balancer, routing client queries to the appropriate database server based on the sharding key or routing rules.

References
MaxScale Documentation
Docker Documentation
Docker Compose Documentation

To stop the containers, execute the following command. Optionally, use the -v
flag to also remove the volumes.

To run maxctrl in the container to see the status of the cluster:
```
$ sudo docker-compose exec maxscale maxctrl list servers
         
    
Server  	 Address         Port	  Connections        	State   	      GTID                        Monitor

masterdb1	 db1        	  3306     	0	 Master, Running               0-3000-4                	MariaDB-Monitor
masterdb2   	 db12	          3306          0	     Running                   0-3001-4	                MariaDB-Monitor


```

Since the database servers are configured as masters, automatic failover may not be necessary for traditional high availability purposes, as there is no slave to promote in case of a failure. However, when you bring down one of the masters, the other master is still running
```
$ sudo docker-compose stop db1
[+] stopping 1/1
container maxscaledocker-db1-1 stopped ... 
$ docker-compose exec maxscale maxctrl list servers
Server  	 Address         Port	  Connections        	State   	      GTID                        Monitor

masterdb1	 db1        	  3306     	0	        Down               0-3000-4                	MariaDB-Monitor
masterdb2   	 db12	          3306          0	       Running             0-3001-4	                MariaDB-Monitor

$ sudo docker-compose start db1
container maxscaledocker-db1-1 started...
$ docker-compose exec maxscale maxctrl list servers

Server  	 Address         Port	  Connections        	State   	      GTID                        Monitor

masterdb1	 db1        	  3306     	0	 Master, Running               0-3000-4                	MariaDB-Monitor
masterdb2   	 db12	          3306          0	     Running                   0-3001-4	                MariaDB-Monitor


```

Once complete, to remove the cluster and maxscale containers:

```
sudo docker-compose down -v
```
