# LLM_Lab
A simple local language model app using [Ollama](https://ollama.com) and Python to translate text between multiple languages.

---

## Pre-requisites

### Install Ollama
To install Ollama, run the following command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Disable Ollama Service
To disable the Ollama service, execute:

```bash
sudo systemctl disable --now ollama.service
```

### Start Ollama in the Background
Start the Ollama service in the background using:

```bash
ollama serve &
```

Once launched, Ollama serves as a local API for language model interactions: [http://localhost:11434](http://localhost:11434)


### Pull Model(s)
To pull the required model(s), use the following command:

```bash
ollama pull qwen3:0.6b

```

### Check Pulled Models

```bash
ollama list
```

---

## Part 1: Simple Translator Using Python

### Clone the repository

```bash
git clone git@github.com:dream-19/Translate_App.git
```

### Create and Activate Virtual Environment
1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
2. Activate the virtual environment:
    - On Linux/macOS:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
  
### Install Dependencies
Install the required library for the interface:

```bash
pip install gradio
pip install requests
```

### Launch the app
The `translator_app.py` script provides a basic translation functionality. To launch it, run:

```bash
python3 translator_app.py
```

---

## Part 2: Simple Translator with Interface


### Launch the Application
Run with an interface:

```bash
python3 translate_app_with_gradio.py
```

Once launched, the application will be available at: [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## End of the Lab (after all of the exercises)

### Remove the model
```bash
ollama rm "qwen3:0.6b"
```

### Stop Ollama service

```bash
pkill -f "ollama serve"
```

--- 
