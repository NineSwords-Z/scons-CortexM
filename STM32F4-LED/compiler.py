import os

# board options
BOARD = 'STM32F407G-DISC1'

# toolchains options
ARCH = 'arm'
CPU = 'cortex-m4'
FPU = 'fpv4-sp-d16'
FLOAT_ABI = 'hard'
# build version: debug or release
BUILD = 'release'
BUILD_ROOT = 'build'

# toolchains
PREFIX = 'arm-none-eabi-'
CC = PREFIX + 'gcc'
AS = PREFIX + 'gcc'
AR = PREFIX + 'ar'
CXX = PREFIX + 'g++'
LINK = PREFIX + 'gcc'
TARGET_EXT = 'elf'
SIZE = PREFIX + 'size'
OBJDUMP = PREFIX + 'objdump'
OBJCPY = PREFIX + 'objcopy'

MCU = ' -mcpu=' + CPU + \
    ' -mthumb -mfpu=' + FPU + ' -mfloat-abi=' + FLOAT_ABI +' -ffunction-sections -fdata-sections'

DEFINES = ' -DUSE_HAL_DRIVER -DSTM32F407xx'

CFLAGS = MCU + \
    ' -g -Wall -Wstrict-aliasing=0 -Wno-uninitialized -Wno-unused-function -Wno-switch' + DEFINES
AFLAGS = ' -c' + MCU + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
LFLAGS = MCU + ' -lm -lgcc -lc' + \
    ' -nostartfiles -Wl,--gc-sections,--print-memory-usage,-Map=build/' + BOARD + '.map,-cref,-u,Reset_Handler -T STM32F407VGTx_FLASH.ld'

CPATH = ''
LPATH = ''

if BUILD == 'debug':
    CFLAGS += ' -O0 -gdwarf-2'
    AFLAGS += ' -gdwarf-2'
else:
    CFLAGS += ' -O2'

CXXFLAGS = CFLAGS
CFLAGS += ' -std=c99'
CXXFLAGS += ' -std=c++14'

POST_ACTION = OBJCPY + ' -O binary $TARGET build/' + BOARD + '.bin\n' + SIZE + ' $TARGET \n'
