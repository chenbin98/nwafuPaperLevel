import pandas as pd
from django.core.management.base import BaseCommand
from goodjournal.models import JournalLevel

class Command(BaseCommand):
    help = '导入期刊等级数据库（CSV 格式），格式必须包含：期刊名称 和 等级'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='CSV 文件路径')

    def handle(self, *args, **kwargs):
        file_path = kwargs['csv_file']

        try:
            df = pd.read_csv(file_path)

            if '期刊名称' not in df.columns or '等级' not in df.columns:
                self.stderr.write("❌ CSV 文件必须包含列：期刊名称 和 等级")
                return

            # 清空旧数据（如需保留可注释）
            # JournalLevel.objects.all().delete()

            for _, row in df.iterrows():
                JournalLevel.objects.create(
                    name=row['期刊名称'].strip(),
                    level=row['等级'].strip()
                )

            self.stdout.write(self.style.SUCCESS("✅ 数据成功导入，共导入 {} 条记录".format(len(df))))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ 导入失败: {str(e)}"))