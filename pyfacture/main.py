import os
from ocr.ocr_processor import extract_ticket_data
from excel.excel_manager import update_excel

# File path
INPUT_IMAGE_PATH = "pyfacture/data/input/ticket1.jpg"
OUTPUT_EXCEL_PATH = "pyfacture/data/output/expenses.xlsx"

def main():
    ticket_data = extract_ticket_data(INPUT_IMAGE_PATH)
    print(f"Data : {ticket_data}")

    update_excel(OUTPUT_EXCEL_PATH, ticket_data)
    print(f"Data saved in : {OUTPUT_EXCEL_PATH}")

if __name__ == "__main__":
    main()
