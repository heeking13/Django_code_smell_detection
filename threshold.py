'''
the threshold of the detection tool
PAR: number of parameters
MLOC: method/function lines of code
CLOC: class lines of code
Long Parameter List: PAR
Long Method: MLOC
Large Class: CLOC
'''

#you can change the threshold as you like.
PAR = 5
MLOC = 38
CLOC = 29

smells_metrics_thresholds = {'Long Parameter List':[PAR],'Long Method':[MLOC], 'Large Class':[CLOC]}
