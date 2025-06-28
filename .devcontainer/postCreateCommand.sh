#!/bin/bash

# Install tools specified in mise.toml
#
cd /workspaces/CryptoQuik
mise trust
mise install
echo 'eval "$(/usr/local/bin/mise activate bash)"' >> ~/.bashrc
source ~/.bashrc

echo "Installing kubectl..."

KUBECTL_VERSION=v1.31.4
curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl" || {
    echo "❌ Failed to download kubectl"; exit 1;
}

install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl || {
    echo "❌ Failed to install kubectl"; exit 1;
}

rm -f kubectl
kubectl version --client --output=yaml || echo "kubectl install failed"



echo "Installing k9s..."

K9S_VERSION="v0.32.4"

curl -Lo k9s.tgz "https://github.com/derailed/k9s/releases/download/${K9S_VERSION}/k9s_Linux_amd64.tar.gz" || {
    echo "❌ Failed to download k9s"; exit 1;
}

tar -xzf k9s.tgz k9s || {
    echo "❌ Failed to extract k9s"; exit 1;
}

install -o root -g root -m 0755 k9s /usr/local/bin/k9s || {
    echo "❌ Failed to install k9s"; exit 1;
}

rm -f k9s k9s.tgz
k9s version || echo "k9s install failed"
