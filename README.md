# solr-field-retrieval-benchmark

For executing the benchmark you can follow the istructions below.
You can find the full dataset used for the benchmark linked at https://github.com/tantivy-search/search-benchmark-game

## run solr
```bash
solr start -a "-Dsolr.data.dir=benchmark" -f -s <cores-directory>
```

## indexing

```bash
python index.py <data> # e.g. data_bench_small/wiki-1000.json
```

## benchmark
```bash
python query.py <query-collection> # e.g. data_bench_small/queries-50.txt
```

## plotting results
```bash
python plot.py
```
