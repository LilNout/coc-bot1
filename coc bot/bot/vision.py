import cv2
import numpy as np

class Vision:
    def __init__(self):
        pass

    def find_template(self, screenshot_path, template_path, threshold=0.8):
        img_rgb = cv2.imread(screenshot_path)
        if img_rgb is None: return None
            
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template_img = cv2.imread(template_path)
        if template_img is None: return None
        template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
            
        w, h = template_gray.shape[::-1]

        res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val >= threshold:
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            return (int(center_x), int(center_y))
        
        return None

    def find_all_templates(self, screenshot_path, template_path, threshold=0.8):
        img_rgb = cv2.imread(screenshot_path)
        if img_rgb is None: return []
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template_img = cv2.imread(template_path)
        if template_img is None: return []
        template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
        w, h = template_gray.shape[::-1]

        res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        
        points = []
        for pt in zip(*loc[::-1]):
            points.append((int(pt[0] + w // 2), int(pt[1] + h // 2)))
            
        if not points:
            return []
            
        grouped_points = []
        if points:
            grouped_points.append(points[0])
            for p in points[1:]:
                is_far = True
                for gp in grouped_points:
                    dist = ((p[0]-gp[0])**2 + (p[1]-gp[1])**2)**0.5
                    if dist < 20:
                        is_far = False
                        break
                if is_far:
                    grouped_points.append(p)
                    
        return grouped_points
