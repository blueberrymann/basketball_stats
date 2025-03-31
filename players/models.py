from django.db import models

# Create your models here.

class Player(models.Model):
    # 基本信息
    name = models.CharField(max_length=100, verbose_name='姓名')
    english_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='英文名')
    number = models.CharField(max_length=10, verbose_name='球衣号码')
    team = models.CharField(max_length=100, verbose_name='所属球队')
    position = models.CharField(max_length=20, verbose_name='位置')
    height = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='身高(米)')
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='体重(公斤)')
    birth_date = models.DateField(verbose_name='出生日期')
    nationality = models.CharField(max_length=50, verbose_name='国籍')
    
    # 个人信息
    experience = models.IntegerField(default=0, verbose_name='球龄')
    draft_year = models.IntegerField(null=True, blank=True, verbose_name='选秀年份')
    draft_position = models.CharField(max_length=10, null=True, blank=True, verbose_name='选秀顺位')
    college = models.CharField(max_length=100, null=True, blank=True, verbose_name='毕业院校')
    
    # 赛季数据
    games_played = models.IntegerField(default=0, verbose_name='出场次数')
    games_started = models.IntegerField(default=0, verbose_name='首发次数')
    minutes_per_game = models.DecimalField(max_digits=4, decimal_places=1, default=0, verbose_name='场均出场时间')
    
    # 得分数据
    # DecimalField参数说明：
    # max_digits: 最大总位数（包括小数点前后的所有数字）
    # decimal_places: 小数点后的位数
    # default: 默认值
    # verbose_name: 在管理界面显示的字段名称
    points_per_game = models.DecimalField(max_digits=4, decimal_places=1, default=0, verbose_name='场均得分')
    
    # 百分比数据使用3位小数以提供更精确的表示(如:0.456表示45.6%)
    field_goal_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0, verbose_name='投篮命中率')
    three_point_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0, verbose_name='三分命中率')
    free_throw_percentage = models.DecimalField(max_digits=4, decimal_places=3, default=0, verbose_name='罚球命中率')
    
    # 其他数据
    # 使用1位小数来记录每场比赛的平均数据
    rebounds_per_game = models.DecimalField(max_digits=4, decimal_places=1, default=0, verbose_name='场均篮板')
    assists_per_game = models.DecimalField(max_digits=4, decimal_places=1, default=0, verbose_name='场均助攻')
    steals_per_game = models.DecimalField(max_digits=4, decimal_places=1, default=0, verbose_name='场均抢断')
    blocks_per_game = models.DecimalField(max_digits=4, decimal_places=1, default=0, verbose_name='场均盖帽')
    turnovers_per_game = models.DecimalField(max_digits=4, decimal_places=1, default=0, verbose_name='场均失误')
    
    # 其他信息
    is_active = models.BooleanField(default=True, verbose_name='是否现役')
    image = models.ImageField(upload_to='player_images/', null=True, blank=True, verbose_name='球员照片')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '球员'
        verbose_name_plural = '球员'

    def __str__(self):
        """
        返回球员对象的字符串表示。
        格式为：球员姓名 - 所属球队 - 球衣号码
        
        Returns:
            str: 包含球员基本信息的字符串
        """
        return f"{self.name} - {self.team} - {self.number}号"
