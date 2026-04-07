cmake_minimum_required(VERSION 3.10)
project(MemoryRiver)

set(CMAKE_CXX_STANDARD 17)

file(GLOB SOURCES "*.cpp")

if(SOURCES)
    add_executable(code ${SOURCES})
else()
    file(WRITE "${CMAKE_CURRENT_SOURCE_DIR}/dummy.cpp" "int main() { return 0; }")
    add_executable(code dummy.cpp)
endif()