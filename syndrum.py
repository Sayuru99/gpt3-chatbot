from dotenv import load_dotenv
from random import choice
from flask import Flask, request, session
import os
import openai

load_dotenv()
open.api_key = os.getenv('OPENAI_API_KEY')
completion = openai.Completion()

start_sequence = "\nSyndrum:"
restart_sequence = "\n\nPerson"
session_prompt = "The following is a story of sahani, just in age 17 she started a affair with Sayuru.And now after 5 years they are very lovely couple and sayuru become a software engineer and sahani became a agricultural sciencist. So what is going on with them?"

def write_story(session_story=None):
    if session_story == None: 
        prompt_text = session_prompt
    else:
        prompt_text = session_story
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.7,
      max_tokens=96,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
    )
    story = response['choices'][0]['text']
    return str(story)

    def append_interaction_to_chat_log(questions, answer, chat_log=None):
        if chat_log is None:
            chat_log = session_prompt
        return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"
