# 📊 Data Analyst Agent

A powerful, intelligent Data Analyst Agent capable of reading and analyzing structured and unstructured documents — including PDFs, Excel files, text files, Word docs, images, and more. It can answer follow-up questions and generate visualizations. Built using Python and the `meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` model via [Together.ai](https://www.together.ai).

---

## 🚀 Features

- 🔍 **Multi-format File Support**: Handles `.pdf`, `.csv`, `.xlsx`, `.txt`, `.docx`, and image files.
- 🧠 **LLM-Powered Analysis**: Uses LLaMA-4 Maverick via Together.ai to understand and interpret documents.
- 📈 **Interactive Q&A**: Ask natural language questions about the uploaded documents.
- 📊 **Data Visualization**: Automatically generates plots and charts based on user queries.
- 📦 **Modular Design**: Easily extendable and maintainable Python codebase.

---

## 🛠️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/data-analyst-agent.git
   cd data-analyst-agent
Create a virtual environment and activate it:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Set your Together.ai API key:
Create a .env file in the project root:


TOGETHER_API_KEY=your_api_key_here
🧪 How to Use
Run the notebook:
Open Data_analyst_agent.ipynb in Jupyter or Colab.

Upload your documents:
Upload files using the notebook interface or modify the script to read from a folder.

Ask questions:
Example:

What was the total expenditure in Q1?
Generate a pie chart of sales by category.
View Results:
The model answers the question and, if applicable, generates a chart or table.


 Folder Structure

data-analyst-agent/
│
├── Data_analyst_agent.ipynb     # Main notebook
├── requirements.txt             # Python dependencies
├── utils/                       # Helper functions for file handling, parsing, etc.
├── .env                         # API keys and config (not included in repo)
└── README.md                    # This file


Requirements
pip install pandas matplotlib seaborn plotly PyMuPDF pdfplumber pytesseract openpyxl python-docx together
