#pragma once

#include <crow.h>
#include <string>

namespace ww {

struct hello_response : public crow::returnable {
  std::string message;

  hello_response(std::string message) : returnable("application/json") {
    this->message = message;
  };

  std::string dump() const override {
    auto json = crow::json::wvalue({{"message", this->message}});
    return json.dump();
  }
};

int run_server();

} // namespace ww
