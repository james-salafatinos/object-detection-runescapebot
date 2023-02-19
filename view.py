from ultralytics import YOLO


def main():
    # Load a model

    model = YOLO(
        r"C:\Users\james\OneDrive\Desktop\repos\rsbot2\best.pt")

    predict(model)


def predict(model):

    # predict on an image
    results = model.predict(
        source="screen 0 3083 97 1250 1080", show=True, conf=0.01)
    return results

    # success = model.export(format="onnx")  # export the model to ONNX format
if __name__ == '__main__':
    # freeze_support() here if program needs to be frozen
    main()  # execute this only when run directly, not when imported!
