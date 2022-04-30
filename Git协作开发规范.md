## Git 协作开发规范

### 1 下载克隆工程到本地

> git账号密码：xingpengcheng/12345678

```
*** 克隆到本地
git clone http://192.9.100.193/ctsi/csdp.git 
```


### 2 跟踪远程分支dev

```
*** 即同步该分支内容到本地
git checkout --track origin/branch_name
```

### 3 创建自己的分支，并检出到本地，将项目push到新建的分支上，后期再进行merge：

```
### 创建自己的分支（新建分支）
git branch 分支名

### 检出分支到本地（切换分支）
git checkout 分支名

### 检出部分代码到本地
git checkout easyservice/src/main/xxx/xxx.xml

### 查看所有分支
git branch -a

### 进行项目上传
git add .
git commit -m "提交的信息注释
git remote add origin 远程仓库地址
git push -u origin 分支名

### 删除本地分支
git branch -d 分支名

### 强制删除
git branch -D 分支名 

### 删除远程分支
git push origin --delete 分支名
```

### 4 添加已经修改的文件到缓存区：

``` 
*** 假设已经修改的文件为xxx1，xxx2
git add xxx1
git add xxx2

*** 添加全部到缓存区（无法释放）
git add .

*** 查看提交状态
git status
```

### 5 提交修改到自己的分支上：

```
git commit -m "添加了文件xxx1，xxx2，必须输入注释"
```


### 6 推送自己的分支到远程服务器上：

> 添加远程库chatApp.git

```
git remote add origin
git@github.com:Wbiokr/chatApp.git
```

> 第一次推送本地仓库到远程仓库

```
git push -u origin branch_name
***上述命令等同于
git push --set-upstream origin -branch_name
```

> 第二次以后的推送命令

```
git push origin branch_name
```

### 7 定期同步更新合并分支的内容

> 拉取远程分支branch_name分支内容到本地

```
git fetch origin branch_name
```

> 合并分支（合并指定分支到当前分支）

```
git merge origin/branch_name
```

> 推送分支到远程服务器上

```
git push origin branch_name
```

### 8 提取／合并某分支的部分文件
>软件开发基本都是多个feature分支并行开发，而在上线前有可能某个分支的开发或测试还没有完成，又或者是产品调整，取消了该分支功能的上线计划，我们在release前不合并该分支即可，然而如果该分支中的某些小调整却需要上线，我们就需要把其中的部分文件合并到release分支。
在feature分支commit，切换至release当前分支，从feature分支检出相应文件：

>在feature分支，将代码提交，并切换至release分支


```
git commit -a -m "msg"
git checkout release
```

>branch release 在release分支，checkout feature分支的 file-x文件。

```
git checkout feature file-01
git checkout feature file-x
...
```

### 9 检查代码，并提交。

```
git status
git commit -a -m "msg"
```

## Git log 篇

> 查看日志：

```
*** 显示每一次提交的信息：作者、日期、hash、commit信息 
git log 

*** 单行显示提交信息：hash、commit信息
git log --pretty=oneline 

*** 提交信息：hash、commit信息
git reflog 
```



> 查看远程和本地所有分支：

```
git branch -a
```

## Git reset 命令

```
*** 仓库文件回退到上一commit版本
git reset --hard HEAD^ 

*** 版本回滚到hash值35f69c开头的commit版本
git reset --hard 35f69c 

*** 把暂存区中a.txt的修改撤销掉，放回工作区
git reset HEAD a.txt 
```


## Git config 命令

> 同一客户端多账号切换

```
*** 切换到工程目录下，执行如下命令：
git config user.name "pengcheng.xing"
git config user.email "pengcheng.xing@krjx.com"
```



## Git pull 命令

```
*** 从远程分支获取最新版本并merge到本地
git pull origin branch_name

*** 从远程分支获取最新版本但不会merge
git fetch origin branch_name
```


>在使用git的过程中，有些时候我们只想要git服务器中的最新版本的项目， 对于本地的项目中修改不做任何理会，就需要用到Git pull的强制覆盖，具体代码如下：

```
[root@ip-100-00-00-21 ~]# git fetch --all  
[root@ip-100-00-00-21 ~]# git reset --hard origin/master 
[root@ip-100-00-00-21 ~]# git pull
```


> Git pull的强制覆盖本地文件在自动化部署项目中很有作用， 比如用SaltStack部署web项目，强制覆盖可以保持与服务器内容一致。

> Git diff 查看差异

