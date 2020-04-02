from django.shortcuts import render, redirect

# Create your views here.
from app01 import models

def login(request):
    info = {}
    username = request.GET.get("username")
    if models.User.objects.filter(username=username).first():
        request.session["username"] = username
        return redirect('index')
    else:
        info['error'] = '没有这个人'
    return render(request, "login.html", locals())


def index(request):
    username = request.session.get("username")
    obj_username = models.User.objects.filter(username=username)[0]
    # print(request.body)
    if request.method == "POST":
        score = request.POST.get("score")
        # print(score)
        models.UserScore.objects.create(user_id=obj_username.id, score=int(score))
    obj_score = models.UserScore.objects.filter(user_id=obj_username.id).order_by("id").last()
    rest_list = []
    obj_user = models.User.objects.all()
    for i in obj_user:
        obj = models.UserScore.objects.filter(user_id=i.id).order_by("id").last()
        dic = {}
        dic["username"] = i.username
        dic['score'] = obj.score
        rest_list.append(dic)
    ret = sorted(rest_list, key=lambda x: x["score"], reverse=True)
    list_index = rest_list.index({"username": username, "score": obj_score.score})
    ret.append(rest_list[list_index])
    ret.remove(rest_list[list_index])
    return render(request, 'index.html', {"username_score": obj_score.score, "ret_list": ret, "username": username})
