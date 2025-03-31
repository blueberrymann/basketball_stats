from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'number', 'position', 'height', 'weight')  # 列表显示的字段
    list_filter = ('team', 'position', 'is_active')  # 过滤器
    search_fields = ('name', 'english_name', 'team')  # 搜索字段
    
    # 字段集
    fieldsets = (
        ('基本信息', {
            'fields': ('name', 'english_name', 'number', 'team', 'position', 'height', 'weight', 'birth_date', 'nationality')
        }),
        ('个人信息', {
            'fields': ('experience', 'draft_year', 'draft_position', 'college')
        }),
        ('赛季数据', {
            'fields': ('games_played', 'games_started', 'minutes_per_game')
        }),
        ('得分数据', {
            'fields': ('points_per_game', 'field_goal_percentage', 'three_point_percentage', 'free_throw_percentage')
        }),
        ('其他数据', {
            'fields': ('rebounds_per_game', 'assists_per_game', 'steals_per_game', 'blocks_per_game', 'turnovers_per_game')
        }),
        ('其他信息', {
            'fields': ('is_active', 'image')
        })
    )
