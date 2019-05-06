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

13.  

14.  

15.  

16. 

1. 