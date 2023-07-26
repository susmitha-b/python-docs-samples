# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]
import streamlit as st
import speech_recognition as sr
import pyttsx3

def main():
    """Deploying Streamlit App with App Engine on GCP"""

    st.title("Streamlit App")
    st.header("Speech-to-Text & Audio-to-Speech Recognition")

    activities = ["Speech-to-Text", "Audio-to-Speech"]

    choices = st.sidebar.selectbox('Select Activities',activities)

    if choices =='Speech-to-Text':
         st.subheader("Speech-to-Text")

    elif choices =='Audio-to-Speech':
       st.subheader("Audio-to-Speech")
    

   


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
