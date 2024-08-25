cmake_minimum_required(VERSION 3.14)
project(crow-sawari CXX)

set(PROJECT_VERSION 1.0.0)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)

set(MY_ASIO_INCLUDE_PATH /usr/local/Cellar/asio/1.30.2/include)

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

find_package(Boost REQUIRED
  COMPONENTS
    context
    filesystem
    program_options
    regex
    system
    thread
    date_time
)
if(Boost_FOUND)
  message (STATUS "Found Boost")
else(Boost_FOUND)
  message(WARNING "Boost not found")
endif()

add_subdirectory(./src/libcsv)
add_subdirectory(./deps/Crow build-crow)
add_subdirectory(./deps/libpqxx build-pqxx)
add_executable(main 
  main.cpp
  src/server.cpp
  src/import_csv.cpp
  src/asobi.cpp
)
target_link_libraries(main PRIVATE
  Threads::Threads
  Boost::program_options
  wwcsv
  Crow
  pqxx
)
target_include_directories(main PUBLIC
  ${MY_ASIO_INCLUDE_PATH}
)
