#pragma once

#include <iostream>
#include <vector>

namespace ww {
namespace csv {

struct reader {
  enum State {
    AfterComma,
    InField,
    InQuote,
    QuoteInQuote,
    AfterCR,
    Error,
  };

  reader(std::istream &is);

  bool readline(std::vector<std::string> &record);

private:
  bool update(char c);

  std::istream &in;
  State state;
  std::string field;
  std::vector<std::string> fields;
};

inline bool reader::update(char c) {
  switch (this->state) {
  case State::AfterComma:
    switch (c) {
    case '\"':
      this->state = State::InQuote;
      break;
    case ',':
      this->fields.push_back(std::move(this->field));
      this->state = State::AfterComma;
      break;
    case '\r':
      this->state = State::AfterCR;
      break;
    case '\n':
      this->fields.push_back(std::move(this->field));
      this->state = State::AfterComma;
      return false;
    default:
      this->field.push_back(c);
      this->state = InField;
      break;
    }
    break;
  case State::InField:
    switch (c) {
    case ',':
      this->fields.push_back(std::move(this->field));
      this->state = State::AfterComma;
      break;
    case '\r':
      this->state = State::AfterCR;
      break;
    case '\n':
      this->fields.push_back(std::move(this->field));
      this->state = State::AfterComma;
      return false;
    default:
      this->field.push_back(c);
      this->state = State::InField;
      break;
    }
    break;
  case State::InQuote:
    switch (c) {
    case '\"':
      this->state = State::QuoteInQuote;
      break;
    default:
      this->field.push_back(c);
      this->state = State::InQuote;
      break;
    }
    break;
  case State::QuoteInQuote:
    switch (c) {
    case '\"':
      this->field.push_back(c);
      this->state = State::InQuote;
      break;
    case ',':
      this->fields.push_back(std::move(this->field));
      this->state = State::AfterComma;
      break;
    case '\r':
      this->state = State::AfterCR;
      break;
    case '\n':
      this->fields.push_back(std::move(this->field));
      this->state = State::AfterComma;
      return false;
    default:
      this->state = State::Error;
    }
    break;
  case State::AfterCR:
    switch (c) {
    case '\n':
      this->fields.push_back(std::move(this->field));
      this->state = State::AfterComma;
      return false;
    default:
      this->state = State::Error;
    }
    break;
  case State::Error:
    return false;
  }

  return true;
}

} // namespace csv
} // namespace ww
