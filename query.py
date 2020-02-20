import json
import random
import string
import pysolr
import sys
import time
import pickle

n_fields_values = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def run_queries(queries, fields_type, n_fields, n_results):
    suffix = "_docvalue" if fields_type == "docv" else "_stored"
    fields = ["field" + str(i) + suffix for i in range(0, n_fields)]

    solr = pysolr.Solr('http://localhost:8983/solr/text-bench', always_commit=True) 
    count = 0

    start = time.time()
    for q in queries:
        result = solr.search('body:(' + q['query'] + ')' , **{
            'rows':n_results,
            'fl': fields
        })
        count += 1
    end = time.time()

    return ((end - start)*1000/count)

def main(query_filename):
    dv_res = []
    stored_res = []
    queries = json.load(open(query_filename))
    for n_results in 100, 200:
        for fields_type in ("stored", "docv"):
            res = []
            for n_fields in n_fields_values:
                # run twice in order to warm up the index
                run_queries(queries, fields_type, n_fields, n_results)
                time = run_queries(queries, fields_type, n_fields, n_results)
                res.append(time)
                print("type: " + fields_type + " n_results:" + str(n_results) + "n_fields:" + str(n_fields) + " time:" + str(time))
            with open('results_{}_{}'.format(fields_type, n_results), 'wb') as fp:
                pickle.dump(res, fp)

if __name__ == "__main__":
    main(sys.argv[1])