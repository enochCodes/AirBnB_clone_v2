#!/bin/bash

# Uninstall Fabric
pip3 uninstall -y Fabric

# Install libffi-dev if not already installed
if ! dpkg -s libffi-dev >/dev/null 2>&1; then
    sudo apt-get install -y libffi-dev
fi

# Install libssl-dev if not already installed
if ! dpkg -s libssl-dev >/dev/null 2>&1; then
    sudo apt-get install -y libssl-dev
fi

# Install build-essential if not already installed
if ! dpkg -s build-essential >/dev/null 2>&1; then
    sudo apt-get install -y build-essential
fi

# Install python3.4-dev if available
if sudo apt-get install -y python3.4-dev >/dev/null 2>&1; then
    echo "python3.4-dev installed successfully"
else
    echo "python3.4-dev not available or already installed"
fi

# Install libpython3-dev if not already installed
if ! dpkg -s libpython3-dev >/dev/null 2>&1; then
    sudo apt-get install -y libpython3-dev
fi

# Install required Python packages
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1
