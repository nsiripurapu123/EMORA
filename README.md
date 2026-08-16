# EMORA – Empathetic Social Chatbot

EMORA is an empathetic conversational AI system inspired by the architecture of Microsoft's XiaoIce. The project focuses on building more engaging and context-aware conversations by combining Natural Language Understanding (NLU), emotion detection, dialogue management, and response generation.

## Overview

Traditional chatbots often focus primarily on completing specific tasks. EMORA explores a more social and empathetic approach to conversational AI by considering the user's intent, emotional state, and conversation context when generating responses.

The system is designed as a modular conversational pipeline in which different components handle different stages of the interaction.

## Architecture

User Input → Intent Classification → Emotion Detection → Dialogue Management → Skills / User Memory → Response Generation → Generated Response

## Key Features

- Natural Language Understanding
- Intent classification
- Emotion detection
- Context-aware dialogue management
- Emotion-aware response generation
- Multi-turn conversational flow
- Modular skill-based architecture
- User memory and personalization
- REST API interface through Flask

## Project Structure

EMORA/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── nlu/
│   ├── __init__.py
│   ├── intent_classifier.py
│   └── emotion_detector.py
├── dialogue/
│   ├── __init__.py
│   └── manager.py
├── core_chat/
│   ├── __init__.py
│   └── generator.py
├── skills/
│   ├── __init__.py
│   ├── jokes.py
│   └── recommendations.py
├── metrics/
│   ├── __init__.py
│   └── metrics.py
└── memory/
    ├── __init__.py
    └── user_memory.py

## How It Works

EMORA processes a user's message through several stages.

### 1. Intent Classification

The intent classifier analyzes the user's message and determines the type of request or conversational intent.

### 2. Emotion Detection

The emotion detection component analyzes the user's input to identify the emotional state expressed in the message.

### 3. Dialogue Management

The dialogue manager combines information about the user's intent, emotion, and conversational context to determine the appropriate response strategy.

### 4. Skills

EMORA can route appropriate interactions to specialized conversational skills such as jokes and recommendations.

### 5. User Memory

The memory component allows relevant information from the conversation to be retained and used to support more personalized interactions.

### 6. Response Generation

The response generator produces the final response based on the information provided by the preceding components.

## Installation

Clone the repository:

git clone https://github.com/nsiripurapu123/EMORA.git

cd EMORA

Create a virtual environment:

python -m venv venv

Activate the virtual environment.

Windows:

venv\Scripts\activate

macOS / Linux:

source venv/bin/activate

Install the dependencies:

pip install -r requirements.txt

## Usage

Run the main conversational application:

python main.py

If using the Flask API:

python app.py

The API exposes a `/chat` endpoint for sending messages to the chatbot.

## Example

User: I've had a really difficult day.

EMORA: I'm sorry to hear that. Would you like to talk about what happened?

The response pipeline considers both the conversational intent and emotional context when determining an appropriate response.

## Technologies

- Python
- Natural Language Processing
- Applied Machine Learning
- Conversational AI
- Natural Language Understanding
- Emotion Detection
- Dialogue Management
- Flask
- Git / GitHub

## Project Goals

The main goals of EMORA are:

1. Explore empathetic conversational AI.
2. Combine intent and emotion understanding.
3. Maintain conversational context across multiple turns.
4. Create a modular architecture that can be extended with additional conversational skills.
5. Investigate approaches for improving the quality and continuity of human–machine conversations.

## Inspiration

The architecture of EMORA is inspired by research and development surrounding Microsoft's XiaoIce, particularly its focus on long-term engagement, emotional intelligence, and social conversation.

## Future Improvements

Potential improvements include:

- More advanced intent classification
- Improved emotion recognition
- More sophisticated long-term user memory
- Additional conversational skills
- Improved response evaluation
- More extensive automated testing
- Improved API documentation
- Deployment as a production web service

## Academic Project

EMORA was developed as an academic project exploring empathetic social chatbot systems, Natural Language Processing, dialogue systems, and emotion-aware computing.

## Author

Nitin Siripurapu

GitHub: https://github.com/nsiripurapu123
                        v
                 Generated Response
