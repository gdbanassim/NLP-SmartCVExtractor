# NLP-SmartCVExtractor 🚀
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

Extract insights with ease using NLP-SmartCVExtractor, a Python-powered tool for intelligent CV analysis! 🔍

## 📑 Table of Contents
- [Repository Structure](#repository-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features ✨

- **Intelligent CV Analysis** 🤖: Utilizes natural language processing to extract relevant information from CVs.
- **Customizable Skills Extraction** 📝: Leverages a JSON skills file (`skills.json`) for tailored extraction.

## Repository Structure 📂

```plaintext
├── app.py # Main application entry point 🚀
├── parser.py # CV parsing and analysis module 🤖
├── requirements.txt # Project dependencies 📦
├── skills.json # Customizable skills extraction file 📝
├── LICENSE # Project license 📜
└── README.md # Project documentation 📖
```

## Installation 🛠️


1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/resume-parser.git
   cd resume-parser
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the SpaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Hugging Face API token:
     ```plaintext
     HF_TOKEN=your_hugging_face_token
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to `http://localhost:8501`.

3. Upload one or more resumes in PDF or DOCX format.

4. View parsed results in JSON format and download them as JSON or CSV fil

## Contributing 🤝

We welcome contributions! Follow these steps to contribute:
1. Fork the repository 🍴.
2. Create a new branch (`git checkout -b feature/your-feature`) 🌿.
3. Commit your changes (`git commit -m "Add your feature"`) ✅.
4. Push to the branch (`git push origin feature/your-feature`) 🚀.
5. Open a pull request 📬.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Project Status 🚧

NLP-SmartCVExtractor is in active development. We are continuously working to improve and expand its capabilities.


## Roadmap 🗺️

- **Upcoming Features**:
  - Support for multiple CV formats (e.g., PDF, DOCX)
  - Enhanced skills extraction using machine learning models

We look forward to your contributions and feedback! 😊
