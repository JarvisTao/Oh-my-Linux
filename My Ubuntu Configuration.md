# My Ubuntu Configuration

1. Install `Ubuntu 16.04.6`

   Refer to [www.baidu.com](www.baidu.com)

   test

   | 挂载点 |  格式  | 大小  | 分区类型 |
   | :----: | :----: | :---: | :------: |
   | /boot  |  ext4  | 305Mb | logistic |
   |   /    |  ext4  | 100Gb |   main   |
   |  swap  | 不用选 | 50Gb  |   main   |
   | /home  |  ext4  | 350Gb |   main   |

   boot at the ***The whole disk, not `/boot`***

2. Install `Chrome`

   ```bash
   sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
   wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
   sudo apt-get update
   sudo apt-get install google-chrome-stable
   google-chrome-stable
   ```

   Then download the `Google-access-helper` extension and add it to `Chrome`

3. Install `zsh + oh my zsh`

   ```bash
   sudo apt install zsh  # 安装 zsh
   sudo apt install git  # 安装 Git 工具
   chsh -s $(which zsh)  # change the default terminal to zsh
   # 下载 GitHub 上的 oh-my-zsh 脚本
   wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
   sudo sh install.sh  # 安装脚本
   sudo gedit /etc/passwd  # 修改最后一行，将 sh 改为 zsh
   ```

