from d16data import *

packets = {}
subpackets = []
sequence = 0

def h2b(hex):
    #return str(bin(int(hex, 16)).zfill(4))
    return "{0:04b}".format(int(hex, 16))

def b2d(bin):
    return int(bin,2)

def parse_data(input):
    hexstr = ""
    hexstr_pad = ""
    binstr = ""
    for char in [char for char in input]:
        hexstr += char
        hexstr_pad += char + '   '
        binstr += h2b(char)

    return hexstr, hexstr_pad, binstr
  
def parse_packet(bits):
    global packets
    global subpackets
    global sequence
    packet = { "sequence": sequence,
               "data": bits[0:6],
               "ver": b2d(bits[0:3]),
               "p_type": b2d(bits[3:6]),
               }    
    
    unprocessed = bits[6:]
    
    if packet["p_type"] == 4: #LITERAL VALUE
        packet["value"] = ''
        more = True
        while more == True:
            if unprocessed[0] == '0':
                more = False
            packet["data"] += unprocessed[:5]
            packet["value"] += unprocessed[1:5]
            unprocessed = unprocessed[5:]

        packet["value"] = b2d(packet["value"])
    
    else: #OPERATOR PACKET
        if unprocessed[0:1] == "1": ##len_type_11
            packet["op_len_type"] = 11
            packet["op_sub_count"] = b2d(unprocessed[1:12])
            packet["data"] += unprocessed[0:12]
            unprocessed = unprocessed[12:]
            packet["op_subs"] = []
            while len(packet["op_subs"]) < packet["op_sub_count"]:
                sequence += 1
                subpackets.append(sequence)
                packet["op_subs"].append(sequence)
                new_packet,unprocessed = parse_packet(unprocessed)
                packets[new_packet["sequence"]] = new_packet
                packet["data"] += new_packet["data"]
        else: ##len_type_15
            packet["op_len_type"] = 15
            packet["op_length"] = b2d(unprocessed[1:16])
            packet["data"] += unprocessed[0:16]
            unprocessed = unprocessed[16:]
            packet["op_subs"] = []
            while len(packet["data"]) < 7 + packet["op_len_type"] + packet["op_length"]:
                sequence += 1
                subpackets.append(sequence)
                packet["op_subs"].append(sequence)
                new_packet,unprocessed = parse_packet(unprocessed)
                packets[new_packet["sequence"]] = new_packet
                packet["data"] += new_packet["data"]
            
    sequence += 1
    return packet,unprocessed

def main():
    global packets
    global sequence
    #data = input("HEX> ")
    hexstr, hexstr_pad, binstr = parse_data(my)

    while len(binstr) > 18:
        packet,binstr = parse_packet(binstr)
        packets[packet["sequence"]] = packet

    print("PART 1: ",end='')
    packet_order = []
    #packet = {}
    versions = 0
    for s,p in packets.items():
        packet_order.append(p["sequence"])
        versions += p["ver"]
        #packet[p["sequence"]] = p
    print(versions)
    
    print("PART 2: ",end='')
    for p in packet_order:
        packet = packets.copy()
        #print(packet)
        p_type = packet[p]["p_type"]
        
        if p_type == 0: # SUM
            packet[p]["value"] = 0
            for sub in packet[p]["op_subs"]:
                packet[p]["value"] += packet[sub]["value"]

        elif p_type == 1: # PRODUCT
            packet[p]["value"] = 1
            for sub in packet[p]["op_subs"]:
                packet[p]["value"] = packet[sub]["value"] * packet[p]["value"]
            
        elif p_type == 2: # MINIMUM
            sub_vals = []
            for sub in packet[p]["op_subs"]:
                sub_vals.append(packet[sub]["value"])
            packet[p]["value"] = min(sub_vals)

        elif p_type == 3: # MAXIMUM
            sub_vals = []
            for sub in packet[p]["op_subs"]:
                sub_vals.append(packet[sub]["value"])
            packet[p]["value"] = max(sub_vals)

        elif p_type == 5: # GREATER THAN
            if packet[packet[p]["op_subs"][0]]["value"] > packet[packet[p]["op_subs"][1]]["value"]:
                packet[p]["value"] = 1
            else: 
                packet[p]["value"] = 0

        elif p_type == 6: # LESS THAN
            if packet[packet[p]["op_subs"][0]]["value"] < packet[packet[p]["op_subs"][1]]["value"]:
                packet[p]["value"] = 1
            else: 
                packet[p]["value"] = 0

        elif p_type == 7: # EQUAL TO
            if packet[packet[p]["op_subs"][0]]["value"] == packet[packet[p]["op_subs"][1]]["value"]:
                packet[p]["value"] = 1
            else: 
                packet[p]["value"] = 0
        
    print(packet[0]["value"])


if __name__ == "__main__":

    main()
