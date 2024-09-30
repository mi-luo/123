from ultralytics.data.converter import convert_dota_to_yolo_obb
"""
    说明:
    假定的DOTA数据集目录结构：

    ├── DOTA
    │   ├── images
    │   │   ├── train
    │   │   └── val
    │   └── labels
    │       ├── train_original
    │       └── val_original

    执行后，该函数将标签组织到：

    ├── DOTA
    │   ├── labels
    │       ├── train
    │       └── val


"""



convert_dota_to_yolo_obb('/data/wangzerui/Code_yolo/ultralytics-8.2.52/datasets/DIOR-dota/') # DOTA标签格式的数据集的根目录路径
print("finish!!")
#关于dataobb文件下的目录可参考https://blog.csdn.net/qq_41301570/article/details/135540398
