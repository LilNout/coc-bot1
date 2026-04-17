import time
import os
from .adb_client import ADBClient
from .vision import Vision

class GameBot:
    def __init__(self, device_id=None):
        self.adb = ADBClient(device_id)
        self.vision = Vision()
        self.templates_dir = "templates"
        
        if not os.path.exists(self.templates_dir):
            os.makedirs(self.templates_dir)

    def collect_resources(self):
        print("Attempting to collect resources...")
        screenshot = self.adb.take_screenshot("current_state.png")
        
        # In a real scenario, we'd have multiple templates for different resource types
        resource_templates = ["gold_collector.png", "elixir_collector.png", "dark_elixir_collector.png"]
        
        for template in resource_templates:
            template_path = os.path.join(self.templates_dir, template)
            if not os.path.exists(template_path):
                print(f"Template {template} not found, skipping.")
                continue
                
            locations = self.vision.find_all_templates(screenshot, template_path)
            for loc in locations:
                print(f"Found resource at {loc}, tapping...")
                self.adb.tap(loc[0], loc[1])
                time.sleep(0.5)

    def run(self):
        print("Bot started. Press Ctrl+C to stop.")
        try:
            while True:
                self.collect_resources()
                # Wait before next cycle
                print("Waiting for next cycle...")
                time.sleep(60) 
        except KeyboardInterrupt:
            print("Bot stopped.")
