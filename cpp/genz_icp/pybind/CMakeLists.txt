find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(genz_icp_pybind MODULE genz_icp_pybind.cpp)
target_link_libraries(genz_icp_pybind PRIVATE genz_icp::core genz_icp::metrics)
install(TARGETS genz_icp_pybind DESTINATION .)
