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
include geometry/CMakeFiles/geometry.dir/depend.make

# Include the progress variables for this target.
include geometry/CMakeFiles/geometry.dir/progress.make

# Include the compile flags for this target's objects.
include geometry/CMakeFiles/geometry.dir/flags.make

geometry/CMakeFiles/geometry.dir/src/camera.cc.o: geometry/CMakeFiles/geometry.dir/flags.make
geometry/CMakeFiles/geometry.dir/src/camera.cc.o: /home/user/OpenSfM/opensfm/src/geometry/src/camera.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object geometry/CMakeFiles/geometry.dir/src/camera.cc.o"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/geometry.dir/src/camera.cc.o -c /home/user/OpenSfM/opensfm/src/geometry/src/camera.cc

geometry/CMakeFiles/geometry.dir/src/camera.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/geometry.dir/src/camera.cc.i"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/OpenSfM/opensfm/src/geometry/src/camera.cc > CMakeFiles/geometry.dir/src/camera.cc.i

geometry/CMakeFiles/geometry.dir/src/camera.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/geometry.dir/src/camera.cc.s"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/OpenSfM/opensfm/src/geometry/src/camera.cc -o CMakeFiles/geometry.dir/src/camera.cc.s

geometry/CMakeFiles/geometry.dir/src/camera.cc.o.requires:

.PHONY : geometry/CMakeFiles/geometry.dir/src/camera.cc.o.requires

geometry/CMakeFiles/geometry.dir/src/camera.cc.o.provides: geometry/CMakeFiles/geometry.dir/src/camera.cc.o.requires
	$(MAKE) -f geometry/CMakeFiles/geometry.dir/build.make geometry/CMakeFiles/geometry.dir/src/camera.cc.o.provides.build
.PHONY : geometry/CMakeFiles/geometry.dir/src/camera.cc.o.provides

geometry/CMakeFiles/geometry.dir/src/camera.cc.o.provides.build: geometry/CMakeFiles/geometry.dir/src/camera.cc.o


geometry/CMakeFiles/geometry.dir/src/essential.cc.o: geometry/CMakeFiles/geometry.dir/flags.make
geometry/CMakeFiles/geometry.dir/src/essential.cc.o: /home/user/OpenSfM/opensfm/src/geometry/src/essential.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object geometry/CMakeFiles/geometry.dir/src/essential.cc.o"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/geometry.dir/src/essential.cc.o -c /home/user/OpenSfM/opensfm/src/geometry/src/essential.cc

geometry/CMakeFiles/geometry.dir/src/essential.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/geometry.dir/src/essential.cc.i"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/OpenSfM/opensfm/src/geometry/src/essential.cc > CMakeFiles/geometry.dir/src/essential.cc.i

geometry/CMakeFiles/geometry.dir/src/essential.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/geometry.dir/src/essential.cc.s"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/OpenSfM/opensfm/src/geometry/src/essential.cc -o CMakeFiles/geometry.dir/src/essential.cc.s

geometry/CMakeFiles/geometry.dir/src/essential.cc.o.requires:

.PHONY : geometry/CMakeFiles/geometry.dir/src/essential.cc.o.requires

geometry/CMakeFiles/geometry.dir/src/essential.cc.o.provides: geometry/CMakeFiles/geometry.dir/src/essential.cc.o.requires
	$(MAKE) -f geometry/CMakeFiles/geometry.dir/build.make geometry/CMakeFiles/geometry.dir/src/essential.cc.o.provides.build
.PHONY : geometry/CMakeFiles/geometry.dir/src/essential.cc.o.provides

geometry/CMakeFiles/geometry.dir/src/essential.cc.o.provides.build: geometry/CMakeFiles/geometry.dir/src/essential.cc.o


geometry/CMakeFiles/geometry.dir/src/covariance.cc.o: geometry/CMakeFiles/geometry.dir/flags.make
geometry/CMakeFiles/geometry.dir/src/covariance.cc.o: /home/user/OpenSfM/opensfm/src/geometry/src/covariance.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object geometry/CMakeFiles/geometry.dir/src/covariance.cc.o"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/geometry.dir/src/covariance.cc.o -c /home/user/OpenSfM/opensfm/src/geometry/src/covariance.cc

geometry/CMakeFiles/geometry.dir/src/covariance.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/geometry.dir/src/covariance.cc.i"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/OpenSfM/opensfm/src/geometry/src/covariance.cc > CMakeFiles/geometry.dir/src/covariance.cc.i

geometry/CMakeFiles/geometry.dir/src/covariance.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/geometry.dir/src/covariance.cc.s"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/OpenSfM/opensfm/src/geometry/src/covariance.cc -o CMakeFiles/geometry.dir/src/covariance.cc.s

geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.requires:

.PHONY : geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.requires

geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.provides: geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.requires
	$(MAKE) -f geometry/CMakeFiles/geometry.dir/build.make geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.provides.build
.PHONY : geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.provides

geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.provides.build: geometry/CMakeFiles/geometry.dir/src/covariance.cc.o


geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o: geometry/CMakeFiles/geometry.dir/flags.make
geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o: /home/user/OpenSfM/opensfm/src/geometry/src/triangulation.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/geometry.dir/src/triangulation.cc.o -c /home/user/OpenSfM/opensfm/src/geometry/src/triangulation.cc

geometry/CMakeFiles/geometry.dir/src/triangulation.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/geometry.dir/src/triangulation.cc.i"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/OpenSfM/opensfm/src/geometry/src/triangulation.cc > CMakeFiles/geometry.dir/src/triangulation.cc.i

