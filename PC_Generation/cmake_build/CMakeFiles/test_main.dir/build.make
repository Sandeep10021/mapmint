# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/user/OpenSfM/opensfm/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/user/OpenSfM/cmake_build

# Include any dependencies generated for this target.
include CMakeFiles/test_main.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/test_main.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test_main.dir/flags.make

CMakeFiles/test_main.dir/testing_main.cc.o: CMakeFiles/test_main.dir/flags.make
CMakeFiles/test_main.dir/testing_main.cc.o: /home/user/OpenSfM/opensfm/src/testing_main.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test_main.dir/testing_main.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/test_main.dir/testing_main.cc.o -c /home/user/OpenSfM/opensfm/src/testing_main.cc

CMakeFiles/test_main.dir/testing_main.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test_main.dir/testing_main.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/OpenSfM/opensfm/src/testing_main.cc > CMakeFiles/test_main.dir/testing_main.cc.i

CMakeFiles/test_main.dir/testing_main.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test_main.dir/testing_main.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/OpenSfM/opensfm/src/testing_main.cc -o CMakeFiles/test_main.dir/testing_main.cc.s

CMakeFiles/test_main.dir/testing_main.cc.o.requires:

.PHONY : CMakeFiles/test_main.dir/testing_main.cc.o.requires

CMakeFiles/test_main.dir/testing_main.cc.o.provides: CMakeFiles/test_main.dir/testing_main.cc.o.requires
	$(MAKE) -f CMakeFiles/test_main.dir/build.make CMakeFiles/test_main.dir/testing_main.cc.o.provides.build
.PHONY : CMakeFiles/test_main.dir/testing_main.cc.o.provides

CMakeFiles/test_main.dir/testing_main.cc.o.provides.build: CMakeFiles/test_main.dir/testing_main.cc.o


# Object files for target test_main
test_main_OBJECTS = \
"CMakeFiles/test_main.dir/testing_main.cc.o"

# External object files for target test_main
test_main_EXTERNAL_OBJECTS =

libtest_main.a: CMakeFiles/test_main.dir/testing_main.cc.o
libtest_main.a: CMakeFiles/test_main.dir/build.make
libtest_main.a: CMakeFiles/test_main.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libtest_main.a"
	$(CMAKE_COMMAND) -P CMakeFiles/test_main.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test_main.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test_main.dir/build: libtest_main.a

.PHONY : CMakeFiles/test_main.dir/build

CMakeFiles/test_main.dir/requires: CMakeFiles/test_main.dir/testing_main.cc.o.requires

.PHONY : CMakeFiles/test_main.dir/requires

CMakeFiles/test_main.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/test_main.dir/cmake_clean.cmake
.PHONY : CMakeFiles/test_main.dir/clean

CMakeFiles/test_main.dir/depend:
	cd /home/user/OpenSfM/cmake_build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/user/OpenSfM/opensfm/src /home/user/OpenSfM/opensfm/src /home/user/OpenSfM/cmake_build /home/user/OpenSfM/cmake_build /home/user/OpenSfM/cmake_build/CMakeFiles/test_main.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test_main.dir/depend

