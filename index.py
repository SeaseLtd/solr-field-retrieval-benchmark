import ijson
import random
import string
import pysolr
import sys
from itertools import zip_longest, filterfalse

N_STRING_FIELDS = 100
SOLR_URL = "http://localhost:8983"
BATCH_SIZE = 1000

def randomString(stringLength=15):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def batch_iterable(iterable, batch_size=2): 
    args = [iter(iterable)] * batch_size 
    return (tuple(filterfalse(lambda x: x is None, group)) for group in zip_longest(fillvalue=None, *args))

def main(filename):
    solr = pysolr.Solr(SOLR_URL + '/solr/text-bench', always_commit=True)
    with open(filename, "r") as input:
        json_rows = ijson.items(input, 'item')
        for batch in batch_iterable(json_rows, BATCH_SIZE):
            to_index = []
            for input_elem in batch:
                output_elem = {}
                output_elem["body"] = input_elem["body"]
                for k in range(0, N_STRING_FIELDS):
                    r = randomString()
                    output_elem["field" + str(k) + "_stored"] = r
                    output_elem["field" + str(k) + "_docvalue"] = r

                to_index.append(output_elem)        
            solr.add(to_index)


if __name__ == "__main__":
    main(sys.argv[1])