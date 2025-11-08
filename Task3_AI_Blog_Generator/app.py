import streamlit as st
import os
import markdown
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# ------------------ CONFIGURE GEMINI ------------------
genai.configure(api_key=os.getenv("AIzaSyDBRAAoMWVKUTmlwaLDnxIRukimx0fqSdY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------ APP LAYOUT ------------------
st.set_page_config(page_title="AI Blog Generator", layout="wide")

st.title("🧠 AI Blog Generator")

# Tabs: one to browse blogs, one to generate a new one
tab1, tab2 = st.tabs(["📚 Existing Blogs", "✨ Generate New Blog"])

# ------------------ TAB 1: EXISTING BLOGS ------------------
with tab1:
    st.subheader("Available Blogs")

    blog_folder = "blog"
    if not os.path.exists(blog_folder):
        os.makedirs(blog_folder)

    blog_files = [f for f in os.listdir(blog_folder) if f.endswith(".md")]

    if blog_files:
        selected_blog = st.selectbox("Select a blog to read:", blog_files)

        if selected_blog:
            with open(os.path.join(blog_folder, selected_blog), "r", encoding="utf-8") as f:
                md_content = f.read()
                html = markdown.markdown(md_content)
                st.markdown(html, unsafe_allow_html=True)
    else:
        st.info("No blogs found. Try generating one from the next tab!")

# ------------------ TAB 2: GENERATE NEW BLOG ------------------
with tab2:
    st.subheader("Generate a New Blog")

    title_input = st.text_input("📝 Blog Title", placeholder="Enter your blog topic (e.g., Introduction to Neural Networks)")
    brief_input = st.text_area("💡 Optional Context", placeholder="Add more details or focus points for the blog...")

    if st.button("🚀 Generate Blog"):
        if not title_input.strip():
            st.error("Please enter a title before generating.")
        else:
            with st.spinner("✨ Generating your blog... please wait..."):
                try:
                    prompt = f"Write a detailed, well-structured technical blog post on '{title_input}'. {brief_input if brief_input else ''} Use Markdown formatting with headers, subheaders, bullet points, and code examples where relevant."
                    response = model.generate_content(prompt)
                    blog_content = response.text

                    # Save generated blog as Markdown
                    file_path = os.path.join("blog", f"{title_input.replace(' ', '_')}.md")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(blog_content)

                    st.success(f"✅ Blog '{title_input}' generated and saved successfully!")
                    st.markdown(blog_content)

                except Exception as e:
                    st.error(f"❌ Error generating blog: {e}")
