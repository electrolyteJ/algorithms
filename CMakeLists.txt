cmake_minimum_required(VERSION 3.20)
project(algorithms)
set(CMAKE_CXX_STANDARD 14)
#target_include_directories(algorithms PUBLIC src/common/)
include_directories(src/common/)
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fno-exceptions")

file(GLOB_RECURSE  dir "${CMAKE_CURRENT_SOURCE_DIR}/src/*/*.cpp"
        "${CMAKE_CURRENT_SOURCE_DIR}/src/*/*.cc"
        "${CMAKE_CURRENT_SOURCE_DIR}/src/*/*.cxx"
        "${CMAKE_CURRENT_SOURCE_DIR}/src/*/*.c")

foreach (file ${dir})
    get_filename_component(name ${file} NAME)
    add_executable(${name} ${file})
endforeach ()


