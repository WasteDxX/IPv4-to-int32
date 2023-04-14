
ip = "0.0.0.0"
def ip_to_int32(ip):

    start = ip.find('.')
    end = ip.rfind('.')
    middle = ip[start+1:end].find('.') + start + 1

    first = int(ip[:start])
    second = int(ip[start+1:middle])
    third = int(ip[middle+1:end])
    fourth = int(ip[end+1:])

    result = first * pow(256,3) + second * pow(256,2) + third * 256 + fourth


    return result