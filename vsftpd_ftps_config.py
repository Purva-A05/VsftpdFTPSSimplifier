import subprocess
import os
import logging
import pwd
import argparse


def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )


def install_vsftpd():
    """Install vsftpd using apt-get."""
    try:
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'vsftpd'], check=True)
        logging.info("vsftpd installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during installation: {e}")


def generate_ssl_cert(cert_path, key_path):
    """Generate SSL certificate and key regardless of existing paths."""
    logging.info("Generating SSL certificate and key...")
    subprocess.run([
        'openssl', 'req', '-newkey', 'rsa:2048', '-nodes', '-keyout', key_path,
        '-x509', '-days', '365', '-out', cert_path, '-subj', '/CN=localhost'
    ], check=True)
    logging.info(f"Generated certificate at {cert_path} and key at {key_path}.")


def configure_vsftpd(cert_path, key_path):
    """Configure vsftpd with given settings."""
    settings = [
        "listen=YES",
        "anonymous_enable=NO",
        "local_enable=YES",
        "write_enable=YES",
        "dirmessage_enable=YES",
        "use_localtime=YES",
        "xferlog_enable=YES",
        "log_ftp_protocol=YES",
        "vsftpd_log_file=/var/log/vsftpd.log",
        "connect_from_port_20=YES",
        f"rsa_cert_file={cert_path}",
        f"rsa_private_key_file={key_path}",
        "listen_port=990",
        "ssl_enable=YES",
        "ssl_ciphers=ALL:COMPLEMENTOFALL",
        "strict_ssl_read_eof=NO",
        "allow_anon_ssl=NO",
        "debug_ssl=YES",
        "force_local_data_ssl=YES",
        "force_local_logins_ssl=YES",
        "ssl_tlsv1=YES",
        "ssl_sslv3=NO",
        "ssl_sslv2=NO",
        "pasv_enable=YES",
        "require_ssl_reuse=NO",
        "userlist_enable=YES",
        "userlist_deny=YES",
        "userlist_file=/etc/vsftpd.user_list"
    ]

    config_file = '/etc/vsftpd.conf'
    backup_file = '/etc/vsftpd.conf.bak'

    # Backup existing config
    if os.path.exists(config_file):
        subprocess.run(['sudo', 'cp', config_file, backup_file])
        logging.info(f"Backup of config file created at {backup_file}")

    try:
        with open(config_file, 'w') as file:
            for setting in settings:
                file.write(setting + '\n')
        logging.info("vsftpd configuration updated successfully.")
    except Exception as e:
        logging.error(f"Error updating configuration: {e}")


def ensure_log_file_exists():
    """Ensure the vsftpd log file exists."""
    try:
        log_file = '/var/log/vsftpd.log'
        if not os.path.exists(log_file):
            subprocess.run(['sudo', 'touch', log_file], check=True)
            subprocess.run(['sudo', 'chmod', '640', log_file], check=True)
            logging.info(f"Log file created at {log_file}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error creating log file: {e}")


def stop_vsftpd():
    """Stop the vsftpd service."""
    try:
        subprocess.run(['sudo', 'service', 'vsftpd', 'stop'], check=True)
        logging.info("vsftpd stopped successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error stopping vsftpd: {e}")


def restart_vsftpd():
    """Restart the vsftpd service."""
    try:
        subprocess.run(['sudo', 'service', 'vsftpd', 'restart'], check=True)
        logging.info("vsftpd restarted successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error restarting vsftpd: {e}")


