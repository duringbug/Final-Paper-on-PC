# 使用官方 Ubuntu 镜像作为基础镜像
FROM ubuntu:20.04

# 设置时区为中国时区（根据需要调整）
ENV TZ=Asia/Shanghai

# 设置非交互模式，避免交互式配置
ENV DEBIAN_FRONTEND=noninteractive

# 更新并安装必要的软件包
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    curl \
    unzip \
    git \
    wget \
    net-tools \
    tzdata \
    bash

# 配置时区
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata

# 安装 Android SDK
RUN mkdir -p /usr/local/android-sdk && cd /usr/local/android-sdk && \
    wget https://dl.google.com/android/repository/commandlinetools-linux-7302050_latest.zip && \
    unzip commandlinetools-linux-7302050_latest.zip && \
    rm commandlinetools-linux-7302050_latest.zip

# 设置 Android SDK 环境变量
ENV ANDROID_HOME=/usr/local/android-sdk
ENV PATH=$ANDROID_HOME/cmdline-tools/bin:$PATH

# 安装 Android SDK 组件
RUN yes | sdkmanager --licenses --sdk_root=$ANDROID_HOME
RUN sdkmanager "platform-tools" "platforms;android-30" "build-tools;30.0.3" "tools" --sdk_root=$ANDROID_HOME

# 设置工作目录
WORKDIR /workspace

# 默认启动命令
CMD ["/bin/bash"]
