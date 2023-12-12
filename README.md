# AI_Keyboard

This repository contains Python code for interacting with the OpenAI GPT-3.5 Turbo model to generate natural language responses based on user input.

## Getting Started

### Prerequisites

Before running the code, you need to have an OpenAI API key. If you don't have one, sign up for the OpenAI API and obtain your API key.

### Installation

1. Install the required dependencies:

    ```bash
    pip install openai
    ```

2. Replace `"YOUR_OPENAI_API_KEY"` in the code with your actual OpenAI API key.
3. Set your option in the `option` variable. 

## Usage

The main script, `ai_keyboard_gpt3.5.py`, allows you to interact with the OpenAI GPT-3.5 Turbo model. Modify the `option` variable to choose the desired chatbot behavior:

- **Tone Options:**
  - Happy: `option = 1`
  - Sad: `option = 2`
  - Friendly: `option = 3`
  - Romantic: `option = 4`
  - Angry: `option = 5`
  - Professional: `option = 6`

- **Content Options:**
  - Expand: `option = 7`
  - Paraphrase: `option = 8`
  - Summarize: `option = 9`
  - Reply: `option = 10`

Enter user input when prompted, and the chatbot will generate responses based on the selected option.

## Configuration

Adjust the `temperature` variable to control the randomness of the generated responses. Higher values make responses more random, while lower values make them more deterministic.

## Acknowledgments

- The Openai `gpt-3.5-turbo` model is used for modifying tone and content based responses based on user input.
