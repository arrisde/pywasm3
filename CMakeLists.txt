cmake_minimum_required(VERSION 3.4.0)

project(pywasm3)

set(PyExec "python")

find_package(PythonExtensions REQUIRED)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")

add_custom_command(
    OUTPUT
        ${CMAKE_BINARY_DIR}/_pywasm3_cffi.c
    DEPENDS 
        ${CMAKE_BINARY_DIR}/_wasm3_pp.h
    COMMAND 
        ${PyExec} ${CMAKE_SOURCE_DIR}/cffi/build_cffi.py ${CMAKE_BINARY_DIR}/_wasm3_pp.h ${CMAKE_BINARY_DIR}/_pywasm3_cffi.c
)

add_custom_command(
    OUTPUT
        ${CMAKE_BINARY_DIR}/_wasm3_pp.h
    DEPENDS 
        ${CMAKE_BINARY_DIR}/_wasm3.h
    COMMAND 
        ${CMAKE_C_COMPILER} -E ${CMAKE_BINARY_DIR}/_wasm3.h > ${CMAKE_BINARY_DIR}/_wasm3_pp.h
)

add_custom_command(
    OUTPUT
        ${CMAKE_BINARY_DIR}/_wasm3.h
    DEPENDS 
        ${CMAKE_SOURCE_DIR}/wasm3.git/source/wasm3.h
    COMMAND 
        ${PyExec} 
        ${CMAKE_SOURCE_DIR}/cffi/remove_std_includes.py 
        ${CMAKE_SOURCE_DIR}/wasm3.git/source/wasm3.h 
        ${CMAKE_BINARY_DIR}/_wasm3.h
)

add_subdirectory(wasm3.git/source)
add_library(_pywasm3 MODULE cffi/stack_accessor.c ${CMAKE_BINARY_DIR}/_pywasm3_cffi.c)

target_include_directories(_pywasm3 PRIVATE wasm3.git/source cffi ${CMAKE_BINARY_DIR})
target_link_libraries(_pywasm3 m3)

python_extension_module(_pywasm3)
install(TARGETS _pywasm3 LIBRARY DESTINATION pywasm3)
