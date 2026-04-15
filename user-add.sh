#!/usr/bin/env bash
source common-bash-config.sh

#============================== MSC License Header ==============================
#
#          FILE:  root-useradd-rootless-podman.sh
#
#         USAGE:  root-useradd-rootless-podman.sh
#
#   DESCRIPTION:  Used to add new users for rootless podman.
#
#       OPTIONS:  None, but the script requests input.
#                 Help improve this script to cover needed steps.
#         NOTES:  Direct CLI access: /usr/local/sbin/root-*.sh
#  REQUIREMENTS:  Root access.
#          BUGS:  Report issues to shanecoley@mscsoftwaresolutions.com
#
#       CREATED:  2025-07-03
#      REVISION:  1.0
#       VERSION:  0.1.0
#        AUTHOR:  Shane Coley (shanecoley@mscsoftwaresolutions.com)
# 
#
#  COPYRIGHT (c) 2025 MSC Software Solutions. All rights reserved.
# 
#  This source code is protected under international copyright law.  All rights
#  reserved and protected by the copyright holders.
#  This file is confidential and only available to authorized individuals with the
#  permission of the copyright holders.  If you encounter this file and do not have
#  permission, please contact the copyright holders and delete this file.
#
#============================== MSC License Footer ==============================

source run-as-root.sh

read -rp "Enter new username: " username
# read -rp "Set initial password? [y/N]: " setpass
# read -rp "Generate SSH keypair for this user? [y/N]: " genkey
# read -rp "Restrict to key-based login only (no password auth)? [y/N]: " keyonly

# Decide how to manage keys later
genkey="y"
keyonly="y"
setpass="n"

# Check user doesn't exist
if id "$username" &>/dev/null; then
  echo "User '$username' already exists."
  exit 1
fi

# Create the user with home directory
useradd --create-home --skel /etc/skel --shell /bin/bash "$username"
USER_HOME="/home/$username"
SSH_DIR="$USER_HOME/.ssh"
SOCKET_DIR="$SSH_DIR/sockets"

# Optionally set password
if [[ "${setpass,,}" == "y" ]]; then
  echo "Set password for $username:"
  passwd "$username"
fi

# Create SSH and systemd directories
install -d -m 700 -o "$username" "$SSH_DIR"
install -d -m 700 -o "$username" "$SOCKET_DIR"
install -d -m 755 -o "$username" "$USER_HOME/.config/systemd/user"

# Should have already written files from skel
chmod 600 "$SSH_DIR/config"
chmod 644 "$USER_HOME/.bash_profile"

user_ssh_file="${HOSTNAME}-${username}-id_ed25519"

# prompt for public key input
echo "Paste the public SSH key for user '$username':"
read -r user_pubkey

# Add provided public key to authorized_keys
echo "$user_pubkey" >> "$SSH_DIR/authorized_keys"
chmod 600 "$SSH_DIR/authorized_keys"
chown "$username:$username" "$SSH_DIR/authorized_keys"

# Adjust ownership of everything
chown -R "$username:$username" "$USER_HOME"

# Restrict SSH login to key-only if chosen
if [[ "${keyonly,,}" == "y" ]]; then
  echo "Restricting $username to key-only login (no password)"
  SSHD_CONFIG="/etc/ssh/sshd_config.d/90-${username}-keyonly.conf"
  cat <<EOF > "$SSHD_CONFIG"
Match User $username
    PasswordAuthentication no
    AuthenticationMethods publickey
EOF
  chmod 644 "$SSHD_CONFIG"
  echo "Reloading sshd to apply login restriction..."
  systemctl reload sshd
fi

echo "User '$username' created with SSH multiplexing support."
if [[ "${genkey,,}" == "y" ]]; then
  echo "SSH public key copied to authorized_keys."
  echo "Give this user access using this public key (above) on your local machine."
fi

user_id=$(id -u $username)

echo "Enabling linger for user: $username and id: $user_id"
systemctl daemon-reexec
systemctl daemon-reload

loginctl enable-linger $username

echo "Restarting user@$user_id.service"
systemctl stop user@$user_id.service
sleep 2
systemctl start user@$user_id.service