#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "Darknet::dark" for configuration ""
set_property(TARGET Darknet::dark APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(Darknet::dark PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "/home/pi/Desktop/Sensing/darknet/libdark.so"
  IMPORTED_SONAME_NOCONFIG "libdark.so"
  )

list(APPEND _cmake_import_check_targets Darknet::dark )
list(APPEND _cmake_import_check_files_for_Darknet::dark "/home/pi/Desktop/Sensing/darknet/libdark.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
