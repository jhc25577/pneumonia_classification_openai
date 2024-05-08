import base64
import requests
import os
import pandas as pd

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
api_key = "YOUR_OPENAI_API_KEY"

# Function to encode the image to base64
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Replace 'path_to_your_image.jpg' with the path to your actual image file
# images path
image_file_path = os.fsencode(r"C:\Users\Jo\Downloads\openai_project\ChestXRay2017\chest_xray\train\NORMAL")
# image_path = r"C:\Users\Jo\Downloads\openai_project\ChestXRay2017\chest_xray\train\PNEUMONIA\person1_bacteria_1.jpeg"

# empty list of dictionaries
data = []

# run for first 10 files in the directory
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
          "model": "gpt-4-turbo",
          "messages": [
            {
              "role": "user",
              "content": [
                {"type": "text", "text": "This is an image on the Step 1 examination, the multiple choice question is as follows. Based on the image, does the patient have A) pneumonia or B) no pneumonia? Only output the answer as A or B."},
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
        # TODO: write response to a file
        try:
            print(file.decode('ascii'), ": ", response.json().get('choices')[0].get('message').get('content'))
            dict['filename'] = file.decode('ascii')
            dict['result'] = response.json().get('choices')[0].get('message').get('content')
            data.append(dict)
        except TypeError:
            print(file.decode('ascii'), ": ", "")
            dict['filename'] = file.decode('ascii')
            dict['result'] = ""
            data.append(dict)
        except:
            print("Unresolved error: excluding the data")

final_data = pd.DataFrame(data)
final_data.to_csv("train_no_pneumonia.csv", sep=',', index=False, encoding='utf-8')