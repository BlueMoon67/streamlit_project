from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Initialize the GenAI client with your API key
client = genai.Client(api_key='AIzaSyAMrHhEcDZEHQSE3tJuGV-uPI66MTwYv1Q')  # Replace with your actual API key

# Generate images based on the prompt
response = client.models.generate_images(
    model='imagen-3.0-generate-002',
    prompt='Fuzzy bunnies in my kitchen',
    config=types.GenerateImagesConfig(
        number_of_images=4,
    )
)

# Check if the response contains generated images
if response.generated_images:
    for generated_image in response.generated_images:
        # Open the image from the generated bytes
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        # Show the image
        image.show()
else:
    print("No images were generated.")