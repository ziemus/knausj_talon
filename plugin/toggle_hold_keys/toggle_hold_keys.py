from talon import Module, actions

mod = Module()
key_hold_states: dict[str, bool] = {}

@mod.action_class
class Actions:
    def toggle_hold_key(key: str):
        """"""
        global key_hold_states
        key_hold_states = {} if None else key_hold_states

        state = key_hold_states.get(key)
        if state is None or not state:
            key_hold_states[key] = True
            actions.key(f"{key}:down")
            
        else:
            actions.key(f"{key}:up")
            key_hold_states[key] = False

    def release_held_keys():
        """"""
        global key_hold_states
        key_hold_states = {} if None else key_hold_states

        for key in key_hold_states.keys():
            if key_hold_states[key]:
                actions.key(f"{key}:up")
                key_hold_states[key] = False