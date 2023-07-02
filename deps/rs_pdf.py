import PyPDF2


def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ""

        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()

        return text


# Usage example
pdf_file = "download.pdf"
extracted_text = read_pdf(pdf_file)
# print(extracted_text)
