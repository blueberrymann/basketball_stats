from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Player

# Create your views here.

class PlayerListView(ListView):
    model = Player
    template_name = 'players/player_list.html'
    context_object_name = 'players'
    paginate_by = 20  # 每页显示20个球员
    ordering = ['-points_per_game']  # 默认按场均得分降序排序

    def get_queryset(self):
        queryset = Player.objects.all()
        # 获取查询参数
        team = self.request.GET.get('team')
        position = self.request.GET.get('position')
        search = self.request.GET.get('search')

        # 根据参数过滤
        if team:
            queryset = queryset.filter(team=team)
        if position:
            queryset = queryset.filter(position=position)
        if search:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(english_name__icontains=search)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 添加所有球队列表用于过滤
        context['teams'] = Player.objects.values_list('team', flat=True).distinct()
        # 添加所有位置列表用于过滤
        context['positions'] = Player.objects.values_list('position', flat=True).distinct()
        return context

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player_detail.html'
    context_object_name = 'player'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = self.get_object()
        
        # 计算一些统计数据
        context['stats'] = {
            'efficiency': (player.points_per_game + player.rebounds_per_game + 
                         player.assists_per_game + player.steals_per_game + 
                         player.blocks_per_game - player.turnovers_per_game),
            'double_double_potential': (player.points_per_game >= 10 and 
                                      (player.rebounds_per_game >= 10 or 
                                       player.assists_per_game >= 10))
        }
        return context

def home(request):
    """主页视图"""
    context = {
        'current_time': timezone.now(),
        'total_players': Player.objects.count(),
    }
    return render(request, 'players/home.html', context)
