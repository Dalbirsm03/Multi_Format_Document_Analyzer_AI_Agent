# Multiformat-pdf-researcher-CrewAI
This application utilizes the **Crew AI Framework** to process and analyze various document formats (PDF, TXT, CSV, XML, JSON, DOCX) and extract actionable insights. It leverages AI agents to perform specialized tasks such as data extraction and summarization.

## Key Features:
- **Multiple File Formats Supported**: Upload documents in PDF, TXT, CSV, XML, JSON, and DOCX formats.
- **AI-Powered Document Analysis**: Uses advanced language models (Google Gemini) to extract insights and generate explanations.
- **Customizable Workflow**: Uses Crew AI’s multi-agent architecture for reading, processing, and extracting data from different document types.
- **Interactive UI**: Built with **Streamlit** for easy document upload and result display.
- **Automated Task Execution**: Crew AI handles the orchestration of tasks between the **Researcher Agent** (data extraction) and **Writer Agent** (summarizing and writing the extracted information).

## How it Works:
1. Upload a document through the Streamlit interface.
2. The system automatically detects the document type and selects the corresponding processing tool.
3. The **Researcher Agent** analyzes the document, extracting key insights.
4. The **Writer Agent** generates a detailed explanation of the extracted information.
5. Results are displayed directly in the app.

