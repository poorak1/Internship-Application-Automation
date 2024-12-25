import pdfkit

DIR ="PATH TO SAVE MODIFIED RESUMES"

def render_resume(input_html, output_name):
    path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    options = {
    'page-size': 'A4',
    'margin-top': '10mm',
    'margin-right': '10mm',
    'margin-bottom': '10mm',
    'margin-left': '10mm',
    'encoding': 'UTF-8',
    }
    output_path=f"./{DIR}/{output_name}"
    pdfkit.from_string(input_html, output_path, configuration=config, options=options)
