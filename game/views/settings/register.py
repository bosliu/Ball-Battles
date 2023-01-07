from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from game.models.player.player import Player


class PlayerView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        if not username or not password:
            return Response({
                'result': "用户名和密码不能为空",
            })
        if password != password_confirm:
            return Response({
                'result': "密码不一致",
            })
        if User.objects.filter(username=username).exists():
            return Response({
                'result': "用户名已存在",
            })
        user = User(username=username)
        user.set_password(password)
        user.save()
        Player.objects.create(user=user, photo="https://n.sinaimg.cn/sinakd10113/266/w584h482/20200505/2670-iteyfwv2755143.jpg")
       
        return Response({
            'result': "success",
        })
