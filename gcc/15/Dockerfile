FROM ubuntu:25.10

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        cmake \
        g++-15 \
        libgmock-dev \
        ninja-build \
        python3 \
        python3-colorama \
 && rm -rf /var/lib/apt/lists/*        
