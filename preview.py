#!/usr/bin/env python3
# 指定Python解释器的路径,确保使用Python3环境

from flask import Flask, render_template_string
# 导入Flask框架和render_template_string函数用于渲染HTML模板
import markdown
# 导入markdown模块用于将Markdown文件转换为HTML内容

app = Flask(__name__)
# 创建Flask应用实例

@app.route('/')
# 定义根路由处理函数
def home():
    with open('README.md', 'r') as markdown_file:
        # 打开当前目录下的README.md文件并读取内容
        content = markdown_file.read()
        # 读取Markdown文件的内容
        html_content = markdown.markdown(content)
        # 将Markdown内容转换为HTML格式
        return render_template_string('''
            <html>
                <head>
                   <style>
                        img {{
                            max-width: 100%;
                            width: auto;
                            height: auto;
                        }}
                    </style>
                </head>
                <body>
                    {}
                </body>
            </html>
        '''.format(html_content))
        # 使用render_template_string函数渲染HTML模板,并将转换后的HTML内容插入到模板中返回

if __name__ == '__main__':
    app.run(debug=True)
    # 当直接运行该脚本时,启动Flask应用,并开启调试模式
