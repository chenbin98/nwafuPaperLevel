# nwafuPaperLevel
查询西北农林科技大学的期刊等级，包含学校G1,各个学院的AB刊等，持续更新。

## 项目说明

本项目是一个基于 Django 开发的 Web 应用，用于查询和管理西北农林科技大学的期刊等级信息。系统支持查询学校 G1 期刊以及各学院的 AB 刊信息。

## 功能特点

- 期刊等级查询
- 期刊信息管理
- 支持多用户访问
- 实时数据更新

## 安装步骤

1. 克隆项目到本地
```bash
git clone [项目地址]
cd nwafuPaperLevel
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 初始化数据库
```bash
python manage.py migrate
```

4. 启动开发服务器
```bash
python manage.py runserver 0.0.0.0:8000
```

## 使用说明

### 查询期刊
访问以下地址进行期刊查询：
- 查询页面：http://10.133.16.115:8000/goodjournal/search/

### 管理期刊
访问以下地址进行期刊管理：
- 更新期刊信息：http://10.133.16.115:8000/goodjournal/update/

## 注意事项

- 本项目仅供西北农林科技大学内部使用（需使用校内网络）
- 数据会定期更新，请以最新数据为准
- 如有问题或建议，请联系管理员

## 技术支持

如有技术问题，请联系项目维护人员。
