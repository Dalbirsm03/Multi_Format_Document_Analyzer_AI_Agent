from crewai_tools import PDFSearchTool
from crewai_tools import TXTSearchTool
from crewai_tools import CSVSearchTool
from crewai_tools import XMLSearchTool
from crewai.json_tools import JSONSearchTool
from crewai_tools import DOCXSearchTool
from crewai_tools import FileReadTool


common_config = dict(
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
    ),file_path='path/to/your/file.txt'
)

pdftool = PDFSearchTool(config=common_config)
txttool = TXTSearchTool(config=common_config)
csvtool = CSVSearchTool(config=common_config)
xmltool = XMLSearchTool(config=common_config)
jsontool = JSONSearchTool(config=common_config)
docxtool = DOCXSearchTool(config=common_config)
filetool = FileReadTool(config=common_config)