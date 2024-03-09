# OpenAI Vision Model - Extract Totals from POS Receipt

This project demonstrates how to use the OpenAI Vision Model to extract the total paid amount and tax amount from a point-of-sale (POS) receipt. This is accomplished by encoding an image of the receipt and sending it to OpenAI's API, which can interpret the contents and return structured data.

## Repository Contents

- **README.md**: This file you're reading that provides installation and usage instructions.
- **requirements.txt**: A list of Python package dependencies required for running the scripts.
- **pos.png**: An example POS receipt image file that you will be analyzing.
- **lib_example.py**: A library file containing utility functions used in `request_example.py`.
- **request_example.py**: The main script that encodes the image and sends the request to OpenAI's API.
- **.env**: A file storing your OpenAI API key (not included in the repository for security reasons).

## Installation

1. Clone or download this repository to your local machine.
2. Install the necessary packages by running:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory with the content:
    ```
    OPENAI_API_KEY="sk-your_api_key_here"
    ```
   Replace `sk-your_api_key_here` with your actual OpenAI secret key.

## Usage

Make sure you have a POS receipt image named `pos.png` in the root directory. If your image has a different name or path, update the `image_path` variable in `request_example.py` accordingly.

Run the following command to perform the OCR and data extraction:

```bash
python request_example.py
```

The script will print the total paid amount and tax amount extracted from the POS receipt as a JSON object.

## How It Works

- **lib_example.py** contains a function `encode_image(image_path)` which takes the path of an image file, reads the image, and returns its base64 encoded string.
  
- **request_example.py** is the entry point. It uses `dotenv` to load environment variables, builds an HTTP header with the OpenAI API key, and creates a JSON payload including the encoded image. Then it sends a POST request to OpenAI's API and prints out the response.

## Important Notes

- You must have a valid OpenAI API key to use this service.
- Be aware of the costs associated with using OpenAI's API, and ensure your usage complies with their billing policies.

## Support and Feedback

If you encounter any issues or have questions about using this code, please refer to the OpenAI documentation or reach out to their support channels.

## Contributing

We welcome contributions to improve this script! Please feel free to submit pull requests or suggest enhancements through issues.

## License

Please include a license here that dictates how others may use this code. If unsure, consider using open-source licenses such as MIT, BSD, or GPL.

---

**Disclaimer:** Be cautious with handling sensitive information. Do not share your API keys publicly and follow best practices for security. This script is for educational and demonstration purposes only; users should modify it as per their needs while adhering to OpenAI's policies.