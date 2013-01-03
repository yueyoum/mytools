# 我的工具

这里是一些我平时会用的工具脚本。


# autowindow.sh

Linux用户使用最多的还是Terminal，经常要缩放Terminal 
我的老笔电上安装的是xubuntu，为了漂亮，加了一个窄边框的主题 
所以用鼠标缩放窗口的时候，常常指针无法放到窗口边框上 
不得不用**Alt+F8**来缩放

更多的需求则是把Terminal缩放到较大的尺寸，并且放置在屏幕中间 
所以就有了这个脚本 
在Terminal中运行，便会自动将当前Terminal缩放置中

*这个脚本是支持所有窗口的*


## TODO

这只是一个心血来潮的仓促制作，现阶段满足了我的需求 
下列为即将要加入/更新的内容：

1. 检测显示器分辨率使用 wmctrl -d。 这样才能获得真正**可用**的分辨率. *去掉panel和dock后的*
2. 完善命令行参数。
3. 去掉硬编码的数字



# shadow.py

恩，为了漂亮的截图，给图片加类似 mac 截图阴影的。

效果就像这样：

原图：

![original](http://i1297.photobucket.com/albums/ag23/yueyoum/mytools_show_zps28afb2da.png)

处理后：

![shaowed](http://i1297.photobucket.com/albums/ag23/yueyoum/mytools_show_shadowed_zps01fc1394.png)



# fdownload.py

一些bt网站很蛋疼的是，只提供 flashget 的下载链接。

这个脚本就是从 flashget链接 获得torrent种子的。


# downh.py

一些网站，(H，你懂得)， 套图都是连续编号号的。

统统下载之！
