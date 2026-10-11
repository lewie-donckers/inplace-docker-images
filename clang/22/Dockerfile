FROM ubuntu:26.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        clang-22 \
        clang-tidy-22 \
        clang-format-22 \
        cmake \
        libclang-rt-22-dev \
        libgmock-dev \
        ninja-build \
        python3 \
        python3-colorama \
 && rm -rf /var/lib/apt/lists/*        
