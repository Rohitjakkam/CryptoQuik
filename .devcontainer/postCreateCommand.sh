#!/bin/bash

# Install tools specified in mise.toml
#
cd /workspaces/CryptoQuik
mise trust
mise install
echo 'eval "$(/usr/local/bin/mise activate bash)"' >> ~/.bashrc
source ~/.bashrc