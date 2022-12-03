import sys
from PIL import Image
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions


def show_image(image):
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'

    matrix = RGBMatrix(options=options)

    matrix.Clear()
    matrix.SetImage(image, 0, 0)

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)


def show_animation(file):
    options = RGBMatrixOptions()
    options.rows = 64
    options.cols = 64
    options.chain_length = 1
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'

    matrix = RGBMatrix(options=options)

    # For some weird reason gif files need to be passed to processes un-opened
    gif = Image.open(file)
    num_frames = gif.n_frames

    canvases = []
    for frame_index in range(0, num_frames):
        gif.seek(frame_index)
        frame = gif.copy()
        frame.thumbnail((64, 64))
        canvas = matrix.CreateFrameCanvas()
        canvas.SetImage(frame.convert("RGB"))
        canvases.append(canvas)
    gif.close()

    try:
        cur_frame = 0
        while (True):
            matrix.SwapOnVSync(canvases[cur_frame])
            if cur_frame == num_frames - 1:
                cur_frame = 0
            else:
                cur_frame += 1
    except KeyboardInterrupt:
        sys.exit(0)
