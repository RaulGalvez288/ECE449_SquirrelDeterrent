# Install script for directory: /home/pi/Desktop/Sensing/darknet

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pi/Desktop/Sensing/darknet")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/libdark.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/libdark.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/libdark.so"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/pi/Desktop/Sensing/darknet/libdark.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet" TYPE SHARED_LIBRARY FILES "/home/pi/Desktop/Sensing/darknet/build-release/libdark.so")
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/libdark.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/libdark.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/libdark.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "dev" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/pi/Desktop/Sensing/darknet/include/darknet/darknet.h;/home/pi/Desktop/Sensing/darknet/include/darknet/yolo_v2_class.hpp")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet/include/darknet" TYPE FILE FILES
    "/home/pi/Desktop/Sensing/darknet/include/darknet.h"
    "/home/pi/Desktop/Sensing/darknet/include/yolo_v2_class.hpp"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/pi/Desktop/Sensing/darknet/uselib")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet" TYPE EXECUTABLE FILES "/home/pi/Desktop/Sensing/darknet/build-release/uselib")
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib"
         OLD_RPATH "/home/pi/Desktop/Sensing/darknet/build-release:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/darknet" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/darknet")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/darknet"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/pi/Desktop/Sensing/darknet/darknet")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet" TYPE EXECUTABLE FILES "/home/pi/Desktop/Sensing/darknet/build-release/darknet")
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/darknet" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/darknet")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/darknet")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib_track" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib_track")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib_track"
         RPATH "")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/pi/Desktop/Sensing/darknet/uselib_track")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet" TYPE EXECUTABLE FILES "/home/pi/Desktop/Sensing/darknet/build-release/uselib_track")
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib_track" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib_track")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib_track"
         OLD_RPATH "/home/pi/Desktop/Sensing/darknet/build-release:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/uselib_track")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetTargets.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetTargets.cmake"
         "/home/pi/Desktop/Sensing/darknet/build-release/CMakeFiles/Export/8f2bc66b1c3e9c2363994e6a2b060b57/DarknetTargets.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetTargets-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetTargets.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetTargets.cmake")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet/share/darknet" TYPE FILE FILES "/home/pi/Desktop/Sensing/darknet/build-release/CMakeFiles/Export/8f2bc66b1c3e9c2363994e6a2b060b57/DarknetTargets.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^()$")
    list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
     "/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetTargets-noconfig.cmake")
    if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
      message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
    endif()
    file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet/share/darknet" TYPE FILE FILES "/home/pi/Desktop/Sensing/darknet/build-release/CMakeFiles/Export/8f2bc66b1c3e9c2363994e6a2b060b57/DarknetTargets-noconfig.cmake")
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetConfig.cmake;/home/pi/Desktop/Sensing/darknet/share/darknet/DarknetConfigVersion.cmake")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/home/pi/Desktop/Sensing/darknet/share/darknet" TYPE FILE FILES
    "/home/pi/Desktop/Sensing/darknet/build-release/CMakeFiles/DarknetConfig.cmake"
    "/home/pi/Desktop/Sensing/darknet/build-release/DarknetConfigVersion.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/pi/Desktop/Sensing/darknet/build-release/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
