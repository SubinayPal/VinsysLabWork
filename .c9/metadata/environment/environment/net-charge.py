{"filter":false,"title":"net-charge.py","tooltip":"/environment/net-charge.py","undoManager":{"mark":20,"position":20,"stack":[[{"start":{"row":0,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["# Python3.6  ","# Coding: utf-8  ","","# Store the human preproinsulin sequence in a variable called preproinsulin:  ","preproInsulin = \"malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn\"  ","","# Store the remaining sequence elements of human insulin in variables:  ","lsInsulin = \"malwmrllpllallalwgpdpaaa\"  ","bInsulin = \"fvnqhlcgshlvealylvcgergffytpkt\"  ","aInsulin = \"giveqcctsicslyqlenycn\"  ","cInsulin = \"rreaedlqvgqvelgggpgagslqplalegslqkr\"  ","insulin = bInsulin + aInsulin","","# Create a new dictionary","pKR = {}","","# Fill the dictionary with key-value pairs","pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":17},"action":"remove","lines":["# Python3.6  ","# Coding: utf-8  "],"id":2}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":5}],[{"start":{"row":16,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["# Count the number of each amino acid contributing to the net charge","seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}",""],"id":6}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["pH = 0",""],"id":7}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["while (pH <= 14):",""],"id":8}],[{"start":{"row":19,"column":17},"end":{"row":20,"column":0},"action":"remove","lines":["",""],"id":9}],[{"start":{"row":19,"column":17},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":13}],[{"start":{"row":20,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["    netCharge = (","        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x]))) \\","        for x in ['k', 'h', 'r']}.values()))","        -(sum({x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x]))) \\","        for x in ['y', 'c', 'd', 'e']}.values())))","    )",""],"id":14}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":15},{"start":{"row":24,"column":50},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":49},"end":{"row":24,"column":50},"action":"remove","lines":[")"],"id":16}],[{"start":{"row":25,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["    print('{0:.2f}'.format(pH), netCharge)",""],"id":18}],[{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"remove","lines":["    "],"id":19}],[{"start":{"row":19,"column":0},"end":{"row":27,"column":0},"action":"remove","lines":["while (pH <= 14):","    netCharge = (","        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x]))) \\","        for x in ['k', 'h', 'r']}.values()))","        -(sum({x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x]))) \\","        for x in ['y', 'c', 'd', 'e']}.values())))","","print('{0:.2f}'.format(pH), netCharge)",""],"id":20},{"start":{"row":19,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["while (pH <= 14):","    netCharge = (","        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x]))) \\","        for x in ['k', 'h', 'r']}.values()))","        -(sum({x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x]))) \\","        for x in ['y', 'c', 'd', 'e']}.values())))","    )","    print('{0:.2f}'.format(pH), netCharge)","    pH += 1",""]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"remove","lines":[")"],"id":21}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":22}],[{"start":{"row":24,"column":50},"end":{"row":25,"column":0},"action":"remove","lines":["",""],"id":23}]]},"ace":{"folds":[],"scrolltop":204,"scrollleft":0,"selection":{"start":{"row":26,"column":11},"end":{"row":26,"column":11},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":10,"state":"start","mode":"ace/mode/python"}},"timestamp":1730821747859,"hash":"83143dddba4918e5f8803fd98280a585e6242b9b"}