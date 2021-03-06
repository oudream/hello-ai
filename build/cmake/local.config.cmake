
message("------------gs_project_path: " ${gs_project_path})
set(gs_hello_path ${gs_project_path}/hello)
set(gs_3rd_path ${gs_project_path}/3rd)
message("------------gs_hello_path: " ${gs_hello_path})
message("------------gs_3rd_path: " ${gs_3rd_path})

if (NOT gs_project_deploy_path)
    set(gs_project_deploy_path ${gs_project_path}/build/deploy)
    if (UNIX)
        set(gs_project_output_path_debug ${gs_project_deploy_path}/unix/bin_d)
        set(gs_project_output_path_release ${gs_project_deploy_path}/unix/bin)
    elseif (WIN32)
        set(gs_project_output_path_debug ${gs_project_deploy_path}/win32/bin_d)
        set(gs_project_output_path_release ${gs_project_deploy_path}/win32/bin)
        if(CMAKE_COMPILER_IS_GNUCC OR CMAKE_COMPILER_IS_GNUCXX)
            # set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -static-libgcc -static-libstdc++")
            # set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -static-libgcc -static-libstdc++")
            set(gs_project_output_path_debug ${gs_project_deploy_path}/win32/bin_gnu_d)
            set(gs_project_output_path_release ${gs_project_deploy_path}/win32/bin_gnu)
        endif()
    endif()

    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG "${gs_project_output_path_debug}")
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE "${gs_project_output_path_release}")
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_DEBUG "${gs_project_output_path_debug}")
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY_RELEASE "${gs_project_output_path_release}")
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG "${gs_project_output_path_debug}")
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE "${gs_project_output_path_release}")
endif()

if (CMAKE_BUILD_TYPE STREQUAL Release)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${gs_project_output_path_release})
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DRELEASE")
    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DRELEASE")
else()
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${gs_project_output_path_debug})
    set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -DDEBUG")
    set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -DDEBUG")
endif()
message("------------CMAKE_RUNTIME_OUTPUT_DIRECTORY: " ${CMAKE_RUNTIME_OUTPUT_DIRECTORY})
