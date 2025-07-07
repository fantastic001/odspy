#!/bin/bash
# filepath: /Users/stefan/data/Development/odspy/distribute.sh

# Ensure the script exits on error
set -e

# Step 1: Clean previous builds
echo "Cleaning up previous builds..."
rm -rf dist/

# Step 2: Build the package
echo "Building the package..."
python3 setup.py sdist bdist_wheel

# Step 3: Upload to PyPI
echo "Uploading to PyPI..."
twine upload dist/*.tar.gz 

# Step 4: Installation instructions
echo "To install the package, run:"
echo "pip install odspy"