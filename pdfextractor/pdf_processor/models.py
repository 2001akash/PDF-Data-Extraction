from django.db import models

class PdfModel(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f"{self.pdf_file.name} - {self.pk}"
