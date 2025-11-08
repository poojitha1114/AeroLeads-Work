# AeroLeads-Work
##🧠 AI Blog Generator

This project is an AI-powered Blog Generator that automatically creates structured, high-quality blog posts using the Gemini API. It allows you to input blog topics, generate multiple articles, and display them neatly in a web interface built with Streamlit.

##🚀 Features

✍️ AI Blog Generation — Automatically generates blogs for any given topic using Google Gemini API.

📂 Auto-Save to Folder — All generated blogs are saved as Markdown files inside the /blog folder.

🧾 Clean, Structured Output — Blogs are generated with titles, headings, and well-formatted sections.

⚡ Dynamic Interface — Easily generate new blogs directly from the Streamlit app.

🧩 Environment-Based Configuration — Uses .env file to securely manage API keys.

##🏗️ Tech Stack

Python 3.x

Streamlit (for the web UI)

Google Gemini API (for AI-generated content)

Markdown (for formatted blog storage)

python-dotenv (for environment variable management)

##📁 Project Structure
AI_Blog_Generator/
│
├── app.py                  # Main Streamlit app
├── generate-blogs.py       # Script to auto-generate multiple blogs
├── .env                    # Environment file (store your API key here)
├── requirements.txt        # Dependencies
│
├── blog/                   # Folder where all generated blog posts are stored
│   ├── python_basics.md
│   ├── machine_learning_intro.md
│   └── ...
│
└── templates/
    └── index.html          # Template for the web layout

##⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/aero-leads-work.git
cd aero-leads-work/Task3_AI_Blog_Generator

2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate    # For Windows
# or
source venv/bin/activate # For Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your API Key

Create a .env file in the root directory:

GOOGLE_API_KEY=your_api_key_here

5️⃣ Run the App
streamlit run app.py

6️⃣ (Optional) Generate Bulk Blogs

To generate multiple blogs at once:

python generate-blogs.py

##🧩 Example Use Case

Open the web app.

Enter a topic such as “Introduction to Machine Learning.”

Click Generate.
