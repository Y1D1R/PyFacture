import cv2
import pytesseract
from matplotlib import pyplot as plt
import os

def extract_ticket_data(image_path):
    """
    Extracts ticket information from image
    
    param:
        image_path: path to image
        
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at : {image_path}")

    # Load theimage
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Error ")

    # Dsiplay the image
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
    plt.show()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold
    processed_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)
    plt.imshow(processed_image, cmap="gray")
    plt.show()
    
    # OCR
    text = pytesseract.image_to_string(processed_image, lang="fra")
    print("OCR : ", text)

    # extract data
    ticket_data = parse_ticket_text(text)
    return ticket_data

def parse_ticket_text(text):
    """
    Text analysis
    """
    lines = text.split("\n")
    data = {"products": [], "total": 0.0, "date": ""}

    for line in lines:
        line = line.strip()
        if "TOTAL" in line.upper():
            try:
                data["total"] = float(line.split()[-1].replace(",", "."))
            except ValueError:
                pass
        elif "DATE" in line.upper() or "/" in line:
 
            data["date"] = line
        elif len(line.split()) > 1:
            try:
                price = float(line.split()[-1].replace(",", "."))
                product = " ".join(line.split()[:-1])
                data["products"].append({"name": product, "price": price})
            except ValueError:
                pass

    return data
