

# PDF Legal Document Analysis with LangChain and RAG

This repository contains Python scripts designed to process and analyze legal PDF documents using a Retrieval-Augmented Generation (RAG) approach. It leverages `LangChain`, `Chroma` vector database, and HuggingFace embeddings to handle document chunking, vectorization, and querying using a custom language model.

## Features
- **PDF Reader:** Efficiently reads and processes PDF files, splits them into chunks, and creates vector embeddings for querying.
- **RAG Chain:** Implements a retrieval-augmented generation pipeline that takes user queries and generates responses based on the document context.
- **Custom Prompt:** Designed for legal document analysis with a prompt that helps retrieve and analyze specific details.

## Project Structure

- **main.py:** The main entry point that ties together PDF processing and query handling.
- **pdf_reader_fun.py:** Contains functionality to read, split, and vectorize PDF documents.
- **rag.py:** Implements the RAG (Retrieval-Augmented Generation) pipeline using `LangChain`, `Chroma`, and `HuggingFace` embeddings.

## Requirements

- Python 3.x
- Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/pdf-legal-analysis.git
    cd pdf-legal-analysis
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables by creating a `.env` file:
    ```bash
    LANGCHAIN_API_KEY=your_langchain_api_key
    GROQ_API_KEY=your_groq_api_key
    ```

## Usage

1. **Prepare the PDF Document:**
   Place the PDF you want to analyze in the desired directory. Update the file path in `main.py`.

2. **Run the Program:**
   Execute the `main.py` script to process the PDF and issue queries:
    ```bash
    python main.py
    ```

3. **Query the Document:**
   Once the document is processed, enter your query when prompted. For example:
    ```
    Who are the parties involved in this endorsement agreement?
    ```

## Example

```bash
$ python main.py
Let's start
Loaded 1 document
Split into 5 chunks
Your data has been processed
Enter your query: Who are the parties involved in this endorsement agreement?
The parties involved are X and Y...
```

## Files

- **`main.py`**: Handles PDF processing and user input for queries.
- **`pdf_reader_fun.py`**: Contains the `pdf_reader` function to load, split, and embed PDF documents into a vector database.
- **`rag.py`**: Implements the retrieval and generation logic using a vector database and custom prompt.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

