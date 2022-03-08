#!/bin/bash
set -e

# Docker image name for this project
DOCKER_IMAGE_TAG="$(git rev-parse --short HEAD)-$(date +"%Y-%m-%d_%H-%M-%S")"
DOCKER_IMAGE_NAME="${DOCKER_IMAGE_NAME:-andrgje/mmocr-job:$DOCKER_IMAGE_TAG}"

set -x
docker build --rm  -t $DOCKER_IMAGE_NAME .