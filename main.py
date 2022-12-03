from multiprocessing import Process
from render import show_animation, show_image
from fastapi import File, UploadFile, FastAPI, Response, HTTPException
from PIL import Image

app = FastAPI()
matrix_process: Process = None


@app.post("/image")
async def image(file: UploadFile = File()):
    contents = file.file
    im = Image.open(contents)
    im.thumbnail((64, 64))
    im = im.convert('RGB')

    # im.save(file.filename)

    global matrix_process
    if matrix_process is not None:
        matrix_process.kill()
    matrix_process = Process(target=show_image, args=(im, ))
    matrix_process.start()

    return {
        "fileb_content_type": file.content_type,
    }


@app.post("/animation")
async def animation(file: UploadFile = File()):

    contents = file.file
    # gif = Image.open(contents)

    # try:
    #     num_frames = gif.n_frames
    #     print(num_frames)
    # except Exception:
    #     raise HTTPException(status_code=403, detail="Image is not a gif")

    # gif.save(file.filename)

    global matrix_process
    if matrix_process is not None:
        matrix_process.kill()
    # matrix_process = Process(target=show_animation, args=(gif, ))
    matrix_process = Process(target=show_animation, args=(contents, ))
    matrix_process.start()

    return {
        "fileb_content_type": file.content_type,
    }
