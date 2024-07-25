# Q-A-system

# Question and Answering System using RoBERTa Base SQuAD Model

## Project Summary

This GitHub project implements a Question and Answering (Q&A) system using the RoBERTa base SQuAD model, built with a Flask backend. The system allows users to upload a text file, from which they can then ask questions and receive answers based on the content of the file.

## Features

- **File Upload**: Users can upload a text file containing the content from which they want to extract answers.
- **Question Answering**: Users can ask questions related to the uploaded text file, and the system will provide answers using the RoBERTa base SQuAD model.
- **Flask Backend**: The application is built with Flask, providing a simple and efficient web interface for interactions.

## Technologies Used

- **Python**: The core language used for development.
- **Flask**: A micro web framework for handling HTTP requests and serving the web interface.
- **Transformers (Hugging Face)**: Utilized for the RoBERTa base SQuAD model to handle the Q&A tasks.
- **HTML/CSS/JavaScript**: For the front-end interface.

## Getting Started

### Prerequisites

- Python 3.6+
- Pip (Python package installer)

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/qa-system-roberta-flask.git
    cd qa-system-roberta-flask
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```sh
    python app.py
    ```

4. Open your web browser and navigate to `http://127.0.0.1:5000`.

### Usage

1. **Upload a Text File**:
    - Click on the "Upload File" button.
    - Select and upload a pdf/doc file (.pdf,.docx) from your local machine.

2. **Ask Questions**:
    - Enter your question in the input field provided.
    - Click the "Ask Question" button to receive an answer based on the uploaded text file.

### Example

- Upload a text file containing content about a topic (e.g., "Climate Change").
- Ask a question like "What are the main causes of climate change?"
- Receive an answer extracted from the uploaded content.

## Project Structure

```
qa-system-roberta-flask/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html         # HTML template for the web interface
|   ├── result.html        # HTML template for the result page interface
└── README.md              # Project summary and documentation
```

## Contributing

We welcome contributions! Please fork the repository and submit pull requests for any enhancements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Hugging Face Transformers library for the RoBERTa model.
- Flask for the web framework.
- SQuAD dataset for providing the foundation for the Q&A model.

Feel free to reach out if you have any questions or need further assistance!
