from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
import json
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

def System_prompt():
    return f"""You are an expert at reading, understanding and analyzing transcripts of podcasts. 
    Your job is to return for the user the complete transcript of the podcast, classified into topics.
    Based on the conversation and the discussion between the speakers, you must classify the transcript into key topics in the same order as they were discussed.
    You must retunr the FULL TRANSCRIPT, not just parts of it. You are only allowed to do to classification, not to add neither to remove any text from the transcript.

    You must return the COMPLETE TRANSCRIPT in the following JSON output format for the user:
    {{
        "topic_1": {{
            "title": "title of the first topic",
            "transcript": "all transcript chunks that cover the first topic" (this should start with the first sentence of the transcript)
        }},
        "topic_2": {{
            "title": "title of the second topic",
            "transcript": "all transcript chunks that cover the second topic"
        }},
        "topic_3": {{
            "title": "title of the third topic",
            "transcript": "all transcript chunks that cover the third topic"
        }},
        ...
        "topic_n": {{
            "title": "title of the tenth topic",
            "transcript": "all transcript chunks that cover the tenth topic" (this should end with the last sentence of the transcript)
        }}
    }}

    Instructions:
    - Don't include any other text in your response except the JSON output format.
    - The topics should cover the whole conversation, FROM THE EVERY BEGINNING TO THE EVERY END. Which means you MUST return back the WHOLE transcript classified in topics as explained in the JSON output format.
    - The topics must be different. No topic should be a subset of another topic. Limit the number of topics as much as possible. 
    - Don't change anything (no added text, no removed text, no changed text) in the transcript. Just classify it into topics. 
    - The topics should be different from each other. Each topic should cover a considerable amount of the transcript, from the beginning to the end.
    - Keep the speaker names in the transcript.
    """

def User_prompt(transcript):
    return f"""Read the following podcast transcript and return the COMPLETE TRANSCRIPT CLASSIFIED INTO TOPICS.  
            Transcript:
            {transcript}
        """

def extract_topics(transcript_path):
    try:
        with open(transcript_path, "r", encoding="utf-8") as f:
            transcript = f.read()
    except FileNotFoundError:
        print(f"Error: Transcript file '{transcript_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading transcript file: {e}")
        sys.exit(1)
    
    # Check if transcript is too long (OpenAI has token limits)
    # Rough estimate: 1 token ≈ 4 characters
    if len(transcript) > 100000:  # Approx 25k tokens
        print("Warning: Transcript is very long. Consider chunking it for better results.")
    
    try:
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": System_prompt()
                },
                {
                    "role": "user",
                    "content": User_prompt(transcript)
                }
            ],
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        topics_json = response.choices[0].message.content
        try:
            topics = json.loads(topics_json)
            return topics
        except json.JSONDecodeError as json_err:
            print(f"Error: API response is not valid JSON.")
            print(f"Response content: {topics_json[:500]}...")
            print(f"JSON decode error: {json_err}")
            sys.exit(1)
    
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        sys.exit(1)


def main():
    # Default transcript file, but allow command line argument
    transcript_file = sys.argv[1] if len(sys.argv) > 1 else "transcription.txt"
    
    print(f"Extracting topics from: {transcript_file}")
    print("This may take a moment...\n")
    
    topics = extract_topics(transcript_file)
    
    print("=" * 80)
    print("MAIN TOPICS EXTRACTED:")
    print("=" * 80)
    print(json.dumps(topics, indent=2, ensure_ascii=False))
    print("=" * 80)
    
    # Optionally save to file
    output_file = transcript_file.replace(".txt", "_topics.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(topics, f, indent=2, ensure_ascii=False)
    
    print(f"\nTopics saved to: {output_file}")


if __name__ == "__main__":
    main()

