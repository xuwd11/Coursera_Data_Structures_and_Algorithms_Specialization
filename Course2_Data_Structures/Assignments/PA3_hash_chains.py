# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [[]]*bucket_count
        
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            #self.write_chain(cur for cur in self.elems[query.ind]
                             #if self._hash_func(cur) == query.ind)  
            self.write_chain(self.elems[query.ind])        
        else:
            idx = self._hash_func(query.s)
            indInElems = -1
            i = 0
            for e in self.elems[idx]:
                if e == query.s:
                    indInElems = i
                    break
                i += 1
            if query.type == 'find':
                self.write_search_result(indInElems != -1)
            elif query.type == 'add':
                if indInElems == -1:
                    self.elems[idx].insert(0,query.s)
            else:
                if indInElems != -1:
                    self.elems[idx].pop(indInElems)
                          
                
    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
