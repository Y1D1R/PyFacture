import moondream as md
from PIL import Image

model = md.vl(model="pyfacture/ocr/moondream-2b-int8.mf")

def moondream_ocr(image_path):
    SYSTEM_PROMPT = """Act as an OCR assistant for PyFacture. Analyze the provided receipt image and Recognize all visible text in the receipt as accurately as possible."""
    

    image = Image.open(image_path)
    encoded_image = model.encode_image(image)
    caption = model.caption(encoded_image)["caption"]
    answer = model.query(encoded_image, SYSTEM_PROMPT)["answer"]
    return caption, answer
