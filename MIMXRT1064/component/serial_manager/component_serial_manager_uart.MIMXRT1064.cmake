# Add set(CONFIG_USE_component_serial_manager_uart true) in config.cmake to use this component

include_guard(GLOBAL)
message("${CMAKE_CURRENT_LIST_FILE} component is included.")

if(CONFIG_USE_component_lpuart_adapter AND CONFIG_USE_component_serial_manager AND (CONFIG_USE_driver_lpuart))

target_sources(${MCUX_SDK_PROJECT_NAME} PRIVATE
${CMAKE_CURRENT_LIST_DIR}/fsl_component_serial_port_uart.c
)

target_include_directories(${MCUX_SDK_PROJECT_NAME} PUBLIC
${CMAKE_CURRENT_LIST_DIR}/
)

if(CONFIG_USE_COMPONENT_CONFIGURATION)
message("===>Import configuration from ${CMAKE_CURRENT_LIST_FILE}")

target_compile_definitions(${MCUX_SDK_PROJECT_NAME} PUBLIC
-DSERIAL_PORT_TYPE_UART=1
)

endif()

else()

message(SEND_ERROR "component_serial_manager_uart.MIMXRT1064 dependency does not meet, please check ${CMAKE_CURRENT_LIST_FILE}.")

endif()