geometry/CMakeFiles/geometry.dir/src/triangulation.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/geometry.dir/src/triangulation.cc.s"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/OpenSfM/opensfm/src/geometry/src/triangulation.cc -o CMakeFiles/geometry.dir/src/triangulation.cc.s

geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.requires:

.PHONY : geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.requires

geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.provides: geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.requires
	$(MAKE) -f geometry/CMakeFiles/geometry.dir/build.make geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.provides.build
.PHONY : geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.provides

geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.provides.build: geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o


geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o: geometry/CMakeFiles/geometry.dir/flags.make
geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o: /home/user/OpenSfM/opensfm/src/geometry/src/absolute_pose.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/geometry.dir/src/absolute_pose.cc.o -c /home/user/OpenSfM/opensfm/src/geometry/src/absolute_pose.cc

geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/geometry.dir/src/absolute_pose.cc.i"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/OpenSfM/opensfm/src/geometry/src/absolute_pose.cc > CMakeFiles/geometry.dir/src/absolute_pose.cc.i

geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/geometry.dir/src/absolute_pose.cc.s"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/OpenSfM/opensfm/src/geometry/src/absolute_pose.cc -o CMakeFiles/geometry.dir/src/absolute_pose.cc.s

geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.requires:

.PHONY : geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.requires

geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.provides: geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.requires
	$(MAKE) -f geometry/CMakeFiles/geometry.dir/build.make geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.provides.build
.PHONY : geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.provides

geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.provides.build: geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o


geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o: geometry/CMakeFiles/geometry.dir/flags.make
geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o: /home/user/OpenSfM/opensfm/src/geometry/src/relative_pose.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/geometry.dir/src/relative_pose.cc.o -c /home/user/OpenSfM/opensfm/src/geometry/src/relative_pose.cc

geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/geometry.dir/src/relative_pose.cc.i"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/user/OpenSfM/opensfm/src/geometry/src/relative_pose.cc > CMakeFiles/geometry.dir/src/relative_pose.cc.i

geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/geometry.dir/src/relative_pose.cc.s"
	cd /home/user/OpenSfM/cmake_build/geometry && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/user/OpenSfM/opensfm/src/geometry/src/relative_pose.cc -o CMakeFiles/geometry.dir/src/relative_pose.cc.s

geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.requires:

.PHONY : geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.requires

geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.provides: geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.requires
	$(MAKE) -f geometry/CMakeFiles/geometry.dir/build.make geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.provides.build
.PHONY : geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.provides

geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.provides.build: geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o


# Object files for target geometry
geometry_OBJECTS = \
"CMakeFiles/geometry.dir/src/camera.cc.o" \
"CMakeFiles/geometry.dir/src/essential.cc.o" \
"CMakeFiles/geometry.dir/src/covariance.cc.o" \
"CMakeFiles/geometry.dir/src/triangulation.cc.o" \
"CMakeFiles/geometry.dir/src/absolute_pose.cc.o" \
"CMakeFiles/geometry.dir/src/relative_pose.cc.o"

# External object files for target geometry
geometry_EXTERNAL_OBJECTS =

geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/src/camera.cc.o
geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/src/essential.cc.o
geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/src/covariance.cc.o
geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o
geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o
geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o
geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/build.make
geometry/libgeometry.a: geometry/CMakeFiles/geometry.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/user/OpenSfM/cmake_build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX static library libgeometry.a"
	cd /home/user/OpenSfM/cmake_build/geometry && $(CMAKE_COMMAND) -P CMakeFiles/geometry.dir/cmake_clean_target.cmake
	cd /home/user/OpenSfM/cmake_build/geometry && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/geometry.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
geometry/CMakeFiles/geometry.dir/build: geometry/libgeometry.a

.PHONY : geometry/CMakeFiles/geometry.dir/build

geometry/CMakeFiles/geometry.dir/requires: geometry/CMakeFiles/geometry.dir/src/camera.cc.o.requires
geometry/CMakeFiles/geometry.dir/requires: geometry/CMakeFiles/geometry.dir/src/essential.cc.o.requires
geometry/CMakeFiles/geometry.dir/requires: geometry/CMakeFiles/geometry.dir/src/covariance.cc.o.requires
geometry/CMakeFiles/geometry.dir/requires: geometry/CMakeFiles/geometry.dir/src/triangulation.cc.o.requires
geometry/CMakeFiles/geometry.dir/requires: geometry/CMakeFiles/geometry.dir/src/absolute_pose.cc.o.requires
geometry/CMakeFiles/geometry.dir/requires: geometry/CMakeFiles/geometry.dir/src/relative_pose.cc.o.requires

.PHONY : geometry/CMakeFiles/geometry.dir/requires

geometry/CMakeFiles/geometry.dir/clean:
	cd /home/user/OpenSfM/cmake_build/geometry && $(CMAKE_COMMAND) -P CMakeFiles/geometry.dir/cmake_clean.cmake
.PHONY : geometry/CMakeFiles/geometry.dir/clean

geometry/CMakeFiles/geometry.dir/depend:
	cd /home/user/OpenSfM/cmake_build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/user/OpenSfM/opensfm/src /home/user/OpenSfM/opensfm/src/geometry /home/user/OpenSfM/cmake_build /home/user/OpenSfM/cmake_build/geometry /home/user/OpenSfM/cmake_build/geometry/CMakeFiles/geometry.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : geometry/CMakeFiles/geometry.dir/depend
