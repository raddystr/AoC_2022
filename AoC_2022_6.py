from aoc_utils import input_parse

input=input_parse('input_6.txt')
signal_input = list(input)

def signal_decoder(signal, op):
    current_signal = []
    for i, s in enumerate(signal):
        if len(current_signal) == int(op):    
            if len(current_signal) == len(set(current_signal)) == int(op):
                return i
            current_signal = current_signal[1:]    
        current_signal.append(s)

print(f"Signal starts from: {signal_decoder(signal_input, 4)}")
print(f"Signal can be decoded from: {signal_decoder(signal_input, 14)}")