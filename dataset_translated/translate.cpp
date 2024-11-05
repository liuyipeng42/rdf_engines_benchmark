
#include <filesystem>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include "sys/types.h"

std::string trim(std::string s) {
    s.erase(0, s.find_first_not_of(" \t\n\r"));
    s.erase(s.find_last_not_of(" \t\n\r") + 1);
    return s;
}

void encode_rdf(std::unordered_map<std::string, uint>& nodes,
                std::unordered_map<std::string, uint>& predicates) {
    std::string s, p, o;

    std::ifstream fin("./original/wikidata-wcg-filtered.nt", std::ios::in);

    std::vector<uint*> triples;

    uint triplet_cnt = 0;

    std::vector<std::string> predicates_list;

    while (fin >> s >> p) {
        fin.ignore();
        std::getline(fin, o);
        for (o.pop_back(); o.back() == ' ' || o.back() == '.'; o.pop_back()) {
        }
        uint* triple = new uint[3];
        auto ret = nodes.insert({s, nodes.size() + 1});
        triple[0] = ret.first->second;
        ret = predicates.insert({p, predicates.size() + 1});
        triple[1] = ret.first->second;
        ret = nodes.insert({o, nodes.size() + 1});
        triple[2] = ret.first->second;
        triples.push_back(triple);

        if (triplet_cnt % 100000 == 0) {
            std::cout << triplet_cnt << " triples processed\r" << std::flush;
        }
        triplet_cnt++;
    }
    std::cout << triplet_cnt << std::endl;

    fin.close();

    std::ofstream fout("./translated.nt", std::ofstream::out | std::ofstream::binary);

    for (uint i = 0; i < triples.size(); i++) {
        std::string triple = std::to_string(triples[i][0]) + ' ' +
                             std::to_string(triples[i][1] + nodes.size()) + ' ' +
                             std::to_string(triples[i][2]) + '\n';

        fout.write(triple.c_str(), triple.size());
        if (i % 100000 == 0) {
            std::cout << i << " triples processed\r" << std::flush;
        }
    }
    std::cout << triples.size() << std::endl;

    fout.close();
}

void split(const std::string& str, std::vector<std::string>& words) {
    std::stringstream ss(str);
    std::string word;
    while (ss >> word)
        words.push_back(word);
}

void encode_sparql(std::unordered_map<std::string, uint>& nodes,
                   std::unordered_map<std::string, uint>& predicates) {
    std::filesystem::path query_path = "./original/wgpb";  // 替换为你的目标文件夹路径

    for (const auto& entry : std::filesystem::directory_iterator(query_path)) {
        if (entry.is_regular_file() && entry.path().extension() == ".txt") {
            std::ifstream fin(query_path.string() + '/' + entry.path().filename().string(), std::ios::in);
            std::ofstream fout(query_path.string() + "_t/" + entry.path().filename().string(),
                               std::ofstream::out | std::ofstream::binary);
            std::cout << query_path.string() + "_t/" + entry.path().filename().string() << std::endl;
            std::string query;
            while (getline(fin, query)) {
                uint start = query.find('{') + 1;
                uint end = query.find('}');
                std::string processed = "";

                std::vector<std::string> parts;
                split(query.substr(start, end - start), parts);

                for (uint i = 0; i < parts.size(); i++) {
                    if (i % 4 == 1) {
                        if (parts[i][0] != '?') {
                            auto it = predicates.find(trim(parts[i]));
                            uint id = 0;
                            if (it != predicates.end())
                                id = it->second;
                            processed += std::to_string(id + nodes.size()) + ' ';
                        }

                        else
                            processed += parts[i] + ' ';
                    } else {
                        if (parts[i] != ".") {
                            if (parts[i][0] != '?') {
                                auto it = nodes.find(trim(parts[i]));
                                uint id = 0;
                                if (it != nodes.end())
                                    id = it->second;
                                processed += std::to_string(id) + ' ';
                            }

                            else
                                processed += parts[i] + ' ';
                        } else {
                            processed += ". ";
                        }
                    }
                }
                processed.resize(processed.length() - 2);
                processed += '\n';
                fout.write(processed.c_str(), processed.size());
            }

            fin.close();
            fout.close();
        }
    }
}

int main() {
    std::unordered_map<std::string, uint> nodes;
    std::unordered_map<std::string, uint> predicates;

    encode_rdf(nodes, predicates);
    encode_sparql(nodes, predicates);
}
