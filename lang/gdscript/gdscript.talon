code.language: gdscript
-
tag(): user.code_imperative
tag(): user.code_object_oriented
tag(): user.code_comment_documentation
tag(): user.code_comment_line
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_keywords
tag(): user.code_libraries
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_lambda
tag(): user.code_operators_math

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

op hint assign: " := "
state (<user.code_keyword>+): user.code_keyword(code_keyword_list)
type {user.code_type}: "{code_type}"
new funk:
    key(enter backspace enter enter)
    insert("funk () -> void:")
    key(home ctrl-right right)