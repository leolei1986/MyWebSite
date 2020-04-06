Title: Git常用命令
Date: 2020-04-06
Modified: 2020-04-06
Category: 工具
Tags: Git，工具
Author: 雷舰
Status: published

**1.获取远程库并创建本地索引名**

git clone -o 远程仓库的本地名 远程仓库
git clone 远程仓库 远程仓库的本地名

**2.管理远程库的本地名称**

git remote -v
git remote show 远程库的本地名
git remote add 远程库的本地名 远程库
git remote rm 远程库的本地名
git remote rename 原名 新名

**3.将远程分支的更新拉到本地分支**

git pull = git fetch + git merge/rebase
git fetch 远程仓库本地名 远程分支名

**4.将本地的分支推到远程分支**

git push 远程仓库本地名 本地分支名：远程分支名

**5.分支管理**

git branch -a //查看本地和远程的分支
git branch -d 本地分支名
git branch -b 新创建的分支名 远程或本地分支
git branch --set-upstream master origin/next
git checkout //切换分支

**6.撤销未提交的修改**

git checkout .
git checkout filename

**7.撤销已提交的修改**

git reset --hard [commit-hashcode] //[commit-hashcode]是某个 commit 的哈希值，可以用 git log 查看

**8.移动到某个历史版本**

git checkout [commit-hashcode] //[commit-hashcode]是某个 commit 的哈希值，可以用 git log 查看