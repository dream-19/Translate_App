import re
import requests


# Function to remove <think> sections from the model's response
def remove_think_section(text):
    # Use regular expression to remove text between <think> and </think>
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()


# Function to send the prompt to the model and get the translated text
def get_answer(source_language, target_language, text):
    # URL of the local Ollama model server
    url = "http://localhost:11434/api/generate"
    
    # HTTP headers to tell the server we're sending JSON
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Create the translation prompt with examples and the user's input
    prompt = (
        "You are an expert translator. Your task is to translate the text from one language to another without adding any comments.\n"
        
        "Examples:\n"
        "Translate the following sentence from Italian to English.\n"
        "Text: Ciao, oggi fa molto caldo!\n"
        "Translation: Hello, today is very hot!\n"

        "Translate the following sentence from Italian to Spanish.\n"
        "Text: Studio Ingegneria Informatica all'università\n"
        "TranslationEstudio Ingeniería Informática en la universidad\n"

        f"Translate the following sentence from {source_language} to {target_language}.\n"
        f"Text: {text}\n"
        "Translation:"
    )

    # Data to send in the request, including model settings
    data = {
        "model": "qwen3:0.6b",  # Model name
        "prompt": prompt,
        "options": {
            "temperature": 0.6,  # Controls randomness; lower = more focused
            "top_k": 20,         # Limits number of words considered at each step
            "top_p": 0.95,       # Nucleus sampling; controls diversity
            "repeat_penalty": 1, # Discourages repeating words
            "stop": ["<|im_start|>", "<|im_end|>"],  # Stop generation at these tokens
            "seed": 42           # Makes results repeatable (optional)
        },
        "stream": False  # We want the full result all at once (not streamed)
    }

    print("Sending request to model...")

    # Send the request to the model and store the response
    response = requests.post(url, json=data, headers=headers)

    # If the request was successful
    if response.status_code == 200:
        # Get the clean response text without <think> parts
        clean_text = remove_think_section(response.json()['response'])

        # Calculate how long the model took (convert from nanoseconds to seconds)
        total_time = round(response.json()['total_duration'] / 1e9, 2)

        # Return the result and the time
        return clean_text, total_time
    else:
        # If there was an error, return the error message
        return f"Error: {response.status_code} {response.text}", None


# ----------- Example usage below -----------

# Define source and target languages and the input text
source_language = "Italian"
target_language = "English"
text = "Oggi voglio andare al mare!"  # Example sentence to translate

# Call the function to get the translation and time taken
answer, time = get_answer(source_language, target_language, text)

# Print the translation and the time
print(answer)
print(f"Time taken: {time} seconds")