#!/bin/sh
docker-compose -f .github/azure/docker-compose.yml stop
docker-compose -f .github/azure/docker-compose.yml rm -f
docker-compose -f .github/azure/docker-compose.yml build micro-ci-events &&
docker-compose -f .github/azure/docker-compose.yml up