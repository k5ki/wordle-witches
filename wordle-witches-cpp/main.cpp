#include "src/asobi.hpp"
#include "src/import_csv.hpp"
#include "src/server.hpp"
#include <boost/program_options.hpp>
#include <string>

int main(const int argc, const char *const *const argv) {
  namespace po = boost::program_options;

  po::options_description global("main.cpp");
  global.add_options()("command",
                       po::value<std::string>()->default_value("server"),
                       "command")("help,h", "help");
  po::positional_options_description pos;
  pos.add("command", 1);

  po::variables_map vm;
  po::parsed_options parsed = po::command_line_parser(argc, argv)
                                  .options(global)
                                  .positional(pos)
                                  .allow_unregistered()
                                  .run();
  po::store(parsed, vm);

  if (vm.count("help")) {
    std::cout << global << std::endl;
    return 0;
  }

  auto command = vm["command"].as<std::string>();

  if (command == "server") {
    return ww::run_server();
  } else if (command == "import-csv") {
    return ww::import_csv();
  } else if (command == "asobi") {
    return asobi();
  } else {
    std::cout << "command: " << command << std::endl;
  }

  return 0;
}
