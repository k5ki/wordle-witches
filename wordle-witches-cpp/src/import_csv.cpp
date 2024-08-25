#include "import_csv.hpp"
#include <csv/reader.hpp>
#include <fstream>
#include <iostream>
#include <vector>

namespace ww {

template <typename T> using vec = std::vector<T>;

int import_csv() {
  auto is = std::ifstream("../witches.csv");
  if (!is.is_open()) {
    std::cerr << "failed to open file." << std::endl;
  }

  auto records = vec<vec<std::string>>();
  auto record = vec<std::string>();
  auto reader = csv::reader(is);
  while (reader.readline(record)) {
    records.push_back(std::move(record));
  }

  is.close();

  for (auto &record : records) {
    for (auto &field : record) {
      std::cout << field << "|";
    }
    std::cout << std::endl;
  }

  return 0;
}

} // namespace ww