```
*** 查看尚未暂存的文件更新了哪些部分
git diff 

*** 查看尚未暂存的某个文件更新了哪些
git diff filename 	

*** 查看已经暂存起来的文件和上次提交的版本之间的差异
git diff –cached 

*** 查看已经暂存起来的某个文件和上次提交的版本之间的差异
git diff –cached filename	

*** 查看某两个版本之间的差异
git diff ffd98b291e0caa6c33575c1ef465eae661ce40c9 b8e7b00c02b95b320f14b625663fdecf2d63e74c 	

*** 查看某两个版本的某个文件之间的差异
git diff ffd98b291e0caa6c33575c1ef465eae661ce40c9:filename b8e7b00c02b95b320f14b625663fdecf2d63e74c:filename 
```

> 生成diff文件的方法，输入如下命令：

```
git diff commit-id-1 commit-id-2 > 20171127.feature-11.diff
或
git diff HEAD^^ > 20171127.feature-11.diff

```


## git stash命令

> 当你想要保存当前的暂存区和工作区的状态的时候，你可以使用git stash命令。 比如：你正在开发一个新功能，写了一些代码（保存暂存的和没有暂存的或没有记录的）， 现在需要去修复一个紧急bug，你又不想提交，这时你可以选择保存当前工作区和暂存区的内容，需要的时候恢复。
这个命令会保存当前的暂存区和工作区的状态，然后返回到HEAD（git reset —hard HEAD）。最新的stach可以在.git/refs/stash中看到。

```
git stash save

save [-p|—patch] [-k|--[no-]keep-index] [-u|--include-untracked] [-a|—all] [-q|—quiet] [message]

[ ]代表这个参数是可选的
```

> -k|--keep-index 表示 stash之后，所有对暂存区的改变会维持不变（比如你之前add 了一个file，提交之后，git status还是能够在暂存区看到你的 add）,
如果是—no-keep-index的话，stash之后的状态就是git reset —hard HEAD。

> -p|—patch 不太了解，只知道用了会开启一个交互式的界面让你选择

> -u|--include-untracked 会把没有记录到的文件也保存下来(比如你新建了一个文件，
但是还没有git add，stash也会把这个文件保存下来)

> -a|—all 会把忽略的文件也保存下来（.gitignore中的）

> -q|—quiet 终端不打印输出

> message 一个对这个stash的描述，如果执行git stash list,我们能够看到这个描述

```
git stash list
list [options]
```

> 不加options，会列出所有的stash，你也可以指定某个stash(stash@{0}代表最近的stash)

```
*** 显示和他parent的差异
git stash show [stash]
```

```
git stash pop
pop [—index] [-q|—quiet] [stash]
```

> 与git stash save执行相反的操作，从stash list中移除这个stash，恢复工作区

> —index 如果指定了这个参数，那么不仅恢复工作区，也会恢复暂存区

```
git stash apply
apply [—index] [-q|—quiet] [stash]
```

> 和pop类似，区别在于apply不会吧stash从stash list中移除

```
git stash branch
branch [branchname] [stash]
```

> 以这个stash被创建的那个commit为起点，创建一个叫branchname的分支，然后再在这个分支执行

```
git stash pop —index stash
```

> 清空当前所有的stash

```
git stash clear
```

```
git stash create
创建一个stash，并返回他的commit对象，但并不在refs中存储这个对象
```

```
git stash store
存储通过create创建的stash。(可以在refs的stash和log/refs下看到这个stash)
```


## git reset 和 git revert区别revert区别

>reset是重置，默认是git reset –mixed 可以让版本库重置到某个commit状态，该commit之后的commit不会保留，并重置暂存区，但是不改变工作区。即这个时候，上次提交的内容在工作区中还会存在。 如果使用git reset –hard 将版本库，暂存区和工作区的内容全部重置为某个commit的状态。之前的commit不会保留。

>revert比reset更加温柔一点，回滚到某次commit且该commit之后的提交记录都会保留，并且会在此基础上新建一个提交。对于已经push到服务器上的内容作回滚，推荐使用revert。


## git修改远程仓库地址

>问：Coding远程仓库地址变了，本地git仓库地址如何更新为最新地址

```
*** 先查看远程仓库地址：
git remote -v

方法有三种：
1.修改命令(git remote set-url传递两个参数)
git remote set-url origin [url]
例如：
git remote  set-url origin http://10.248.17.4:8090/krjx/rebot.git
git remote  set-url origin http://222.128.117.230:8090/krjx/credat_jasr.git 
 
2.先删后加
git remote rm origin
git remote add origin [url]

3.直接修改config文件

```


