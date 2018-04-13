# Bash commands

#### 1. 显示日期时间

* ```bash
  date -u # 显示，查看当前系统时间，-u 显示格林尼治时间
  date +%Y--%m--%d # 格式化时间显示
  ```

* ```bash
  hwclock # show the hardware time
  sudo hwclock # use root host to show the hardware time
  ```

* ```bash
  cal # show the current calender
  ```

#### 2. 输出、查看命令

* ```bash
  echo # 显示输入的内容
  echo "everything"
  echo everything
  ```

* ```bash
  # 显示文件内容的命令
  cat filename # 显示文件所有内容，需要自己滑动
  more filename # 用于翻页显示文件内容（只能向下翻页）
  less filename # 用于翻页显示文件内容（上下翻页皆可），q 直接退出，			      # 不在命令行中保存文件内容
  head -n number filename # 显示文件头n行（默认10行）
  tail -n number filename # 显示文件尾n行（默认10行）
  tail -f # 动态追踪显示文件更新的内容，（用于查看日志，命令不会退出，
  		# 会持续显示输入的内容
  ```

* ```bash
  # 查看硬件信息
  lspci -v # 显示PCI设备，-v 显示详细信息
  lsusb -v # 显示USB设备，-v 显示详细信息
  lsmod # 显示加载的模块
  ```

#### 关机、重启命令

* ```bash
  # 关机、重启命令
  shutdown -h now # 立即关机
  shutdown -h +10 # 10分钟后关机
  shutdown -h 23:20 # 定点关机
  shutdown -r now # 立即重启（其他命令类似）

  poweroff # 立即关机
  reboot # 立即重启
  ```

#### 归档、压缩

```bash
# zip压缩文件
zip zipfile.zip myfile
# unzip 解压缩
unzip zipfile.zip
# gzip 压缩文件
gzip gzipfile.net
# tar 用以归档文件（就是打包文件, 并不压缩）
tar -cvf filename.tar myfile
tar -xvf filename.tar # 打开一个归档的文件包
tar -cvzf filename.tar.gz /etc
# -z 参数将归档后的.tar文件调用gzip进行压缩，形成.tar.gz
```

#### 查找命令

```bash
# locate 快速查找文件、文件夹
locate keyword # 此命令需要预先建立数据库，数据库默认每天更新一次
updatedb       # 用于手工建立、更新数据库
# find 命令用以高级查找文件、文件夹
find 查找位置 查找参数
find . -name *linuxcast* # .当前文件夹下，搜包含linuxcast的文件
find / -name *.conf # 在根分区下查找
find / -perm 777
find / -type d
find . -name "a*" -exec ls -l {} \; # 查找完文件后，进行ls -l的操作，操									 # 作命令可以改，但其他的为固定格式
-name # 搜索文件名
-perm # 搜索权限为。。。的文件
-user # 搜索某个用户的文件
-group
-ctime # 搜索某个时间段建立的文件
-type # 搜索某个类型的文件
-size # 以文件大小为条件，搜索文件
```

#### 显示文件的命令ls

```bash
ls -a # 显示所有文件，包括隐藏文件
ls -l # 显示详细信息
ls -R # 递归显示文件夹的信息，包括文件夹下的内容
ls -ld # 显示指定文件夹的详细信息
```

#### file 命令来查看文件夹或文件的信息

```bash
file filename/directory
```

