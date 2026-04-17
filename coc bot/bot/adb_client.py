import subprocess
import os

class ADBClient:
    def __init__(self, device_id=None):
        self.device_id = device_id
        self.adb_path = "adb"

    def _run_command(self, command):
        base_cmd = [self.adb_path]
        if self.device_id:
            base_cmd.extend(["-s", self.device_id])
        
        full_cmd = base_cmd + command
        try:
            result = subprocess.run(full_cmd, capture_output=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error running adb command: {e}")
            print(f"Stderr: {e.stderr}")
            return None

    def take_screenshot(self, filename="screenshot.png"):
        # Take screenshot on device
        self._run_command(["shell", "screencap", "-p", "/sdcard/screenshot.png"])
        # Pull to host
        self._run_command(["pull", "/sdcard/screenshot.png", filename])
        return filename

    def tap(self, x, y):
        self._run_command(["shell", "input", "tap", str(x), str(y)])

    def swipe(self, x1, y1, x2, y2, duration=500):
        self._run_command(["shell", "input", "swipe", str(x1), str(y1), str(x2), str(y2), str(duration)])

    def get_devices(self):
        output = subprocess.run([self.adb_path, "devices"], capture_output=True, text=True).stdout
        lines = output.strip().split("\n")[1:]
        devices = [line.split("\t")[0] for line in lines if line.strip()]
        return devices
