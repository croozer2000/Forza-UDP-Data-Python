import struct

def convert_bytes_to_type(fmt, index, message):
    '''Converts 4 byte increments to the correct data type
    Forza sends data as little endian'''
    
    if fmt == "f32":
        return struct.unpack('<f',message[index:index+4])
    else: #other types used is u32,s32,u8,s8
        return int.from_bytes(message[index:index+4],"little")

def gauge_bar(value,maxVal = 10):
    '''print(f"[{gauge_bar(i)}]\r", end="")'''
    try:
        now = abs(int((value/maxVal) * 10))
        text = '{:_<{c}}'.format('',c=now)
        text = text + '{:<{c}}'.format('',c=10-now)
    except:
        print(value)
    

    return text


class ForzaCarStats(dict):
    
    # oredered list of forza packet structure
    packet_struct = ["s32","u32","f32","f32","f32"]
    packet_item_variables = ["IsRaceOn","TimestampMS","EngineMaxRpm","EngineIdleRpm","CurrentEngineRpm","AccCarX","AccCarY","AccCarZ"]

    # IsRaceOn = None
    # TimeStamp = None

    def __init__(self, message):
        count = 0
        for item in self.packet_struct:
            self.__dict__[self.packet_item_variables[count]] = convert_bytes_to_type(item,count*4,message)
            count += 1
    
    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()

    def pop(self, *args):
        return self.__dict__.pop(*args)

    def __cmp__(self, dict_):
        return self.__cmp__(self.__dict__, dict_)

    def __contains__(self, item):
        return item in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __unicode__(self):
        return unicode(repr(self.__dict__))
