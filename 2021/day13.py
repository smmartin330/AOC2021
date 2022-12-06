import d13data

def parse_data(data):
    dots = { "size": [0,0],
             "xy": [],
             "grid": []
    }
    folds = []
    all_x = []
    all_y = []

    for l in data.split('\n'):
        if ',' in l:
            xy = l.split(',')
            x = int(xy[0])
            y = int(xy[1])
            dots["xy"].append([x,y])
            all_x.append(x)
            all_y.append(y)
        if 'fold' in l:
            if 'x' in l:
                folds.append(['x',int(l.split('=')[1])])
            if 'y' in l:
                folds.append(['y',int(l.split('=')[1])])
    
    dots["size"] = [max(all_x)+1,max(all_y)+1]
    print(dots["size"])

    for y in range(0,dots["size"][1]+1):
        new_row = []
        for x in range(0,dots["size"][0]+1):
            new_row.append('.')
        dots["grid"].append(new_row)

    return dots, folds

def fold_paper(dots,fold):
    new_dots = []
    direction = fold[0]
    position = fold[1]

    if direction == 'x':        
        dots['size'][0] = position
        for row in dots["xy"]:
            if row[0] < position:
                new_x = row[0]
            else:
                new_x = abs(row[0] - (position*2))

            if [new_x,row[1]] not in new_dots:
                new_dots.append([new_x,row[1]])            
    
    elif direction == 'y':
        dots["size"][1] = position
        for row in dots["xy"]:
            if row[1] < position:
                new_y = row[1]
            else:
                new_y = abs(row[1] - (position*2))
                
            if [row[0],new_y] not in new_dots:                
                new_dots.append([row[0],new_y])

    return new_dots

def results(dots,folds):
    for fold in folds:
        dots['xy'] = fold_paper(dots,fold)

    for y in range(0,dots["size"][1]):
        for x in range(0,dots["size"][0]):
            if [x,y] in dots["xy"]:
                print("#",end='')
            else:
                print(".",end='')
        print()

print('###SAMPLE###')
dots,folds = parse_data(d13data.sample)
results(dots,folds)

print('###MY DATA###')
dots,folds = parse_data(d13data.my)
results(dots,folds)
