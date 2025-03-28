for i in $(seq 1 14740); do
    start_time=$(date +%s%N)
    ./rdf_engines/rdf-3x/bin/rdf3xquery ./rdf_engines/rdf-3x/bin/swdf ./datasets/split_queries/swdf/$i > /dev/null 2>&1
    end_time=$(date +%s%N)
    duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)

    echo "Query $i took $duration ms"
    echo $duration >> ./results/cli/swdf/rdf-3x/results.txt
done
