for i in {1..7}; do
    query_file="./datasets/split_queries/lubm-100/Q${i}.txt"
    result_file="./results/cli/lubm-100/rdf-3x/Q${i}"
    for j in {1..5}; do
        start_time=$(date +%s%N)
        ./rdf_engines/rdf-3x/bin/rdf3xquery ./rdf_engines/rdf-3x/bin/lubm-100 ${query_file} > /dev/null 2>&1
        end_time=$(date +%s%N)
        duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
        echo $duration >> ${result_file}
    done
done
