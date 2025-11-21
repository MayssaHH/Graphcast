from openai import OpenAI
from dotenv import load_dotenv
import os
import sys
import json
from typing import Dict, Any, List, Optional
from schema.schema_type import Schema, SchemaType
from schema.nodes_type import NodeType, NodeTypeDefinition
from schema.connections_type import ConnectionType, ConnectionTypeDefinition

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def system_prompt():
    schema_info = Schema.get_all_schemas()
    
    prompt = f"""You are an expert at analyzing text and identifying its schema type.
    The following are the schema types and their key characteristics:
    {json.dumps(schema_info, indent=2)}
    """
    return prompt


def user_prompt(transcript_chunk: str) -> str:
    """Create a prompt for schema selection."""
    prompt = f"""Read the following transcript chunk and determine which schema type best fits it:
    {transcript_chunk}

Return a JSON object with:
{{
    "selected_schema": "one of: narrative, descriptive, informative, instructional, argumentative",
    "confidence": "high, medium, or low",
    "reasoning": "brief explanation of why this schema was chosen"
}}
"""
    return prompt


def structure_system_prompt(
     schema_type: SchemaType
) -> str:
    """Create a prompt for extracting nodes and connections based on the selected schema."""
    schema = Schema(schema_type)
    allowed_nodes = schema.get_allowed_node_types()
    allowed_connections = schema.get_allowed_connection_types()
    
    # Get node type descriptions
    node_descriptions = {}
    for node_type_str in allowed_nodes:
        try:
            node_type = NodeType[node_type_str]
            node_def = NodeTypeDefinition.get_definition(node_type)
            node_descriptions[node_type_str] = node_def["description"]
        except KeyError:
            node_descriptions[node_type_str] = f"Node type: {node_type_str}"
    
    # Get connection type descriptions
    connection_descriptions = {}
    for conn_type_str in allowed_connections:
        try:
            conn_type = ConnectionType[conn_type_str]
            conn_def = ConnectionTypeDefinition.get_definition(conn_type)
            connection_descriptions[conn_type_str] = conn_def["description"]
        except KeyError:
            connection_descriptions[conn_type_str] = f"Connection type: {conn_type_str}"
    
    prompt = f"""You are an expert at rewriting text into structured information.
    Use the following schema to rewrite the full complete transcript into a structured format. 
    Schema Type: {schema_type.value}
    Schema Definition: {schema.get_definition()}

    Allowed Node Types:
    {json.dumps(node_descriptions, indent=2)}

    Allowed Connection Types:
    {json.dumps(connection_descriptions, indent=2)}
    """
    return prompt

def structure_user_prompt(transcript_chunk: str, transcript_topic) -> str:
    prompt = f"""Transcript chunk:
    {transcript_chunk}

    Extract the complete structure by:
    1. Identifying all entities/concepts as nodes (using only the allowed node types)
    2. Identifying all relationships as connections (using only the allowed connection types)
    3. Preserving the full content of the transcript chunk in the structure

    Return a JSON object with this structure:
    {{
        "topic": "{transcript_topic}",
        "nodes": [
            {{
                "id": "unique identifier (e.g., node_1, node_2)",
                "type": "one of the allowed node types",
                "content": "the text content or description of this node",
                "speaker": "the speaker of the node",
                "text_reference": "the exact text from the transcript that this node represents"
                
            }}
        ],
        "connections": [
            {{
                "id": "unique identifier (e.g., conn_1, conn_2)",
                "type": "one of the allowed connection types",
                "content": "the text content or description of this connection",
                "source_node_id": "id of the source node",
                "target_node_id": "id of the target node",
                "text_reference": "the exact text from the transcript that this connection represents"
            }}
        ]
    }}

    Important:
    - The structure should fully represent the content of the transcript chunk
    - The output JSON object MUST cover the whole transcript chunk, from the beginning to the end. 
    - ALL THE NODES SHOULD BE CONNECTED TO EACH OTHER.
    """
    return prompt


def transcript_to_structured_format(transcript_chunk: str, transcript_topic: str) -> Dict[str, Any]:
    try:
        # Initialize conversation with system prompt
        messages = [
            {
                "role": "system",
                "content": system_prompt()
            },
            {
                "role": "user",
                "content": user_prompt(transcript_chunk)
            }
        ]
        
        # Step 1: Select schema
        print("Step 1: Selecting schema...")
        response1 = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        schema_selection = json.loads(response1.choices[0].message.content)
        selected_schema_str = schema_selection.get("selected_schema")
        
        try:
            schema_type = SchemaType(selected_schema_str)
        except ValueError:
            print(f"Warning: Invalid schema type '{selected_schema_str}', defaulting to informative")
            schema_type = SchemaType.INFORMATIVE
        
        print(f"Selected schema: {selected_schema_str} (confidence: {schema_selection.get('confidence', 'unknown')})")
        print(f"Reasoning: {schema_selection.get('reasoning', 'N/A')}")
        
        # Add assistant's response to conversation history
        messages.append({
            "role": "assistant",
            "content": response1.choices[0].message.content
        })
        
        # Step 2: Generate structured format based on selected schema
        print("Step 2: Generating structured format...")
        
        # Update system message with schema-specific instructions
        messages[0] = {
            "role": "system",
            "content": structure_system_prompt(schema_type)
        }
        
        # Add user message for structure extraction
        messages.append({
            "role": "user",
            "content": structure_user_prompt(transcript_chunk, transcript_topic)
        })
        
        response2 = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.3,
            response_format={"type": "json_object"}
        )
        
        structure_result = json.loads(response2.choices[0].message.content)
        
        # Combine results
        final_result = {
            "schema_type": selected_schema_str,
            "schema_selection": schema_selection,
            **structure_result
        }
        
        print(f"Extracted {len(structure_result.get('nodes', []))} nodes and {len(structure_result.get('connections', []))} connections")
        
        return final_result
        
    except Exception as e:
        print(f"Error in transcript_to_structured_format: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def process_transcript_chunk(transcript_chunk: str, transcript_topic: str) -> Dict[str, Any]:
    print(f"Processing transcript chunk ({len(transcript_chunk)} characters)...")
    return transcript_to_structured_format(transcript_chunk, transcript_topic)



