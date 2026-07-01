from nlu.intent_classifier import get_intent
from nlu.emotion_detector import get_emotion
from dialogue.manager import decide
from core_chat.generator import generate
from skills.jokes import handle as joke_skill
from skills.recommendations import handle as rec_skill

from nlu.intent_classifier import get_intent
from nlu.emotion_detector import get_emotion
from dialogue.manager import decide
from core_chat.generator import generate
from skills.jokes import handle as joke_skill
from skills.recommendations import handle as rec_skill

# Metrics
from metrics.metrics import measure_latency, log, SkillTracker, CPSCounter

# Initialize trackers
skill_tracker = SkillTracker()
cps_counter = CPSCounter()

def chatbot(user_input):
    intent = get_intent(user_input)
    emotion = get_emotion(user_input)

    action = decide(intent, emotion)

    # Route to correct module
    if action == "skill:jokes":
        skill_tracker.log_call(True)
        response = joke_skill()

    elif action == "skill:recommend":
        skill_tracker.log_call(True)
        response = rec_skill()

    else:
        skill_tracker.log_call(False)
        response = generate(user_input)

    return response, intent, emotion, action


if __name__ == "__main__":
    print("Chatbot started. Type 'exit' to stop.\n")

    conversation_turns = []

    while True:
        msg = input("You: ")

        if msg.lower() == "exit":
            break

        # Measure latency
        (response, intent, emotion, action), latency = measure_latency(chatbot, msg)

        print("Bot:", response)

        # Track conversation
        conversation_turns.append(msg)
        conversation_turns.append(response)

        # Log everything
        log({
            "input": msg,
            "response": response,
            "intent": intent,
            "emotion": emotion,
            "action": action,
            "latency": latency
        })

    # After session ends → compute metrics
    cps_counter.add_session(conversation_turns)

    print("\n📊 SESSION METRICS")
    print("CPS:", cps_counter.compute())
    print("Skill Usage Rate:", skill_tracker.usage_rate())