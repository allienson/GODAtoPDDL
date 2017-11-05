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

pyhop.declare_operators(completed, not_completed)
