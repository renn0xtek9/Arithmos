#!/bin/bash
cd Docker 
docker build -t arithmos:latest .
docker run -it arithmos
