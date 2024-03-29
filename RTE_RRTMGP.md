# RTE_RRTMGP Installation and Simulation

## Docker installation

create an container

$ sudo docker run -it ghcr.io/earth-system-radiation/rte-rrtmgp-ci:ifort /bin/bash

ctrl + C to exit

$ sudo docker ps -a

CONTAINER ID   IMAGE                                                COMMAND       CREATED        STATUS                      PORTS     NAMES
756XXX   ghcr.io/earth-system-radiation/rte-rrtmgp-ci:ifort   "/bin/bash"   16 hours ago   Exited (127) 16 hours ago             musing_burnell
83bXXX   ghcr.io/earth-system-radiation/rte-rrtmgp-ci:ifort   "/bin/bash"   16 hours ago   Up 2 hours                            naughty_dijkstra

re-enter the container

$ sudo docker exec -it 83bXXX bin/bash


## RTE_RRTMGP Installation

$ mkdir rrtmgp

$ cd rrtmgp/

$ git clone https://github.com/earth-system-radiation/rte-rrtmgp.git

## Install vim in a container

$ apt-get update

$ apt-get install vim

## Set up libraries

$ echo $FC

ifort

$ export FCFLAGS="-m64 -g -traceback -heap-arrays -assume realloc_lhs -extend-source 132 -check bounds,uninit,pointers,stack -stand f08"

$ export RRTMGP_ROOT=/home/rrtmgp/rte-rrtmgp

$ export NCHOME=/usr

$ export NFHOME=/opt/netcdf-fortran

## RTE_RRTMGP installation

$ make libs

$ make tests

$ make check

$ python validation-plots.py

## Transfer data to outside of Docker

In a different terminal

$ sudo docker cp 83bXXX:/home/rrtmgp/rte-rrtmgp/tests/validation-figures.pdf /mnt/bigdrive/docker_transfer/

## Run the RTE_RRTMGP

For longwave simulation

$ ./rrtmgp_rfmip_lw   8 multiple_input4MIPs_radiation_RFMIP_UColorado-RFMIP-1-2_none.nc ../../rrtmgp/data/rrtmgp-data-lw-g256-2018-12-04.nc

For shortwave simulation

$ ./rrtmgp_rfmip_sw   8 multiple_input4MIPs_radiation_RFMIP_UColorado-RFMIP-1-2_none.nc ../../rrtmgp/data/rrtmgp-data-sw-g224-2018-12-04.nc

## After rebooting a server

$ systemctl start docker

Then, choose identity to authenticate

$ sudo docker start containerID

