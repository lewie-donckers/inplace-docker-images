FROM ubuntu:26.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        cmake \
        libgmock-dev \
        ninja-build \
        python3 \
        python3-colorama \
        software-properties-common \
 && rm -rf /var/lib/apt/lists/*        

COPY ./llvm-snapshot.gpg.key /etc/apt/trusted.gpg.d/apt.llvm.org.asc
RUN add-apt-repository "deb https://apt.llvm.org/resolute/ llvm-toolchain-resolute-23 main"

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        clang-23 \
        clang-tidy-23 \
        clang-format-23 \
        libclang-rt-23-dev \
 && rm -rf /var/lib/apt/lists/*        
