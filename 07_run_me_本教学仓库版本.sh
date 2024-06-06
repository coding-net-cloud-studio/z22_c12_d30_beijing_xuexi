#! /bin/bash

# NOTE 本教程是针对完全的初学者
# NOTE 本教程是针对"泛开发者"
# NOTE 泛开发者是指:在本职工作领域是专业人士,但不以编程作为谋生手段
# NOTE 本教程不适合初级程序员_初级程序员应该去看更深的教程了_不需要看本教程
	# NOTE 向已经是程序员的群体,深度推荐:白明,柴树杉,丁尔男,史斌,郝林,徐秋华,陈剑煜,刘丹冰,廖显东,郭宏志,湖南长沙老郭(Nick),王中阳,申专等老师与专家的专业课程
# NOTE 所有曾经编写过300行代码的人士_都不适合看本初级教程了_应该去看其他更深的教程了
# NOTE Makefile中是支持utf-8(unicode)作为目标名称的_我们这样写的目的是给"泛开发者"在初期容易理解实行的
# NOTE 在后继的课程中_我们将取消这些方法_回归到_英文目标名的传统方式
# NOTE 在bash shell script脚本中_针对_泛开发者_我们使用很长的函数名称这样的_非传统方式
# NOTE 在后继的课程中_我们将取消上述_长函数名的_非传统方式_回归常规写法

# NOTE 相当于_真的要停止60秒_给操作人员看看_log
# pause_60_second(){
# 	if read -t 60 -p "暂停60秒,按回车继续运行: "
# 	then
# 		# echo "hello $REPLY,welcome to cheng du"
# 		printf "\n";
# 	else
# 		# echo "sorry, Output timeout, please execute the command again !"
# 		printf "\n时间已到,继续运行\n";
# 	fi
# }

# NOTE 相当于_不做调试
pause_60_second(){
	echo "啥都不做"
	return 0
}

# ==============================================================

# 在cloudstudio环境中_更新_vscode的_用户_settings_文件
# 主要是设置cloud studio为"永不休眠"
f16_cs_vs_settings_user_update(){
	# cloud studio中用户设置文件
	CS_VSCODE_SETTINGS_USER=/root/.local/share/code-server/data/User/settings.json
	# -----------------------------------------------------------
	# '嵌入文档涵盖了生成脚本的主体部分.

	(
	cat <<'EOF'
{
	"cloudstudio.autosleep": "no",
	"extensions.autoCheckUpdates": false,
	"extensions.autoUpdate": false,
	"update.mode": "none",
	"update.showReleaseNotes": false,
	"code-runner.runInTerminal": true,
  "codingcopilot.enableAutoCompletions": true,
	"window.menuBarVisibility": "visible",
  "terminal.integrated.tabs.location": "left",
  "terminal.integrated.tabs.enabled": false
}
EOF
	) > ${CS_VSCODE_SETTINGS_USER}

	# 可能有用的设置_暂时被取消了
	# "Codegeex.Survey": false,
	# "CS.CodeAssistant.EnableExtension": false,
	# "go.toolsManagement.autoUpdate": true,

}


f20_linux_git_setting() {
	#在Linux操作系统环境下
	# git status中文显示乱码解决:
	# https://www.cnblogs.com/v5captain/p/14832597.html
	#相当于在~/.gitconfig 文件中加入一行 file:/root/.gitconfig   core.quotepath=false
	# core.quotepath=false
	git config --global user.email "自学自讲@网上自习室"
	git config --global user.name "自学自讲"

	git config --global core.quotepath false
	git config --global --add safe.directory $(pwd)

	# git config命令详解
	# http://www.mybatis.cn/archives/2151.html
	# git config --list --show-origin

	# 来自廖雪峰的git教程
	# https://www.liaoxuefeng.com/wiki/896043488029600/898732837407424
	git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

	git config --global alias.count "rev-list --all --count"

	# REVIEW 这里可能会有问题.立足解决,从本机上用tar.gz传输到cloud studio中直接解开.git用户信息的问题.
	# 相信,git clone模式,不会需要这个语句.
	git config --global --add safe.directory $(pwd)
}

