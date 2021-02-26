#!/usr/bin/env bash

docker exec -it `docker ps | grep ncpi-dataset-interop-survey_py-dev | awk '{print $1}'` /bin/bash
