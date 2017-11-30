# Linux 
## Add PATH variable
```bash
# example for add Moeditor PATH
# add PATH for all usrs
sudo vim /etc/profile
export PATH="/home/jarvis/usr/moeditor:$PATH"
# add PATH for your usr
sudo vim ~/.bashrc
export PATH="/home/jarvis/usr/moeditor:$PATH"
# update
source /etc/profile
source ~/.bashrc
```
## Turn on the IPV6
> Get the IPV6-hosts from LAOD websites

1. firefox and chrome can't open [六维空间](http://bt.neu6.edu.cn/forum.php) , [Google](http://ipv6.google.com.hk/?gws_rd=cr), [Youtube](https://www.youtube.com/), [Google Scholar](https://scholar.google.com/schhp?hl=en&as_sdt=0,5)
2. Then suddenly I can open the [洛樱](https://pt.whu.edu.cn/index.php)
3. Then the [六维空间](http://bt.neu6.edu.cn/forum.php) , [Google](http://ipv6.google.com.hk/?gws_rd=cr), [Youtube](https://www.youtube.com/), [Google Scholar](https://scholar.google.com/schhp?hl=en&as_sdt=0,5) are available

## Change the Pycharm path without uninstall it
1. find the pycharm path file in `/usr/local/bin/charm.py`
2. then modify the PATH to fit your real path
```python
# see com.intellij.idea.SocketLock for the server side of this interface
RUN_PATH = u'/home/jarvis/usr/pycharm-2017.2.4/bin/pycharm.sh'
CONFIG_PATH = u'/home/jarvis/.PyCharm2017.2/config'
SYSTEM_PATH = u'/home/jarvis/.PyCharm2017.2/system'
```

## Install the "deb" program
we can learn from the [CSDN blog](http://blog.csdn.net/kevinhg/article/details/5934462)
```bash
dpkg -i <package.deb>
# 1.安装一个 Debian 软件包，如你手动下载的文件。
dpkg -c <package.deb>
# 2.列出 <package.deb> 的内容。
dpkg -I <package.deb>
# 3.从 <package.deb> 中提取包裹信息。
dpkg -r <package>
# 4.移除一个已安装的包裹。
dpkg -P <package>
# 5.完全清除一个已安装的包裹。和 remove 不同的是，remove 只是删掉数据和可执行文件，purge 另外还删除所有的配制文件。
dpkg -L <package>
# 6.列出 <package> 安装的所有文件清单。同时请看 dpkg -c 来检查一个 .deb 文件的内容。
dpkg -s <package>
# 7.显示已安装包裹的信息。同时请看 apt-cache 显示 Debian 存档中的包裹信息，以及 dpkg -I 来显示从一个 .deb 文件中提取的包裹信息。
dpkg-reconfigure <package>
# 8.重新配制一个已经安装的包裹，如果它使用的是 debconf (debconf 为包裹安装提供了一个统一的配制界面)。
```

## The VIM using tips
```vim
:sh "暂时退出VIM，按<CTRL+d>回来
```

## Configure The powerful VIM editor
 1. Install the K-VIM from the [github](https://github.com/wklken/k-vim), and the Chinese Configure steps from [explanation](https://github.com/wklken/k-vim)
 2. The colorscheme is `solarized dark`
 3. Autoinstall the plugins e.g. `YouCompleteMe`,etc
 
## Configure the Terminal
1. change the default shell from `bash` to `zsh`,and install the `oh-my-zsh`, and custom the **plugins** and **themes** in the the `~/.zshrc` file
```bash
sudo apt-get install zsh
sudo apt-get install zsh -y #install zsh
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
#将默认的shell切换成zsh
chsh -s /bin/zsh 
# 新建一个.zshrc配置文件，和.bashrc作比较
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```

2. Then install the `tmux` to realize **splitting** the terminal to multiple tasks, configuration is in the file `~/.tmux.conf`. Then I find these in the [website](http://www.jianshu.com/p/0d4334cdeeeb)
```bash
# 只用了下面一句代码安装了tmux，从网上找的.tmux.conf
sudo apt-get install tmux -y
mkdir -p ~/.tmux
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```