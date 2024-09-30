import os
import shutil
from tqdm import tqdm

def copy_and_rename_files(src_dir, dest_dir, start_index, end_index):
    # 获取源文件夹中的所有文件，并按名称排序
    files = sorted([f for f in os.listdir(src_dir) if f.endswith('.jpg')]) # ----------.txt .jpg 可更换 处理不同顺序的文件例如：0001.txt 或者0001.jpg----------

    # 确保目标文件夹存在
    os.makedirs(dest_dir, exist_ok=True)

    # 复制并重命名指定范围内的文件
    for i, file_name in enumerate(tqdm(files[start_index-1:end_index], desc="Copying files", unit="file")):
        src_file = os.path.join(src_dir, file_name)
        dest_file = os.path.join(dest_dir, f"{start_index + i:05d}.jpg")  #   ------- .txt .jpg 可更换 处理不同顺序的文件例如：0001.txt 或者0001.jpg   注：05d的作用！！---------
        
        print("++++",start_index,f"{start_index + i:05d}.jpg") # -----检查复制的具体情况-----

        shutil.copy(src_file, dest_file) 

if __name__ == "__main__":
    src_directory = '/data/wangzerui/Code_yolo/ultralytics-8.2.52/datasets/DIOR-R/raw/DIOR/JPEGImages-trainval/'  # ----------替换为实际的源文件夹路径---------
    dest_directory = '/data/wangzerui/Code_yolo/ultralytics-8.2.52/datasets/DIOR-dota/iamges/val/'  # ----------替换为实际的目标文件夹路径-----------
    copy_and_rename_files(src_directory, dest_directory, start_index=5863, end_index=11725) # -----------处理文件的范围设定 [start_index: end_index]----------


# import os
# import shutil
# from tqdm import tqdm

# def rename_files_in_sequence(src_dir, dest_dir):
#     # 获取源文件夹中的所有.txt文件，并按名称排序
#     files = sorted([f for f in os.listdir(src_dir) if f.endswith('.txt')])

#     # 确保目标文件夹存在
#     os.makedirs(dest_dir, exist_ok=True)

#     # 复制并重命名所有文件
#     for i, file_name in enumerate(tqdm(files, desc="Renaming files", unit="file")):
#         src_file = os.path.join(src_dir, file_name)
#         dest_file = os.path.join(dest_dir, f"{i+1:05d}.txt")
#         shutil.copy(src_file, dest_file)

# if __name__ == "__main__":
#     src_directory = '/data/wangzerui/Code_yolo/ultralytics-8.2.52/datasets/DIOR-dota/labels/train_original/'  # 替换为实际的源文件夹路径
#     dest_directory = '/data/wangzerui/Code_yolo/ultralytics-8.2.52/datasets/DIOR-dota/labels/train_original111/'  # 替换为实际的目标文件夹路径
#     rename_files_in_sequence(src_directory, dest_directory)
