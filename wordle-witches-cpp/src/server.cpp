#include "server.hpp"
#include <boost/program_options.hpp>
#include <crow.h>
#include <string>

namespace ww {

int run_server() {
  crow::SimpleApp app;

  CROW_ROUTE(app, "/")
  ([]() {
    auto h = hello_response(std::string("hello"));
    return h;
  });

  app.port(18080).multithreaded().run();

  return 0;
}

} // namespace ww
