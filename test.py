from ultralytics import YOLO


def main():
    # Load a model
    # model = YOLO("yolov8n.yaml")  # build a new model from scratch
    # load a pretrained model (recommended for training)
    model = YOLO("yolov8n.pt")

    # Use the model
    model.train(data="custom_training.yaml", epochs=100)  # train the model
    metrics = model.val()  # evaluate model performance on the validation set
    # predict on an image
    results = model(
        r"C:\Users\james\OneDrive\Desktop\repos\rsbot2\fb7ef358-image13.png")


    # success = model.export(format="onnx")  # export the model to ONNX format
if __name__ == '__main__':
    # freeze_support() here if program needs to be frozen
    main()  # execute this only when run directly, not when imported!
