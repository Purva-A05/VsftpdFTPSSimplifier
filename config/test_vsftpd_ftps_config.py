import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import logging

# Add the directory containing vsftpd_ftps_config.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import vsftpd_ftps_config

def setup_logging():
    """Set up logging configuration for tests."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

class TestVsftpdConfig(unittest.TestCase):
    test_results = []  # Class-level list to store test results

    @classmethod
    def tearDownClass(cls):
        print("\nSummary of Test Results:")
        print("{:<4} {:<30} {:<10}".format("No.", "Test Name", "Result"))
        print("-" * 50)
        for index, result in enumerate(cls.test_results, start=1):
            print("{:<4} {:<30} {:<10}".format(index, result['name'], result['result']))

    def setUp(self):
        self.test_number = len(self.test_results) + 1
        print(f"\nRunning Test {self.test_number}: {self._testMethodName}")

    def log_test_result(self, result):
        test_name = self._testMethodName
        self.test_results.append({'name': test_name, 'result': result})

    @patch('subprocess.run')
    def test_install_vsftpd(self, mock_subproc_run):
        try:
            vsftpd_ftps_config.install_vsftpd()
            mock_subproc_run.assert_any_call(['sudo', 'apt-get', 'update'], check=True)
            mock_subproc_run.assert_any_call(['sudo', 'apt-get', 'install', '-y', 'vsftpd'], check=True)
            self.log_test_result('PASS')
        except AssertionError:
            self.log_test_result('FAIL')

    @patch('subprocess.run')
    def test_generate_ssl_cert(self, mock_subproc_run):
        cert_path = '/etc/ssl/certs/vsftpd.pem'
        key_path = '/etc/ssl/private/vsftpd.key'
        try:
            vsftpd_ftps_config.generate_ssl_cert(cert_path, key_path)
            mock_subproc_run.assert_called_with([
                'openssl', 'req', '-newkey', 'rsa:2048', '-nodes', '-keyout', key_path,
                '-x509', '-days', '365', '-out', cert_path, '-subj', '/CN=localhost'
            ], check=True)
            self.log_test_result('PASS')
        except AssertionError:
            self.log_test_result('FAIL')

    @patch('builtins.open', new_callable=MagicMock)
    @patch('subprocess.run')
    def test_configure_vsftpd(self, mock_subproc_run, mock_open):
        cert_path = '/etc/ssl/certs/vsftpd.pem'
        key_path = '/etc/ssl/private/vsftpd.key'
        try:
            vsftpd_ftps_config.configure_vsftpd(cert_path, key_path)
            mock_subproc_run.assert_any_call(['sudo', 'cp', '/etc/vsftpd.conf', '/etc/vsftpd.conf.bak'])
            mock_open.assert_called_with('/etc/vsftpd.conf', 'w')
            self.log_test_result('PASS')
        except AssertionError:
            self.log_test_result('FAIL')

    @patch('subprocess.run')
    def test_restart_vsftpd(self, mock_subproc_run):
        try:
            vsftpd_ftps_config.restart_vsftpd()
            mock_subproc_run.assert_called_with(['sudo', 'service', 'vsftpd', 'restart'], check=True)
            self.log_test_result('PASS')
        except AssertionError:
            self.log_test_result('FAIL')

    @patch('subprocess.run')
    def test_check_port_listening(self, mock_subproc_run):
        mock_subproc_run.return_value.stdout = "tcp LISTEN 0 0 :::990 :::*"
        try:
            vsftpd_ftps_config.check_port_listening(990)
            mock_subproc_run.assert_called_with(['sudo', 'ss', '-tuln'], check=True, capture_output=True, text=True)
            self.log_test_result('PASS')
        except AssertionError:
            self.log_test_result('FAIL')

if __name__ == '__main__':
    setup_logging()
    unittest.main()