from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .scraping import getPageSource, getTime, exportAsDict, makeList, changeData, beRowData
from scheduler.models import  User, Org
from d2b import d2b,make_countlist,makeOrg,makedata

def index(request):
    #indexを読み込んでデフォルトの画面表示
    return render(request, "scheduler/index.html")


def makeuser(request):
    if request.method == 'POST':
        # ユーザー登録に必要なデータ軍の定義
        id = request.POST["school_number"]
        pswd       = request.POST["password"]
        
        # ユーザーの講義データを取得
        html      = getPageSource(id, pswd)
        dict_data = exportAsDict(html)
        dict_data = dict_data['Spring']
        pre_class, aft_class = changeData(dict_data)

        # 講義データのバイナリ変換
        pre_class = beRowData(pre_class)
        aft_class = beRowData(aft_class)

        # 書き出しサイズがオーバーフローを起こすため10進数に変換して書き込む
        db_user = User(
            student_id = id,
            team = None,
            qtr_pre = int(pre_class, 2),
            qtr_aft = int(aft_class, 2),
        )
        db_user.save()
    return render(request, "scheduler/makeuser.html")


def makeorg(request):#チームID作成
    if request.method == 'POST':
        team_id = request.POST["team_id"] # 任意のteam_id
        init_data=makedata()
        db_org = Org(team_id=team_id,team_pre =init_data ,team_aft=init_data)
        db_org.save()

    return render(request, "scheduler/makeorg.html")


def joinorg(request):
    if request.method == 'POST':
        #if request.filter(Org.objects.get("team_id").exists()):
        #    print("ok")
        #id = request.POST["school_number"]
        #print(mode_data.qtr_pre)
        team_id_post = request.POST["team_id"] # 参加するチームのteam_idのOrgオブジェクト
        team_id_org = Org.objects.get(team_id=team_id_post)

        Org_predata=team_id_org.team_pre
        Org_aftdata=team_id_org.team_aft


        school_number_post =request.POST["school_number"]#ユーザのオブジェクト作成
        school_number_user=User.objects.get(student_id=school_number_post)
        user_predata=d2b(school_number_user.qtr_pre)
        user_aftdata=d2b(school_number_user.qtr_aft)

        #####更新#####
       
        """
        db_usr = User(team_id=team_id_org,team_pre = 1,team_aft= 1)#Database更新
        db_usr.save()
        """
    return render(request, "scheduler/join.html")

