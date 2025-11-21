from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
import json
from typing import Dict, Any

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def regenerate_from_structured_data(structured_file: str) -> str:
    try:
        print("Reading structured data...")
        with open(structured_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{structured_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Prepare the structured data for the LLM
    structured_summary = json.dumps(data, indent=2, ensure_ascii=False)
    
    prompt = f"""You are an expert at analyzing podcast content and creating another podcast transcript.
    I will provide you with a structured representation of a podcast transcript that has been organized into topics, 
    nodes (key concepts/entities), and connections (relationships between concepts). The new podcast should be based on the given structured data ONLY.

    Structured Podcast Data:
    {structured_summary}

    The podcast should be detailed enough to give someone who hasn't listened to the podcast a complete understanding of the content so all content of the given structured_schema is present and concise enough to be readable.
    Format your response as a clear, well-structured podcast with appropriate sections if needed and ensure the narrative flows smoothly without gaps or abrupt transitions.
    The generated podcast transcript should be in such form:
    Speaker1 Name
    what he said

    Speaker2 Name
    what he said ...
    """
    
    print("Regenerating podcast from structured data...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert at analyzing and regenerating podcast content based on graph schema. Provide clear, comprehensive, and well-structured regenerated podcast."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7
        )
        
        summary = response.choices[0].message.content
        print("✓ podcast generated from structured data")
        return summary
        
    except Exception as e:
        print(f"Error regenerating podcast: {e}")
        sys.exit(1)


# def judge_summary(
#     summary: str,
#     full_transcript: str,
#     summary_source: str = "Structured Data"
# ) -> Dict[str, Any]:
#     """
#     Use an LLM as a judge to evaluate a summary against the full transcript.
    
#     Args:
#         summary: Summary text to evaluate
#         full_transcript: Full transcript for reference
#         summary_source: Label for the summary source
        
#     Returns:
#         Dictionary with judgment results including score and detailed evaluation
#     """
#     print("Evaluating summary against full transcript...")
    
#     prompt = f"""You are an expert judge evaluating a summary of a podcast against the original transcript.

#             I will provide you with:
#             1. The full transcript of the podcast (the ground truth)
#             2. A summary generated from {summary_source}

#             Your task is to evaluate the summary based on:
#             - Accuracy: How well does it capture the actual content of the podcast?
#             - Completeness: Does it cover the main topics and important points?
#             - Clarity: Is it well-written and easy to understand?
#             - Coherence: Does it flow well and make sense as a narrative?
#             - Insight: Does it capture the key insights and important takeaways?

#             Full Transcript (Ground Truth):
#             {full_transcript}

#             ---

#             Summary (from {summary_source}):
#             {summary}

#             ---

#             Please provide your evaluation as a JSON object with the following structure:
#             {{
#                 "score": <overall score from 1-10>,
#                 "accuracy_score": <score from 1-10 for accuracy>,
#                 "completeness_score": <score from 1-10 for completeness>,
#                 "clarity_score": <score from 1-10 for clarity>,
#                 "coherence_score": <score from 1-10 for coherence>
#                 "justification": <explanation your choice of the scores>
#             }}
#         """
    
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": "You are an expert judge evaluating summaries. Be thorough, fair, and provide detailed reasoning. Always return valid JSON."
#                 },
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],
#             temperature=0.3,
#             response_format={"type": "json_object"}
#         )
        
#         judgment = json.loads(response.choices[0].message.content)
#         print("✓ Judgment completed")
#         return judgment
        
#     except Exception as e:
#         print(f"Error in judgment: {e}")
#         import traceback
#         traceback.print_exc()
#         sys.exit(1)


# def save_summary_and_judgment(
#     summary: str,
#     judgment: Dict[str, Any],
#     output_dir: str = "summaries"
# ) -> None:
#     """
#     Save summary and judgment to files.
    
#     Args:
#         summary: Summary text
#         judgment: Judgment results
#         output_dir: Directory to save files
#     """
#     # Create output directory if it doesn't exist
#     os.makedirs(output_dir, exist_ok=True)
    
#     # Save summary and judgment
#     summary_file = os.path.join(output_dir, "summary_from_structured_data.txt")
#     judgment_file = os.path.join(output_dir, "judgment.json")
    
#     print(f"\nSaving results to {output_dir}/...")
    
#     try:
#         with open(summary_file, "w", encoding="utf-8") as f:
#             f.write(summary)
#         print(f"  ✓ Saved: {summary_file}")
        
#         with open(judgment_file, "w", encoding="utf-8") as f:
#             json.dump(judgment, f, indent=2, ensure_ascii=False)
#         print(f"  ✓ Saved: {judgment_file}")
        
#     except Exception as e:
#         print(f"Error saving files: {e}")
#         sys.exit(1)
def save_podcast(text: str, output_dir: str = "Regenerated_Podcasts") -> None:
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "regenerated_podcast.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"✓ Regenerated podcast saved to: {output_file}")


def main():
    """Main function to recostruct podcast from structured data"""
    print("=" * 80)
    
    # File paths
    structured_file = "final_result.json"
    transcript_file = "transcription.txt"
    
    # Step 1: Generate summary from structured data
    print("\n[STEP 1] Regenerating podcast content from structured data...")
    print("-" * 80)
    new_podcast = regenerate_from_structured_data(structured_file)
    
    # Step 2: Read full transcript
    print("\n[STEP 2] Reading full transcript...")
    print("-" * 80)
    try:
        with open(transcript_file, "r", encoding="utf-8") as f:
            full_transcript = f.read()
        print(f"✓ Transcript loaded ({len(full_transcript)} characters)")
    except FileNotFoundError:
        print(f"Error: Transcript file '{transcript_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading transcript: {e}")
        sys.exit(1)
    
    # # Step 3: Evaluate summary against transcript
    # print("\n[STEP 3] Evaluating summary against transcript...")
    # print("-" * 80)
    # judgment = judge_summary(
    #     summary,
    #     full_transcript,
    #     summary_source="Structured Data"
    # )
    
    # # Step 4: Save results
    # print("\n[STEP 4] Saving results...")
    # print("-" * 80)
    # save_summary_and_judgment(summary, judgment)
    
    # Print judgment results
    # print("\n" + "=" * 80)
    # print("EVALUATION RESULTS")
    # print("=" * 80)
    # print(f"Overall Score: {judgment.get('score', 'N/A')}/10")
    # print(f"\nDetailed Scores:")
    # print(f"  - Accuracy: {judgment.get('accuracy_score', 'N/A')}/10")
    # print(f"  - Completeness: {judgment.get('completeness_score', 'N/A')}/10")
    # print(f"  - Clarity: {judgment.get('clarity_score', 'N/A')}/10")
    # print(f"  - Coherence: {judgment.get('coherence_score', 'N/A')}/10")
    # print(f"  - Insight: {judgment.get('insight_score', 'N/A')}/10")
    # print(f"\nOverall Assessment:\n{judgment.get('overall_assessment', 'N/A')}")
    # print(f"\nStrengths:\n{judgment.get('strengths', 'N/A')}")
    # print(f"\nWeaknesses:\n{judgment.get('weaknesses', 'N/A')}")
    # print("=" * 80)
    save_podcast(new_podcast)

    print("\n✓ Regenrated Podcasts are save to 'Regenerated_Podcasts/' directory")


if __name__ == "__main__":
    main()

