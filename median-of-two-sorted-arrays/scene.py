from manim import *

def TextInRectangle(self, s):
    rectangle = Rectangle(width = 1.5, height = 1)
    text = Text(s).move_to(rectangle.get_center())
    return VGroup(rectangle, text)

def ArrayToVGroup(self, texts):
    temp = VGroup(*[TextInRectangle(self, text) for text in texts])
    for i in range(1, len(texts)):
        temp[i].next_to(temp[i-1], RIGHT, buff = 0)
    return temp

class Example1(Scene):
    def construct(self):
        romans = ['I','I','I']
        romans_vgroup = ArrayToVGroup(self, romans).move_to(0)

        decimals = ['1','1','1']
        decimals_vgroup = ArrayToVGroup(self, decimals).move_to(0)

        sum_left = Text('SUM = ').set_color(PINK)
        sum_right = Text('1 + 1 + 1').next_to(sum_left, RIGHT)
        sum_vgroup = VGroup(sum_left, sum_right).move_to(0 + DOWN*2)

        # Animation
        self.play(Write(romans_vgroup))
        self.play(Transform(romans_vgroup, decimals_vgroup))
        self.play(Write(sum_vgroup))
        temp = Text('3').next_to(sum_left, RIGHT)
        self.play(Transform(sum_right, temp))

class Example2(Scene):
    def construct(self):
        romans = ['I','V']
        romans_vgroup = ArrayToVGroup(self, romans).move_to(0)

        decimals = ['1','5']
        decimals_vgroup = ArrayToVGroup(self, decimals).move_to(0)

        sum_left = Text('SUM = ').set_color(PINK)
        sum_right = Text('0').next_to(sum_left, RIGHT)
        sum_vgroup = VGroup(sum_left, sum_right).move_to(0 + DOWN*2)

        # Animation
        self.play(Write(romans_vgroup))
        self.play(Transform(romans_vgroup, decimals_vgroup))
        self.play(Write(sum_vgroup))
        
        curved_arrow = CurvedArrow(decimals_vgroup[0].get_bottom(), decimals_vgroup[1].get_bottom())
        self.play(ShowCreation(curved_arrow))
        self.play(FadeOut(curved_arrow))
        temp = Text('- 1 + 5').next_to(sum_left, RIGHT)
        self.play(Transform(sum_right, temp))
        temp = Text('4').next_to(sum_left, RIGHT)
        self.play(Transform(sum_right, temp))

class Solution(Scene):
    def construct(self):
        romans = ['M','C','M','X','C','I','V']
        romans_vgroup = ArrayToVGroup(self, romans).move_to(0)

        decimals = ['1000','100','1000','10','100','1','5']
        decimals_vgroup = ArrayToVGroup(self, decimals).move_to(0)

        sum = 0
        sum_left = Text('SUM = ').set_color(PINK)
        sum_right = Text(str(sum)).next_to(sum_left, RIGHT)
        sum_vgroup = VGroup(sum_left, sum_right).move_to(0 + DOWN*2)

        # Animation
        self.play(Write(romans_vgroup))
        self.play(Transform(romans_vgroup, decimals_vgroup))
        self.play(Write(sum_vgroup))
        
        last = 0
        surroundingRectangle = SurroundingRectangle(decimals_vgroup[6])
        for i in reversed(range(7)):
            # Animate Surrounding Rectangle
            if i == 6:
                self.play(ShowCreation(surroundingRectangle))
            else:
                self.play(Transform(surroundingRectangle, SurroundingRectangle(decimals_vgroup[i])))
                curved_arrow = CurvedArrow(start_point=decimals_vgroup[i].get_bottom(), end_point=decimals_vgroup[i+1].get_bottom())
                self.play(ShowCreation(curved_arrow))
                self.play(FadeOut(curved_arrow))

            # Calculation
            curr = int(decimals[i])
            if curr > last:
                temp = Text(str(sum) + ' + ' + decimals[i]).next_to(sum_left, RIGHT)
                sum += curr
            else:
                temp = Text(str(sum) + ' - ' + decimals[i]).next_to(sum_left, RIGHT)
                sum -= curr
            last = curr

            # Animate sum calculation
            self.play(Transform(sum_right, temp))
            temp = Text(str(sum)).next_to(sum_left, RIGHT)
            self.play(Transform(sum_right, temp))

        # Animate removal of the last Surrounding Rectangle
        self.play(FadeOut(surroundingRectangle))
