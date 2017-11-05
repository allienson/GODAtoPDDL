import pyhop

def and_seq(state, *plans):
	count = 0
	for i in range(1, len(plans)):
		plan = plans[i]
		if state.objects[plan] == True:
			count += 1
	if count == len(plans)-1:
		return [('completed', plans[0])]
	else:
		return False
pyhop.declare_methods('and_seq', and_seq)

def and_par(state, *plans):
	count = 0
	for i in range(1, len(plans)):
		plan = plans[i]
		if state.objects[plan] == True:
			count += 1
	if count == len(plans)-1:
		return [('completed', plans[0])]
	else:
		return False
pyhop.declare_methods('and_par', and_par)

def or_seq(state, *plans):
	count = 0
	for i in range(1, len(plans)):
		plan = plans[i]
		if state.objects[plan] == True:
			count += 1
	if count != 0:
		return [('completed', plans[0])]
	else:
		return False
pyhop.declare_methods('or_seq', or_seq)

def or_par(state, *plans):
	count = 0
	for i in range(1, len(plans)):
		plan = plans[i]
		if state.objects[plan] == True:
			count += 1
	if count != 0:
		return [('completed', plans[0])]
	else:
		return False
pyhop.declare_methods('or_par', or_par)

def k_times(state, plan, k):
	if k > 0:
		if state.objects[plan] == False:
			retorno = []
			#for x in range(0, k):
			#	retorno.append(('completed', plan))
			return [('completed', plan), ('completed', plan)]
	else:
		return False
pyhop.declare_methods('k_times', k_times)

def k_times_par(state, plan, k):
	if k > 0:
		if state.objects[plan] == False:
			retorno = []
			for x in range(0, k):
				retorno.append(('completed', plan))
			return retorno
	else:
		return False
pyhop.declare_methods('k_times_par', k_times_par)

# def k_tries():
# 	if k < 1:
# 		return False
# 	if state.objects[plan] == False:


# def opt():
# 	return [('not_completed', plan)]

# pyhop.declare_methods('opt', opt)

def try_op(state, plan, plan1, plan2):
	if state.objects[plan] == True:
		if plan1 == 'skip':
			return [('skip', plan1)]
		else:
			return [('completed', plan1)] 
	elif state.objects[plan] == False:
		if plan2 == 'skip':
			return [('skip', plan2)]
		else:
			return [('completed', plan2)] 
	else:
		return False

pyhop.declare_methods('try_op',try_op)


def xor(state, plan, plan1, plan2):
	if state.objects[plan1] == True:
		return [('completed', plan), ('not_completed', plan2)]
	elif state.objects[plan2] == True:
		return [('completed', plan), ('not_completed', plan1)]
	else:
		return False

pyhop.declare_methods('xor', xor)

def means_end(state, plan, plan1):
	if state.objects[plan1] == True:
		return [('completed', plan)]
	else:
		return False

pyhop.declare_methods('means_end', means_end)