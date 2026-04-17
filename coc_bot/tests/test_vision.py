import unittest
import cv2
import numpy as np
import os
from bot.vision import Vision

class TestVision(unittest.TestCase):
    def setUp(self):
        self.vision = Vision()
        self.test_img_path = "test_screenshot.png"
        self.test_template_path = "test_template.png"
        
        # Create dummy images with enough variance
        np.random.seed(42)
        # 300x300 image with random noise
        img = np.random.randint(0, 100, (300, 300, 3), dtype=np.uint8)
        
        # Template at (150, 150)
        template = np.random.randint(10, 90, (30, 30, 3), dtype=np.uint8)
        img[150:180, 150:180] = template
        
        cv2.imwrite(self.test_img_path, img)
        cv2.imwrite(self.test_template_path, template)

    def tearDown(self):
        if os.path.exists(self.test_img_path):
            os.remove(self.test_img_path)
        if os.path.exists(self.test_template_path):
            os.remove(self.test_template_path)

    def test_find_template(self):
        result = self.vision.find_template(self.test_img_path, self.test_template_path)
        self.assertIsNotNone(result)
        self.assertEqual(result, (165, 165))

    def test_find_template_not_found(self):
        wrong_template_path = "wrong_template.png"
        # Template that is random noise, different from what's in the image
        wrong_template = np.random.randint(100, 200, (30, 30, 3), dtype=np.uint8)
        cv2.imwrite(wrong_template_path, wrong_template)
        
        result = self.vision.find_template(self.test_img_path, wrong_template_path, threshold=0.8)
        self.assertIsNone(result)
        
        os.remove(wrong_template_path)

if __name__ == '__main__':
    unittest.main()
