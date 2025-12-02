# 🧠 LangChain Notes & Projects — Hands-on Exploration

This repository contains my hands-on journey with **LangChain**, exploring its core features for building generative AI applications like **RAG-based systems**, **tool-using agents**, **memory-powered assistants**, and more.

I’ve structured the repo to reflect **modular learning** across key LangChain concepts — from loading documents, creating embeddings, building chains, using tools, and handling structured outputs.

> 🧪 This is an **experimental, hands-on repo** — every notebook is a practical implementation of what I learned through a LangChain YouTube course (in Hindi, self-translated and coded in English).

---

## 🗂️ Folder Structure & Topics Covered

| Folder / File                     | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| **📁 Chains/**                   | Multi-step LangChain pipelines — combines LLMs, retrievers, tools, etc.    |
| **📁 Language_Model.ipynb**      | Basics of LLM invocation in LangChain — including prompt handling.          |
| **📁 Prompts_and_Memory/**       | Prompt templates, input variables, and memory (buffer window, summary, etc.) |
| **📁 RAG Components/**           | Core components for Retrieval-Augmented Generation (RAG): loaders, splitters, embeddings, vector DB. |
| **📁 Structured Output/**        | Structured outputs (JSON parsing, function-style tool calls, etc.)          |
| **📁 Tools/**                    | Defining and binding external tools LangChain agents can call               |
| **📄 requirements.txt**          | Python dependencies to recreate the environment                             |

---

## 🔍 Topics & Concepts Practically Explored

### 🔗 LangChain Basics
- Working with `LLMs`, prompt templates, and chaining outputs
- Introduction to memory: `ConversationBufferMemory`, `SummaryMemory`, `WindowMemory`

### 📄 Document Loading & Text Splitting
- Using loaders like `PyPDFLoader`, `TextLoader`
- Splitting strategies: `RecursiveCharacterTextSplitter`, `TokenTextSplitter`

### 🧠 Embeddings & Vector Stores
- Using `OpenAIEmbeddings` and `HuggingFaceEmbeddings`
- Vector DBs: `FAISS`, `Chroma`
- Customizing chunk sizes and semantic splits

### 📚 Retrieval-Augmented Generation (RAG)
- Ingest documents → embed → retrieve relevant chunks → generate with LLM
- Connecting retrievers with LLMs for document-based QA

### 🛠️ Tool Binding & Tool Calling
- Creating custom tools using `@tool` decorators
- Structured tool invocation via JSON output
- Tool routing with `MultiRetrievalTool`, `ToolExecutor`, `RunnableWithMessageHistory`

### 📊 Structured Output
- Forcing model to return structured JSON-like outputs
- Useful for downstream parsing, tool selection, or reasoning

---

## 🚀 Getting Started

### 🔧 Requirements
Make sure to install the required dependencies:
```bash
pip install -r requirements.txt
