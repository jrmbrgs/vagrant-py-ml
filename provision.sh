#!/bin/bash

echo "Provisioning virtual machine..."

# Python ML stach
sudo apt-get -y install python-pip python-dev
sudo apt-get -y install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
sudo python -m pip install --upgrade pip

sudo pip install -U scikit-learn
