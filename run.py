import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
 
if __name__ == '__main__':

    model = YOLO('/data/wangzerui/Code_yolo/ultralytics-8.2.52/ultralytics/cfg/models/v8/yolov8n.yaml').load("yolov8n.pt") # 好像是加载预训练

    
    
    # model.load('yolov8n.pt') # loading pretrain weights
    model.train(
                data=r'/data/wangzerui/Code_yolo/ultralytics-8.2.52/ultralytics/cfg/datasets/DIOR.yaml',
                # data=r"/data/wangzerui/Code_yolo/ultralytics-8.2.52/ultralytics/cfg/datasets/DOTA1.0_hbb.yaml",
                # data=r"/data/wangzerui/Code_yolo/ultralytics-8.2.52/ultralytics/cfg/datasets/NWPU VHR-10.yaml",
                # 如果大家任务是其它的'ultralytics/cfg/default.yaml'找到这里修改task可以改成detect, segment, classify, pose
                cache=False,
                patience = 250,
                imgsz=640,
                epochs=250,
                single_cls=False,  # 是否是单类别检测
                batch=32,
                close_mosaic=10,
                workers=0,
                device= [1],
                optimizer='SGD', # using SGD
                # resume='', # 如过想续训就设置last.pt的地址
                amp=False,  # 如果出现训练损失为Nan可以关闭amp
                project='/data/wangzerui/paper2_result',
                name='exp',
                )


