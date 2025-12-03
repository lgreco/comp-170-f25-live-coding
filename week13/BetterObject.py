class PAM:
    
    """A collection of tuples where the first element of the tuple
    is treated as a PRIMARY KEY (ie unique)."""

    
    _KEYS = 0
    _VALUES = 1


    def __init__(self):
        self._underlying = []  # Start with an empty list
    
    def size(self) -> int:
        """Returns the number of entries in the underlying list."""
        # length = -1                            # int length = -1;
        # if self._underlying is not None:       # if (this.underlying != null)
        #     length = len(self._underlying)     #   length = this.underlying.length;
        # return length                          # return length;
        # VERY PYTHONIC WAY TO DO THE SAME: ternary operator
        return -1 if self._underlying is None else len(self._underlying)
        # In java: return (this.underlying==null) ? -1 : self.underlying.length;

    def add(self, key:int, value:str):
        """Adds the tuple (key,value) to the underlying list."""
        # Make sure key does not already exist
        if not self.key_exists(key):  
            # Append a the combination of key and value. These can be
            # added as a tuple (k,v) or as a list [k,v].
            self._underlying.append([key, value])
    
    def put(self, key:int, value:str):
        """If the key exists, replace the existing record's value
        with the new value given here and return the existing value.
        Otherwise, just add the new key-value pair and return None."""  
        existing_value = None
        location_to_update = self._index_of(key)
        if location_to_update > -1:
            existing_value = self._underlying[location_to_update][self._VALUES]
            self._underlying[location_to_update][self._VALUES] = value
        else:
            self.add(key,value)
        return existing_value

    def _index_of(self, key) -> int:
        index_of = -1
        i = 0
        found = False
        while i < len(self._underlying) and not found:
            found = self._underlying[i][self._KEYS] == key
            i += 1
        if found:
            index_of -= i
        return index_of
    
    def key_exists(self, key:int) -> bool:
        return self._index_of(key) > -1

    def find(self, name:str):
        """Looks up for the given name in the underlying array and returns the
        corresponding entry; or empty list if the entry not there."""
        
        # initialize return item
        records = []
        
        # Look through the collection for an entry with a matching name
        for i in range(len(self._underlying)):
            # Check contents of second item, i.e., [1], in [i]-th element,
            # match the search criterion
            if self._underlying[i][1] == name:
                records.append(self._underlying[i])

        return records
    
    def _get_data(self, column):
        data_from_records = []
        for record in self._underlying:
            data_from_records.append(record[column])
        return data_from_records
    
    def get_keys(self):
        return self._get_data(self._KEYS)
    
    def get_values(self):
        return self._get_data(self._VALUES)
    

if __name__ == "__main__":
    test = PAM()

    test.add(123, "Brad Paul")
    test.add(234, "Tim Burt")
    test.add(234, "Leo Irakliotis")
    test.add(456, "Leo Irakliotis")
    test.add(567, "Tim Burt")
    test.add(678, "Tim Burt")
    print(test._underlying)
    print(test.find("Tim Burt"))
    print(test.get_values())
    print(test.get_keys())