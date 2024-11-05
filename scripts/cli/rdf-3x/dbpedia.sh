for i in $(seq 1 554); do
    start_time=$(date +%s%N)
    ./rdf_systems/rdf-3x/bin/rdf3xquery ./rdf_systems/rdf-3x/bin/dbpedia ./datasets/split_queries/dbpedia/$i > /dev/null 2>&1
    end_time=$(date +%s%N)
    duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)

    echo "Query $i took $duration ms"
    echo $duration >> ./results/cli/dbpedia/rdf-3x/dbpedia_result
done
