FROM ubuntu:25.10

ADD ubuntu.* /etc/apt/sources.list.d/
RUN dpkg --add-architecture armhf

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        cmake \
        g++-15-arm-linux-gnueabihf \
        ninja-build \
        python3 \
        python3-colorama \
        qemu-user \
        \
        libc6:armhf \
        libstdc++6:armhf \
        libgmock-dev:armhf \
 && rm -rf /var/lib/apt/lists/*        
