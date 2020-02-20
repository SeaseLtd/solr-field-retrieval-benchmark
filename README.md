# solr-field-retrieval-benchmark

## run solr
```bash
solr start -a "-Dsolr.data.dir=benchmark" -f -s <cores-directory>
```

## indexing

```bash
python index.py <json-data>
```

## benchmark
```bash
python query.py <query-collection>
```

## plot
```bash
python plot.py
```
