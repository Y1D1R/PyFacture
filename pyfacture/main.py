import os
from ocr.ocr_processor import extract_ticket_data
from ocr.ollama_ocr import perform_ocr
from excel.excel_manager import update_excel
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text


# Initialize Rich Console
console = Console()


# File path
INPUT_IMAGE_PATH = "pyfacture/data/input/ticket1.jpg"
OUTPUT_EXCEL_PATH = "pyfacture/data/output/expenses.xlsx"


def show_menu():
    
    console.print(Panel(Text("PyFacture", justify="center", style="bold blue"), expand=True))

    # Menu Options
    console.print("")
    console.print("[1] OCR using Tesseract", style="green", justify="center")
    console.print("[2] OCR using LLM", style="green", justify="center")
    console.print("[3] Exit", style="red", justify="center")
    
    console.print("")

    # Get User Choice
    choice = Prompt.ask("[bold magenta]Enter your choice[/bold magenta]", choices=["1", "2", "3"])
    return choice



def main():
    while True:
        user_choice = show_menu()

        if user_choice == "1":
            console.print("[bold green]You selected: OCR using Tesseract[/bold green]")
            ticket_data = extract_ticket_data(INPUT_IMAGE_PATH)
            print(f"Data : {ticket_data}")

            update_excel(OUTPUT_EXCEL_PATH, ticket_data)
            print(f"Data saved in : {OUTPUT_EXCEL_PATH}")
        elif user_choice == "2":
            console.print("[bold green]You selected: OCR using LLM[/bold green]")
            result = perform_ocr(INPUT_IMAGE_PATH)
            if result:
                print("OCR using Llama 3.2-Vision Recognition Result:")
                print(result)
            break
        elif user_choice == "3":
            console.print("[bold red]Exiting... Goodbye![/bold red]")
            break
    

if __name__ == "__main__":
    main()
