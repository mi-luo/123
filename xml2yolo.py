import os
import xml.etree.ElementTree as ET
from tqdm import tqdm

# 加载类别信息
class_info = {
    "golffield": 0,
    "vehicle": 1,
    "Expressway_toll_station": 2,
    "trainstation": 3,
    "chimney": 4,
    "storagetank": 5,
    "ship": 6,
    "harbor": 7,
    "airplane": 8,
    "tenniscourt": 9,
    "groundtrackfield": 10,
    "dam": 11,
    "basketballcourt": 12,
    "Expressway_Service_area": 13,
    "stadium": 14,
    "airport": 15,
    "baseballfield": 16,
    "bridge": 17,
    "windmill": 18,
    "overpass": 19
}

def convert_dior_to_yolo_rotated(xml_folder, output_folder):
    """
    Convert DIOR-R XML labels to YOLO format with rotation.
    :param xml_folder: The folder containing XML files.
    :param output_folder: The folder to save YOLO formatted labels.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get all XML files in the folder
    xml_files = [f for f in os.listdir(xml_folder) if f.endswith('.xml')]
    
    for xml_file in tqdm(xml_files, desc="Converting XML to YOLO format"):
        # Parse the XML file
        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()
        
        # Get image size
        size = root.find('size')
        img_width = int(size.find('width').text)
        img_height = int(size.find('height').text)
        
        # Open a corresponding YOLO label file
        yolo_label_path = os.path.join(output_folder, os.path.splitext(xml_file)[0] + '.txt')
        with open(yolo_label_path, 'w') as yolo_label_file:
            for obj in root.findall('object'):
                # Extract object information
                name_element = obj.find('name')
                if name_element is not None:
                    name = name_element.text
                    class_id = class_info.get(name)
                    
                    if class_id is not None:
                        bndbox = obj.find('robndbox')
                        
                        if bndbox is not None:
                            x_left_top = float(bndbox.find('x_left_top').text)
                            y_left_top = float(bndbox.find('y_left_top').text)
                            x_right_bottom = float(bndbox.find('x_right_bottom').text)
                            y_right_bottom = float(bndbox.find('y_right_bottom').text)
                            angle = float(obj.find('angle').text)
                            
                            # Calculate center coordinates, width, and height
                            cx = (x_left_top + x_right_bottom) / 2.0 / img_width
                            cy = (y_left_top + y_right_bottom) / 2.0 / img_height
                            w = abs(x_right_bottom - x_left_top) / img_width
                            h = abs(y_right_bottom - y_left_top) / img_height
                            
                            # Convert to YOLO format (class, cx, cy, w, h, angle)
                            yolo_label_file.write(f"{class_id} {cx} {cy} {w} {h} {angle}\n")
    
    print("Conversion completed successfully!")

if __name__ == "__main__":

    # Folder containing the XML files
    xml_folder = "/data/wangzerui/Code_yolo/ultralytics-8.2.52/datasets/DIOR-R/DIOPR-R-Completed/DIOR/Annotations/Oriented Bounding Boxes"
    # Folder to save YOLO formatted labels
    output_folder = "/data/wangzerui/Code_yolo/ultralytics-8.2.52/datasets/DIOR-R/DIOPR-R-Completed/DIOR/Annotations/xml2yolo"
    
    convert_dior_to_yolo_rotated(xml_folder, output_folder)
