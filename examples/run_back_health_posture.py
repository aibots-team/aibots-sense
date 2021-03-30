import cv2
import os
import json
import numpy as np
import time
import ctypes

from sense.controller import Controller

global_timer = time.perf_counter()
local_timer = 0


class MyController(Controller):

    def display_prediction(self, img: np.ndarray, prediction_postprocessed: dict):
        super().display_prediction(img, prediction_postprocessed)

        global global_timer
        global local_timer
        local_timer = time.perf_counter()
        print(local_timer, global_timer, global_timer + 60)
        if local_timer > global_timer + 10:
            prediction, prob = prediction_postprocessed['sorted_predictions'][0]
            print(prediction, prob)
            if 'unhealthy' in prediction:
                os.system("notify-send 'Warning!' 'Time to straighten your back!' -t 5000")
                os.system("zenity --error --text='Time to straighten your back!' --title='Warning!'")
            global_timer = time.perf_counter()
