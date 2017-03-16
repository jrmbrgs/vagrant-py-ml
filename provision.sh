#!/bin/bash

echo "Provisioning virtual machine..."

# Python ML stach
sudo apt-get -y install python-pip python-dev
sudo apt-get -y install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
sudo python -m pip install --upgrade pip

sudo pip install -U scikit-learn

# Java 1.8
sudo apt-get -y install software-properties-common
sudo add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install oracle-java8-installer


# Opennlp

