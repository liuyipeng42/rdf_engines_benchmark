
for i in {1..5}; do
    query_file="./datasets/split_queries/watdiv/L${i}.txt"
    result_file="./results/cli/watdiv/rdf-3x/L${i}"
    for j in {1..5}; do
        start_time=$(date +%s%N)
        ./rdf_engines/rdf-3x/bin/rdf3xquery ./rdf_engines/rdf-3x/bin/watdiv ${query_file} > /dev/null 2>&1
        end_time=$(date +%s%N)
        duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
        echo $duration >> ${result_file}
    done
done

for i in {1..7}; do
    query_file="./datasets/split_queries/watdiv/S${i}.txt"
    result_file="./results/cli/watdiv/rdf-3x/S${i}"
    for j in {1..5}; do
        start_time=$(date +%s%N)
        ./rdf_engines/rdf-3x/bin/rdf3xquery ./rdf_engines/rdf-3x/bin/watdiv ${query_file} > /dev/null 2>&1
        end_time=$(date +%s%N)
        duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
        echo $duration >> ${result_file}
    done
done

for i in {1..5}; do
    query_file="./datasets/split_queries/watdiv/F${i}.txt"
    result_file="./results/cli/watdiv/rdf-3x/F${i}"
    for j in {1..5}; do
        start_time=$(date +%s%N)
        ./rdf_engines/rdf-3x/bin/rdf3xquery ./rdf_engines/rdf-3x/bin/watdiv ${query_file} > /dev/null 2>&1
        end_time=$(date +%s%N)
        duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
        echo $duration >> ${result_file}
    done
done

for i in {1..3}; do
    query_file="./datasets/split_queries/watdiv/C${i}.txt"
    result_file="./results/cli/watdiv/rdf-3x/C${i}"
    for j in {1..5}; do
        start_time=$(date +%s%N)
        ./rdf_engines/rdf-3x/bin/rdf3xquery ./rdf_engines/rdf-3x/bin/watdiv ${query_file} > /dev/null 2>&1
        end_time=$(date +%s%N)
        duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
        echo $duration >> ${result_file}
    done
done
