# VsftpdFTPSSimplifier

A Python-based tool to simplify the installation, configuration, and management of the `vsftpd` service for secure FTPS.

## Features
- Automates the installation of `vsftpd` using `apt-get`.
- Configures `vsftpd` for secure FTPS with SSL/TLS.
- Dynamically generates SSL certificates and private keys if not already present.
- Creates FTP users with test files in their home directories.
- Provides commands to manage the `vsftpd` service (start, stop, restart, status).
- Logs client commands for testing FTPS connections.
- Ensures proper permissions for user directories and files.

## Functions
The following are the key functions provided by the `VsftpdFTPSSimplifier` tool:

- **install_vsftpd()**: Installs the `vsftpd` package using the system's package manager.
- **generate_ssl_cert(cert_path, key_path)**: Generates SSL certificates and private keys at the specified paths.
- **configure_vsftpd(cert_path, key_path)**: Configures the `vsftpd` service for secure FTPS, including SSL/TLS settings.
- **ensure_log_file_exists()**: Ensures the `vsftpd` log file exists and has the correct permissions.
- **stop_vsftpd()**: Stops the `vsftpd` service.
- **restart_vsftpd()**: Restarts the `vsftpd` service.
- **check_status_vsftpd()**: Checks the status of the `vsftpd` service.
- **check_port_listening(port)**: Verifies if the `vsftpd` service is listening on the specified port.
- **create_random_file(file_path, size_kb)**: Creates a random file of the specified size in KB.
- **create_ftp_user(username, password, file_type, size_kb)**: Creates an FTP user with a test file in their home directory.
- **log_client_commands(username, password)**: Logs commands for testing FTP and FTPS connections.

## Prerequisites
- Python 3.6 or higher
- OpenSSL
- `vsftpd` (installed automatically by the script if not present)
- `sudo` privileges for system-level changes

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/VsftpdFTPSSimplifier.git
   cd VsftpdFTPSSimplifier
   ```

2. Ensure Python and OpenSSL are installed:
   ```bash
   sudo apt-get install -y python3 openssl
   ```

3. Make the script executable:
   ```bash
   chmod +x vsftpd_ftps_config.py
   ```

## Usage
Run the script with the desired options:

```bash
python3 vsftpd_ftps_config.py [OPTIONS]
```

### Available Options
- `--cert`: Path to the SSL certificate file (default: `/etc/ssl/certs/vsftpd.pem`).
- `--key`: Path to the SSL private key file (default: `/etc/ssl/private/vsftpd.key`).
- `--user`: FTP username (default: `ftpuser`).
- `--password`: FTP user password (default: `password`).
- `--stop`: Stop the `vsftpd` service.
- `--restart`: Restart the `vsftpd` service.
- `--status`: Check the status of the `vsftpd` service.
- `--check-port`: Check if `vsftpd` is listening on port 990.
- `--file-type`: File type for the default test file (default: `txt`).
- `--size`: File size in KB for the default test file (default: `1`).

### Example Commands
1. Install and configure `vsftpd` with default settings:
   ```bash
   python3 vsftpd_ftps_config.py
   ```

2. Create a user with a custom password and test file:
   ```bash
   python3 vsftpd_ftps_config.py --user myuser --password mypassword --file-type txt --size 10
   ```

3. Restart the `vsftpd` service:
   ```bash
   python3 vsftpd_ftps_config.py --restart
   ```

4. Check if `vsftpd` is listening on port 990:
   ```bash
   python3 vsftpd_ftps_config.py --check-port
   ```

## Logs
The script logs all actions and outputs to the console for easy debugging and monitoring.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

### Guidelines
- Follow PEP 8 for Python code style.
- Ensure all changes are tested before submitting a pull request.
- Open an issue for any bugs or feature requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This script modifies system-level configurations and requires `sudo` privileges. Use it at your own risk.
```