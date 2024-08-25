cmake_minimum_required(VERSION 3.14)
project(wwcsv CXX)

set(PROJECT_VERSION 1.0.0)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(wwcsv STATIC ./csv/reader.cpp)
target_include_directories(wwcsv INTERFACE .)
set_target_properties(wwcsv
    PROPERTIES
    VERSION ${PROJECT_VERSION})