4. Configure `oh-my-zsh`

   refer to the [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh) and [zsh configure website](https://blog.e9china.net/lesson/yixieshiyongchangyongchajiantuijianforzshoh-my-zsh.html)

   ```bash
   # change the default theme to **agnoster**, install **font-powerline**
   sudo apt install fonts-powerline
   git clone https://github.com/powerline/fonts.git
   cd fonts
   ./install.sh
   Then choose the fonts `Ubuntu Mono derivative Powerline`
   # zsh-syntax-highlighting
   git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
   # zsh-autosuggestions
   git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
   zsh plugins = (git z zsh-highlighting zsh-autosuggestions)
   ```

5. Install `Typora`

   Error: 	

   `A JavaScript error occurred in the main process
   Uncaught Exception:
   Error: EACCES: permission denied, open '/home/jarvis2019/.config/Typora/typora.log'`

   Solution: 

   `sudo chown -R $USER:$GROUP ~/.config`

   `sudo chown -R $USER:$GROUP ~/docu`

   ```bash
   # or run:
   # sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
   wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
   # add Typora's repository
   sudo add-apt-repository 'deb https://typora.io/linux ./'
   sudo apt-get update
   # install typora
   sudo apt-get install typora
   ```

6. Install `vim` to support `python`

   (1) Error and solutions

   ```bash
   # error1: You need to install a terminal library; for example ncurses.
   # solution: 
   sudo apt-get install libncurses5-dev
   # error2: python2 and python3 fatal error: Python.h: 没有那个文件或目录的解决方法
   # solution:
   sudo apt-get install python-dev # Python-dev，这是Python2的头文件和静态库包
   sudo apt-get install python3-dev # Python3-dev，这是Python3的头文件和静态库包
   # error3: vim not found, sudo vim command not found
   # solution: add your vim bin path to your self(~/.zshrc) and root profile(/etc/sudoers)
   sudo vi ~/.zshrc
   add $PATH /usr/local/vim/bin
   sudo vi /etc/sudoers 
   add "/usr/local/vim/bin" to Defaults secure_path=”/bin:/usr/bin:/usr/local/bin:…”
   # error4: don't support clipboard
   # solution：recompile the vim and add configuration --enable-gui==auto --with-x
   ```

   (2) Steps for compile `vim+python+gui+clipboard`

   ```bash
   # install the dependences
   sudo apt-get install liblua5.1-dev luajit libluajit-5.1 python-dev ruby-dev libperl-dev libncurses5-dev libatk1.0-dev libx11-dev libxpm-dev libxt-dev
   # compile vim from sources
   git clone https://github.com/vim/vim.git
   cd vim/src
   make clean
   ./configure --with-features=huge --enable-python3interp --enable-pythoninterp --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu/ --enable-rubyinterp --enable-luainterp --enable-perlinterp --with-python3-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/  --enable-multibyte --enable-cscope   --enable-gui=auto --with-x   --prefix=/usr/local/vim/
   sudo make install
   ```

   Comments: 

   > --with-features=huge：支持最大特性
   >  --enable-rubyinterp：打开对ruby编写的插件的支持
   >  --enable-pythoninterp：打开对python编写的插件的支持
   >  --enable-python3interp：打开对python3编写的插件的支持
   >  --enable-luainterp：打开对lua编写的插件的支持
   >  --enable-perlinterp：打开对perl编写的插件的支持
   >  --enable-multibyte：打开多字节支持，可以在Vim中输入中文
   >  --enable-cscope：打开对cscope的支持
   >  --with-python-config-dir=/usr/lib/python2.7/config-x86_64-linux-gnu/ 指定python 路径
   >  --with-python-config-dir=/usr/lib/python3.5/config-3.5m-x86_64-linux-gnu/ 指定python3路径
   >  --prefix=/usr/local/vim：指定将要安装到的路径(自行创建)

   (3) Configure your own `vim` for your working

   > wait to be done

7. Install `NVIDIA GPU driver`，`cuda8.0`，`cudnn`

   refer to [ubuntu16.04下安装CUDA，cuDNN及tensorflow-gpu版本过程](https://blog.csdn.net/u014595019/article/details/53732015)

   (1) NVIDIA GPU driver: install it from ubuntu software center

   (2) cuda8.0

   * error:

     `Installing the CUDA Toolkit in /usr/local/cuda-8.0 ...
     Missing recommended library: libGLU.so
     Missing recommended library: libX11.so
     Missing recommended library: libXi.so
     Missing recommended library: libXmu.so` 

   * solution:

     `sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev `

   * Install `cuda8.0`

     ```bash
     sudo ./cuda_8.0.61_375.26_linux.run --tmpdir=/tmp
     ```

     > Do you accept the previously read EULA?
     > accept/decline/quit: accept
     >
     > Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 367.48?
     > (y)es/(n)o/(q)uit: n
     >
     > Install the CUDA 8.0 Toolkit?
     > (y)es/(n)o/(q)uit: y
     >
     > Enter Toolkit Location
     > [ default is /usr/local/cuda-8.0 ]:
     >
     > Do you want to install a symbolic link at /usr/local/cuda?
     > (y)es/(n)o/(q)uit: y
     >
     > Install the CUDA 8.0 Samples?
     > (y)es/(n)o/(q)uit: y

   (3) cudnn

   ```bash
   tar -xvf cudnn-8.0-linux-x64-v5.1.tgz
   sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
   sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/
   sudo chmod a+r /usr/local/cuda/include/cudnn.h
   sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
   ```

8. Install `tensorflow-gpu`

   * Install `tensorflow_gpu-1.4.0-cp36-cp36m-linux_x86_64.whl`
   * Then an error happened: `RuntimeWarning: compiletime version 3.5 of module 'tensorflow.python.framework.fast_tensor_util' does not match runtime version 3.6`
   * Solution: go to the website [https://github.com/lakshayg/tensorflow-build](https://github.com/lakshayg/tensorflow-build), download the specific version to support `FMA, AVX, AVX2, SSE4.1, SSE4.2`,  use `pip install --ignore-installed --upgrade /path/to/binary.whl --user`
   * Then after that, the `numpy=1.16` has installed from `pip`, but the `conda` doesn't have a latest version of `numpy`, it comes an error that the `numpy` has a uncompatiable version.
   * So, finally, reinstall the `numpy` from `conda installl numpy`

9. Install `pytorch-gpu, torchvision`

   1. add `tuna` mirror resource to `~/.condarc`
   2. `conda install pytorch torchvision cudatoolkit=8.0 -c pytorch` didn't work.
   3. download the `pytorch-nightly-1.0.0.dev20190104-py3.6_cuda8.0.61_cudnn7.1.2_0.tar.bz2` from `tuna mirror resources`, and add it  to the `~/anaconda3/pkgs/`,  install by conda, but it doesn't work.
   4. **Finally, ** I download the package `pytorch-1.0.0-py3.6_cuda8.0.61_cudnn7.1.2_1.tar.bz2` from [<https://anaconda.org/pytorch/pytorch/files>](https://anaconda.org/pytorch/pytorch/files), then install it by `conda install ~/anaconda3/pkgs/pytorch-1.0.0-py3.6_cuda8.0.61_cudnn7.1.2_1.tar.bz2`  **without error**
   5. **But**, when i `import torch`, it shows `ImportError: libmkl_gnu_thread.so: cannot open shared object file: No such file or `,  then I reinstall the `mkl` package. **I think the reason is an uncomplete process when i install numpy by `conda install numpy` ,  the download speed is  so slow**.
   6. ***And I have download the `torch-1.0.0-cp36-cp36m-linux_x86_64.whl`*** from [https://pytorch.org/get-started/previous-versions](https://pytorch.org/get-started/previous-versions/), once the above step can't work, i will install this package through pip, finally.

10. Install `Pycharm`

    1. Download the package from official website.
    2. Extract it, `cd bin & ./pycharm.sh`
    3. Add the `0.0.0.0 account.jetbrains.com 0.0.0.0 www.jetbrains.com` to `/etc/hosts`
    4. Download the activation file from [http://idea.lanyus.com](http://idea.lanyus.com/)
    5. Add the activated code getting from [http://idea.lanyus.com](http://idea.lanyus.com/)

11. Compile and install `opencv3.4.2 + contib`

    Refer to [<https://www.learnopencv.com/install-opencv3-on-ubuntu/>](https://www.learnopencv.com/install-opencv3-on-ubuntu/) 

12. Remount the `swap` to `SSD` in order to lift up the speed of `swap`(**The lack of physical memory!!!**)

    1. Refer to the [<https://www.jianshu.com/p/b8a4fef0ff58>](https://www.jianshu.com/p/b8a4fef0ff58) and [<https://my.oschina.net/tcstory/blog/466240>](https://my.oschina.net/tcstory/blog/466240)

13. **Repair** the **read-only** permission of your U flash disk

    ```bash
    df -h # find the disk location that your U flash disk mount
    #eg: /dev/sdc1
    # then, umount the flash disk driver
    sudo umount /media/user_name/disk_name
    # finally, repair the filesystem
    sudo dosfsck -v -a /dev/sdc1
    # echo log
    fsck.fat 3.0.28 (2015-05-16)
    Checking we can access the last sector of the filesystem
    There are differences between boot sector and its backup.
    This is mostly harmless. Differences: (offset:original/backup)
      52:da/00, 53:25/00, 54:18/00, 55:c1/00, 67:1e/47, 68:23/aa, 69:cd/fb
      , 70:a6/2f, 480:00/65, 481:00/73, 482:00/74, 483:00/61, 484:00/72, 485:00/74
      , 486:00/0d, 487:00/0a, 494:04/00
      Not automatically fixing this.
    Boot sector contents:
    System ID "MSDOS5.0"
    Media byte 0xf8 (hard disk)
           512 bytes per logical sector
          8192 bytes per cluster
            38 reserved sectors
    First FAT starts at byte 19456 (sector 38)
             2 FATs, 32 bit entries
       7795200 bytes per FAT (= 15225 sectors)
    Root directory start at cluster 2 (arbitrary size)
    Data area starts at byte 15609856 (sector 30488)
       1948675 data clusters (15963545600 bytes)
    63 sectors/track, 255 heads
          2232 hidden sectors
      31209288 sectors total
    Orphaned long file name part "monkaa_frames_cleanpass"
      Auto-deleting.
    Reclaiming unconnected clusters.
    Checking free cluster summary.
    Performing changes.
    /dev/sdc1: 1038 files, 68875/1948675 clusters
    ```




# My Ubuntu 18.04 Configuration on X299

1. Change the **User Name** of  System

   Refer to [https://blog.csdn.net/sailor201211/article/details/52305591](https://blog.csdn.net/sailor201211/article/details/52305591)

   (1) set your ***root*** passward 

   ```bash
   sudo passwd
   ```

   (2) log out your old user, then ***CTRL + ALT + F1***  open the terminal and login with **root** 

   (3) 2 command to finish changing your user name

   ```bash
   usermod -l New_Login_Name -md Home_Directory Old_Login_Name
   groupmod -n NewName OldName
   ```

2. make the speed of `git clone` more faster

   (0) Refer to [小技巧-如何加快github下载代码的速度](https://blog.csdn.net/mist99/article/details/80602090) 

   get the ip address of global.ssl.fastly from [http://github.global.ssl.fastly.net.ipaddress.com/#ipinfo](http://github.global.ssl.fastly.net.ipaddress.com/#ipinfo) 

   get the ip address of github.com from [http://github.com.ipaddress.com/#ipinfo](http://github.com.ipaddress.com/#ipinfo)

   add them to `/etc/hosts` and restart the network  `/etc/init.d/networking restart`

   

   (1) modify the ***/etc/hosts***

   Error: RPC failed; curl 18 transfer closed with outstanding read data remaining

   > 151.101.72.249 **github**.[http://global.ssl.fastly.net](https://link.zhihu.com/?target=http%3A//global.ssl.fastly.net)
   > 192.30.253.112 **github**.com

   (2) use the ***git:*** instead of ***https:***

   (3) make the buffer larger

   > git config --global http.postBuffer 524288000
   > git config --global http.lowSpeedLimit 0
   > git config --global http.lowSpeedTime 999999

   (4) Only fetch the latest version of code(repository)

   > git clone --depth 1 $clone_url

3. Fix the problem: `sudo vim: command not found`

   Refer to [https://blog.csdn.net/duguduchong/article/details/8804117](https://blog.csdn.net/duguduchong/article/details/8804117)

   Reason: 

   > 不知道有多少人遇到这种 加上 sudo 找不命令的情况，怎么办呢，谢天谢天我们有google，百度不知道的google一定知道。
   >
   > 很多人就可以病急乱投医了，一会在 /etc/profile修改修改，一会在/etc/environment修改，~/.bashrc 修改了好多地方还是不行。网上也有些人是瞎指挥，帮倒忙。出现这种情况就是因为对linux了解不深的原因。不过网上总是有热心的高人的。
   >
   > 其实出现这种情况的原因，主要是因为当 sudo以管理权限执行命令的时候，linux将PATH环境变量进行了重置，当然这主要是因为系统安全的考虑，以防用户执行可引起灾难性的程序。
   >
   > 这个配置信息存储在了/etc/sudoers这个文件是，当指行sudo命令的时候系统寻找的是 secure_path下的目录，所有在 /etc/profile ~/.bashrc下对PATH做的配置都会被忽略。所以就出现加上 sudo xxx 找不到命令的情况，解决办法用很多种了，可以将要执行sudo的命令软链接到 secure_path的目录下，或者修改 secure_path变量。
   >
   > 解决办法:关掉执行 sudo 时,执行管理员权限时, linux的重置操作,
   >
   > 1. 编辑/etc/sudoers文件，把Defaults env_reset改成Defaults ! env_reset
   >
   > 2. 编辑.bashrc,最后添加alias sudo='sudo env PATH=$PATH'
   >
   > 3. 还可以在/etc/sudoers文件里, 将 secure_path 中加上/usr/local/vim

4. Add **Pycharm** to Ubuntu docker

   Refer to [https://blog.csdn.net/yfy1127yfy/article/details/88431477](https://blog.csdn.net/yfy1127yfy/article/details/88431477)

   Add a *.desktop file to:

   > /usr/share/applications
   >
   > or
   >
   > ~/.local/share/applications

   The **pycharm.desktop** file:

   > [Desktop Entry]
   > Encoding=UTF-8
   > Version=1.0
   > Type=Application
   > Name=Welcome to PyCharm
   > Icon=/home/jarvis/download/pycharm-2019.1/bin/pycharm.png
   > Path=/home/jarvis/download/pycharm-2019.1/bin
   > Exec=/home/jarvis/download/pycharm-2019.1/jre64/bin/java -classpath /home/jarvis/download/pycharm-2019.1/lib/bootstrap.jar:/home/jarvis/download/pycharm-2019.1/lib/extensions.jar:/home/jarvis/download/pycharm-2019.1/lib/util.jar:/home/jarvis/download/pycharm-2019.1/lib/jdom.jar:/home/jarvis/download/pycharm-2019.1/lib/log4j.jar:/home/jarvis/download/pycharm-2019.1/lib/trove4j.jar:/home/jarvis/download/pycharm-2019.1/lib/jna.jar -Xms128m -Xmx750m -XX:ReservedCodeCacheSize=240m -XX:+UseConcMarkSweepGC -XX:SoftRefLRUPolicyMSPerMB=50 -ea -Dsun.io.useCanonCaches=false -Djava.net.preferIPv4Stack=true -Djdk.http.auth.tunneling.disabledSchemes="" -XX:+HeapDumpOnOutOfMemoryError -XX:-OmitStackTraceInFastThrow -Dawt.useSystemAAFontSettings=lcd -Dsun.java2d.renderer=sun.java2d.marlin.MarlinRenderingEngine -XX:ErrorFile=/home/jarvis2019/java_error_in_PYCHARM_%p.log -XX:HeapDumpPath=/home/jarvis2019/java_error_in_PYCHARM.hprof -Didea.paths.selector=PyCharm2019.1 -Djb.vmOptionsFile=/home/jarvis/download/pycharm-2019.1/bin/pycharm64.vmoptions -Didea.platform.prefix=Python com.intellij.idea.Main
   > StartupNotify=false
   > StartupWMClass=jetbrains-pycharm
   > OnlyShowIn=Unity;
   > X-UnityGenerated=true

5. Install `opencv-3.4.2 and opencv_contrib` on Ubuntu 18.04

   Refer to: 

   [https://www.learnopencv.com/install-opencv-3-4-4-on-ubuntu-18-04/](https://www.learnopencv.com/install-opencv-3-4-4-on-ubuntu-18-04/) , [https://www.learnopencv.com/install-opencv-3-4-4-on-ubuntu-16-04/](https://www.learnopencv.com/install-opencv-3-4-4-on-ubuntu-16-04/)[https://www.learnopencv.com/install-opencv3-on-ubuntu/](https://www.learnopencv.com/install-opencv3-on-ubuntu/) 

   The compile and install code is as following:

   (1) Install OS Libraries

   ```bash
   sudo apt -y update
   sudo apt -y upgrade
   
   sudo apt -y remove x264 libx264-dev
    
   ## Install dependencies
   sudo apt -y install build-essential checkinstall cmake pkg-config yasm
   sudo apt -y install git gfortran
   sudo apt -y install libjpeg8-dev libpng-dev
    
   sudo apt -y install software-properties-common
   sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
   sudo apt -y update
    
   sudo apt -y install libjasper1
   sudo apt -y install libtiff-dev
   sudo apt -y install libtiff5-dev
    
   sudo apt -y install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
   sudo apt -y install libxine2-dev libv4l-dev
   cd /usr/include/linux
   sudo ln -s -f ../libv4l1-videodev.h videodev.h
   cd -
    
   sudo apt -y install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
   sudo apt -y install libgtk2.0-dev libtbb-dev qt5-default
   sudo apt -y install libatlas-base-dev
   sudo apt -y install libfaac-dev libmp3lame-dev libtheora-dev
   sudo apt -y install libvorbis-dev libxvidcore-dev
   sudo apt -y install libopencore-amrnb-dev libopencore-amrwb-dev
   sudo apt -y install libavresample-dev
   sudo apt -y install x264 v4l-utils
    
   # Optional dependencies
   sudo apt -y install libprotobuf-dev protobuf-compiler
   sudo apt -y install libgoogle-glog-dev libgflags-dev
   sudo apt -y install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen
   ```

   (2) Compile and Install OpenCV with contrib modules

   Error: 

   > `makefile:162: recipe for target 'all' failed opencv`
   >
   >   `//usr/lib/libvtkIO.so.5.10：对‘TIFFNumberOfTiles@LIBTIFF_4.0’未定义的引用` 

   Resolution: add cmake configuration `-D BUILD_TIFF=ON`

   ```bash
   cmake -D CMAKE_BUILD_TYPE=RELEASE \
               -D CMAKE_INSTALL_PREFIX=/usr/local \
               -D INSTALL_C_EXAMPLES=ON \
               -D INSTALL_PYTHON_EXAMPLES=ON \
               -D WITH_TBB=ON \
               -D WITH_V4L=ON \
           -D WITH_QT=ON \
           -D WITH_OPENGL=ON \
           -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
           -D BUILD_EXAMPLES=ON -D BUILD_TIFF=ON..
   ```

   ```bash
   make -j10
   sudo make install
   ```

   

6. 