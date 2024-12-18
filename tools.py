from crewai_tools import PDFSearchTool
from crewai_tools import TXTSearchTool
from crewai_tools import CSVSearchTool
from crewai_tools import XMLSearchTool
from crewai.json_tools import JSONSearchTool
from crewai_tools import DOCXSearchTool
from crewai_tools import FileReadTool

filetool = FileReadTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-pro",
                temperature=0.5,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    ), file_path='path/to/your/file.txt'
)

#PDF
pdftool = PDFSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-pro",
                temperature=0.5,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    ), pdf='path/to/your/document.pdf'
)

#TXT
txttool = TXTSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-pro",
                temperature=0.5,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    ),txt='path/to/your/document.txt'
)

#CSV
csvtool = CSVSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-pro",
                temperature=0.5,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    ), csv='path/to/your/document.csv'
)

#XML
xmltool = XMLSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-pro",
                temperature=0.5,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    ), xml='path/to/your/document.xml'
)

#JSON
jsontool = JSONSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-pro",
                temperature=0.5,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    ),json_path = 'path/to/your/document.json'
)

#DOCX
docxtool = DOCXSearchTool(
    config=dict(
        llm=dict(
            provider="google",
            config=dict(
                model="gemini-1.5-pro",
                temperature=0.5,
            ),
        ),
        embedder=dict(
            provider="google",
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                title="Embeddings",
            ),
        ),
    ),docx='path/to/your/document.docx'
)
