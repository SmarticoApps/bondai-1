from .tool import Tool
import requests
from pydantic import BaseModel
from bond.util import get_website_text
from bond.models.openai_wrapper import get_completion

TOOL_NAME = 'download_file'
TOOL_DESCRIPTION = "This tool allows to you to download a file. Just provide the url to the file in the 'url' parameter and the filename it should be saved to in the 'filename' parameter."
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

class DefaultParameters(BaseModel):
    url: str
    thought: str

class DownloadFileTool(Tool):
    def __init__(self):
        super(DownloadFileTool, self).__init__(TOOL_NAME, TOOL_DESCRIPTION, DefaultParameters)
    
    def run(self, arguments):
        url = arguments['url']
        filename = arguments['filename']

        try:
            response = requests.get(url)

            with open(filename, 'wb') as output_file:
                output_file.write(response.content)
            
            return f"The file was successfully downloaded to {filename}."
        except requests.Timeout:
            return "The request timed out."

