# goodjournal/views.py
from django.http import JsonResponse
from django.shortcuts import render
from .models import JournalLevel
import pandas as pd

def search_journal(request):
    context = {}
    journal_name = request.POST.get("journal_name") if request.method == "POST" else request.GET.get("journal_name")
    if journal_name:
        journal = JournalLevel.objects.filter(name__iexact=journal_name.strip()).first()
        if journal:
            context["result"] = {"期刊名称": journal.name, "等级": journal.level}
        else:
            context["message"] = "未找到该期刊"
    elif request.method == "POST" or request.GET.get("submit") == "true":
        context["error"] = "请输入期刊名称"
    return render(request, "search.html", context)

def update_journal(request):
    context = {}
    if request.method == "GET":
        journal_name = request.GET.get("journal_name")
        level = request.GET.get("level")
        delete_flag = request.GET.get("delete")
        if not journal_name:
            context["error"] = "请提供期刊名称"
        elif delete_flag == "true":
            journal = JournalLevel.objects.filter(name__iexact=journal_name.strip()).first()
            if journal:
                # Save to recycle bin
                with open("recycle_bin.csv", "a", encoding="utf-8") as f:
                    f.write(f"{journal.name},{journal.level}\n")
                journal.delete()
                context["message"] = "期刊记录已删除并移至回收站"
            else:
                context["error"] = "未找到该期刊"
        elif level:
            JournalLevel.objects.update_or_create(
                name=journal_name.strip(),
                defaults={'level': level.strip()}
            )
            context["message"] = "已更新或添加该期刊"
        else:
            context["error"] = "请提供等级"

    elif request.method == "POST":
        file = request.FILES.get("file")
        if not file or not file.name.endswith('.csv'):
            context["error"] = "请上传 .csv 格式的数据库文件"
        else:
            try:
                df = pd.read_csv(file)
                if '期刊名称' not in df.columns or '等级' not in df.columns:
                    context["error"] = "CSV 文件必须包含 '期刊名称' 和 '等级' 两列"
                else:
                    for _, row in df.iterrows():
                        JournalLevel.objects.update_or_create(
                            name=row['期刊名称'].strip(),
                            defaults={'level': row['等级'].strip()}
                        )
                    context["message"] = "数据库已成功更新"
            except Exception as e:
                context["error"] = f"导入失败: {str(e)}"
    return render(request, "update.html", context)