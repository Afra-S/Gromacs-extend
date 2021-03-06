module purge
module load intel/18.1 openmpi/intel/2.0.4

# variables for gromacs                                                                                                                                                                                    
export GROMACS_ROOT=/home/sabei/bin/ #"gromacs directory"                                                                                  
export PATH=$GROMACS_ROOT/bin:$PATH
export LD_LIBRARY_PATH=$GROMACS_ROOT/lib64:$LD_LIBRARY_PATH
export PKG_CONFIG_PATH=$GROMACS_ROOT/lib64/pkgconfig:$PKG_CONFIG_PATH
export MANPATH=$GROMACS_ROOT/share/man:$MANPATH
export GMXBIN=$GROMACS_ROOT/bin
export GMXLDLIB=$GROMACS_ROOT/lib64
export GMXMAN=$GROMACS_ROOT/share/man
export GMXDATA=$GROMACS_ROOT/share/gromacs

# variables for plumed                                                                                                                                                                                     
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/sabei/bin/plumed/lib
export PATH=$PATH:/home/sabei/bin/plumed/bin


export OMP_NUM_THREADS=1

gmx_mpi convert-tpr -s md-2.tpr -extend 500000 
