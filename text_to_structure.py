import json
import sys
from typing import Dict, Any, List
from schema_manager import transcript_to_structured_format


def process_transcript_topics_file(
    input_file: str,
    output_file: str
) -> Dict[str, Any]:
 
    try:
        # Read the input file
        print(f"Reading transcript topics from: {input_file}")
        with open(input_file, "r", encoding="utf-8") as f:
            topics_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Process each topic
    results = {}
    total_topics = len(topics_data)
    
    print(f"\nFound {total_topics} topics to process")
    print("=" * 80)
    
    for topic_key, topic_data in topics_data.items():
        topic_title = topic_data.get("title")
        transcript = topic_data.get("transcript")
        
        if not transcript:
            print(f"\nWarning: {topic_key} has no transcript, skipping...")
            continue
        
        print(f"\nProcessing {topic_key}: {topic_title}")
        print(f"Transcript length: {len(transcript)} characters")
        print("-" * 80)
        
        try:
            # Process the transcript chunk
            structured_result = transcript_to_structured_format(transcript, topic_title)
            
            # Store the result with the same topic key
            results[topic_key] = {
                "title": topic_title,
                "original_transcript": transcript,
                "schema_type": structured_result.get("schema_type"),
                "schema_selection": structured_result.get("schema_selection"),
                "topic": structured_result.get("topic", topic_title),
                "nodes": structured_result.get("nodes", []),
                "connections": structured_result.get("connections", [])
            }
            
            print(f"✓ Successfully processed {topic_key}")
            print(f"  - Schema: {structured_result.get('schema_type', 'unknown')}")
            print(f"  - Nodes: {len(structured_result.get('nodes', []))}")
            print(f"  - Connections: {len(structured_result.get('connections', []))}")
            
        except Exception as e:
            print(f"✗ Error processing {topic_key}: {e}")
            import traceback
            traceback.print_exc()
            # Store error information
            results[topic_key] = {
                "title": topic_title,
                "original_transcript": transcript,
                "error": str(e),
                "nodes": [],
                "connections": []
            }
    
    # Save results to output file
    print("\n" + "=" * 80)
    print(f"Saving results to: {output_file}")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"✓ Successfully saved {len(results)} topics to {output_file}")
    except Exception as e:
        print(f"✗ Error saving output file: {e}")
        sys.exit(1)
    
    # Print summary
    print("\n" + "=" * 80)
    print("PROCESSING SUMMARY")
    print("=" * 80)
    print(f"Total topics processed: {len(results)}")
    
    # Count by schema type
    schema_counts = {}
    total_nodes = 0
    total_connections = 0
    
    for topic_key, result in results.items():
        if "error" not in result:
            schema = result.get("schema_type", "unknown")
            schema_counts[schema] = schema_counts.get(schema, 0) + 1
            total_nodes += len(result.get("nodes", []))
            total_connections += len(result.get("connections", []))
    
    print(f"\nSchema distribution:")
    for schema, count in sorted(schema_counts.items()):
        print(f"  - {schema}: {count} topics")
    
    print(f"\nTotal nodes extracted: {total_nodes}")
    print(f"Total connections extracted: {total_connections}")
    print("=" * 80)
    
    return results


def main():
    """Main function for command-line usage."""
    if len(sys.argv) < 3:
        print("Usage: python text_to_structure.py <input_topics_file> <output_file>")
        print("  input_topics_file: Path to JSON file with topics (e.g., transcription_topics.json)")
        print("  output_file: Path to save the structured output JSON file")
        print("\nExample:")
        print("  python text_to_structure.py transcription_topics.json structured_output.json")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    process_transcript_topics_file(input_file, output_file)


if __name__ == "__main__":
    main()

