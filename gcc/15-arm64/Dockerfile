FROM ubuntu:25.10

ADD ubuntu.* /etc/apt/sources.list.d/
RUN dpkg --add-architecture arm64

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        cmake \
        g++-15-aarch64-linux-gnu \
        ninja-build \
        python3 \
        python3-colorama \
        qemu-user \
        \
        libc6:arm64 \
        libstdc++6:arm64 \
        libgmock-dev:arm64 \
 && rm -rf /var/lib/apt/lists/*        
