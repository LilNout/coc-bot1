import unittest
from unittest.mock import patch, MagicMock
from bot.adb_client import ADBClient

class TestADBClient(unittest.TestCase):
    def setUp(self):
        self.client = ADBClient(device_id="test_device")

    @patch('subprocess.run')
    def test_run_command(self, mock_run):
        mock_run.return_value = MagicMock(stdout=b"success")
        result = self.client._run_command(["shell", "ls"])
        self.assertEqual(result, b"success")
        mock_run.assert_called_with(["adb", "-s", "test_device", "shell", "ls"], capture_output=True, check=True)

    @patch.object(ADBClient, '_run_command')
    def test_tap(self, mock_run_command):
        self.client.tap(100, 200)
        mock_run_command.assert_called_with(["shell", "input", "tap", "100", "200"])

    @patch.object(ADBClient, '_run_command')
    def test_swipe(self, mock_run_command):
        self.client.swipe(100, 200, 300, 400, 1000)
        mock_run_command.assert_called_with(["shell", "input", "swipe", "100", "200", "300", "400", "1000"])

if __name__ == '__main__':
    unittest.main()
