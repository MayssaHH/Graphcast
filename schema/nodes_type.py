from enum import Enum
from typing import Dict, Any, List


class NodeType(Enum):
    """Enumeration of all available node types across all schemas."""
    # Narrative schema nodes
    CHARACTER = "CHARACTER"
    LOCATION = "LOCATION"
    OBJECT = "OBJECT"
    GROUP = "GROUP"
    
    # Descriptive schema nodes
    SUBJECT = "SUBJECT"
    ATTRIBUTE = "ATTRIBUTE"
    FEATURE = "FEATURE"
    DETAILS = "DETAILS"
    
    # Informative schema nodes
    CONCEPT = "CONCEPT"
    FACT = "FACT"
    DEFINITION = "DEFINITION"
    EXAMPLE = "EXAMPLE"
    EXPLANATION = "EXPLANATION"
    
    # Instructional schema nodes
    STEP = "STEP"
    ACTION = "ACTION"
    TOOL = "TOOL"
    CONDITION = "CONDITION"
    WARNING = "WARNING"
    GOAL = "GOAL"
    
    # Argumentative schema nodes
    CLAIM = "CLAIM"
    ARGUMENT = "ARGUMENT"
    COUNTER_ARGUMENT = "COUNTER_ARGUMENT"
    EVIDENCE = "EVIDENCE"
    CONCLUSION = "CONCLUSION"


