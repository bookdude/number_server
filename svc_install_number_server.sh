#!/bin/bash

# Script to create and manage a service for the Number Server application

# Define global variables
SERVICE_NAME="number_server"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"
APP_PATH="/opt/number_server/web_count_app.py"

# Function to check if the script is run as root
check_root() {
  if [[ $EUID -ne 0 ]]; then
    printf "This script must be run as root\n" >&2
    exit 1
  fi
}

# Function to create the service file
create_service_file() {
  cat <<EOF > "${SERVICE_FILE}"
[Unit]
Description=Number Server Application Service
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/bin/python3 ${APP_PATH}
Restart=on-abort

[Install]
WantedBy=multi-user.target
EOF
}

# Function to enable and start the service
enable_and_start_service() {
  if ! systemctl enable "${SERVICE_NAME}"; then
    printf "Failed to enable ${SERVICE_NAME} service\n" >&2
    return 1
  fi

  if ! systemctl start "${SERVICE_NAME}"; then
    printf "Failed to start ${SERVICE_NAME} service\n" >&2
    return 1
  fi

  printf "Service ${SERVICE_NAME} has been started and enabled to start at boot\n"
}

# Function to check if the service file already exists
check_service_exists() {
  if [[ -f "${SERVICE_FILE}" ]]; then
    printf "Service file ${SERVICE_FILE} already exists.\n" >&2
    return 1
  fi
}

# Main function to control the flow of the script
main() {
  check_root
  check_service_exists || return 1
  create_service_file
  enable_and_start_service
}

# Call the main function
main
