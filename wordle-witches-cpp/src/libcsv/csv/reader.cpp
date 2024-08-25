#include "reader.hpp"
#include <iostream>
#include <vector>

namespace ww {
namespace csv {

template <typename T> using vec = std::vector<T>;

reader::reader(std::istream &in)
    : in(in), state(State::AfterComma), field(std::string()),
      fields(vec<std::string>()) {}

bool reader::readline(vec<std::string> &record) {
  char c;
  while (in.get(c) && this->update(c)) {
  }
  if (this->state == State::Error) {
    // TODO: exception
    record = vec<std::string>();
    return false;
  }
  if (this->fields.empty()) {
    record = vec<std::string>();
    return false;
  }

  record = std::move(this->fields);
  return true;
}

} // namespace csv
} // namespace ww
