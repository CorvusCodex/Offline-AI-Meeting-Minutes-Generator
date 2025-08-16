from utils import run_llama

def meeting_minutes(transcript):
    prompt = f"Summarize this meeting into minutes with action points:\n{transcript}"
    return run_llama(prompt)

if __name__ == "__main__":
    text = open("meeting.txt").read()
    print(meeting_minutes(text))
