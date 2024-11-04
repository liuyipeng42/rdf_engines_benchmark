# RDF Systems Benchmark
This repository contains benchmarks for various RDF systems using both command-line interfaces and SPARQL endpoints. The systems benchmarked include RDF-3X, Ring, Tentris, and Jena-LTJ.

## Installation

To get started, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/yourusername/rdf_systems_benchmark.git
cd rdf_systems_benchmark
git submodule update --init
```

## Datasets

Datasets are available [here](https://mega.nz/folder/5ulXkYZT#j54ThyZBnX34_VANelVWoA). Place RDF files and queries into their respective directories.

## Usage

To run the benchmarks, use the following commands:

```bash
python ./scripts/endpoint.py <dataset_path> <rdf_system>
./scripts/cli/rdf-tdaa/watdiv.sh
./scripts/cli/rdf-tdaa/wgpb.sh
./scripts/cli/rdf-tdaa/dbpedia.sh
./scripts/cli/rdf-3x/watdiv.sh
./scripts/cli/rdf-3x/wgpb.sh
./scripts/cli/rdf-3x/dbpedia.sh
./scripts/cli/ring/watdiv.sh
./scripts/cli/ring/wgpb.sh
./scripts/cli/ring/dbpedia.sh
```