import base64
import requests
import os
import pandas as pd

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
api_key = ""

# Function to encode the image to base64
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Replace 'path_to_your_image.jpg' with the path to your actual image file
# images path
image_file_path = os.fsencode(r"path_to_your_image_folder")
# image_path = r""

# empty list of dictionaries
data = []

# run for first x files in the directory
for file in os.listdir(image_file_path)[:500]:
    # filename = os.fsdecode(file)
    dict = {}
    if '.jpeg' in file.decode('ascii'):
        base64_image = encode_image(os.path.join(image_file_path, file))
        # base64_image = encode_image(image_path)
        headers = {
          "Content-Type": "application/json",
          "Authorization": f"Bearer {api_key}"
        }

        payload = {
          "model": "gpt-4o",
          "messages": [
            {
              "role": "user",
              "content": [
                {"type": "text", "text": '''I want you to analyze an image with these qualities in mind, and input your data into these qualities: Quality of the X-ray: Including penetration (whether the spine can be seen through the heart shadow), rotation (alignment of the clavicles relative to the spinous processes), and inspiration (whether the diaphragm is at the level of the 10th posterior rib or lower).
                  
                  Lung Fields: Assess for any areas of increased opacity (which could indicate consolidation, mass, or effusion) or decreased opacity (which could suggest pneumothorax). Check for patterns such as reticular (net-like), nodular, or cystic, which could indicate various lung pathologies.

                  Heart: Examine the size and contour of the heart. An enlarged heart could suggest cardiomegaly, while an abnormal contour could indicate an aneurysm or other cardiac conditions.

                  Mediastinum: Evaluate the width and contours of the mediastinum for any widening, masses, or other abnormalities that might suggest lymphadenopathy, mediastinal mass, or other pathologies.

                  Diaphragm: Assess the shape, contour, and position of the diaphragm. Look for signs of elevation, which could indicate subdiaphragmatic pathology, or blunting of the costophrenic angles, which could suggest pleural effusion.

                  Pleural Space: Check for any pleural thickening, pleural plaques, or fluid, which could present as blunting of the costophrenic angles or a meniscus sign.

                  Bones: Review the visible bones, including the ribs, clavicles, scapulae, and thoracic spine, for any fractures, lesions, or other abnormalities.

                  Soft Tissues: Examine the soft tissues around the thorax for any masses, subcutaneous air (indicative of pneumomediastinum), or other abnormalities.

                  Airways: Look at the trachea and main bronchi for any deviation, obstruction, or other abnormality.

                  Hilum: Assess the hila for enlargement or mass that may suggest lymphadenopathy or other pathology.

                  Devices and Tubes: Identify any medical devices such as pacemakers, central venous catheters, endotracheal tubes, nasogastric tubes, and their positions.

                  Additional Findings: Note any calcifications, foreign bodies, or previous surgical changes (e.g., clips, valves, or prostheses).

                  Based on this chest xray description, can you tell me if you think this description indicates a) pneumonia or b) no pneumonia
                  
                  Only output the answer as A or B.'''},
                {
                  "type": "image_url",
                  "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                  }
                }
              ]
            }
          ],
          "max_tokens": 300
        }

        # Make the API request and print out the response
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        # parse out chatgpt message that we care about: add filename and the corresponding chatgpt response to dataframe
        try:
            print(file.decode('ascii'), ": ", response.json().get('choices')[0].get('message').get('content'))
            dict['filename'] = file.decode('ascii')
            dict['result'] = response.json().get('choices')[0].get('message').get('content')
            data.append(dict)
        # got an empty response rarely
        except TypeError:
            print(file.decode('ascii'), ": ", "")
            dict['filename'] = file.decode('ascii')
            dict['result'] = ""
            data.append(dict)
        # for anything else that I didn't expect
        except:
            print("Unresolved error: excluding the data")

# write all responses to a file
final_data = pd.DataFrame(data)
final_data.to_csv("cons_pneumonia_5.csv", sep=',', index=False, encoding='utf-8')