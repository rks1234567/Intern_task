# AI Article Summarizer CLI

A command-line application that summarizes text articles using Google's Gemini API.

## Features

* Command-line interface using argparse
* Reads articles from text files
* Uses Gemini API for summarization
* Supports summary length options
* Supports summary style options
* Handles missing files
* Handles empty files
* Handles missing API keys
* Handles API errors and rate limits

## Requirements

Python 3.14

## Installation

pip install -r requirements.txt

Create a .env file:

GEMINI_API_KEY=YOUR_API_KEY

## Usage

Short formal summary:

python summarize.py article1.txt --length short --style formal

Long casual summary:

python summarize.py article2.txt --length long --style casual

## Project Structure

Day7Task/

├── summarize.py
├── summarizer.py
├── article1.txt
├── article2.txt
├── .env
├── requirements.txt
├── README.md
└── .gitignore

## Concepts Used

* argparse
* File I/O
* Classes and Objects
* Exception Handling
* Environment Variables
* Gemini API Integration
* Git and GitHub
