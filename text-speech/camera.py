import pyvirtualcam
import numpy as np

with pyvirtualcam.Camera(width=1280, height=720, fps=30) as cam:
    print("Virtual camera running:", cam.device)

    frame = np.zeros((720, 1280, 3), dtype=np.uint8)
    frame[:] = [0, 255, 0]

    while True:
        cam.send(frame)
        cam.sleep_until_next_frame()