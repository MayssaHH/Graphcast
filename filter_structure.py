import json
import sys
from typing import Dict, Any, List


def filter_structured_data(input_file: str, output_file: str) -> Dict[str, Any]:
    """
    Filter structured output to keep only required fields:
    - title
    - nodes: id, content, speaker
    - connections: id, content, source_node_id, target_node_id
    
    Args:
        input_file: Path to the input structured JSON file
        output_file: Path to save the filtered output JSON file
        
    Returns:
        Dictionary containing filtered data
    """
    try:
        # Read the input file
        print(f"Reading structured data from: {input_file}")
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in input file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Filter each topic
    filtered_data = {}
    total_topics = len(data)
    
    print(f"\nFound {total_topics} topics to filter")
    print("=" * 80)
    
    for topic_key, topic_data in data.items():
        # Extract title
        title = topic_data.get("title", "")
        
        # Filter nodes: keep only id, content, speaker
        nodes = []
        for node in topic_data.get("nodes", []):
            filtered_node = {
                "id": node.get("id", ""),
                "content": node.get("content", ""),
                "speaker": node.get("speaker", "")
            }
            nodes.append(filtered_node)
        
        # Filter connections: keep only id, content, source_node_id, target_node_id
        connections = []
        for conn in topic_data.get("connections", []):
            filtered_conn = {
                "id": conn.get("id", ""),
                "content": conn.get("content", ""),
                "source_node_id": conn.get("source_node_id", ""),
                "target_node_id": conn.get("target_node_id", "")
            }
            connections.append(filtered_conn)
        
        # Create filtered topic entry
        filtered_data[topic_key] = {
            "title": title,
            "nodes": nodes,
            "connections": connections
        }
        
        print(f"✓ Filtered {topic_key}: {len(nodes)} nodes, {len(connections)} connections")
    
    # Save filtered data
    print("\n" + "=" * 80)
    print(f"Saving filtered data to: {output_file}")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(filtered_data, f, indent=2, ensure_ascii=False)
        print(f"✓ Successfully saved filtered data to {output_file}")
    except Exception as e:
        print(f"✗ Error saving output file: {e}")
        sys.exit(1)
    
    # Print summary
    print("\n" + "=" * 80)
    print("FILTERING SUMMARY")
    print("=" * 80)
    total_nodes = sum(len(topic.get("nodes", [])) for topic in filtered_data.values())
    total_connections = sum(len(topic.get("connections", [])) for topic in filtered_data.values())
    
    print(f"Total topics: {len(filtered_data)}")
    print(f"Total nodes: {total_nodes}")
    print(f"Total connections: {total_connections}")
    print("=" * 80)
    
    return filtered_data


def main():
    """Main function for command-line usage."""
    if len(sys.argv) < 2:
        print("Usage: python filter_structure.py [input_file] [output_file]")
        print("  input_file: Path to structured JSON file (default: structured_output_2.json)")
        print("  output_file: Path to save filtered output (default: final_result.json)")
        print("\nExample:")
        print("  python filter_structure.py structured_output_2.json final_result.json")
        sys.exit(1)
    
    input_file = sys.argv[1] if len(sys.argv) > 1 else "structured_output_2.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "final_result.json"
    
    filter_structured_data(input_file, output_file)


if __name__ == "__main__":
    main()

