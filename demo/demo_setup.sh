#!/usr/bin/bash
sudo apt-get update
sudo apt-get install -y subversion unzip git
sudo apt-get install -y build-essential pkg-config gfortran
sudo apt-get install -y libopenblas-base libopenblas-dev
sudo apt-get install -y libblas-dev libblas3
sudo apt-get install -y liblapack3 liblapack-dev
sudo apt-get install -y libatlas3-base libatlas-base-dev
# Download Ipopt 3.12
# This may require to accept the ssh fingerprint.
svn co https://projects.coin-or.org/svn/Ipopt/stable/3.12 CoinIpopt
# Apply the patch
cp ipopt.patch CoinIpopt/Ipopt/src/Common/
cd CoinIpopt/Ipopt/src/Common/
patch < ipopt.patch
cd -
# Get Ipopt dependencies
tar -zxf coinhsl-2014.01.10.tar.gz
mv coinhsl-2014.01.10 CoinIpopt/ThirdParty/HSL/coinhsl
cd CoinIpopt
cd ThirdParty
cd Metis
./get.Metis
cd ..
cd Mumps
./get.Mumps
cd ../..
# Compile Ipopt
mkdir build
cd build
../configure --prefix /usr/local
make -j4
sudo make install
sudo ldconfig
cd ../..
# Get miniconda for all the Python packages
wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
bash Miniconda-latest-Linux-x86_64.sh -b
export PATH=$HOME/miniconda/bin:$PATH
# Adds the path prepend to bashrc
echo "PATH=$HOME/miniconda/bin:$PATH" >> $HOME/.bashrc
# Install all the Python dependencies
conda install -y -c pydy python=2.7 pip numpy scipy cython matplotlib pandas pytables ipython-notebook pydy
wget https://bitbucket.org/moorepants/cyipopt/get/tip.zip
unzip tip.zip
cd moorepants-cyipopt-beafd15fbfe2
python setup.py install
cd ..
git clone https://github.com/csu-hmc/opty.git
pip install -e opty
# Get the presentation and demo repository
git clone https://github.com/csu-hmc/ISBTGCS2015.git
