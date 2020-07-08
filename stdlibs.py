Import("env")

env.Append(
    LINKFLAGS=["--specs=nano.specs"]
)

# For some reason nano specs requires to include -lc twice
env.Replace(
    LIBS=["stdc++", "supc++", "m", "c", "nosys", "c"]
)
