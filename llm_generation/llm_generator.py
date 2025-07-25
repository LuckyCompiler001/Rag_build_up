# === Core ===
import os
import sys
import time
import random

# === Data Handling ===
import pandas as pd
import json

# === NLP + Progress ===
from tqdm import tqdm
import tiktoken

# === OpenAI Client ===
import openai

# === Typing (optional but useful) ===
from typing import List, Dict, Tuple, Optional

from config import client, LLM_MODEL

def generate_answer(prompt: str) -> str:
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()