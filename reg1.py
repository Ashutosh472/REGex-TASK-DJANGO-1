from reg import Evaluate
exp = "231*+9-"
obj = Evaluate(len(exp))
print ('postfix evaluation: %d'%(obj.evaluatePostfix(exp)))
