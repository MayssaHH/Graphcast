from enum import Enum
from typing import List, Dict, Any


class SchemaType(Enum):
    """Enumeration of available schema types."""
    NARRATIVE = "narrative"
    DESCRIPTIVE = "descriptive"
    INFORMATIVE = "informative"
    INSTRUCTIONAL = "instructional"
    ARGUMENTATIVE = "argumentative"


class Schema:
    """
    Defines different text schema types with their characteristics,
    key elements, and allowed node/connection types.
    """
    
    # Schema definitions
    DEFINITIONS = {
        SchemaType.NARRATIVE: (
            "A narrative schema tells a story or recounts events in a chronological sequence. "
            "It focuses on characters, plot development, and the progression of events over time."
        ),
        SchemaType.DESCRIPTIVE: (
            "A descriptive schema provides detailed information about the characteristics, "
            "qualities, or features of a subject, person, place, or object."
        ),
        SchemaType.INFORMATIVE: (
            "An informative schema presents facts, data, and information in an objective manner "
            "to educate or inform the reader about a topic without persuasion."
        ),
        SchemaType.INSTRUCTIONAL: (
            "An instructional schema provides step-by-step guidance, directions, or procedures "
            "to help the reader accomplish a task or understand how something works."
        ),
        SchemaType.ARGUMENTATIVE: (
            "An argumentative schema presents a claim or position supported by evidence, reasoning, "
            "and counterarguments to persuade the reader to accept a particular viewpoint."
        )
    }
    
    # Key elements/characteristics to search for in text
    KEY_CHARACTERISTICS = {
        SchemaType.NARRATIVE: [
            "chronological sequence markers (first, then, next, finally, after, before)",
            "temporal transitions (meanwhile, later, eventually, suddenly)",
            "character actions and dialogue",
            "plot progression and conflict",
            "narrative arc (beginning, middle, end)",
            "storytelling elements (setting, characters, events)",
            "past tense verbs",
            "cause-and-effect relationships in story context",
            "emotional or dramatic elements",
            "resolution or conclusion of events"
        ],
        SchemaType.DESCRIPTIVE: [
            "sensory details (sight, sound, smell, taste, touch)",
            "adjectives and adverbs describing qualities",
            "spatial relationships (above, below, beside, inside)",
            "comparisons and metaphors",
            "detailed observations",
            "physical characteristics",
            "atmospheric or mood descriptions",
            "specific details about appearance, texture, color",
            "figurative language",
            "vivid imagery"
        ],
        SchemaType.INFORMATIVE: [
            "factual statements and data",
            "definitions and explanations",
            "statistics and numerical information",
            "objective language (no opinion markers)",
            "categorization and classification",
            "comparison and contrast of information",
            "cause-and-effect relationships (factual)",
            "examples and illustrations",
            "technical terms and jargon",
            "informational transitions (furthermore, additionally, similarly)"
        ],
        SchemaType.INSTRUCTIONAL: [
            "imperative verbs (do, make, create, follow)",
            "step-by-step sequences (first, second, third, step 1, step 2)",
            "action verbs and commands",
            "procedural language (how to, instructions, guide)",
            "conditional statements (if-then, when, after)",
            "sequential markers (next, then, finally, last)",
            "checklists and numbered lists",
            "prerequisites and requirements",
            "warnings and cautions",
            "goal-oriented language"
        ],
        SchemaType.ARGUMENTATIVE: [
            "claims and thesis statements",
            "evidence and supporting data",
            "reasoning and logical connections",
            "counterarguments and rebuttals",
            "persuasive language (should, must, important, crucial)",
            "rhetorical questions",
            "concessions and acknowledgments",
            "conclusions and calls to action",
            "comparative language (better, worse, superior, inferior)",
            "causal reasoning (because, therefore, as a result)"
        ]
    }
    
    # Allowed node types for each schema
    ALLOWED_NODE_TYPES = {
        SchemaType.NARRATIVE: [
            "CHARACTER",
            "LOCATION",
            "OBJECT",
            "GROUP"
        ],
        SchemaType.DESCRIPTIVE: [
            "SUBJECT",
            "ATTRIBUTE",
            "FEATURE",
            "DETAILS"
        ],
        SchemaType.INFORMATIVE: [
            "CONCEPT",
            "FACT",
            "DEFINITION",
            "EXAMPLE",
            "EXPLANATION"
        ],
        SchemaType.INSTRUCTIONAL: [
            "STEP",
            "ACTION",
            "TOOL",
            "CONDITION",
            "WARNING",
            "GOAL"
        ],
        SchemaType.ARGUMENTATIVE: [
            "CLAIM",
            "ARGUMENT",
            "COUNTER_ARGUMENT",
            "EVIDENCE",
            "CONCLUSION"
        ]
    }
    
    # Allowed connection types for each schema
    ALLOWED_CONNECTION_TYPES = {
        SchemaType.NARRATIVE: [
            "ACTION_RELATION",
            "SPATIAL_RELATION",
            "TEMPORAL_RELATION",
        ],
        SchemaType.DESCRIPTIVE: [
            "HAS",
            "IS",
        ],
        SchemaType.INFORMATIVE: [
            "CONCEPT_TO_CONCEPT",
            "IS_DEFINITION",
            "IS_EXAMPLE",
            "IS_EXPLANATION"
        ],
        SchemaType.INSTRUCTIONAL: [
            "SEQUENTIAL_RELATION",
            "CONDITIONAL_RELATION"
        ],
        SchemaType.ARGUMENTATIVE: [
            "SUPPORTING_RELATION",
            "COUNTER_SUPPORTING_RELATION",
            "CONCLUSION_RELATION"
        ]
    }
    
    def __init__(self, schema_type: SchemaType):
        """
        Initialize a Schema instance.
        
        Args:
            schema_type: The type of schema (narrative, descriptive, etc.)
        """
        if not isinstance(schema_type, SchemaType):
            raise ValueError(f"schema_type must be a SchemaType enum, got {type(schema_type)}")
        self.schema_type = schema_type
    
    def get_definition(self) -> str:
        """Get the definition of this schema type."""
        return self.DEFINITIONS[self.schema_type]
    
    def get_key_characteristics(self) -> List[str]:
        """Get the key elements/characteristics to search for in text."""
        return self.KEY_CHARACTERISTICS[self.schema_type]
    
    def get_allowed_node_types(self) -> List[str]:
        """Get the list of allowed node types for this schema."""
        return self.ALLOWED_NODE_TYPES[self.schema_type]
    
    def get_allowed_connection_types(self) -> List[str]:
        """Get the list of allowed connection types for this schema."""
        return self.ALLOWED_CONNECTION_TYPES[self.schema_type]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_type": self.schema_type.value,
            "definition": self.get_definition(),
            "key_characteristics": self.get_key_characteristics(),
            "allowed_node_types": self.get_allowed_node_types(),
            "allowed_connection_types": self.get_allowed_connection_types()
        }
    
    @classmethod
    def get_all_schemas(cls) -> Dict[str, Dict[str, Any]]:
        return {
            schema_type.value: Schema(schema_type).to_dict()
            for schema_type in SchemaType
        }
    
    def __repr__(self) -> str:
        return f"Schema(type={self.schema_type.value})"
    
    def __str__(self) -> str:
        return f"Schema: {self.schema_type.value}"

