import bisect


def insert(list, n): 
    bisect.insort(list, n)  
    return list


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        981. Time Based Key-Value Store
        """
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.store.get(key):
            self.store[key] = {
                'series': [],
                'value_map': {}
            }
        # self.store[key]['series'].append({'timestamp': timestamp, 'value': value})
        # self.store[key]['series'].sort(key=lambda x: x['timestamp'])
        self.store[key]['series'] = insert(self.store[key]['series'], timestamp)
        self.store[key]['value_map'][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        return self.get_nearest_fresh_value(self.store[key]['series'], timestamp, self.store[key]['value_map']) if self.store.get(key) else ''
    
    def get_nearest_fresh_value(self, l: list, timestamp: int, value_map: dict) -> dict:
        start = 0
        end = len(l)
        while start < end:
            mid = int(start + ((end - start) / 2))
            # print(start, end, mid)
            direc = 0
            
            if end == start + 1:
                if l[start] <= timestamp:
                    return value_map[l[start]]
                else:
                    return ''

            if l[mid] == timestamp:
                direc = 0
            elif l[mid] > timestamp:
                direc = -1
            else:
                direc = 1
            
            if direc == 0:
                return value_map[l[mid]]
            elif direc == -1:
                end = mid
            else:
                start = mid
        return value_map[l[start]]
        


kv = TimeMap()

# kv.set("foo", "bar", 1)
# print(kv.get("foo", 1))
# print(kv.get("foo", 3))
# kv.set("foo", "bar2", 4)
# print(kv.get("foo", 4))
# print(kv.get("foo", 5))

kv.set('love', 'high', 10)
kv.set('love', 'low', 20)
print(kv.get('love', 5))