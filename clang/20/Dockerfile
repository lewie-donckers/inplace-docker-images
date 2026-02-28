FROM ubuntu:25.10

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        clang-20 \
        clang-tidy-20 \
        clang-format-20 \
        cmake \
        libclang-rt-20-dev \
        libgmock-dev \
        libstdc++-15-dev \
        ninja-build \
        python3 \
        python3-colorama \
 && rm -rf /var/lib/apt/lists/*        
