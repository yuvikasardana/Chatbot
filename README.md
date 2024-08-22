

THis is a simple chatbot application built using [Streamlit](https://streamlit.io/) and [Google Generative AI](https://developers.generativeai.google/) (Gemini model). 
This project allows users to input questions and receive AI-generated responses in real-time.

## Features

- Powered by Google Generative AI's Gemini model.
- Simple and interactive web interface using Streamlit.
- Easy to set up and configure with API keys.

## Prerequisites

To run this project, ensure you have the following:

- **Python 3.8+**
- A Google API key for accessing the Generative AI service.
- The following Python libraries:
  - `streamlit`
  - `dotenv`
  - `google-generativeai`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Chatbot.git
    cd Chatbot
    ```

2. Installing the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Setting up your environment variables:

- Create a `.env` file in the project root.
- Add your Google API key to the `.env` file:

    ```plaintext
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Input your question in the text box, click the "Ask your question" button, and view the AI-generated response.
