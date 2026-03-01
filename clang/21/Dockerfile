FROM ubuntu:25.10

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        clang-21 \
        clang-tidy-21 \
        clang-format-21 \
        cmake \
        libclang-rt-21-dev \
        libgmock-dev \
        ninja-build \
        python3 \
        python3-colorama \
 && rm -rf /var/lib/apt/lists/*        