# REVIEW 这个函数_是我自己加入的_安装一些函数
f23_install_some_software(){
	if [[ -f $(which cloudstudio) ]]; then
		apt update -y
		DEBIAN_FRONTEND=noninteractive apt install -y \
			iputils-ping \
			make \
			lsof \
      net-tools \
			psmisc \
			file \
			rsync \
			curl \
			direnv \
			sqlite3 \
      libsqlite3-dev \
      bats \
      jq \
      gron \
      pdfgrep \
      ripgrep \
      httpie \
      duff \
      mlocate

	fi

	return 0
}

# NOTE 从a22_vs_ext移植过来的
# NOTE 本函数被Makefile的make imgcat所调用
#类似imgcat等小工具位于.wmstudy/bin的目录下
f28_20_install_some_wmstudy_bin_tools(){
	# pause_60_second
	# 只有位于cloudstudio工作空间中才执行
	if [[ -f $(which cloudstudio) ]]; then
		# pause_60_second
		# 只有具有如下的目录才执行
		if [[ -d .wmstudy/bin/ ]]; then
			# pause_60_second
			chmod +x .wmstudy/bin/*
			# ls -lah .wmstudy/bin/
			cp -r -f .wmstudy/bin/* /usr/bin/
			# ls -lah /usr/bin/imgcat
			cp -r -f .wmstudy/bin/* /bin/
			# ls -alh /bin/imgcat

			# 尝试在jupyter notebook中使用
			if [[ -f $(which imgcat) ]]; then
				ln -s -f $(which imgcat) /usr/bin/看图      || echo "已经_建立_看图_软连接"
				ln -s -f $(which imgcat) /usr/bin/查看图片  || echo "已经_建立_查看图片_软连接"
			fi
		fi
	fi
}

# ==============================================================

# NOTE 本函数被f36_42_fy_lookup_english_dictionary_for_cloudstudio所调用
# 被调用的原因是_防止在_非腾云扣钉cloudstudio的环境_调用
# 怕误操作_污染自己的linux或ubuntu环境
# 安装fanyi_翻译_在cloudstudio的终端与命令行中_可以查找英文单词的中文解释_还有点_例句
f36_40_fanyi_helper(){

	# 需要增加阿里巴巴源_因为有几个小软件_腾讯源没有

	# touch /etc/apt/sources.list.d/ali.list

(
cat <<'EOF'
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
EOF
) > /etc/apt/sources.list.d/ali.list

	# 更新apt
	apt update

	# 安装辅助软件
	apt install -y festvox-don festvox-rablpc16k festvox-kallpc16k festvox-kdlpc16k

	# 安装fanyi
	npm install fanyi -g

	# 测试翻译
	fanyi word

	pause_60_second

	fy word
	fanyi love
	fanyi 和谐

	pause_60_second

	fanyi 子非鱼焉知鱼之乐

	# fanyi的命令_列出今天查找的单词
	pause_60_second

	fy list

	# 为了jupyter_notebok_中_更加直观的_创建了_ln_链接
	if [[ -f $(which fanyi) ]]; then
		ln -s $(which fanyi) /usr/bin/翻译 || echo "已经_建立_翻译_软连接"
		ln -s $(which fanyi) /usr/bin/查词 || echo "已经_建立_查词_软连接"
	fi

	return 0
}


# NOTE 这个函数才是被Makefile中调用的
# 本函数调用的是 f36_40_fanyi_helper
# NOTE 主要目的是 判断位于腾云扣钉cloudstudio的工作空间_才执行
# make fy
f36_42_fy_lookup_english_dictionary_for_cloudstudio(){

	echo "运行在_f36_42_fy_lookup_english_dictionary_for_cloudstudio_函数"

	echo -e "\n运行在 $(pwd)/${BASH_SOURCE[${#BASH_SOURCE[@]} - 1]} 脚本的 ${FUNCNAME} 函数中 ${LINENO} 行\n"

	# 判断是否是cloudstudio的环境
	[[ -f $(which cloudstudio) ]] && f36_40_fanyi_helper

	# 可以_在cloudstudio的编辑器中_获得翻译的结果
	if [[ -f $(which cloudstudio) ]] && [[ -f $(which fanyi) ]]; then
		(fanyi list | cloudstudio -) &
	fi

	return 0

}


# ==============================================================

# NOTE 把06_样例目录拷贝到/workspace/下面去
# NOTE 这个函数_在本git仓库的_设置_cloudstudio_工作空间中_没有被调用
# 保留一段时间_为了保持一致
l06_copy_06_example(){

	export v06_OLDPWD=$(pwd)

	if [[ ! -d /workspace/06_样例 ]]; then
		if [[ -d ./06_样例 ]]; then
			cp -r ./06_样例 /workspace/
		fi
	fi

	cd ${v06_OLDPWD}
	return 0
}


#  ==============================================================
# NOTE 本cloudstudio教学仓库下面_自带的_安装vscode扩展的_那个目录
# NOTE 本函数被f94_2828_30_main()函数所调用
l07_this_git_call_script_to_install_vscode_ext(){
	export v08_OLDPWD=$(pwd)

	if [[ -d ./03_vscode_extension ]]; then
		cd ./03_vscode_extension

		if [[ -f ./03_cloudstudio_install_vsix.sh ]]; then
			# NOTE 执行安装脚本
			./03_cloudstudio_install_vsix.sh
		fi
	fi

	cd ${v08_OLDPWD}
	return 0
}



# NOTE 调用安装grasspy的脚本
l08_call_script_to_install_vscode_ext(){
	export v08_OLDPWD=$(pwd)

	if [[ -d /root/.pyenv/03_vscode_extension ]]; then
		cd /root/.pyenv/03_vscode_extension

		if [[ -f /root/.pyenv/03_vscode_extension/03_cloudstudio_install_vsix.sh ]]; then
			# NOTE 执行安装脚本
			./03_cloudstudio_install_vsix.sh
		fi
	fi

	cd ${v08_OLDPWD}
	return 0
}

# ==============================================================

# NOTE 下面是老版本p27的_这里不再调用了
l10_install_me(){

	export v10_OLDPWD=$(pwd)

	if [[ -f $(which cloudstudio) ]]; then
		if [[ -d /root/.pyenv ]]; then
			if [[ ! -d /root/.pyenv/03_vscode_extension ]]; then
				# NOTE 此时,还是原始状态_可以进行替换
					# 老的目录修改名称
					echo "正在处置原始的/root/.pyenv目录,时间较长,请耐心等待一小会"

					# NOTE 为了化简逻辑判断_不再区分SaaS版本的cloudstudio.net
					# 还是社区版本的club.cloudstudio.net的工作空间
					# 直接做出凶残的动作_把/root/.pyenv/目录直接地,彻底地,给删除了
					# mv /root/.pyenv /root/38_wmold_pyenv_这里是原始版本的pyenv
					rm -rf /root/.pyenv
					echo "正在把新的pyenv版本拷贝到/root/.pyenv/目录下"
					# 拷贝新的版本的pyenv到/root/.pyenv的位置
					cp -r $(pwd) /root/.pyenv

					# NOTE 把06_样例目录拷贝到/workspace/下面去
					l06_copy_06_example

					# NOTE 调用安装grasspy等vscode扩展的脚本

					if [[ ! -f /root/.local/share/code-server/extensions/lock_08_安装_vscode_扩展_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt ]]; then
						# 到这里_没有发现特征_锁文件_也就是_没有安装过我们自己的vscode扩展
						# 这个步骤_主要是cloudstudio社区版只有1G的存储空间
						# 而在"复刻"工作空间的时候/root/.local/share/code-server/extensions/会占用很多的存储空间
						# 只有删除
						# 再安装我们自己的vscode扩展
						rm -rf /root/.local/share/code-server/extensions/
						mkdir -p /root/.local/share/code-server/extensions
						# 删除完毕_开始安装我们自己版本的
						l08_call_script_to_install_vscode_ext

						mkdir -p /root/.local/share/code-server/extensions/

						touch /root/.local/share/code-server/extensions/lock_08_安装_vscode_扩展_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt

						echo "新安装我们自己的vscode扩展组合_并且生成了_vscode_扩展_安装_锁文件"

						pause_60_second

						cloudstudio --list-extensions

						pause_60_second

						ls -lah /root/.local/share/code-server/extensions/

						pause_60_second

					else
						echo "/root/.local/share/code-server/extensions/_目录下_已经是我们自己的vscode扩展组合_不需要再次安装了"
						pause_60_second
					fi


					echo "已经把/root/.pyenv更新为新的草莽grasspy3.10.1的版本了"
					echo "欢迎加入 草蟒极速 QQ 交流群:760167264 风里雨里,我们在那里等你 "
					echo "编程语言开发社区网址: https://www.ploc.org.cn/ploc/ "
					echo "我作为一名普通的"编程语言开放社区成员_与_grasspy.cn社区成员",以个人的身份,向吴烜xuan三声,凹语言群体,林纳斯·本纳第克特·托瓦兹(Linus Benedict Torvalds)等致敬!"
			else
				echo "已经执行过/root/.pyenv的替换操作_不需要再次进行"
			fi
		else
			echo "没有找到/root/.pyenv,无法进行后继操作"
		fi
	fi

	cd ${v10_OLDPWD}

	if [[ -f $(which cloudstudio) ]]; then
		if [[ -d /workspace/06_样例 ]]; then
			# 在cloudstudio.net中再打开一个窗口
			cloudstudio -n /workspace/06_样例
		fi
	fi

	return 0
}


# ==============================================================
# NOTE 针对club.cloudstudio.net社区版本
# NOTE 从github.com上获得git仓库建立工作空间以后
# NOTE 需要从gitee上获取新的pyenv环境
l30_git_clone_and_install_new_pyenv(){

	export v10_OLDPWD=$(pwd)

	# NOTE 判断是否_有必要_执行本函数
	# 如果没有_必要_再次执行_就return_0
	if [[ -f $(which cloudstudio) ]]; then
		if [[ -f /workspace/lock_01_run_me_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt ]]; then
			# 标志性的锁文件已经存在了
			if [[ -d /root/.pyenv/03_vscode_extension ]]; then
				echo "没有必要再次执行_01_rum_me_的l30()函数"
				return 0
			fi
		fi
	fi



	if [[ -f $(which cloudstudio) ]]; then
		if [[ -d /root/.pyenv ]]; then
			if [[ ! -d /root/.pyenv/03_vscode_extension ]]; then

				# 如果发现_锁文件_把原有的那个文件删除
				# 后面会重新创建的
				[[ -f /workspace/lock_01_run_me_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt ]] && rm /workspace/lock_01_run_me_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt

				# NOTE 此时,还是原始状态_可以进行替换
					# 老的目录修改名称
					echo "正在处置原始的/root/.pyenv目录,时间较长,请耐心等待一小会"

					# NOTE 为了化简逻辑判断_不再区分SaaS版本的cloudstudio.net
					# 还是社区版本的club.cloudstudio.net的工作空间
					# 直接做出凶残的动作_把/root/.pyenv/目录直接地,彻底地,给删除了
					# mv /root/.pyenv /root/38_wmold_pyenv_这里是原始版本的pyenv

					[[ -d /root/.pyenv ]] && rm -rf /root/.pyenv

					echo "正在把新的pyenv版本_git_clone_到/root/.pyenv/目录下"
					# git_clone_新的版本的pyenv到/root/.pyenv的位置
					git clone --depth=1 https://gitee.com/coding_net_cloud_studio/ploc_grasspy_pyenv.git /root/.pyenv

					# NOTE 把06_样例目录拷贝到/workspace/下面去
					# l06_copy_06_example

					# NOTE 调用安装grasspy等vscode扩展的脚本

					if [[ ! -f /root/.local/share/code-server/extensions/lock_08_安装_vscode_扩展_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt ]]; then
						# 到这里_没有发现特征_锁文件_也就是_没有安装过我们自己的vscode扩展
						# 这个步骤_主要是cloudstudio社区版只有1G的存储空间
						# 而在"复刻"工作空间的时候/root/.local/share/code-server/extensions/会占用很多的存储空间
						# 只有删除
						# 再安装我们自己的vscode扩展
						rm -rf /root/.local/share/code-server/extensions/
						mkdir -p /root/.local/share/code-server/extensions
						# NOTE 必须手工建立一个如下的文件_才会正确的安装vscode的扩展
						echo "[]" > /root/.local/share/code-server/extensions/extensions.json

						ls -lah /root/.local/share/code-server/extensions/
						pause_60_second

						# 删除完毕_开始安装我们自己版本的
						l08_call_script_to_install_vscode_ext

						mkdir -p /root/.local/share/code-server/extensions/

						touch /root/.local/share/code-server/extensions/lock_08_安装_vscode_扩展_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt

						echo "新安装我们自己的vscode扩展组合_并且生成了_vscode_扩展_安装_锁文件"

						pause_60_second

						cloudstudio --list-extensions

						pause_60_second

						ls -lah /root/.local/share/code-server/extensions/

						pause_60_second

					else
						echo "/root/.local/share/code-server/extensions/_目录下_已经是我们自己的vscode扩展组合_不需要再次安装了"
						pause_60_second
					fi


					echo "已经把/root/.pyenv更新为新的草莽grasspy3.10.1的版本了"
					echo "欢迎加入 草蟒极速 QQ 交流群:760167264 风里雨里,我们在那里等你 "
					echo "编程语言开发社区网址: https://www.ploc.org.cn/ploc/ "
					echo "我作为一名普通的"编程语言开放社区成员_与_grasspy.cn社区成员",以个人的身份,向吴烜xuan三声,凹语言群体,林纳斯·本纳第克特·托瓦兹(Linus Benedict Torvalds)等致敬!"

					touch /workspace/lock_01_run_me_已经被执行过一次_锁文件_不需要再次执行_wmgitignore.txt
			else
				echo "已经执行过/root/.pyenv的替换操作_不需要再次进行"
			fi
		else
			echo "没有找到/root/.pyenv,无法进行后继操作"
		fi
	fi

	cd ${v10_OLDPWD}

	# NOTE 如下的都不要再进行了
	# if [[ -f $(which cloudstudio) ]]; then
	# 	if [[ -d /workspace/06_样例 ]]; then
	# 		# 在cloudstudio.net中再打开一个窗口
	# 		cloudstudio -n /workspace/06_样例
	# 	fi
	# fi

	return 0
}

# ==============================================================
# NOTE 通过git_subtree的形式把子git仓库加入进来_并新增一个cloudstudio的窗口
# NOTE 这个模式太复杂了_相互协调很麻烦_放弃了
l57_30_git_clong_c28_aig_meetup(){

	if [[ ! -d /workspace/w22_c28_aig_meetup ]]; then
		git subtree \
			add \
			-P  w22_c28_aig_meetup \
			https://gitee.com/coding_net_cloud_studio/w22_c28_aig_meetup.git \
			wmstudy \
			--squash
	fi

	if [[ ! -f /tmp/c06_新码农在家背单词_主窗口已经打开_不需要再次打开_锁.sh ]]; then
		# 上述的特殊文件_不存在_就创建
		# 该锁文件_防止_相互_循环拉起
		touch /tmp/c06_新码农在家背单词_主窗口已经打开_不需要再次打开_锁.sh
	fi

	# git clone subtree完毕以后_新增一个cloudstudio窗口去展示_该子git仓库的信息
	# if [[ -d /workspace/w22_c28_aig_meetup ]]; then
	# 	cloudstudio -n /workspace/w22_c28_aig_meetup
	# fi

	return 0
}

# ==============================================================

# NOTE 由于通过git_clone_下载新的pyenv到/root/.pyenv位置以后
# /root/.pyenv/.git目录会占有148M的存储空间
# /root/.pyenv/06_样例_目录_会占用_53M_的存储空间
# 删除上述两个目录_释放一定的空间
# 大约释放200M左右的存储空间
l77_clean_root_pyenv_sub_directories(){

	if [[ -d /root/.pyenv/06_样例 ]]; then
		rm -rf /root/.pyenv/06_样例
	fi

	if [[ -d /root/.pyenv/.git ]]; then
		rm -rf /root/.pyenv/.git
	fi

	return 0
}

# NOTE 做一些设置
l79_final_settings(){

	# NOTE 把当前目录下_很可能位于/workspace目录下_所有的bash_script_都变为可执行文件
	find . -name "*.sh" -exec chmod +x {} \;

	if [[ ! -f /usr/bin/cloudstudio ]]; then
		if [[ -f /.PlnPyKFp4CRfFtgC1/vendor/modules/code-oss-dev/bin/remote-cli/cloudstudio ]]; then
			ln -s /.PlnPyKFp4CRfFtgC1/vendor/modules/code-oss-dev/bin/remote-cli/cloudstudio /usr/bin/cloudstudio
		fi
	fi

	# NOTE 找到bash脚本wmcloudstudio并且变为可执行文件
	find . -name "wmcloudstudio" -exec chmod +x {} \;

	# NOTE 把当前目录下wmcloudstudio拷贝到容易被找到的目录中去
	if [[ ! -f $(which wmcloudstudio) ]]; then
		if [[ -f ./wmcloudstudio ]]; then
			cp ./wmcloudstudio /usr/bin/wmcloudstudio
			cp ./wmcloudstudio /bin/wmcloudstudio
		fi
	fi

	return 0
}

# ==============================================================
# REVIEW 在好几个地方_建立_linux_commands_目录_用于存放_linux_命令
# NOTE 原因是_泛开发者_开始的cd_pwd_ls_命令都不熟悉
v20_create_linux_commands_directory(){

	if [[ -f .tutorial/d22_给d18增加前缀.txt ]]; then

		while read -r line
		do
			mkdir -p /workspace/mm/$line
			# mkdir -p ~/$line
			# mkdir -p /$line
			# mkdir -p /usr/bin/$line
		done < ".tutorial/d22_给d18增加前缀.txt"
	fi

	return 0
}

# 被下面的_f94_2828_30_main()_函数_所调用
z22_c6_d27_e22_linux_deal_with_this_club_space(){

	# REVIEW 在好几个地方_建立_linux_commands_目录_用于存放_linux_命令
	v20_create_linux_commands_directory

	return 0
}

# ==============================================================
# NOTE 定义main()函数的主体
f94_2828_30_main(){

	# 无论何时都先尝试建立这样一个目录
	# mkdir -p /root/.pyenv

	f16_cs_vs_settings_user_update

	f20_linux_git_setting

	# f23_install_some_software

	# NOTE 把类似imgcat等_进行设置
	f28_20_install_some_wmstudy_bin_tools

	# NOTE 在cloudstudio安装一个npm的module_查找_英文单词的中文解释_等
	# TODO 由于安装时间比较长_这里没有_在开始的时候就安装_以后需要的时候_再安装与使用
	# f36_42_fy_lookup_english_dictionary_for_cloudstudio

	# NOTE 下面是老版本p27的_这里不再调用了
	# l10_install_me

	# 需要从gitee上获取新的pyenv环境
	# l30_git_clone_and_install_new_pyenv

	# NOTE 通过git_subtree的形式把子git仓库加入进来_并新增一个cloudstudio的窗口
	# NOTE 这个模式太复杂了_相互协调很麻烦_放弃了
	# l57_30_git_clong_c28_aig_meetup

	# NOTE 增加一个clean的函数_释放/root/.pyenv下更多的空间
	# l77_clean_root_pyenv_sub_directories

	# NOTE 如果本cloudstudio社区版本的教学仓库中_具有自带的_03_vscode_extension目录
	# NOTE 该目录下_具有很少数的几个必须安装的vscode扩展
	# NOTE 把这几个扩展给安装上
	l07_this_git_call_script_to_install_vscode_ext

	l79_final_settings

	z22_c6_d27_e22_linux_deal_with_this_club_space

	return 0
}

# ==============================================================
# NOTE 设置变量_古诗
gs22_bc10_30_env_of_shiren(){

	export gs22_sg77_yuqian=".tutorial/cs36_learning_grade/gs22_祝贺古文诗词_80首_诗人/sg77_石灰吟_于谦.png"
	return 0
}

# REVIEW 通过诗人展开古诗的开始
gs22_bc20_30_show_shiren_image(){

	# NOTE 设置变量_古诗
	gs22_bc10_30_env_of_shiren

	[[ -f ${gs22_sg77_yuqian} ]] && imgcat ${gs22_sg77_yuqian}

	return 0
}

# ==============================================================

gs(){

	if [[ -f $(which cloudstudio) ]]; then
		# 已经位于cloudstudio.net的工作空间以内了
		if [[ $(whoami) == "root" ]]; then
			echo "$(whoami)"
			if [[ -d /workspace ]]; then
				# 这里可以执行本脚本
				echo "可以执行后继的操作"

				# REVIEW 通过诗人展开古诗的开始
				gs22_bc20_30_show_shiren_image

			fi
		else
			# echo "不知道是_啥环境_不能运行本脚本"
			# 不符合运行条件_退出本脚本的运行
			exit 0
		fi
	fi

	return 0
}


# ==============================================================


f96_3060_check_environment_and_run_main(){

	if [[ -f $(which cloudstudio) ]]; then
		# 已经位于cloudstudio.net的工作空间以内了
		if [[ $(whoami) == "root" ]]; then
			echo "$(whoami)"
			if [[ -d /workspace ]]; then
				# 这里可以执行本脚本
				echo "可以执行后继的操作"

				# 这里是main函数
				f94_2828_30_main

				# REVIEW 通过诗人展开古诗的开始
				gs22_bc20_30_show_shiren_image

			fi
		else
			echo "不知道是_啥环境_不能运行本脚本"
			# 不符合运行条件_退出本脚本的运行
			exit 0
		fi
	fi

	return 0
}

# ==============================================================
# NOTE main()是f94_2828_30_main()的便捷名称
main(){

	if [[ -f $(which cloudstudio) ]]; then
		# 已经位于cloudstudio.net的工作空间以内了
		if [[ $(whoami) == "root" ]]; then
			echo "$(whoami)"
			if [[ -d /workspace ]]; then
				# 这里可以执行本脚本
				echo "可以执行后继的操作"

				# 这里是main函数
				f94_2828_30_main

			fi
		else
			echo "不知道是_啥环境_不能运行本脚本"
			# 不符合运行条件_退出本脚本的运行
			exit 0
		fi
	fi

	return 0
}

# NOTE 调用main()函数
# main

# ==============================================================
# 下面是_正式_的入口
# echo $*
# [ -z "$1" ] && eval f96_3060_check_environment_and_run_main || eval $1 $*
[ -z "$1" ] && eval main || eval $1 $*
