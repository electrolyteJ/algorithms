cmake_minimum_required(VERSION 3.20)
project(algorithms)
set(CMAKE_CXX_STANDARD 14)
#target_include_directories(algorithms PUBLIC src/common/)
include_directories(src/common/)

file(GLOB dir "${CMAKE_CURRENT_SOURCE_DIR}/src/basic/*.cpp")

foreach (file ${dir})
    get_filename_component(name ${file} NAME)
    add_executable(${name} ${file} src/basic/_01_Array_LinkedList_141.cpp src/basic/_01_Array_LinkedList_142.cpp src/basic/_01_Array_LinkedList_206.cpp)
endforeach ()

