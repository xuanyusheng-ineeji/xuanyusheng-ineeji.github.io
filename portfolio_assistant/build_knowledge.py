"""
Build FAISS vector index from Jekyll site content.
Run once: python build_knowledge.py
"""
import re
import os
from pathlib import Path
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

PAGES_DIR = Path(__file__).parent.parent / "_pages"
INDEX_DIR = Path(__file__).parent / "data" / "faiss_index"

def clean_markdown(text: str) -> str:
    text = re.sub(r"---.*?---", "", text, flags=re.DOTALL)       # frontmatter
    text = re.sub(r"\{%.*?%\}", "", text, flags=re.DOTALL)        # Liquid tags
    text = re.sub(r"<[^>]+>", " ", text)                          # HTML tags
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)         # links
    text = re.sub(r"[`*_#>|\\]", "", text)                        # markdown chars
    text = re.sub(r"\n{3,}", "\n\n", text)                        # blank lines
    return text.strip()

def load_pages() -> list[Document]:
    docs = []
    for md_file in PAGES_DIR.glob("*.md"):
        raw = md_file.read_text(encoding="utf-8")
        content = clean_markdown(raw)
        if content:
            docs.append(Document(
                page_content=content,
                metadata={"source": md_file.name}
            ))
            print(f"  Loaded: {md_file.name} ({len(content)} chars)")
    return docs

def build_index():
    print("Loading pages...")
    docs = load_pages()

    print("Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80,
        separators=["\n\n", "\n", ".", " "],
    )
    chunks = splitter.split_documents(docs)
    print(f"  {len(chunks)} chunks created")

    print("Embedding with nomic-embed-text (Ollama)...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    vectorstore.save_local(str(INDEX_DIR))
    print(f"Index saved to {INDEX_DIR}")

if __name__ == "__main__":
    build_index()
