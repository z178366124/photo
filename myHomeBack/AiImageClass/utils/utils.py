from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # pretrained YOLOv8n model

# Run batched inference on a list of images
def predict_cls(path):
    ret = []
    results = model.predict(path)  # return a list of Results objects
    for t in results:
        for box in t.boxes:
            # print(box)
            x1, y1, x2, y2 = box.xyxy[0]
            # print(x1, y1,x2, y2)
            ret.append({"label": int(box.cls) + 1, "locationX1": float(x1), "locationY1": float(y1),
                        "locationX2": float(x2), "locationY2": float(y2)})
    return ret
# predict_cls("1.jpg")
# results = model.predict("1.jpg")
# Process results list
# for result in results:
#     boxes = result.boxes  # Boxes object for bounding box outputs
#     masks = result.masks  # Masks object for segmentation masks outputs
#     keypoints = result.keypoints  # Keypoints object for pose outputs
#     probs = result.probs  # Probs object for classification outputs
#     obb = result.obb  # Oriented boxes object for OBB outputs
#     # result.show()  # display to screen
#     result.save(filename="result.jpg")  # save to disk