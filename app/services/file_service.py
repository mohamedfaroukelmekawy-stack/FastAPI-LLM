from fastapi import UploadFile
from PIL import Image
from pypdf import PdfReader
import io


class FileService:

    async def extract_content(self, file: UploadFile) -> str:

        filename = file.filename.lower()

        # TEXT FILE
        if filename.endswith(".txt"):
            content = await file.read()
            return content.decode("utf-8")

        # PDF FILE
        elif filename.endswith(".pdf"):
            pdf_bytes = await file.read()
            reader = PdfReader(io.BytesIO(pdf_bytes))

            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            return text

        # IMAGE FILE
        elif filename.endswith((".png", ".jpg", ".jpeg")):
            image_bytes = await file.read()
            image = Image.open(io.BytesIO(image_bytes))

            return f"Image uploaded: size={image.size}, mode={image.mode}"

        else:
            return "Unsupported file type"