def check_status_vsftpd():
    """Check the status of the vsftpd service."""
    try:
        result = subprocess.run(['sudo', 'service', 'vsftpd', 'status'], check=True, capture_output=True, text=True)
        logging.info("vsftpd service status:\n" + result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking status of vsftpd: {e}")


def check_port_listening(port):
    """Check if vsftpd is listening on the specified port."""
    try:
        result = subprocess.run(['sudo', 'ss', '-tuln'], check=True, capture_output=True, text=True)
        if f':{port}' in result.stdout:
            logging.info(f"vsftpd is listening on port {port}.")
        else:
            logging.warning(f"vsftpd is not listening on port {port}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking port {port}: {e}")


def create_random_file(file_path, size_kb):
    """Create a random file with specified size in KB."""
    with open(file_path, 'wb') as f:
        f.write(os.urandom(size_kb * 1024))
    logging.info(f"Created file {file_path} with size {size_kb} KB.")


def create_ftp_user(username, password, file_type='txt', size_kb=1):
    """Create an FTP user, deleting the user first if they exist, and add a test file in their home directory."""
    try:
        # Delete user if they already exist
        try:
            pwd.getpwnam(username)
            logging.info(f"User {username} already exists. Deleting user.")
            subprocess.run(['sudo', 'deluser', '--remove-home', username], check=True)
            logging.info(f"User {username} deleted successfully.")
        except KeyError:
            logging.info(f"User {username} does not exist. Proceeding to create user.")

        # Create the user
        logging.info(f"Creating user {username}.")
        subprocess.run(['sudo', 'adduser', '--disabled-password', '--gecos', '', username], check=True)
        logging.info(f"User {username} created successfully.")

        # Set the password
        logging.info(f"Setting password for user {username}.")
        logging.info(f"Password being set: {password}")  # Log the password
        subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{password}".encode(), check=True)
        logging.info(f"Password for user {username} set successfully.")

        # Create directory and set permissions in /home/<username>
        user_file_dir = f"/home/{username}"
        os.makedirs(user_file_dir, exist_ok=True)
        default_file_name = f"default_{size_kb}KB.{file_type}"
        default_file_path = os.path.join(user_file_dir, default_file_name)
        create_random_file(default_file_path, size_kb)

        # Set correct permissions for the user directory and file
        subprocess.run(['sudo', 'chown', '-R', f"{username}:{username}", user_file_dir], check=True)
        subprocess.run(['sudo', 'chmod', '750', user_file_dir], check=True)  # Directory permissions
        subprocess.run(['sudo', 'chmod', '640', default_file_path], check=True)  # File permissions
        logging.info(f"Permissions set for directory and file in /home/{username}.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error creating user or default test file: {e}")


def log_client_commands(username, password):
    """Log the commands for client FTP and FTPS traffic based on input parameters."""
    logging.info("FTP and FTPS are configured to listen on the following ports:")
    logging.info("FTP: Port 21")
    logging.info("FTPS: Port 990")

    # Construct the curl command dynamically using the provided username and password
    curl_command = f"curl --ftp-ssl -u {username}:{password} ftp://<server-ip>:990/default_1KB.txt -k -v -o default_1KB.txt"
    logging.info("To download a file using curl with FTPS, use:")
    logging.info(curl_command)


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description='Install and configure vsftpd for FTP and FTPS.')
    parser.add_argument('--cert', default='/etc/ssl/certs/vsftpd.pem', help='Path to SSL certificate file')
    parser.add_argument('--key', default='/etc/ssl/private/vsftpd.key', help='Path to SSL private key file')
    parser.add_argument('--user', default='ftpuser', help='FTP username')
    parser.add_argument('--password', default='password', help='FTP user password')
    parser.add_argument('--stop', action='store_true', help='Stop the vsftpd service')
    parser.add_argument('--restart', action='store_true', help='Restart the vsftpd service')
    parser.add_argument('--status', action='store_true', help='Check the status of the vsftpd service')
    parser.add_argument('--check-port', action='store_true', help='Check if vsftpd is listening on port 990')
    parser.add_argument('--file-type', default='txt', help='File type for the default test file')
    parser.add_argument('--size', type=int, default=1, help='File size in KB for the default test file')
    args = parser.parse_args()

    if args.stop:
        stop_vsftpd()
    elif args.restart:
        restart_vsftpd()
    elif args.status:
        check_status_vsftpd()
    elif args.check_port:
        check_port_listening(990)
    else:
        install_vsftpd()
        generate_ssl_cert(args.cert, args.key)
        configure_vsftpd(args.cert, args.key)
        ensure_log_file_exists()
        restart_vsftpd()
        create_ftp_user(args.user, args.password, args.file_type, args.size)
        log_client_commands(args.user, args.password)


if __name__ == "__main__":
    main()