class NodeTypeDefinition:
    """
    Defines node types with their descriptions, characteristics, and usage.
    """
    
    DEFINITIONS = {
        # Narrative schema nodes
        NodeType.CHARACTER: {
            "description": "Represents a person, character, or individual mentioned in the narrative",
            "characteristics": [
                "Named individuals",
                "Character roles (protagonist, antagonist, etc.)",
                "Personal attributes or traits",
                "Actions performed by the person"
            ],
            "usage": "Used in narrative schemas to represent characters and their roles in the story"
        },
        NodeType.LOCATION: {
            "description": "Represents a place, setting, or geographical location in the narrative",
            "characteristics": [
                "Physical places (cities, buildings, rooms)",
                "Geographical locations",
                "Settings where events occur",
                "Spatial contexts"
            ],
            "usage": "Used in narrative schemas to represent where events take place"
        },
        NodeType.OBJECT: {
            "description": "Represents a physical object, item, or thing mentioned in the narrative",
            "characteristics": [
                "Physical items",
                "Objects that play a role in the story",
                "Items that characters interact with",
                "Tangible entities"
            ],
            "usage": "Used in narrative schemas to represent objects that appear in the story"
        },
        NodeType.GROUP: {
            "description": "Represents a collection of people, organizations, or entities",
            "characteristics": [
                "Organizations or institutions",
                "Groups of people",
                "Collective entities",
                "Social structures"
            ],
            "usage": "Used in narrative schemas to represent groups or organizations"
        },
        
        # Descriptive schema nodes
        NodeType.SUBJECT: {
            "description": "Represents the main subject or entity being described",
            "characteristics": [
                "The primary focus of description",
                "Can be a person, place, object, or abstract concept",
                "The central entity being characterized"
            ],
            "usage": "Used in descriptive schemas as the main entity being described"
        },
        NodeType.ATTRIBUTE: {
            "description": "Represents a quality, property, or characteristic of a subject",
            "characteristics": [
                "Qualities or properties",
                "Adjectives describing the subject",
                "Inherent characteristics",
                "Distinguishing features"
            ],
            "usage": "Used in descriptive schemas to represent qualities of the subject"
        },
        NodeType.FEATURE: {
            "description": "Represents a notable or distinctive aspect of the subject",
            "characteristics": [
                "Distinctive aspects",
                "Notable characteristics",
                "Prominent elements",
                "Key distinguishing features"
            ],
            "usage": "Used in descriptive schemas to highlight important aspects"
        },
        NodeType.DETAILS: {
            "description": "Represents specific, detailed information about the subject",
            "characteristics": [
                "Specific information",
                "Detailed observations",
                "Particular aspects",
                "Granular descriptions"
            ],
            "usage": "Used in descriptive schemas to provide specific details"
        },
        
        # Informative schema nodes
        NodeType.CONCEPT: {
            "description": "Represents an abstract idea, concept, or topic being explained",
            "characteristics": [
                "Abstract ideas or topics",
                "Theoretical concepts",
                "Main topics of discussion",
                "Core ideas"
            ],
            "usage": "Used in informative schemas to represent main concepts"
        },
        NodeType.FACT: {
            "description": "Represents a factual statement, data point, or verifiable information",
            "characteristics": [
                "Verifiable information",
                "Objective data",
                "Statements of truth",
                "Empirical information"
            ],
            "usage": "Used in informative schemas to present factual information"
        },
        NodeType.DEFINITION: {
            "description": "Represents a definition or explanation of what something means",
            "characteristics": [
                "Formal definitions",
                "Meaning explanations",
                "Term clarifications",
                "Conceptual boundaries"
            ],
            "usage": "Used in informative schemas to define terms or concepts"
        },
        NodeType.EXAMPLE: {
            "description": "Represents an example or instance that illustrates a concept",
            "characteristics": [
                "Concrete instances",
                "Illustrative cases",
                "Specific examples",
                "Real-world instances"
            ],
            "usage": "Used in informative schemas to provide examples"
        },
        NodeType.EXPLANATION: {
            "description": "Represents an explanation that clarifies or elaborates on a concept",
            "characteristics": [
                "Clarifications",
                "Elaborations",
                "Detailed explanations",
                "How or why explanations"
            ],
            "usage": "Used in informative schemas to explain concepts in detail"
        },
        
        # Instructional schema nodes
        NodeType.STEP: {
            "description": "Represents a discrete step in a procedure or process",
            "characteristics": [
                "Individual steps in a sequence",
                "Ordered actions",
                "Procedural elements",
                "Sequential components"
            ],
            "usage": "Used in instructional schemas to represent steps in a process"
        },
        NodeType.ACTION: {
            "description": "Represents an action or task that needs to be performed",
            "characteristics": [
                "Verbs or action words",
                "Tasks to complete",
                "Operations to perform",
                "Activities"
            ],
            "usage": "Used in instructional schemas to represent actions to take"
        },
        NodeType.TOOL: {
            "description": "Represents a tool, resource, or instrument needed for a task",
            "characteristics": [
                "Physical or digital tools",
                "Resources required",
                "Instruments or equipment",
                "Necessary items"
            ],
            "usage": "Used in instructional schemas to represent required tools or resources"
        },
        NodeType.CONDITION: {
            "description": "Represents a condition, requirement, or prerequisite",
            "characteristics": [
                "If-then conditions",
                "Prerequisites",
                "Requirements",
                "Necessary conditions"
            ],
            "usage": "Used in instructional schemas to represent conditions or requirements"
        },
        NodeType.WARNING: {
            "description": "Represents a warning, caution, or important notice",
            "characteristics": [
                "Cautions or warnings",
                "Important notices",
                "Safety information",
                "Critical alerts"
            ],
            "usage": "Used in instructional schemas to highlight warnings or cautions"
        },
        NodeType.GOAL: {
            "description": "Represents the goal, objective, or desired outcome",
            "characteristics": [
                "End objectives",
                "Desired outcomes",
                "Target states",
                "Purpose or aim"
            ],
            "usage": "Used in instructional schemas to represent the goal of the procedure"
        },
        
        # Argumentative schema nodes
        NodeType.CLAIM: {
            "description": "Represents a claim, thesis, or assertion being made",
            "characteristics": [
                "Main arguments or theses",
                "Assertions or propositions",
                "Central claims",
                "Positions taken"
            ],
            "usage": "Used in argumentative schemas to represent the main claim"
        },
        NodeType.ARGUMENT: {
            "description": "Represents an argument or reasoning that supports a claim",
            "characteristics": [
                "Supporting reasoning",
                "Logical arguments",
                "Rationale",
                "Supporting points"
            ],
            "usage": "Used in argumentative schemas to represent supporting arguments"
        },
        NodeType.COUNTER_ARGUMENT: {
            "description": "Represents an opposing argument or counterpoint",
            "characteristics": [
                "Opposing viewpoints",
                "Counterpoints",
                "Alternative perspectives",
                "Contrary arguments"
            ],
            "usage": "Used in argumentative schemas to represent opposing arguments"
        },
        NodeType.EVIDENCE: {
            "description": "Represents evidence, data, or proof supporting an argument",
            "characteristics": [
                "Supporting data",
                "Proof or evidence",
                "Facts supporting claims",
                "Empirical support"
            ],
            "usage": "Used in argumentative schemas to represent evidence"
        },
        NodeType.CONCLUSION: {
            "description": "Represents a conclusion, summary, or final statement",
            "characteristics": [
                "Final statements",
                "Summaries",
                "Concluding remarks",
                "Final positions"
            ],
            "usage": "Used in argumentative schemas to represent conclusions"
        }
    }
    
    @classmethod
    def get_definition(cls, node_type: NodeType) -> Dict[str, Any]:
        """Get the complete definition for a node type."""
        return cls.DEFINITIONS.get(node_type, {
            "description": "No definition available",
            "characteristics": [],
            "usage": "Unknown usage"
        })
    
    @classmethod
    def get_all_definitions(cls) -> Dict[str, Dict[str, Any]]:
        """Get all node type definitions."""
        return {
            node_type.value: cls.get_definition(node_type)
            for node_type in NodeType
        }
    
    @classmethod
    def get_node_types_by_category(cls) -> Dict[str, List[str]]:
        """Get node types organized by schema category."""
        return {
            "narrative": [
                NodeType.CHARACTER.value,
                NodeType.LOCATION.value,
                NodeType.OBJECT.value,
                NodeType.GROUP.value
            ],
            "descriptive": [
                NodeType.SUBJECT.value,
                NodeType.ATTRIBUTE.value,
                NodeType.FEATURE.value,
                NodeType.DETAILS.value
            ],
            "informative": [
                NodeType.CONCEPT.value,
                NodeType.FACT.value,
                NodeType.DEFINITION.value,
                NodeType.EXAMPLE.value,
                NodeType.EXPLANATION.value
            ],
            "instructional": [
                NodeType.STEP.value,
                NodeType.ACTION.value,
                NodeType.TOOL.value,
                NodeType.CONDITION.value,
                NodeType.WARNING.value,
                NodeType.GOAL.value
            ],
            "argumentative": [
                NodeType.CLAIM.value,
                NodeType.ARGUMENT.value,
                NodeType.COUNTER_ARGUMENT.value,
                NodeType.EVIDENCE.value,
                NodeType.CONCLUSION.value
            ]
        }

