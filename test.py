import os
from pocketsphinx import LiveSpeech

speech = LiveSpeech(
    verbose=False,
    sampling_rate=44100,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(os.path.dirname(__file__), "models/en-us"),  # fixed
    lm=False,
    dict="words.dict",
    kws="keywords.list"
)

print("🎤 Listening... Say 'help' or 'sos' to trigger SOS.")

for phrase in speech:
    print("Heard:", phrase)  # debug
    keyword = str(phrase).lower()
    if "help" in keyword:
        print("🚨 SOS Triggered: HELP detected!")
    elif "sos" in keyword:
        print("🚨 SOS Triggered: SOS detected!")
