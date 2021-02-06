# Terra Dataset Size Survey

## About

This repo contains the scripts, and a dev environment for, a dataset size survey.
I'm using this to explore the datasets available to Terra through a variety of
NIH projects.

## Running

To run the environment in Docker:

- `git clone https://github.com/briandoconnor/terra-dataset-size-survey.git`
- `docker-compose up` or `docker-compose up -d` if you want to avoid console output

At this point you now have a Docker container running that you can connect
to and use for development, see below.

## Organization

I've reorganized the services into the `services` directory and the
`working` directory is mounted and shared across the docker containers when run.

## Python Version

See the [official python images](https://hub.docker.com/_/python) on DockerHub
as well as the [releases of Debian](https://wiki.debian.org/DebianReleases).  I'm
using Debian Buster and Python 3 as the basis for the Python environment that gets
launched:

    python:3-buster

It's probably a good idea to use a specific version number of Python when
writing real scripts/services.

## Connecting to Python Dev Environments

Once you launch with `docker-compose up` you can login in to the Python service
container using:

```
# list out the running containers
$> docker ps
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                    NAMES
02d2b8fce3af   python:3-buster   "sh -c 'pip install …"   44 seconds ago   Up 43 seconds   0.0.0.0:9000->9000/tcp   blog-docker-dev-environment-example_py-dev_1

# connect to this running container
$> docker exec -it 02d2b8fce3af /bin/bash

# now within the container I'm running as root and in the ~/py1 directory
# which is the directory containing the flask app
root@02d2b8fce3af:~/py1# whoami
root

# now if I go to ~/py-dev it contains the working directory with my scripts
root@02d2b8fce3af:~# cd ~/py-dev/
root@02d2b8fce3af:~/py-dev# ls
scripts

# a shortcut to connecting
$> docker exec -it `docker ps | grep terra-dataset-size-survey_py-dev | awk '{print $1}'` /bin/bash
```

## Python Server

The flask server is running on `http://localhost:9000` and just returns "Hello from py1".
I might use this for future development but for now it's unused.

## Python Script

See `scripts/calculate_sizes_python_script/process.py`

See `scripts/calculate_sizes_python_script/data_sources.tsv` which is a TSV version
of this [Google spreadsheet](https://docs.google.com/spreadsheets/d/10A5kbSqUcWWUoPWHwREwCrRjCORZ5jrxQpWW5cMVgh0/edit#gid=0).

### Goal

The goal is to work through this document and determine if there's a
programmatic approach to determining 1) # of participants and 2) file sizes.

### Data Sources

See the document [DATA.md](DATA.md) for information on each dataset the
script pulls from.
