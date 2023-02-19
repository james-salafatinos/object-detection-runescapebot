from ultralytics import YOLO
import time
from PIL import ImageGrab
import pyautogui
import sys

cls = ["rune_pickaxe"]


def load_model(mp=r"C:\Users\james\OneDrive\Desktop\repos\rsbot2\best.pt"):
    # Load a model
    model = YOLO(mp)
    return model


def parse_results(result, game_window):
    r = result[0]
    res = r.boxes

    print("Number of objects detected: ", len(res))
    print("Game window: ", game_window)

    if len(res) > 0:
        print("boxes array", res.xywh)
        print("cls array", res.cls)
        print("conf array", res.conf)

        x = res.xywh[0][0] + game_window[0]
        y = res.xywh[0][1] + game_window[1]
        pyautogui.moveTo(x, y)

    return {}

    # for result in results_list:
    #     detected_class = result.boxes.cls
    #     num_detected_objects_of_class = result.Size[0]


def main():
    model = load_model()

    for i in range(100):
        game_window = check_runelite_window()

        # mpos top left of runelite
        # (left, top, left+width, top+height) 3083, 97, 3083+1250, 97+1080 ([l, t, l+w, t+h])
        img = ImageGrab.grab([game_window[0], game_window[1], game_window[0] +
                             game_window[2], game_window[1] + game_window[3]])

        # predict on an image
        # list of Results obejecst
        results = model.predict(img, show=True, conf=0.01)

        parse_results(results, game_window)
        # print("results", results)
        # if results[0] is not None:
        #     print(results[0].boxes)
        #     tensor = results[0]
        #     print(tensor.boxes.xywh)
        #     x = tensor.boxes.xywh[0][0] + 3083
        #     y = tensor.boxes.xywh[0][1] + 97
        #     pyautogui.moveTo(x, y)
        #     print(cls[int(tensor.boxes.cls[0])])

        time.sleep(1.5)


def check_runelite_window():
    if len(pyautogui.getWindowsWithTitle("Rune")) == 0:
        print("RuneLite is not open")
        exit()
    else:
        rl = pyautogui.getWindowsWithTitle("Rune")[0]
        pyautogui.getWindowsWithTitle("Rune")[0].restore()
        print("RuneLite is open at ", rl)
        return [rl.left, rl.top, rl.width, rl.height]


# success = model.export(format="onnx")  # export the model to ONNX format
if __name__ == '__main__':
    # freeze_support() here if program needs to be frozen
    main()  # execute this only when run directly, not when imported!
