import d14data
from math import ceil

def parse_data(data):
    chain = ''
    pairs = {}
    yields = {}
    pair_count = {}

    for line in data.split('\n'):
        if ' -> ' in line:
            pair = line.split(' -> ')
            pairs[pair[0]] = pair[1]
            pair_count[pair[0]] = 0
        elif line == '':
            pass
        else:
            chain = line

        for k,v in pairs.items():
            # IF AB -> C, THAN AB -> AC & CB
            yields[k] = [k[0]+v, v+k[1]]

    for i in range(0,len(chain)):
        this_pair = chain[i:i+2]
        if len(this_pair) == 2:
            pair_count[this_pair] += 1
            i+=1

    return yields, pair_count

def step_pairs(pair_count,yields,steps):
    for s in range(0,steps):
        this_step = {}
        for k,v in pair_count.items():
            if v > 0:
                try:
                    this_step[yields[k][0]] += v
                except:
                    this_step[yields[k][0]] = v
                try:
                    this_step[yields[k][1]] += v
                except:
                    this_step[yields[k][1]] = v                
                try:
                    this_step[k] -= v
                except:
                    this_step[k] = -v
        
        for k,v in this_step.items():
            pair_count[k] += v

        s += 1

def base_count(pair_count):
    base_count = {}
    counts = []
    for k,v in pair_count.items():
        try:
            base_count[k[0]] += v
        except:
            base_count[k[0]] = v
        try:
            base_count[k[1]] += v
        except:
            base_count[k[1]] = v
    
    for k,v in base_count.items():
        counts.append(ceil(v/2))
    
    print(max(counts)-min(counts))

print('SAMPLE:')
yields,pair_count = parse_data(d14data.sample)
step_pairs(pair_count,yields,10)
print("PART 1: ", end='')
base_count(pair_count)
step_pairs(pair_count,yields,30)
print("PART 2: ", end='')
base_count(pair_count)

print('MY DATA:')
yields,pair_count = parse_data(d14data.my)
step_pairs(pair_count,yields,10)
print("PART 1: ", end='')
base_count(pair_count)
step_pairs(pair_count,yields,30)
print("PART 2: ", end='')
base_count(pair_count)
