import d12data

def build_dict(data):
    rooms = {}
    
    for row in data.split('\n'):
        room = row.split('-')
        if room[0] in rooms:
            rooms[room[0]].append(room[1])
        else:
            rooms[room[0]] = [room[1]]
        if room[1] in rooms:
            rooms[room[1]].append(room[0])
        else:
            rooms[room[1]] = [room[0]]

    return rooms


def check_path(path,dest):
    check = []
    if dest == 'start':
        return False

    if dest == 'end':
        return True

    if dest not in path:
        return True
    
    for room in path:
        if room.lower() == room:
            if room not in check:
                check.append(room)      
            else:
                return False

    return True


def build_paths(rooms):
    paths = []
    added = True
    
    for dest in rooms['start']:
        paths.append(['start',dest])

    while added == True:
        added = False
        for path in paths:
            this_path = path.copy()
            
            if this_path[-1] == 'end':
                continue
            
            for dest in rooms[this_path[-1]]:
                new_path = this_path.copy()
                new_path.append(dest)

                if dest.lower() == dest:
                    if check_path(this_path,dest) == False:
                        continue
                
                if new_path not in paths:
                    paths.append(new_path)
                    added = True
            
            paths.remove(this_path)
            #print(len(paths))

    return paths 
                
                
def main():        
    sample1_rooms = build_dict(d12data.sample1)
    #sample2_rooms = build_dict(d12data.sample2)
    my_rooms = build_dict(d12data.my)

    sample1_paths = build_paths(sample1_rooms)
    #sample2_paths = build_paths(sample2_rooms)
    my_paths = build_paths(my_rooms)
    
    print(len(sample1_paths))
    #print(len(sample2_paths))
    print(len(my_paths))



if __name__ == '__main__':
    main()
