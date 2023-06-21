#!/bin/bash

# Install dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip -y

# Install howto tool using pip
sudo pip3 install howto

# Add /usr/local/bin to PATH
echo "export PATH=/usr/local/bin:$PATH" >> ~/.bashrc
source ~/.bashrc

echo "Installation complete!"

