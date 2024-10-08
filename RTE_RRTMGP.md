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



# RRTMGP with aerosol simulation

To be able to conduct aerosol simulation, I installed a new version of RRTMGP.

## download docker image

$ docker pull earthsystemradiation/rte-rrtmgp-ci:oneapi

There are two versions available. Since the current AWS instance doesn’t have a GPU, I chose this version. Unlike the other one, this image does not include the RRTMGP model; it only contains the FORTRAN compiler. This might change, so it’s a good idea to search the Docker Hub for the latest version.

## install docker image

$ docker run -it --name rrtmgp-aerosol-test earthsystemradiation/rte-rrtmgp-ci:oneapi /bin/bash

## install software in the docker container

$ apt-get update && apt-get install -y wget bzip2

$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

$ bash miniconda.sh -b -p /opt/conda

$ export PATH=/opt/conda/bin:$PATH

$ conda init

$ conda --version

$ apt-get install -y vim

Install python package by using the provided yml files.

$ conda env create -f environment.yml

$ conda env create -f environment-noplots.yml 

$ conda env create -f environment-dev.yml 

## download the RRTMGP data

$ git clone https://github.com/earth-system-radiation/rrtmgp-data.git

## compile

The readme document is from here https://earth-system-radiation.github.io/rte-rrtmgp/how-tos/build-and-test.html

$ echo $FC

it returns "ifx", which is different than the document, so, it needs to update following the document. 

$ export FC=ifort

$ export FCFLAGS="-m64 -O3 -g -traceback -heap-arrays -assume realloc_lhs -extend-source 132"

$ export RRTMGP_DATA=/root/rrtmgp-data/

$ export RRTMGP_ROOT=~/rte-rrtmgp/

## make

Different folders have different Makefile, so I choose the all-sky folder. The $ make occurs error message in the RRTMGP_ROOT, but no error message in the all-sky folder.

Then, go to ~/rte-rrtmgp/examples/all-sky/

$ make


## running

Login

$ docker exec -it container_id /bin/bash

It seems every time logged in, it needs the following steps.

$ export FC=ifort

$ export FCFLAGS="-m64 -O3 -g -traceback -heap-arrays -assume realloc_lhs -extend-source 132"

$ export RRTMGP_DATA=/root/rrtmgp-data/

$ export RRTMGP_ROOT=~/rte-rrtmgp/

I used the following command to test in the direction "~/rte-rrtmgp/examples/all-sky/":

$ ./rrtmgp_allsky 24 72 1 rrtmgp-allsky-lw.nc  ${RRTMGP_DATA}/rrtmgp-gas-lw-g256.nc ${RRTMGP_DATA}/rrtmgp-clouds-lw.nc ${RRTMGP_DATA}/rrtmgp-aerosols-merra-lw.nc 

it returns as the following:

  ncol   nlay   ngpt  clouds aerosols time_per_col_ms nloops time_total_s time_m
 in_s
    24     72    256       1        1           0.946      1        0.023      0.023

The python environment I tested is the following

$ conda activate rte_rrtmgp_test
