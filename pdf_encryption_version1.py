#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PySimpleGUI as sg
from PyPDF2 import PdfWriter, PdfReader
import os

def encrypt_pdf(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through PDF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            # Open the PDF file
            pdf_file = PdfReader(open(input_file_path, "rb"))

            # Create a PdfFileWriter object
            pdf_writer = PdfWriter()

            # Add pages from the original PDF
            for page_num in range(len(pdf_file.pages)):
                page = pdf_file.pages[page_num]
                pdf_writer.add_page(page)

            # Set the encryption options, restricting print functionality
            pdf_writer.encrypt("", "", use_128bit=True, permissions_flag=3)

            # Save the encrypted PDF
            with open(output_file_path, "wb") as output_file:
                pdf_writer.write(output_file)

layout = [
    [sg.Text("Select input folder containing PDF files:")],
    [sg.InputText(key="input_folder"), sg.FolderBrowse()],
    [sg.Text("Select output folder to save encrypted PDF files:")],
    [sg.InputText(key="output_folder"), sg.FolderBrowse()],
    [sg.Button("Encrypt"), sg.Button("Exit")]
]

window = sg.Window("PDF Encryption Tool", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Encrypt":
        input_folder = values["input_folder"]
        output_folder = values["output_folder"]
        encrypt_pdf(input_folder, output_folder)
        sg.popup("Encryption completed!", title="Success")

window.close()


# In[ ]:




