#include "asobi.hpp"
#include <iostream>
#include <pqxx/pqxx>
#include <string_view>

int asobi() {
  std::cout << "hello" << std::endl;
  pqxx::connection c("host=localhost "
                     "port=5432 "
                     "user=postgres "
                     "password=postgres "
                     "dbname=postgres "
                     "connect_timeout=10");
  try {
    pqxx::work w(c);
    pqxx::row r = w.exec1("SELECT 1");
    std::cout << "row: " << r[0].as<int>() << std::endl;
    w.commit();
  } catch (std::exception &e) {
    std::cerr << e.what() << std::endl;
    return 1;
  }
  try {
    pqxx::work w(c);
    w.exec0("DROP SCHEMA IF EXISTS test1 CASCADE");
    w.exec0("CREATE SCHEMA test1");
    w.exec0("CREATE TABLE test1.customers ("
            "id SERIAL PRIMARY KEY,"
            "code VARCHAR(255) NOT NULL"
            ")");
    c.prepare("hoge", "INSERT INTO test1.customers (code) VALUES"
                      "($1),"
                      "($2),"
                      "($3),"
                      "($4),"
                      "($5),"
                      "($6)");
    w.exec_prepared("hoge", "X0001", "X0002", "X0003", "X0004", "X0005",
                    "X0006");
    w.commit();
  } catch (std::exception &e) {
    std::cerr << e.what() << std::endl;
    return 1;
  }
  try {
    pqxx::work w(c);
    for (auto [id, code] :
         w.query<int, std::string_view>("SELECT * FROM test1.customers")) {
      std::cout << "(id: " << id << ", code: " << code << ")" << std::endl;
    }
    w.commit();
  } catch (std::exception &e) {
    std::cerr << e.what() << std::endl;
    return 1;
  }

  return 0;
}
