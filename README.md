# CBA球员数据统计网站

这是一个基于Django开发的CBA（中国篮球职业联赛）球员数据统计网站。该网站提供了全面的球员数据展示、统计分析和数据可视化功能。

## 功能特点

- 📊 **球员数据展示**
  - 球员基本信息（姓名、球队、位置等）
  - 详细统计数据（得分、篮板、助攻等）
  - 球员照片展示

- 🔍 **数据筛选与搜索**
  - 按球队筛选
  - 按位置筛选
  - 球员名称搜索
  - 分页显示

- 📈 **数据统计与分析**
  - 效率值计算
  - 两双潜力分析
  - 数据可视化展示

- 🎨 **现代化界面**
  - 响应式设计
  - 清晰的数据展示
  - 直观的用户界面

## 技术栈

- Python 3.x
- Django 5.0
- Bootstrap 5
- SQLite（默认数据库）

## 安装步骤

1. 克隆项目
```bash
git clone [项目地址]
cd cba_stats_site
```

2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 数据库迁移
```bash
python manage.py makemigrations
python manage.py migrate
```

5. 创建超级用户
```bash
python manage.py createsuperuser
```

6. 运行开发服务器
```bash
python manage.py runserver
```

7. 访问网站
打开浏览器访问 http://127.0.0.1:8000/

## 项目结构

```
cba_stats_site/
├── cba_stats_site/      # 项目配置目录
├── players/             # 球员应用目录
│   ├── models.py       # 数据模型
│   ├── views.py        # 视图函数
│   ├── urls.py         # URL配置
│   └── templates/      # 模板文件
├── media/              # 媒体文件目录
├── static/             # 静态文件目录
└── manage.py           # Django管理脚本
```

## 数据模型

### Player（球员）模型包含以下字段：
- 基本信息：姓名、英文名、球队、号码、位置等
- 身体数据：身高、体重、出生日期等
- 统计数据：出场次数、得分、篮板、助攻等
- 其他信息：选秀信息、毕业院校等

## 开发计划

- [ ] 添加更多数据可视化图表
- [ ] 实现球员数据对比功能
- [ ] 添加历史数据查询
- [ ] 优化移动端显示
- [ ] 添加数据导出功能

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进这个项目。

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 联系方式

如有问题或建议，请通过以下方式联系：
- 提交Issue

## 致谢

感谢所有为这个项目做出贡献的开发者。 