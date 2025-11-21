from enum import Enum
from typing import Dict, Any, List


class ConnectionType(Enum):
    """Enumeration of all available connection types across all schemas."""
    # Narrative schema connections
    ACTION_RELATION = "ACTION_RELATION"
    SPATIAL_RELATION = "SPATIAL_RELATION"
    TEMPORAL_RELATION = "TEMPORAL_RELATION"
    
    # Descriptive schema connections
    HAS = "HAS"
    IS = "IS"
    
    # Informative schema connections
    CONCEPT_TO_CONCEPT = "CONCEPT_TO_CONCEPT"
    IS_DEFINITION = "IS_DEFINITION"
    IS_EXAMPLE = "IS_EXAMPLE"
    IS_EXPLANATION = "IS_EXPLANATION"
    
    # Instructional schema connections
    SEQUENTIAL_RELATION = "SEQUENTIAL_RELATION"
    CONDITIONAL_RELATION = "CONDITIONAL_RELATION"
    
    # Argumentative schema connections
    SUPPORTING_RELATION = "SUPPORTING_RELATION"
    COUNTER_SUPPORTING_RELATION = "COUNTER_SUPPORTING_RELATION"
    CONCLUSION_RELATION = "CONCLUSION_RELATION"


class ConnectionTypeDefinition:
    """
    Defines connection types with their descriptions, characteristics, and usage.
    """
    
    DEFINITIONS = {
        # Narrative schema connections
        ConnectionType.ACTION_RELATION: {
            "description": "Represents a relationship where one entity performs an action involving another entity",
            "characteristics": [
                "Subject-verb-object relationships",
                "Actions performed by characters",
                "Interactions between entities",
                "Agent-action-patient patterns"
            ],
            "usage": "Used in narrative schemas to connect characters/entities with their actions",
            "example": "CHARACTER --[ACTION_RELATION]--> OBJECT (e.g., 'John opened the door')"
        },
        ConnectionType.SPATIAL_RELATION: {
            "description": "Represents spatial or locational relationships between entities",
            "characteristics": [
                "Location relationships (in, on, at, near)",
                "Spatial positioning",
                "Geographical relationships",
                "Where entities are located"
            ],
            "usage": "Used in narrative schemas to represent where entities are located",
            "example": "CHARACTER --[SPATIAL_RELATION]--> LOCATION (e.g., 'John is in the kitchen')"
        },
        ConnectionType.TEMPORAL_RELATION: {
            "description": "Represents temporal or time-based relationships between events or entities",
            "characteristics": [
                "Chronological sequences (before, after, during)",
                "Time-based ordering",
                "Temporal dependencies",
                "Event sequencing"
            ],
            "usage": "Used in narrative schemas to represent temporal ordering of events",
            "example": "EVENT1 --[TEMPORAL_RELATION]--> EVENT2 (e.g., 'Event A happened before Event B')"
        },
        
        # Descriptive schema connections
        ConnectionType.HAS: {
            "description": "Represents a possession or attribute relationship where one entity has a property",
            "characteristics": [
                "Possession relationships",
                "Attribute ownership",
                "Has-a relationships",
                "Property relationships"
            ],
            "usage": "Used in descriptive schemas to connect subjects with their attributes or features",
            "example": "SUBJECT --[HAS]--> ATTRIBUTE (e.g., 'The car has red color')"
        },
        ConnectionType.IS: {
            "description": "Represents an identity or classification relationship",
            "characteristics": [
                "Identity relationships",
                "Classification (is-a relationships)",
                "Equivalence",
                "Type relationships"
            ],
            "usage": "Used in descriptive schemas to represent what something is or classify it",
            "example": "SUBJECT --[IS]--> FEATURE (e.g., 'The rose is a flower')"
        },
        
        # Informative schema connections
        ConnectionType.CONCEPT_TO_CONCEPT: {
            "description": "Represents a relationship between two concepts",
            "characteristics": [
                "Conceptual relationships",
                "Related concepts",
                "Conceptual associations",
                "Topic relationships"
            ],
            "usage": "Used in informative schemas to connect related concepts",
            "example": "CONCEPT1 --[CONCEPT_TO_CONCEPT]--> CONCEPT2 (e.g., 'AI is related to Machine Learning')"
        },
        ConnectionType.IS_DEFINITION: {
            "description": "Represents a definition relationship where one entity defines another",
            "characteristics": [
                "Definition relationships",
                "What something means",
                "Term definitions",
                "Conceptual definitions"
            ],
            "usage": "Used in informative schemas to connect terms with their definitions",
            "example": "CONCEPT --[IS_DEFINITION]--> DEFINITION (e.g., 'AI is the simulation of human intelligence')"
        },
        ConnectionType.IS_EXAMPLE: {
            "description": "Represents an example relationship where one entity exemplifies another",
            "characteristics": [
                "Example relationships",
                "Illustrative instances",
                "Concrete examples",
                "Instance-of relationships"
            ],
            "usage": "Used in informative schemas to connect concepts with examples",
            "example": "CONCEPT --[IS_EXAMPLE]--> EXAMPLE (e.g., 'ChatGPT is an example of AI')"
        },
        ConnectionType.IS_EXPLANATION: {
            "description": "Represents an explanation relationship where one entity explains another",
            "characteristics": [
                "Explanation relationships",
                "Clarification relationships",
                "How/why explanations",
                "Elaboration relationships"
            ],
            "usage": "Used in informative schemas to connect concepts with their explanations",
            "example": "CONCEPT --[IS_EXPLANATION]--> EXPLANATION (e.g., 'Neural networks explain how AI learns')"
        },
        
        # Instructional schema connections
        ConnectionType.SEQUENTIAL_RELATION: {
            "description": "Represents a sequential relationship where one step follows another",
            "characteristics": [
                "Step ordering (first, then, next)",
                "Sequential dependencies",
                "Procedural ordering",
                "Before/after in procedures"
            ],
            "usage": "Used in instructional schemas to represent the order of steps",
            "example": "STEP1 --[SEQUENTIAL_RELATION]--> STEP2 (e.g., 'Step 1 must be done before Step 2')"
        },
        ConnectionType.CONDITIONAL_RELATION: {
            "description": "Represents a conditional relationship where one entity depends on another",
            "characteristics": [
                "If-then relationships",
                "Dependencies",
                "Prerequisites",
                "Conditional logic"
            ],
            "usage": "Used in instructional schemas to represent conditions or prerequisites",
            "example": "ACTION --[CONDITIONAL_RELATION]--> CONDITION (e.g., 'You can proceed if the condition is met')"
        },
        
        # Argumentative schema connections
        ConnectionType.SUPPORTING_RELATION: {
            "description": "Represents a supporting relationship where one entity supports another",
            "characteristics": [
                "Support relationships",
                "Evidence supporting claims",
                "Arguments supporting positions",
                "Strengthening relationships"
            ],
            "usage": "Used in argumentative schemas to connect claims with supporting evidence or arguments",
            "example": "EVIDENCE --[SUPPORTING_RELATION]--> CLAIM (e.g., 'Data supports the claim')"
        },
        ConnectionType.COUNTER_SUPPORTING_RELATION: {
            "description": "Represents a counter-supporting relationship where one entity opposes another",
            "characteristics": [
                "Opposition relationships",
                "Contradicting evidence",
                "Counterarguments",
                "Weakening relationships"
            ],
            "usage": "Used in argumentative schemas to connect claims with counterarguments or opposing evidence",
            "example": "COUNTER_ARGUMENT --[COUNTER_SUPPORTING_RELATION]--> CLAIM (e.g., 'This argument contradicts the claim')"
        },
        ConnectionType.CONCLUSION_RELATION: {
            "description": "Represents a conclusion relationship where one entity leads to a conclusion",
            "characteristics": [
                "Conclusion relationships",
                "Logical conclusions",
                "Inference relationships",
                "Therefore relationships"
            ],
            "usage": "Used in argumentative schemas to connect arguments/evidence with conclusions",
            "example": "ARGUMENT --[CONCLUSION_RELATION]--> CONCLUSION (e.g., 'The argument leads to this conclusion')"
        }
    }
    
    @classmethod
    def get_definition(cls, connection_type: ConnectionType) -> Dict[str, Any]:
        """Get the complete definition for a connection type."""
        return cls.DEFINITIONS.get(connection_type, {
            "description": "No definition available",
            "characteristics": [],
            "usage": "Unknown usage",
            "example": "No example available"
        })
    
    @classmethod
    def get_all_definitions(cls) -> Dict[str, Dict[str, Any]]:
        """Get all connection type definitions."""
        return {
            connection_type.value: cls.get_definition(connection_type)
            for connection_type in ConnectionType
        }
    
    @classmethod
    def get_connection_types_by_category(cls) -> Dict[str, List[str]]:
        """Get connection types organized by schema category."""
        return {
            "narrative": [
                ConnectionType.ACTION_RELATION.value,
                ConnectionType.SPATIAL_RELATION.value,
                ConnectionType.TEMPORAL_RELATION.value
            ],
            "descriptive": [
                ConnectionType.HAS.value,
                ConnectionType.IS.value
            ],
            "informative": [
                ConnectionType.CONCEPT_TO_CONCEPT.value,
                ConnectionType.IS_DEFINITION.value,
                ConnectionType.IS_EXAMPLE.value,
                ConnectionType.IS_EXPLANATION.value
            ],
            "instructional": [
                ConnectionType.SEQUENTIAL_RELATION.value,
                ConnectionType.CONDITIONAL_RELATION.value
            ],
            "argumentative": [
                ConnectionType.SUPPORTING_RELATION.value,
                ConnectionType.COUNTER_SUPPORTING_RELATION.value,
                ConnectionType.CONCLUSION_RELATION.value
            ]
        }
    
    @classmethod
    def get_directionality(cls, connection_type: ConnectionType) -> str:
        """
        Get the directionality of a connection type.
        
        Returns:
            "directed" if the connection has a clear direction (e.g., supports, precedes)
            "undirected" if the connection is bidirectional (e.g., related_to)
        """
        # Most connections are directed, but some could be undirected
        # For now, all are directed based on the schema definitions
        return "directed"
    
    @classmethod
    def get_allowed_node_pairs(cls, connection_type: ConnectionType) -> List[tuple]:
        """
        Get examples of allowed node type pairs for a connection type.
        This helps validate graph construction.
        """
        pairs = {
            ConnectionType.ACTION_RELATION: [
                ("CHARACTER", "OBJECT"),
                ("CHARACTER", "LOCATION"),
                ("GROUP", "OBJECT")
            ],
            ConnectionType.SPATIAL_RELATION: [
                ("CHARACTER", "LOCATION"),
                ("OBJECT", "LOCATION"),
                ("GROUP", "LOCATION")
            ],
            ConnectionType.TEMPORAL_RELATION: [
                ("CHARACTER", "CHARACTER"),  # Character's actions over time
                ("OBJECT", "OBJECT")   # Object states over time
            ],
            ConnectionType.HAS: [
                ("SUBJECT", "ATTRIBUTE"),
                ("SUBJECT", "FEATURE"),
                ("SUBJECT", "DETAILS")
            ],
            ConnectionType.IS: [
                ("SUBJECT", "FEATURE"),
                ("SUBJECT", "ATTRIBUTE")
            ],
            ConnectionType.CONCEPT_TO_CONCEPT: [
                ("CONCEPT", "CONCEPT")
            ],
            ConnectionType.IS_DEFINITION: [
                ("CONCEPT", "DEFINITION")
            ],
            ConnectionType.IS_EXAMPLE: [
                ("CONCEPT", "EXAMPLE"),
                ("FACT", "EXAMPLE")
            ],
            ConnectionType.IS_EXPLANATION: [
                ("CONCEPT", "EXPLANATION"),
                ("FACT", "EXPLANATION")
            ],
            ConnectionType.SEQUENTIAL_RELATION: [
                ("STEP", "STEP"),
                ("ACTION", "ACTION")
            ],
            ConnectionType.CONDITIONAL_RELATION: [
                ("ACTION", "CONDITION"),
                ("STEP", "CONDITION"),
                ("ACTION", "TOOL")
            ],
            ConnectionType.SUPPORTING_RELATION: [
                ("EVIDENCE", "CLAIM"),
                ("ARGUMENT", "CLAIM"),
                ("FACT", "CLAIM")
            ],
            ConnectionType.COUNTER_SUPPORTING_RELATION: [
                ("COUNTER_ARGUMENT", "CLAIM"),
                ("EVIDENCE", "CLAIM")
            ],
            ConnectionType.CONCLUSION_RELATION: [
                ("ARGUMENT", "CONCLUSION"),
                ("EVIDENCE", "CONCLUSION"),
                ("CLAIM", "CONCLUSION")
            ]
        }
        return pairs.get(connection_type, [])

