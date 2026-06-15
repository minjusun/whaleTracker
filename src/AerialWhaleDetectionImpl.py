from ultralytics import YOLO

'''
model=YOLO  ('yolov8n.pt')  # load a pretrained model (recommended for training)

#results=model("test_whale.jpg")
#results[0].show()

model.train(
    data='data.yaml',  # path to dataset
    epochs=10,  # number of epochs to train for (how many time it looks at the image. too many can cause overfitting)
    imgsz=640,  # size of images
    batch=8,  # batch size (how many images it looks at at once before moving on to next batch with corrected model)
)
'''

#Results
"""
mAP50: 0.966   ← 96.6% accuracy (finds whale correctly)
P:     0.935   ← Precision (gets it right that its a whale)
R:     0.924   ← Recall (finds all the whales in the image)

saved in: runs/detect/train/weights/best.pt
"""

#Test on real image
model=YOLO  ('runs/detect/train/weights/best.pt')  # load the trained model
results=model("aerialwhaleimg.jpg", conf=0.1)  # test on a real image
results[0].show()  # show the results
