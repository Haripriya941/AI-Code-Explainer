# AI-Code-Explainer
# AI Code Explainer

AI Code Explainer is a simple Streamlit web application that uses Google's Gemini AI model to explain source code in easy-to-understand language. It is designed for beginners who want to learn programming concepts by understanding how code works step by step.

## Features

* Explain code in simple English
* Beginner-friendly explanations
* Automatically adds comments to the code
* Clean and simple Streamlit interface
* Powered by Gemini 2.5 Flash

## Technologies Used

* Python
* Streamlit
* Google Generative AI (Gemini API)

## Project Structure

```text
AI-Code-Explainer/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Code-Explainer.git
cd AI-Code-Explainer
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

## Requirements

Create a `requirements.txt` file with:

```txt
streamlit
google-generativeai
```

## Configure Gemini API Key

Replace the API key in the code:

```python
genai.configure(api_key="YOUR_API_KEY")
```

You can obtain an API key from Google AI Studio.

## Run the Application

```bash
streamlit run app.py
```

## How to Use

1. Launch the application.
2. Paste any Python or programming code into the input box.
3. Click **Submit**.
4. The AI will:

   * Explain the code in simple language.
   * Describe each important section.
   * Add comments to help beginners understand the code.

## Sample Use Case

### Input

```python
for i in range(5):
    print(i)
```

### Output

```text
This code uses a loop to print numbers from 0 to 4.

Explanation:
- range(5) generates numbers from 0 to 4.
- The for loop runs once for each number.
- print(i) displays the current number.

Commented Code:

# Loop through numbers 0 to 4
for i in range(5):
    # Print the current number
    print(i)
```

## Application Screenshot

Add a screenshot of your application here:

```text
screenshots/app.png
```

## Future Enhancements

* Support multiple programming languages
* Syntax highlighting
* Download explanation as PDF
* Code complexity analysis
* Bug detection and suggestions

## License

This project is licensed under the MIT License.

## Author

**Haripriya G**

Built using Streamlit and Gemini AI to help beginners understand programming code more effectively. 🚀

