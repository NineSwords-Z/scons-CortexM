if exist CMakeFiles (RD /s /Q CMakeFiles)
if exist Makefile (DEL /s /Q /F Makefile)
if exist cmake_install.cmake (DEL /s /Q /F cmake_install.cmake)
if exist CMakeCache.txt (DEL /s /Q /F CMakeCache.txt)
cmake -DCMAKE_TOOLCHAIN_FILE="armgcc.cmake" -DCMAKE_VERBOSE_MAKEFILE=ON -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=debug  .
make -j > build_log.txt 
