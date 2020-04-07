# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1



class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        981. Time Based Key-Value Store
        """
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.store.get(key):
            self.store = {
                series: []
            }
        self.store[key].series.append({'timestamp': timestamp, 'value': value})
        self.store[key].series.sort(key=lambda x: x['timestamp'])
        
    def get(self, key: str, timestamp: int) -> str:
        pass
    
    def get_nearest_fresh_value(self, l: list, timestamp: int) -> dict:
        start = 0
        end = len(l)
        while start < end:
            mid = int(start + ((end - start) / 2))
            print(start, end, mid)
            direc = 0
            if l[mid]['timestamp'] == timestamp:
                direc = 0
            elif l[mid]['timestamp'] > timestamp:
                direc = -1
            else:
                direc = 1
            
            if direc == 0:
                return l[mid]
            elif direc == -1:
                end = mid
            else:
                start = mid
        return l[start]
        


t = TimeMap()
print(t.get_nearest_fresh_value([
    {
        'timestamp': 1,
        'value': 1
    },
    {
        'timestamp': 2,
        'value': 2
    },
    {
        'timestamp': 3,
        'value': 3
    },
    {
        'timestamp': 4,
        'value': 4
    },
    {
        'timestamp': 5,
        'value': 5
    },
    {
        'timestamp': 6,
        'value': 6
    },
    {
        'timestamp': 7,
        'value': 7
    },
    {
        'timestamp': 8,
        'value': 8
    },
    {
        'timestamp': 9,
        'value': 9
    },
    {
        'timestamp': 10,
        'value': 10
    },
    {
        'timestamp': 13,
        'value': 13
    },
    {
        'timestamp': 16,
        'value': 16
    },
    {
        'timestamp': 17,
        'value': 17
    },
    {
        'timestamp': 20,
        'value': 20
    }
], 12))