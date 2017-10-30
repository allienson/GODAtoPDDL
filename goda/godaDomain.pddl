(define (domain godaDomain)

(:requirements :typing :fluents :strips :equality :durative-actions)

(:types task goal value)  	; Por enquanto coloquei so esses tipos para comecar

(:predicates				; Ainda to pensando como expressar melhor os predicados,
    (completed ?task)      	; mas a ideia eh que sejam principalmente esses ai
    (notcompleted ?task) 
    (achieved ?goal)      
    (notachieved ?goal)      
)

(:durative-action and-sequential
    :parameters (?task1 ?task2)
    
    :precondition ( and
    	(notcompleted ?task1)
    	(notcompleted ?task2)
    )
    
    :effect ( and
      	(at start (completed ?task1))
      	(at end (completed ?task2))
    )
)

(:action and-parallel
    :parameters (?task1 ?task2)
    
    :precondition ( and
    	(notcompleted ?task1)
    	(notcompleted ?task2)
    )
    
    :effect ( and
      	(completed ?task1)
    	(completed ?task2)
    )
)

(:durative-action or-sequential
    :parameters (?task1 ?task2)
    
    :precondition ( and
    	(notcompleted ?task1)
    	(notcompleted ?task2)
    )
    
    :effect ( or
      	(at start (completed ?task1))
      	(at start (completed ?task2))
      	(at end (completed ?task1))
      	(at end (completed ?task2))
    )
)

(:action or-parallel
    :parameters (?task1 ?task2)
    
    :precondition ( and
    	(notcompleted ?task1)
    	(notcompleted ?task2)
    )
    
    :effect ( or
      	(completed ?task1)
    	(completed ?task2)
    )
)

(:action or-exclusive
    :parameters (?task1 ?task2)
    
    :precondition ( and
    	(notcompleted ?task1)
    	(notcompleted ?task2)
    )
    
    :effect ( 	   )				; Ainda nao sei como definir corretamente o XOR
)

(:action k-times-sequential
    :parameters (?task ?k)
    
    :precondition ()
    
    :effect ( (forall (?k)
      	(completed ?task))
    )
)

(:action k-times-parallel
    :parameters (?task ?k)
    
    :precondition ()
    
    :effect( (forall (?k)
      	(completed ?task)))
)

(:action k-tries
	:parameters (?task ?k)
    
    :precondition (		)			; Essa regra tambem nao sei ainda como vai funcionar
    
    :effect (     )
)

(:action optional
    :parameters (?task)
    
    :precondition (		)			; Essa regra tambem nao sei ainda como vai funcionar
    
    :effect (     )
)

(:action try
    :parameters (?task ?task1 ?task2)
    
    :precondition ( and
    	(completed ?task)
    	(notcompleted ?task1)
    	(notcompleted ?task2)
    )
    
    :effect (
      (completed ?task1)
    )
)

(:action skip
    :parameters (?task)
    
    :precondition (
    	(notcompleted ?task)
    )
    
    :effect (
    	(notcompleted ?task)
    )
)