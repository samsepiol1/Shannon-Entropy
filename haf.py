import math
def prob_ocurr(info):
    sum_shannon = []
    entropy = 0
    lax = list(map(chr, range(97,123)))
    size = len(info)
    for x in lax:
       total_ocurrencies = info.count(x)
       prob = total_ocurrencies/size
       try:
              prob_log = math.log(round(prob,1),2)
              entropy = prob*prob_log
              sum_shannon.append(entropy)
              print(sum_shannon)
              print(sum(sum_shannon))
       except:
              print(x)
              



prob_ocurr("araraquara")
