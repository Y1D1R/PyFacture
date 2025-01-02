import cv2
import pytesseract
from matplotlib import pyplot as plt
import os
import re
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

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
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold
    processed_image = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 3)
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
    Analyzes the extracted ticket text to extract product information, total amount, and date.
    
    Parameters:
        text (str): Text extracted from the image via OCR.
    
    Returns:
        dict: A dictionary containing a list of products, the total amount, and the date.
    """
    # Split the text into individual lines
    lines = text.split("\n")
    
    # Initialize the data dictionary
    data = {"products": [], "total": 0.0, "date": ""}
    
    # Define regular expressions for matching patterns
    regex_date = re.compile(r'(\d{2}[\/\-]\d{2}[\/\-]\d{4})')  # Matches dates like 12/12/2023 or 12-12-2023
    regex_price = re.compile(r'([\d\s.,]+)€')  # Matches prices like 0,88€ or 0.88€
    regex_product = re.compile(r'^(\d+)\s+([A-Za-zÀ-ÿ\s\.\-]+)')  # Matches lines starting with quantity and product name
    
    # Variables to keep track of the last product without price
    last_product = None
    
    # Lists to keep track of product prices and other prices (potential totals)
    product_prices = []
    other_prices = []
    
    # Iterate through each line to extract information
    for i, line in enumerate(lines):
        line = line.strip()  # Remove leading and trailing whitespace
        if not line:
            continue  # Skip empty lines
        
        # Attempt to extract the date
        if not data["date"]:
            match_date = regex_date.search(line)
            if match_date:
                data["date"] = match_date.group(1)
                print(f"Date extracted: {data['date']}")
                continue  # Move to the next line after extracting date
        
        # Attempt to extract a product
        match_product = regex_product.match(line)
        if match_product:
            quantity = int(match_product.group(1))
            product_name = match_product.group(2).strip()
            # Initialize product dictionary
            product = {"name": f"{quantity} {product_name}", "price": 0.0}
            
            # Try to find price in the same line
            price_match = regex_price.search(line)
            if price_match:
                price_str = price_match.group(1).replace(" ", "").replace(",", ".")
                try:
                    price = float(price_str)
                    product["price"] = price
                    data["products"].append(product)
                    product_prices.append(price)
                    print(f"Product extracted: {product['name']} - {price}€")
                except ValueError:
                    print(f"Unable to convert price '{price_str}' to float for product '{product['name']}'.")
            else:
                # If price not found in the same line, check the next line
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    price_match = regex_price.match(next_line)
                    if price_match:
                        price_str = price_match.group(1).replace(" ", "").replace(",", ".")
                        try:
                            price = float(price_str)
                            product["price"] = price
                            data["products"].append(product)
                            product_prices.append(price)
                            print(f"Product extracted: {product['name']} - {price}€")
                            # Skip the next line as it has been processed
                            continue
                        except ValueError:
                            print(f"Unable to convert price '{price_str}' to float for product '{product['name']}'.")
            # If price still not found, keep track to assign it later
            if product["price"] == 0.0:
                last_product = product
        
        # If the line is not a product, check if it is a price for the last product
        elif last_product:
            price_match = regex_price.match(line)
            if price_match:
                price_str = price_match.group(1).replace(" ", "").replace(",", ".")
                try:
                    price = float(price_str)
                    last_product["price"] = price
                    data["products"].append(last_product)
                    product_prices.append(price)
                    print(f"Product updated with price: {last_product['name']} - {price}€")
                    last_product = None  # Reset after assigning the price
                except ValueError:
                    print(f"Unable to convert price '{price_str}' to float for product '{last_product['name']}'.")
            else:
                # If not a price, reset last_product
                last_product = None
        
        # Attempt to extract other prices (potential total)
        else:
            # Find all price matches in the line
            price_matches = regex_price.findall(line)
            for price_str in price_matches:
                clean_price_str = price_str.replace(" ", "").replace(",", ".")
                try:
                    price = float(clean_price_str)
                    other_prices.append(price)
                    print(f"Other price extracted: {price}€")
                except ValueError:
                    print(f"Unable to convert price '{price_str}' to float.")
    
    # Assign total as the last price in other_prices if any
    if other_prices:
        data["total"] = other_prices[-1]
        print(f"Total assigned: {data['total']}€")
    elif product_prices:
        # If no other prices, assign total as the sum of product prices
        data["total"] = sum(product_prices)
        print(f"Total assigned as sum of product prices: {data['total']}€")
    
    # If no date was found, assign the current date
    if not data["date"]:
        current_date = datetime.now().strftime("%d/%m/%Y")
        data["date"] = current_date
        print(f"No date found. Assigned current date: {data['date']}")
    
    return data
