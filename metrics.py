import time
import json
import os
from nltk.translate.bleu_score import sentence_bleu
import torch

LOG_FILE = "logs/metrics.json"

# Ensure log folder exists
os.makedirs("logs", exist_ok=True)


# -------------------------
# BASIC UTIL
# -------------------------
def log(data):
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")


# -------------------------
# NLU METRICS
# -------------------------
def accuracy(pred, actual):
    if len(actual) == 0:
        return 0
    correct = sum(p == a for p, a in zip(pred, actual))
    return correct / len(actual)


# -------------------------
# BLEU SCORE
# -------------------------
def bleu(reference, candidate):
    try:
        return sentence_bleu([reference.split()], candidate.split())
    except:
        return 0


# -------------------------
# PERPLEXITY
# -------------------------
def perplexity(model, input_ids):
    try:
        with torch.no_grad():
            outputs = model(input_ids, labels=input_ids)
            loss = outputs.loss
        return torch.exp(loss).item()
    except:
        return None


# -------------------------
# LATENCY TRACKER
# -------------------------
def measure_latency(func, *args):
    start = time.time()
    result = func(*args)
    latency = time.time() - start
    return result, latency


# -------------------------
# CPS (Conversation Turns Per Session)
# -------------------------
class CPSCounter:
    def __init__(self):
        self.sessions = []

    def add_session(self, turns):
        self.sessions.append(turns)

    def compute(self):
        if len(self.sessions) == 0:
            return 0
        total_turns = sum(len(s) for s in self.sessions)
        return total_turns / len(self.sessions)


# -------------------------
# SKILL USAGE TRACKING
# -------------------------
class SkillTracker:
    def __init__(self):
        self.skill_calls = 0
        self.total_calls = 0

    def log_call(self, used_skill):
        self.total_calls += 1
        if used_skill:
            self.skill_calls += 1

    def usage_rate(self):
        if self.total_calls == 0:
            return 0
        return self.skill_calls / self.total_calls