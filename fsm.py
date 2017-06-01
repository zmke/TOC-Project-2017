# encoding: utf-8
from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def start_chosen(self, update):
        text = update.message.text
        return text == "/start"

    def shoulder_chosen(self, update):
        text = update.message.text
        return text == u"肩頸"

    def upper_chosen(self, update):
        text = update.message.text
        return text == u"上半身"

    def lower_chosen(self, update):
        text = update.message.text
        return text == u"下半身"

    def s_1_chosen(self, update):
        text = update.message.text
        return text == u"枕下肌"

    def s_2_chosen(self, update):
        text = update.message.text
        return text == u"上斜方肌"    
    
    def s_2_1_chosen(self, update):
        text = update.message.text
        return text == u"站式"
    
    def s_2_2_chosen(self, update):
        text = update.message.text
        return text == u"坐式"

    def s_3_chosen(self, update):
        text = update.message.text
        return text == u"肩胛提肌"

    def u_1_chosen(self, update):
        text = update.message.text
        return text == u"胸大肌"

    def u_2_chosen(self, update):
        text = update.message.text
        return text == u"胸小肌"

    def u_3_chosen(self, update):
        text = update.message.text
        return text == u"束脊肌"

    def l_1_chosen(self, update):
        text = update.message.text
        return text == u"膕旁肌"

    def l_2_chosen(self, update):
        text = update.message.text
        return text == u"梨狀肌"

    def l_3_chosen(self, update):
        text = update.message.text
        return text == u"腓腸肌"

    def on_enter_start(self, update):
        self.go_back(update)

    def on_enter_user(self, update):
        update.message.reply_text("想伸展哪邊呢？\n肩頸\n上半身\n下半身")

    def on_enter_shoulder(self, update):
        update.message.reply_text("想伸展哪個肌肉\n枕下肌\n上斜方肌\n肩胛提肌")

    def on_exit_shoulder(self, update):
        print('Leaving shoulder')

    def on_enter_upper(self, update):
        update.message.reply_text("想伸展哪個肌肉\n胸大肌\n胸小肌\n束脊肌")     

    def on_exit_upper(self, update):
        print('Leaving upper')

    def on_enter_lower(self, update):
        update.message.reply_text("想伸展哪個肌肉\n膕旁肌\n梨狀肌\n腓腸肌")     

    def on_exit_lower(self, update):
        print('Leaving lower')

    def on_enter_s_1(self, update):
        update.message.reply_text("雙手放在耳後，下巴下壓並點頭持續五秒鐘後放鬆，持續15次")
        self.go_back(update)    

    def on_exit_s_1(self, update):
        print('Leaving s_1')

    def on_enter_s_2(self, update):
        update.message.reply_text("想要站著拉?坐著拉？\n站式\n坐式")    

    def on_exit_s_2(self, update):
        print('Leaving s_2')

    def on_enter_s_2_1(self, update):
        update.message.reply_text("​如果要拉左邊，則將右手繞過頭放在左側腦後，左手放在背後，右手將頭下壓並向腋下扭轉，持續30秒")    
        self.go_back(update)

    def on_exit_s_2_1(self, update):
        print('Leaving s_2_1')

    def on_enter_s_2_2(self, update):
        update.message.reply_text("​如果要拉左邊，則將右手繞過頭放在左側腦後，左手放在大腿下，右手將頭下壓並向腋下扭轉，持續30秒")    
        self.go_back(update)

    def on_exit_s_2_2(self, update):
        print('Leaving s_2_2')

    def on_enter_s_3(self, update):
        update.message.reply_text("如果要拉左邊，則把左手放在左側肩胛骨內緣扣好，右手繞過頭放頭上，將頭下壓並向腋下扭轉，持續30秒")    
        self.go_back(update)

    def on_exit_s_3(self, update):
        print('Leaving s_3')

    def on_enter_u_1(self, update):
        update.message.reply_text("首先你要找到一個門框，確保附近沒人。如果要拉左邊，則把左腳向前彎曲成弓箭步，雙手水平放在門框上，身體慢慢向前傾")    
        self.go_back(update)

    def on_exit_u_1(self, update):
        print('Leaving u_1')

    def on_enter_u_2(self, update):
        update.message.reply_text("先找到一面牆，如果要拉左邊，將左手放於牆上與肩膀同高的位置，腳與牆離大約50公分，左腳向前彎曲成弓箭步，身體慢慢向前傾，注意身體不能往牆壁轉，要跟牆面水平移動")    
        self.go_back(update)

    def on_exit_u_2(self, update):
        print('Leaving u_2')    

    def on_enter_u_3(self, update):
        update.message.reply_text("平躺雙手抱膝，先維持這樣30秒再用膝蓋頂著手6秒，重複到覺得肌肉放鬆或疼通減輕為止")    
        self.go_back(update)

    def on_exit_u_3(self, update):
        print('Leaving u_3')

    def on_enter_l_1(self, update):
        update.message.reply_text("如果要拉左邊，將左腳抬高放在床上，抬高後再以腹部往大腿方向將身體下壓。")    
        self.go_back(update)

    def on_exit_l_1(self, update):
        print('Leaving l_1')

    def on_enter_l_2(self, update):
        update.message.reply_text("如果要拉左邊，坐姿翹左腳將腳踝放到右膝上，以腹部往大腿方向將身體下壓")    
        self.go_back(update)

    def on_exit_l_2(self, update):
        print('Leaving l_2')    

    def on_enter_l_3(self, update):
        update.message.reply_text("先找到一面牆，如果要拉左邊，先將手向前放在牆上，左腳向後，腳底要貼著地面，右腳向前成功箭步，腳底要貼著地面，慢慢把重心向下移")    
        self.go_back(update)

    def on_exit_l_3(self, update):
        print('Leaving l_3')