import re

from talon import Context, Module, actions, settings

from ..tags.operators import Operators

mod = Module()
ctx = Context()
ctx.matches = r"""
code.language: gdscript
"""

ctx.lists["user.code_keyword"] = {
    "break": "break",
    "continue": "continue",
    "import": "import ",
    "null": "None",
    "none": "None",
    "yield": "yield ",
    
    #actual
    "return": "return ",
    "true": "true",
    "false": "false",
    "pass": "pass",
    "var": "var ",
    "funk": "func ",
    "signal": "signal ",
    "extends": "extends ",
    "export": "@export ",
    "export category": "@export_category(\"\")",
    "input": "Input",

    "await": "await ",

    "position": "position",
    "rotation": "rotation",
    "linear velocity": "linear_velocity",

    "pi": "PI",
    "tau": "TAU",
}

ctx.lists["user.code_common_function"] = { 
    "length": "len",
    "list": "list",
    "set": "set",

    #actual gdscript
    "init": "_init",
    "process": "_process",
    "physics process": "_physics_process",
    "print": "print",
    "range": "range",
    "string": "str",
    "integer": "int",

    "vector two": "Vector2",
    "vector three:": "Vector3",
    "array": "Array",

    "unhandled input": "_unhandled_input",
    "set process": "set_process",
    "is processing": "is_processing",
    "connect": "connect",
    "ready": "_ready",
    "move and slide": "move_and_slide",
    "get slide collision count": "get_slide_collision_count",
    "get slide collision": "get_slide_collision",
    
    "queue free": "queue_free",

    "hide": "hide",
    "show": "show",
    "rotated": "rotated",

    "add child": "add_child",
    "get tree": "get_tree",
    "get node": "get_node",

    "rand F": "randf",
    "rand float": "randf",
    "rand F range": "randf_range",
    "rand I": "randi",
    "rand int": "randi",
    "rand I range": "randi_range",

    "radian to degree": "rad_to_deg",
    "rad to deg": "rad_to_deg",

    "get viewport rect": "get_viewport_rect",

}

ctx.lists["user.code_type"] = {
    
    "none": "None",
    "dick": "Dict",
    
    "any": "Any",
    "tuple": "Tuple",
    "union": "UnionAny",
    "iterable": "Iterable",
    "vector": "Vector",
    "bytes": "bytes",
    "sequence": "Sequence",
    "callable": "Callable",
    "list": "List",
    "no return": "NoReturn",

    #actual
    "boolean": "bool",
    "integer": "int",
    "string": "String",
    "float": "float",
    "void": "void",

    "array": "Array",

    "vector two": "Vector2",
    "vector two aye": "Vector2i",
    "vector three": "Vector3",
    "vector three aye": "Vector3i",
    "path two D": "Path2D",
    "path follow two D": "PathFollow2D",
    "marker two D": "Marker2D",
    "marker three D": "Marker3D",

    "node two D": "Node2D",
    "area two D": "Area2D",
    "canvas item": "CanvasItem",
    "canvas layer": "CanvasLayer",
    "animated sprite two D": "AnimatedSprite2D",
    "rigid body two D": "RigidBody2D",
    "visible on screen notifier two D": "VisibleOnScreenNotifier2D",

    "static body two D": "StaticBody2D",
    "static body three D": "StaticBody3D",
    "character body two D": "CharacterBody2D",
    "character body three D": "CharacterBody3D",
    "collision shape two D": "CollisionShape2D",
    "collision shape three D": "CollisionShape3D",
    "box shape three D": "BoxShape3D",
    "mesh instance three D": "MeshInstance3D",
    "directional light two D": "DirectionalLight2D",
    "directional light three D": "DirectionalLight3D",

    "timer": "Timer",
    "node": "Node",
    "packed scene": "PackedScene",
}

operators = Operators(
    # code_operators_array
    SUBSCRIPT=lambda: actions.user.insert_between("[", "]"),
    # code_operators_assignment
    ASSIGNMENT=" = ",
    ASSIGNMENT_SUBTRACTION=" -= ",
    ASSIGNMENT_ADDITION=" += ",
    ASSIGNMENT_MULTIPLICATION=" *= ",
    ASSIGNMENT_DIVISION=" /= ",
    ASSIGNMENT_MODULO=" %= ",
    ASSIGNMENT_INCREMENT="+= 1",
    ASSIGNMENT_BITWISE_AND=" &= ",
    ASSIGNMENT_BITWISE_OR=" |= ",
    ASSIGNMENT_BITWISE_EXCLUSIVE_OR=" ^= ",
    ASSIGNMENT_BITWISE_LEFT_SHIFT=" <<= ",
    ASSIGNMENT_BITWISE_RIGHT_SHIFT=" >>= ",
    # code_operators_bitwise
    BITWISE_NOT="~",
    BITWISE_AND=" & ",
    BITWISE_OR=" | ",
    BITWISE_EXCLUSIVE_OR=" ^ ",
    BITWISE_LEFT_SHIFT=" << ",
    BITWISE_RIGHT_SHIFT=" >> ",
    # code_operators_lambda
    LAMBDA=lambda: actions.user.insert_between("lambda ", ": "),
    # code_operators_math
    MATH_SUBTRACT=" - ",
    MATH_ADD=" + ",
    MATH_MULTIPLY=" * ",
    MATH_DIVIDE=" / ",
    MATH_MODULO=" % ",
    MATH_EXPONENT=" ** ",
    MATH_EQUAL=" == ",
    MATH_NOT_EQUAL=" != ",
    MATH_GREATER_THAN=" > ",
    MATH_GREATER_THAN_OR_EQUAL=" >= ",
    MATH_LESS_THAN=" < ",
    MATH_LESS_THAN_OR_EQUAL=" <= ",
    MATH_AND=" and ",
    MATH_OR=" or ",
    MATH_NOT="not ",
    MATH_IN=" in ",
    MATH_NOT_IN=" not in ",
)


@ctx.action_class("user")
class UserActions:
    def code_get_operators() -> Operators:
        return operators

    def code_self():
        actions.auto_insert("self")

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_insert_null():
        actions.auto_insert("None")

    def code_insert_is_null():
        actions.auto_insert(" is None")

    def code_insert_is_not_null():
        actions.auto_insert(" is not None")

    def code_state_if():
        actions.user.insert_between("if ", ":")

    def code_state_else_if():
        actions.user.insert_between("else if ", ":")

    def code_state_else():
        actions.insert("else:")
        actions.key("enter")

    def code_state_switch():
        actions.user.insert_between("match ", ":")

    def code_state_case():
        actions.user.insert_between("case ", ":")

    def code_state_for():
        #actions.auto_insert("for ")
        actions.user.insert_between("for ", " in range():")

    def code_state_for_each():
        actions.user.insert_between("for ", " in ")

    def code_state_while():
        actions.user.insert_between("while ", ":")

    def code_define_class():
        actions.auto_insert("class ")

    def code_import():
        actions.auto_insert("import ")

    def code_comment_line_prefix():
        actions.auto_insert("# ")

    def code_state_return():
        actions.insert("return ")

    def code_insert_true():
        actions.auto_insert("true")

    def code_insert_false():
        actions.auto_insert("false")

    def code_comment_documentation():
        actions.user.insert_between('"""', '"""')

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "func _{}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_public_function(text: str):
        result = "func {}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" -> {type}")

    def code_break():
        actions.insert("break")

    def code_next():
        actions.insert("continue")

