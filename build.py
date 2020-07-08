import os

Import("env")


def extract_project_defines():
    defines = env.ParseFlags(env.get("BUILD_FLAGS", {})).get("CPPDEFINES", [])
    if "BOARD" in env and "build.extra_flags" in env.BoardConfig():
        defines.extend(
            env.ParseFlags(env.BoardConfig().get("build.extra_flags")).get(
                "CPPDEFINES", []
            )
        )
    return defines


# Generic
env.Append(
    CCFLAGS=["-Wall"],
    CPPDEFINES=["USE_HAL_DRIVER"],
    CPPPATH=[
        os.path.join("$PROJECT_SRC_DIR", "McuApi/STM32/IncStm32"),
        os.path.join(
            "$PROJECT_SRC_DIR", "McuApi", "STM32", "Drivers", "CMSIS", "Include"
        ),
        os.path.join("$PROJECT_SRC_DIR", "UserCode"),
        os.path.join("$PROJECT_SRC_DIR", "McuApi"),
        os.path.join("$PROJECT_SRC_DIR", "MinimouseSrc"),
        os.path.join("$PROJECT_SRC_DIR", "radio", "sx1272"),
        os.path.join("$PROJECT_SRC_DIR", "radio", "SX1276Lib", "registers"),
        os.path.join("$PROJECT_SRC_DIR", "radio", "SX1276Lib", "sx1276"),
        os.path.join("$PROJECT_SRC_DIR", "radio", "SX126X"),
        os.path.join("$PROJECT_SRC_DIR", "PointToPoint"),
        os.path.join("$PROJECT_SRC_DIR", "RadioPlaner"),
    ],
    CXXFLAGS=["-std=c++11"],
)

env.Replace(
    SRC_FILTER=[
        "-<*>",
        "+<UserCode/appli.cpp>",
        "+<UserCode/main.cpp>",
        "+<radio/sx1272/sx1272.cpp>",
        "+<radio/SX1276Lib/sx1276/sx1276.cpp>",
        "+<radio/SX126X/SX126x.cpp>",
        "+<RadioPlaner/RadioPlaner.cpp>",
        "+<MinimouseSrc/>",
    ]
)

cpp_defines = env.Flatten(extract_project_defines())
if "RADIO_SX1276" in cpp_defines:
    env.Append(
        SRC_FILTER=[
            "+<PointToPoint/PointToPointReceiver.cpp>",
            "+<PointToPoint/PointToPointTransmitter.cpp>",
            "+<UserCode/MainRelay.cpp>",
        ]
    )
if "MURATA_BOARD" in cpp_defines:
    env.Append(
        CPPPATH=[
            os.path.join(
                "$PROJECT_SRC_DIR",
                "McuApi",
                "STM32",
                "Drivers",
                "STM32L0xx_HAL_Driver",
                "Inc",
            ),
            os.path.join(
                "$PROJECT_SRC_DIR",
                "McuApi",
                "STM32",
                "Drivers",
                "STM32L0xx_HAL_Driver",
                "Inc",
                "Legacy",
            ),
            os.path.join(
                "$PROJECT_SRC_DIR",
                "McuApi",
                "STM32",
                "Drivers",
                "CMSIS",
                "Device",
                "ST",
                "STM32L0xx",
                "Include",
            ),
        ],
        SRC_FILTER=[
            "+<McuApi/STM32/SrcStm32/stm32l0xx_it.cpp>",
            "+<McuApi/STM32/SrcStm32/stm32l0xx_hal_msp.cpp>",
            "+<McuApi/STM32/SrcStm32/system_stm32l0xx.c>",
            "+<McuApi/STM32/startup_stm32l072xx.S>",
            "+<McuApi/ClassSTM32L072.cpp>",
            "+<McuApi/STM32/Drivers/STM32L0xx_HAL_Driver/Src>",
            "-<McuApi/STM32/Drivers/STM32L0xx_HAL_Driver/Src/stm32l0xx_hal_msp_template.c>",
        ],
    )
else:
    env.Append(
        CPPPATH=[
            os.path.join(
                "$PROJECT_SRC_DIR",
                "McuApi",
                "STM32",
                "Drivers",
                "STM32L4xx_HAL_Driver",
                "Inc",
            ),
            os.path.join(
                "$PROJECT_SRC_DIR",
                "McuApi",
                "STM32",
                "Drivers",
                "STM32L4xx_HAL_Driver",
                "Inc",
                "Legacy",
            ),
            os.path.join(
                "$PROJECT_SRC_DIR",
                "McuApi",
                "STM32",
                "Drivers",
                "CMSIS",
                "Device",
                "ST",
                "STM32L4xx",
                "Include",
            ),
        ],
        SRC_FILTER=[
            "+<McuApi/ClassSTM32L4.cpp>",
            "+<McuApi/STM32/SrcStm32/stm32l4xx_it.cpp>",
            "+<McuApi/STM32/SrcStm32/stm32l4xx_hal_msp.cpp>",
            "+<McuApi/STM32/SrcStm32/system_stm32l4xx.c>",
            "+<McuApi/STM32/Drivers/STM32L4xx_HAL_Driver/Src/*.c>"
            "+<McuApi/STM32/startup_stm32l476xx.S>"
        ],
    )

# Change ASM file extension to uppercase
mcu_api_dir = os.path.join(env.subst("$PROJECT_SRC_DIR"), "McuApi", "STM32")
for item in os.listdir(mcu_api_dir):
    filepath = os.path.join(mcu_api_dir, item)
    if os.path.isfile(filepath) and item.endswith(".s"):
        print("Changing file extension for assembly files...")
        os.rename(filepath, filepath[:-2] + ".S")
