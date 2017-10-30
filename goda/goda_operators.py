import pyhop

def completed(state, plan): 
    if state.objects[plan] == False:
        state.objects[plan] = True
        return state
    else:
        return False

def not_completed(state, plan): 
    if state.objects[plan] == True:
        state.objects[plan] = False
        return state
    else:
        return False

# def achieved(state, goal):
#     if state.objects[goal] == False:
#         state.objects[goal] = True
#         return state
#     else:
#         return False

# def not_achieved(goal):
#     if state.objects[goal] == True:
#         state.objects[goal] = False
#         return state
#     else:
#         return False

pyhop.declare_operators(completed, not_completed)
