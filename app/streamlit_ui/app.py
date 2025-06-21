import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Knowledge Graph Explorer", layout="wide")

st.title("📚 Knowledge Graph Builder + Query Engine")

# --- Upload Section ---
st.sidebar.header("📤 Upload Files")
uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs, DOCX, TXT, or Images (JPG, PNG)", 
    type=["pdf", "docx", "txt", "jpg", "jpeg", "png"], 
    accept_multiple_files=True
)

if uploaded_files:
    st.sidebar.success(f"{len(uploaded_files)} file(s) uploaded.")
    # Save them for processing
    for file in uploaded_files:
        file_path = Path("data/raw") / file.name
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(file.read())
    st.sidebar.info("Files saved. Proceed to query after processing.")

# --- Query Section ---
st.header("🔍 Ask a Question")
query = st.text_input("Type your question related to the uploaded documents:")

submit = st.button("Search")

# --- Answer Display ---
if submit and query:
    with st.spinner("Thinking..."):
        # Call your backend here (placeholder result below)
        # e.g., answer = query_pipeline(query)
        answer = "📌 Sample answer: Alan Turing built the Bombe to break Enigma."

        st.subheader("📬 Answer")
        st.success(answer)

# --- Graph Visualization ---
st.header("🌐 Knowledge Graph Viewer")

graph_html_path = Path("graphs/graph.html")

if graph_html_path.exists():
    with open("graphs/graph.html", "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=600, scrolling=True)
else:
    st.info("Graph not generated yet. Upload files and build the graph to view it here.")
