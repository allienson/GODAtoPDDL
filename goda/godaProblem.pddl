(define (problem godaProblem)
	
	(:domain godaDomain)
  	
	(:objects 
		G0 - task
		G1 - task
		G2 - task
		G3 - task
		G4 - task
		T1 - task
		T1_1 - task
		T1_2 - task
	)

  	(:init 
  		(notcompleted T1)
  		(notcompleted T1_1)
  		(notcompleted T1_2)
  		(notachieved G0)
  		(notachieved G1)
  		(notachieved G2)
  		(notachieved G3)
  		(notachieved G4)
  	)
  	
  	(:goal 
  		(achieved G0)
  	)
)