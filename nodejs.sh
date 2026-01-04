#!/bin/bash
# nodejs.sh - Install NVM, Node.js (LTS), and npm on Linux

set -e  # Exit immediately if a command fails

# Step 1: Install NVM
if [ ! -d "$HOME/.nvm" ]; then
    echo "Installing NVM..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
else
    echo "NVM already installed."
fi

# Step 2: Load NVM into current shell
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Step 3: Install Node.js LTS if not installed
if ! command -v node >/dev/null 2>&1; then
    echo "Installing Node.js LTS..."
    nvm install --lts
else
    echo "Node.js already installed."
fi

# Step 4: Use the LTS version
nvm use --lts

# Step 5: Verify installation
echo "Node.js version: $(node -v)"
echo "npm version: $(npm -v)"
