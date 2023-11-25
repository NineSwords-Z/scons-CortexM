import os

# board options
BOARD = 'MIMXRT1064'

# toolchains options
ARCH = 'arm'
CPU = 'cortex-m7'
FPU = 'fpv5-d16'
FLOAT_ABI = 'hard'
# build version: debug or release
BUILD = 'debug'
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

CDEFINES = ' -DDEBUG -DCPU_MIMXRT1064DVL6A -DMCUXPRESSO_SDK -DSERIAL_PORT_TYPE_UART=1 -DSDK_DEBUGCONSOLE=1 -DXIP_EXTERNAL_FLASH=1 -DXIP_BOOT_HEADER_ENABLE=1'
ADEFINES = ' -DDEBUG -D__STARTUP_CLEAR_BSS -D__STARTUP_INITIALIZE_NONCACHEDATA'

CFLAGS = ' -c' + MCU + CDEFINES +\
    ' -g -Wall -MMD -MP -MD -MT -fno-common -ffreestanding -fno-builtin -mapcs'

AFLAGS = ' -c' + MCU + ADEFINES +\
    ' -x assembler-with-cpp'

LFLAGS = MCU + ' --specs=nano.specs -TMIMXRT1064xxxxx_flexspi_nor.ld ' + \
    ' -lgcc -lc -lm -lnosys' + \
    ' -Wl,--print-memory-usage,--start-group,--end-group,-Map=build/' + BOARD + '.map,-cref,-u,Reset_Handler' + \
    ' -Xlinker --gc-sections -Xlinker -static -Xlinker -z -Xlinker muldefs'

if BUILD == 'debug':
    CFLAGS += ' -O0 -gdwarf-3'
    AFLAGS += ' -gdwarf-3'
else:
    CFLAGS += ' -O2'

CXXFLAGS = CFLAGS
CFLAGS += ' -std=gnu99'
CXXFLAGS += ' -std=c++14'

POST_ACTION_PRE = SIZE + ' $TARGET \n'
POST_ACTION_HEX = OBJCPY + ' -O ihex $TARGET build/' + BOARD + '.hex\n'
POST_ACTION_BIN = OBJCPY + ' -O binary $TARGET build/' + BOARD + '.bin\n'
