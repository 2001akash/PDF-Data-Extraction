from django.shortcuts import render
from .models import PdfModel
from .utils import extract_text_from_pdf
# pdf_processor/views.py

def upload_file(request):
    if request.method == 'POST':
        pdf_file = request.FILES.get('pdf_file')

        if pdf_file:
            # Extract text from PDF
            extracted_data = extract_text_from_pdf(pdf_file)

            # Save extracted data to the database (assuming you have a model for it)
            pdf_model = PdfModel(data=extracted_data)
            pdf_model.save()

            # Pass the extracted data to the template
            return render(request, 'pdf_processor/upload.html', {'extracted_data': extracted_data})

    return render(request, 'pdf_processor/upload.html')
