# RRTM/RRTMG installation and simulation

## RRTM installation

### RRTM download

The raditive transfer model can be downloaded from http://rtweb.aer.com/rrtm_frame.html

### makefile modification

To install it, the ./makefile/makefile.common should be modified according to the computing platform environment.

Can choose any FC_TYPE, which does not matter.

The makefile uses PLATFORM=$(shell uname) to find the platform type, and I uses 

$(info $$PLATFORM is [${PLATFORM}])

to see what platform I am working on. Then, finding the approparite operation systems (such as Darwin, Linux, IRIX64, and SunOS) in the following lines. I am using Linux, so move to the line ifeq ($(PLATFORM),Linux)  PLTFRM = linux

Then, the FC_TYPE. Focusing on the line FC = pgf90 (or intel, or g95). However, I don't find any of these FORTRAN compiler on the server. The compiler I found is gfortran, which is not in the section PLTFRM=Linux but in PLTFRM=OS_X. So, I copied the following lines from gnu to the g95.

FC = gfortran
FCFLAG =   -fdefault-integer-8 -fdefault-real-8 -Wall -frecord-marker=4
UTIL_FILE = util_gfortran.f

So, the FC_TYPE = g95 is still using, but the FC is changed from g95 to gfortran.

### make and debug

After that, RUN MAKEFILE from parent directory using make -f makefiles/make_rrtm

There is an error message,

gfortran: error trying to exec 'f951': execvp: No such file or directory

After several tests, I found it is due to the fortran compiler on Trellis is broken. So, I tried to re-install the gfortran on the Linux server by

$ sudo yum install gcc-gfortran

Then, the make command of RRTM works.

### simulation

After the installation, there is a software generated at ./rrtm_v3.3_linux_gfortran . We can run it or link it to other places for the simulation.

There are several examples in ./run_examples/ Can test by running ./run_examples/script.run_testcases

Basically, prepare a file named INPUT_RRTM at the same folder as rrtm_v3.3_linux_gfortran. Then, run the command $rrtm_v3.3_linux_gfortran . The result will be generated as OUTPUT_RRTM at the same folder.

### INPUT file instruction

Take input_rrtm_MLS as an example.

All contents before the first $ can be treated as comments, which is

APE5 FOR MLS
0        1         2         3         4         5         6         7         8         9
123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-

The '123456789-12345...' is used to indicate the location (number of column)

The first line after the line with $ is RECORD 1.2 in the RRTM_instruction file, which is

                                                 0                   0              3    0

Let's combine first several lines together to discribe it.
123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-
$ STANDARD MID-LATITUDE SUMMER ATMOSPHERE
                                                 0                   0              3    0
                                                 
The first 0 is at the 50th column, that is IATM mentioned in the RRTM_instruction file

      IATM,  IXSECT, ISCAT,  NUMANGS,   IOUT,   ICLD
 
        50,      70,      83,  84-85,  88-90,     95   
 
   49X, I1, 19X, I1, 12X, I1,     I2, 2X, I3, 4X, I1

Before IATM, there is 49 spaces (49X), the IATM only occupy 1 column (I1), then 19 spaces (19X) for the next argument IXSECT.

Noted that, if I understand correctly, some words written on the spaces do not matter, just as comments. And not mentioning some arguments also do not matter. It seems some arguments have default values. Such as the next line, which is RECORD 1.4 in the RRTM_instruction file.

 1 51    7  1.000000MIDLATITUDE SUMM H1=    0.00 H2=   70.00 ANG=   0.000 LEN= 0

The following lines are the pressure, temperature, and something that I don't know.

   952.1147        291.77              3   0.000 1013.00 294.20  1.100  891.46 289.25

Then, 7 gas species mixing ratios. The default is 7 species as Table II.

  1.5946558E-02  3.5495765E-04  3.1872162E-08  3.2014773E-07  1.4735235E-07  1.7007853E-06  2.0897518E-01  2.0212141E+24

(1) H2O  (2) CO2  (3) O3 (4) N2O (5) CO (6) CH4 (7) O2


