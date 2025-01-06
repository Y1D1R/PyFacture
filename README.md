# PyFacture

PyFacture is a Python project designed to automate expense management from receipts. The application utilizes image processing techniques and Optical Character Recognition (OCR) to extract relevant information from a photo of a receipt, such as purchased products, their prices, and the date of purchase.

## Features

- **Image Processing:** Enhances receipt images for better OCR accuracy.
- **Optical Character Recognition (OCR):** Extracts text from receipt images using Tesseract.
- **Data Extraction:** Analyzes OCR text to identify products, prices, and dates.
- **Excel File Management:** Creates and updates Excel files to store extracted data.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Y1D1R/PyFacture.git
cd PyFacture
```

### 2. Install Dependencies
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR and Ollama
PyFacture relies on Tesseract OCR for text extraction.<br>
Follow the instructions below based on your operating system.

Once you have Ollama installed, install the Llama 3.2-Vision model(6 GB):<br>
```bash
ollama run llama3.2-vision
```
More information here : https://sebastian-petrus.medium.com/build-a-local-ollama-ocr-application-using-llama-3-2-vision-bfc3014e3ad6  

### 4. Usage
#### 4.1. Prepare Your Data
Place your receipt images in the "data/input/" directory.<br> 
Ensure that the images are clear, well-lit, and free from distortions for optimal OCR results.


#### 4.2. Run the Application
Execute the main script, then choose the method from the menu to process the receipts and extract data:

```bash
python pyfacture/main.py
```
<img src="pyfacture/img/Figure_4.png" alt="Menu" width="900">


#### 4.3. View the Results
##### 4.3.1 Tesseract OCR
<img src="pyfacture/img/Figure_1.png" alt="Original Receipt" width="400">
<img src="pyfacture/img/Figure_2.png" alt="Thresholded Receipt" width="400">
The extracted data will be saved as Excel files in the "data/output/" directory. 
<img src="pyfacture/img/Figure_3.png" alt="OCR Result" width="700">

##### 4.3.1 Llama OCR
<img src="pyfacture/img/Figure_5.png" alt="Llam OCR" width="300">
