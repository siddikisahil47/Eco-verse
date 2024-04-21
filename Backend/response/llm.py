from langchain_core.messages import HumanMessage
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)
import base64
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=api_key,
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
    # max_output_tokens=1024,
)


def get_mime_type(file_path):
    extension_to_mime_type = {
        "png": "image/png",
        "jpeg": "image/jpeg",
        "jpg": "image/jpeg",
        "webp": "image/webp",
        "heic": "image/heic",
        "heif": "image/heif",
        "tmp": "image/jpeg",
    }

    extension = os.path.splitext(file_path)[1][1:].lower()
    return extension_to_mime_type.get(extension)


def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def get_gemini_response(image_path):
    image = encode_image(image_path)
    mime_type = get_mime_type(image_path)

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": """
                    Make it shorter and more informative.
                    1. Accurately identify the goods in the image.
                    2. Provide an appropriate Carbon Footprint in grams.
                    3. Provide Recycling steps.
                    4. Provide steps to convert the goods into a decorative material.
                    5. Suggest potential uses of the decorative material.

                    Ensure that your analysis is consistent throughout.
                """,
            },
            {"type": "image_url", "image_url": f"data:{mime_type};base64,{image}"},
        ]
    )
    output = llm.invoke([message])

    response = output.content

    return response
