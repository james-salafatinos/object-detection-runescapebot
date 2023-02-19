from ultralytics import YOLO


def main():
    # Load a model

    model = YOLO(
        r"C:\Users\james\OneDrive\Desktop\repos\rsbot2\best.pt")

    # predict on an image
    results = model.predict(
        r"C:\Users\james\OneDrive\Desktop\repos\rsbot2\fb7ef358-image13.png", save=True, conf=0.01)
    print(results)

    # success = model.export(format="onnx")  # export the model to ONNX format
if __name__ == '__main__':
    # freeze_support() here if program needs to be frozen
    main()  # execute this only when run directly, not when imported!
