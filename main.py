import os
import asyncio
import tempfile
from dotenv import load_dotenv
from crewai import Crew, Agent, Task, Process
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# Load environment variables
load_dotenv()

from crewai_tools import PDFSearchTool, TXTSearchTool, CSVSearchTool, XMLSearchTool, JSONSearchTool, DOCXSearchTool, FileReadTool

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
    ),
)

# Define the tools without file paths
pdftool = PDFSearchTool(config=common_config)
txttool = TXTSearchTool(config=common_config)
csvtool = CSVSearchTool(config=common_config)
xmltool = XMLSearchTool(config=common_config)
jsontool = JSONSearchTool(config=common_config)
docxtool = DOCXSearchTool(config=common_config)
filetool = FileReadTool(config=common_config)

# Function to create an event loop and run the LLM initialization
def init_llm():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return ChatGoogleGenerativeAI(
        model='gemini-1.5-flash',
        verbose=True,
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

# Initialize the language model
llm = init_llm()

# Define the Researcher Agent
researcher_agent = Agent(
    role='Document Processing Specialist',
    goal='Extract actionable insights',
    backstory="You are a Document Information Extraction Specialist who is an expert in extracting information from the provided documents",
    tools=[pdftool, txttool, csvtool, xmltool, jsontool, docxtool, filetool],
    llm=llm,
    verbose=True, 
    allow_delegation=True,
)

# Define the Writer Agent
writer_agent = Agent(
    role='Document Writing Specialist',
    goal='Write the extracted information',
    backstory="You are a Document Writing Specialist who is an expert in noting down the information which is provided by the researcher agent",
    tools=[pdftool, txttool, csvtool, xmltool, jsontool, docxtool],
    llm=llm,
    verbose=True, 
    allow_delegation=True,
)

# Define Manager Agent

# Streamlit UI
st.title("DOCUMENT RAG SEARCH")
uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "csv", "xml", "json", "docx"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name
    
    # Detect file type
    file_extension = uploaded_file.name.split('.')[-1].lower()

    # Select the appropriate tool based on file type
    if file_extension == 'pdf':
        tool = pdftool
    elif file_extension == 'txt':
        tool = txttool
    elif file_extension == 'csv':
        tool = csvtool
    elif file_extension == 'xml':
        tool = xmltool
    elif file_extension == 'json':
        tool = jsontool
    elif file_extension == 'docx':
        tool = docxtool
    else:
        st.error(f"Unsupported file type: {file_extension}")
        tool = None

    if tool:
        # Define the Researcher Task
        researcher_task = Task(
            description=f'Extract information from the uploaded document: {uploaded_file.name}',
            expected_output=f'Detailed information extracted from the document: {uploaded_file.name}',
            agent=researcher_agent,
            tools=[tool]
        )

        # Define the Writer Task
        writer_task = Task(
            description=f'Document and explain the extracted information from the uploaded document: {uploaded_file.name}',
            expected_output=f'A detailed explanation of the extracted information from the document: {uploaded_file.name}',
            agent=writer_agent,
            async_execution=False,
            tools=[tool],
            output_file='code_documentation.md'
        )

        # Create and execute the Crew process
        my_crew = Crew(
            agents=[researcher_agent, writer_agent],
            tasks=[researcher_task, writer_task],
            process=Process.sequential,
            verbose=True,
        )

        result = my_crew.run(input_file=tmp_file_path)  # Execute the Crew process with the uploaded file
        st.write(result)
