# Usage Guide for VsftpdFTPSSimplifier

This guide provides detailed instructions on how to use the `VsftpdFTPSSimplifier` tool to install, configure, and manage the `vsftpd` service for secure FTP and FTPS.

---

## Prerequisites

Before using the tool, ensure the following prerequisites are met:
- Python 3.6 or higher is installed.
- OpenSSL is installed on your system.
- You have `sudo` privileges to make system-level changes.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/VsftpdFTPSSimplifier.git
   cd VsftpdFTPSSimplifier
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the script is executable:
   ```bash
   chmod +x vsftpd_ftps_config.py
   ```

---

## Running the Script

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

---

## Example Commands

1. **Install and configure `vsftpd` with default settings**:
   ```bash
   python3 vsftpd_ftps_config.py
   ```

2. **Create a user with a custom password and test file**:
   ```bash
   python3 vsftpd_ftps_config.py --user myuser --password mypassword --file-type txt --size 10
   ```

3. **Restart the `vsftpd` service**:
   ```bash
   python3 vsftpd_ftps_config.py --restart
   ```

4. **Check if `vsftpd` is listening on port 990**:
   ```bash
   python3 vsftpd_ftps_config.py --check-port
   ```

---

## Logs

The script logs all actions and outputs to the console for easy debugging and monitoring.

---

## Troubleshooting

- **Permission Denied**: Ensure you are running the script with `sudo` if required.
- **Missing Dependencies**: Verify that Python, OpenSSL, and `vsftpd` are installed on your system.
- **Service Not Starting**: Check the `vsftpd` configuration file for errors.

---

## Additional Notes

- The script modifies system-level configurations. Use it with caution.
- Always back up your existing `vsftpd` configuration before running the script.

For further assistance, refer to the project's `README.md` or open an issue in the repository.
```