

types=("J3" "J4" "P2" "P3" "P4" "S1" "S2" "S3" "S4" "T2" "T3" "T4" "TI2" "TI3" "TI4" "Tr1" "Tr2")

for type in "${types[@]}"; do
    for i in $(seq 1 50); do
        start_time=$(date +%s%N)
        ./rdf_systems/rdf-3x/bin/rdf3xquery ./rdf_systems/rdf-3x/bin/wgpb "./datasets/split_queries/wgpb/${type}_$i.txt" > /dev/null 2>&1
        end_time=$(date +%s%N)
        duration=$(echo "scale=3; ($end_time - $start_time) / 1000000" | bc)
        echo $duration >> ./results/cli/wgpb/rdf-3x/${type}
    done
done
