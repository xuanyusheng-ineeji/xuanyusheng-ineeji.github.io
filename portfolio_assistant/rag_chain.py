from pathlib import Path
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

INDEX_DIR = Path(__file__).parent / "data" / "faiss_index"

SYSTEM_PROMPT = """You are an AI assistant for Xuanyu Sheng's academic portfolio website.
Your role is to help visitors learn about Xuanyu's research, projects, education, and professional experience.

Guidelines:
- Answer based on the provided context. If the answer isn't in the context, say so honestly.
- Be friendly, concise, and professional.
- Respond in the same language as the question (English or Chinese/中文).
- For research topics, highlight key findings and contributions.
- For projects, emphasize technical depth and impact.

Context from portfolio:
{context}
"""

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

def build_chain():
    if not INDEX_DIR.exists():
        raise FileNotFoundError(
            f"Knowledge base not found at {INDEX_DIR}.\n"
            "Please run: python build_knowledge.py"
        )

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.load_local(
        str(INDEX_DIR), embeddings, allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatOllama(model="qwen2.5:7b", temperature=0.3)

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{question}"),
    ])

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain

_chain = None

def get_chain():
    global _chain
    if _chain is None:
        _chain = build_chain()
    return _chain
