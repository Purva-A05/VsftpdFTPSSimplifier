# VsftpdFTPSSimplifier 🛠️

![VsftpdFTPSSimplifier](https://img.shields.io/badge/VsftpdFTPSSimplifier-Python-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

Welcome to **VsftpdFTPSSimplifier**! This project provides a Python-based tool that simplifies the installation, configuration, and management of the vsftpd service for secure FTPS. With this tool, you can automate essential tasks such as SSL certificate generation, FTP user creation, and service management. Our goal is to make it easier for you to set up and maintain a secure FTP server.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Managing Users](#managing-users)
- [SSL Certificate Generation](#ssl-certificate-generation)
- [Service Management](#service-management)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features 🌟

- **Easy Installation**: Quickly set up the vsftpd service with a few commands.
- **Automated Configuration**: Generate configuration files tailored to your needs.
- **User Management**: Create and manage FTP users effortlessly.
- **SSL Support**: Automatically generate SSL certificates for secure connections.
- **Service Management**: Start, stop, and restart the vsftpd service with simple commands.
- **Comprehensive Documentation**: Detailed guides to help you through every step.

## Installation 🛠️

To get started with **VsftpdFTPSSimplifier**, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Purva-A05/VsftpdFTPSSimplifier.git
   cd VsftpdFTPSSimplifier
   ```

2. **Install Required Packages**:
   Ensure you have Python installed. Then, install the necessary packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Latest Release**:
   You can find the latest release [here](https://github.com/Purva-A05/VsftpdFTPSSimplifier/releases). Download the file and execute it to set up the tool.

## Usage 📚

After installation, you can start using **VsftpdFTPSSimplifier**. The main command to run the tool is:
```bash
python vsftpd_simplifier.py
```

This command will launch the interactive interface where you can choose various options for setting up your FTP server.

## Configuration ⚙️

### Basic Configuration

Upon running the tool, you will be prompted to enter basic configuration details such as:

- **Server IP Address**: Enter the IP address of your server.
- **FTP Port**: Default is 21, but you can specify a different port if needed.
- **Passive Mode Ports**: Define the range of ports for passive mode.

### Advanced Configuration

For advanced users, you can manually edit the `vsftpd.conf` file located in the `/etc/vsftpd/` directory. The tool provides templates for common configurations.

## Managing Users 👥

### Adding Users

To add a new FTP user, you can use the command:
```bash
python vsftpd_simplifier.py add_user
```
You will be prompted to enter the username and password.

### Removing Users

To remove an existing user, use:
```bash
python vsftpd_simplifier.py remove_user
```
Enter the username of the user you wish to remove.

## SSL Certificate Generation 🔒

To ensure secure connections, you need SSL certificates. **VsftpdFTPSSimplifier** can generate these for you. Use the command:
```bash
python vsftpd_simplifier.py generate_ssl
```
Follow the prompts to create your SSL certificates.

## Service Management 🔄

### Starting the Service

To start the vsftpd service, use:
```bash
sudo systemctl start vsftpd
```

### Stopping the Service

To stop the service, run:
```bash
sudo systemctl stop vsftpd
```

### Restarting the Service

If you make changes to the configuration, restart the service with:
```bash
sudo systemctl restart vsftpd
```

## Contributing 🤝

We welcome contributions to improve **VsftpdFTPSSimplifier**. Here’s how you can help:

1. **Fork the Repository**: Click on the fork button in the top right corner.
2. **Create a New Branch**: Use a descriptive name for your branch.
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add a new feature"
   ```
5. **Push to Your Branch**:
   ```bash
   git push origin feature/YourFeature
   ```
6. **Open a Pull Request**: Go to the original repository and click on "New Pull Request".

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact 📧

For questions or feedback, feel free to reach out:

- **Email**: your-email@example.com
- **GitHub**: [Purva-A05](https://github.com/Purva-A05)

For more details, visit the [Releases section](https://github.com/Purva-A05/VsftpdFTPSSimplifier/releases) to find the latest updates and download the latest version of the tool.

---

Thank you for using **VsftpdFTPSSimplifier**! We hope this tool makes your FTP server management easier and more secure.