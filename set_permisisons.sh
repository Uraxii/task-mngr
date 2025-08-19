#!/bin/bash

# Setup script for Epson TM-T20III printer permissions
# This script configures udev rules to give the current user access to the printer

# Get current username
CURRENT_USER=$(whoami)

echo "Setting up Epson TM-T20III permissions for user: $CURRENT_USER"
echo

# Add user to dialout group
echo "Adding user to dialout group..."
sudo usermod -a -G dialout $CURRENT_USER
echo "✓ Done"

# Create udev rule
echo "Creating udev rule..."
sudo tee /etc/udev/rules.d/99-epson-tm-t20iii.rules > /dev/null << EOF
# Epson TM-T20III Receipt Printer - Access for user: $CURRENT_USER
SUBSYSTEM=="usb", ATTR{idVendor}=="04b8", ATTR{idProduct}=="0e28", MODE="0660", OWNER="$CURRENT_USER", GROUP="dialout"
EOF
echo "✓ Done"

# Reload udev rules
echo "Reloading udev rules..."
sudo udevadm control --reload-rules
sudo udevadm trigger
echo "✓ Done"

echo
echo "Setup complete!"
echo
echo "Next steps:"
echo "1. Logout and login again (or reboot)"
echo "2. Unplug and replug your printer"
echo "3. Test with: python test.py"
