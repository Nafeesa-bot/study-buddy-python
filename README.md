# Python AI Teacher (Study Buddy)

A Streamlit-based educational application that uses Google's Generative AI (Gemini) to create an interactive learning experience.

## 🎯 Features

- Interactive Q&A interface powered by Gemini AI
- Chat history tracking
- Keyword-based history filtering
- Real-time responses
- Clean and intuitive user interface

## 🛠️ Technologies Used

- Python 3.12+
- UV (Fast Python package installer and resolver)
- Streamlit
- Google Generative AI (Gemini)
- Python-dotenv

## 📋 Prerequisites

- Python 3.12 or higher
- Gemini API key

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NaveenBen/study-buddy-python.git
   cd python-ai-teacher
   ```

2. Install UV (if you haven't already):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create and activate a virtual environment:

   ```bash
   uv venv
   source .venv/bin/activate  # On Linux/macOS
   ```

4. Install dependencies using UV:

   ```bash
   uv sync
   ```

5. Set up your environment variables:

   ```bash
   export GEMINI_API_KEY="your_api_key"
   ```

   Or create a `.env` file with:

   ```plaintext
   GEMINI_API_KEY=your_api_key
   ```

## 🎮 Usage

1. Start the Streamlit application:

   ```bash
   streamlit run study_buddy.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. Enter your question in the text input field and click "Ask"

4. View answers and browse through your chat history

5. Use the keyword filter to search through previous questions

## 📦 Project Structure

- `study_buddy.py`: Main application file containing the Streamlit interface and AI integration
- `main.py`: Basic entry point for the application
- `pyproject.toml`: Project configuration and dependencies
- `.env`: Environment variables (create this file - not tracked in git)

## 🔑 Key Components

- Streamlit UI components for user interaction
- Gemini AI integration for generating responses
- Chat history management with filtering capabilities
- Environment variable management for secure API key storage

## 📝 Notes

- Make sure to keep your Gemini API key secure and never commit it to version control
- The application demonstrates various Python concepts including:
  - Global variables and scope
  - Lists and dictionaries
  - Functions and return values
  - Control flow
  - Lambda functions and list comprehensions
  - Input/Output operations

## 📄 License

[Add your license information here]
