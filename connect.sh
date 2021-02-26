#!/usr/bin/env bash

docker exec -it `docker ps | grep ncpi-dataset-size-survey_py-dev | awk '{print $1}'` /bin/bash
