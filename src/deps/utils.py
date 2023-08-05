import PyPDF2


def read_pdf(file_path):
    """
    read_pdf is a function that reads a pdf file and returns the text
    """
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text = ""

        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text += page.extract_text()

        return text
