for i in {1..4}; do
    query_file="./datasets/split_queries/yago2/y${i}.q"
    result_file="./results/cli/yago2/rdf-3x/y${i}.q"
    for j in {1..5}; do
        start_time=$(date +%s%N)
        ./rdf_engines/rdf-3x/bin/rdf3xquery ./rdf_engines/rdf-3x/bin/yago2 ${query_file} > /dev/null 2>&1
        end_time=$(date +%s%N)
        duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
        echo $duration >> ${result_file}
    done
done
