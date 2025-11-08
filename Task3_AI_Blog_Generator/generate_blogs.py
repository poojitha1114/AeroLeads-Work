import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("api key"))

# Create /blog directory if not exists
os.makedirs("blog", exist_ok=True)

# List of topics (you can modify this)
blog_topics = [
    "Understanding Machine Learning Algorithms",
    "Getting Started with Python for Data Science",
    "A Beginner’s Guide to APIs and RESTful Services",
    "How to Build a Simple Web App with Flask",
    "Exploring Neural Networks with TensorFlow",
    "Introduction to Cloud Computing for Developers",
    "Version Control with Git and GitHub",
    "Understanding Prompt Engineering for AI",
    "How AI is Revolutionizing Web Development",
    "Top 10 Python Libraries Every Developer Should Know"
]

model = genai.GenerativeModel("gemini-2.5-flash")

# Generate and save blogs
for topic in blog_topics:
    print(f"Generating blog for: {topic}")
    response = model.generate_content(f"Write a detailed, structured, SEO-friendly blog on: {topic}")
    blog_content = response.text

    # Save to file
    safe_title = topic.lower().replace(" ", "_").replace("/", "_")
    with open(f"blog/{safe_title}.md", "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n{blog_content}\n")

print("\n✅ All blogs generated and saved in /blog folder.")

