from manim import *

def TextInRectangle(self, s):
    rectangle = Rectangle(width = 1.5, height = 1)
    text = Text(s).move_to(rectangle.get_center())
    return VGroup(rectangle, text)

def ArrayToVGroup(self, texts):
    temp = VGroup(*[TextInRectangle(self, text) for text in texts], buff = 0)
    for i in range(1, len(texts)):
        temp[i].next_to(temp[i-1], RIGHT, buff = 0)
    return temp

def showTitle(self, title):
    text = Tex(title).scale(2)
    self.play(Write(text))
    self.play(FadeOut(text))

def writeText(self, text):
    mathTex = MathTex('median ', text).scale(1.5)
    mathTex[0].set_color(GREEN_SCREEN)
    self.play(Write(mathTex.move_to(2*DOWN)))
    return mathTex

def evenExample(self, nums):
    # Set objects
    one = TextInRectangle(self, nums[0])
    two = TextInRectangle(self, nums[1]).next_to(one, RIGHT, buff = 0)
    three = TextInRectangle(self, nums[2])
    four = TextInRectangle(self, nums[3]).next_to(three, RIGHT, buff = 0)
    median_left = TextInRectangle(self, nums[1])
    median_right = TextInRectangle(self, nums[2]).next_to(median_left, RIGHT, buff = 0)
    median_vgroup = VGroup(median_left, median_right).move_to(ORIGIN)

    # Animation
    self.play(Write(VGroup(one, two).move_to(ORIGIN + UP*2)))
    self.play(Write(VGroup(three, four).move_to(ORIGIN + DOWN*2)))
    self.play(
        ApplyMethod(one.next_to, median_left, LEFT, 0),
        ApplyMethod(two.next_to, median_left, 0),
        ApplyMethod(three.next_to, median_right, 0),
        ApplyMethod(four.next_to, median_right, RIGHT, 0),
    )

    # Surrounding rectangle
    rectangle = SurroundingRectangle(median_vgroup)
    self.play(ShowCreation(rectangle))

    # Write bottom text
    mathTex = writeText(self, '= ({0} + {1}) / 2 = {2}'.format(nums[1], nums[2], (int(nums[1])+int(nums[2]))/2))

    # Clear screen
    self.play(FadeOut(VGroup(one, two, three, four, rectangle, mathTex)))

class Introduction(Scene):
    def construct(self):
        # Show title
        tex1 = Tex('Median of Two Sorted Arrays').scale(2).move_to(UP)
        tex2 = MathTex('O(log (m+n))').scale(2).move_to(DOWN)
        self.play(Write(tex1))
        self.wait()
        line = Line()
        self.play(ShowCreation(line))
        self.play(Write(tex2))
        self.wait()
        self.play(FadeOut(VGroup(tex1, line, tex2)))

class Example1(Scene):
    def construct(self):
        # Show title
        showTitle(self, 'Example 1')

        one = TextInRectangle(self, '1')
        two = TextInRectangle(self, '2').move_to(2*DOWN)
        three = TextInRectangle(self, '3').next_to(one, RIGHT, buff = 0)
        median = TextInRectangle(self, '2').move_to(ORIGIN)

        # Animation
        self.play(Write(VGroup(one, three).move_to(ORIGIN + UP*2)))
        self.play(Write(two))
        self.play(
            ApplyMethod(one.next_to, median, LEFT, 0),
            ApplyMethod(two.next_to, median, 0),
            ApplyMethod(three.next_to, median, RIGHT, 0),
        )

        # Surrounding rectangle
        rectangle = SurroundingRectangle(median)
        self.play(ShowCreation(rectangle))

        # Write bottom text
        mathTex = writeText(self, '= 2')

        # Clear screen
        self.play(FadeOut(VGroup(one, two, three, rectangle, mathTex)))

class Example2(Scene):
    def construct(self):
        # Show title
        showTitle(self, 'Example 2')

        evenExample(self, ['1', '2', '3', '4'])

class Example3(Scene):
    def construct(self):
        # Show title
        showTitle(self, 'Example 3')
        evenExample(self, ['0', '0', '0', '0'])

class Example4(Scene):
    def construct(self):
        # Show title
        showTitle(self, 'Odd example')

        #[0,0,0]
        #[-1,0,0,0,1]
        # Set objects
        t1 = TextInRectangle(self, '0')
        t2 = TextInRectangle(self, '0').next_to(t1, RIGHT, buff = 0)
        t3 = TextInRectangle(self, '0').next_to(t2, RIGHT, buff = 0)
        top = VGroup(t1, t2, t3).move_to(ORIGIN + UP*2)
        b1 = TextInRectangle(self, '-1')
        b2 = TextInRectangle(self, '0').next_to(b1, RIGHT, buff = 0)
        b3 = TextInRectangle(self, '0').next_to(b2, RIGHT, buff = 0)
        b4 = TextInRectangle(self, '0').next_to(b3, RIGHT, buff = 0)
        b5 = TextInRectangle(self, '1').next_to(b4, RIGHT, buff = 0)
        bottom = VGroup(b1, b2, b3, b4, b5).move_to(ORIGIN + DOWN*2)
        m1 = TextInRectangle(self, '0')
        m2 = TextInRectangle(self, '0').next_to(m1, RIGHT, buff = 0)
        m3 = TextInRectangle(self, '0').next_to(m2, RIGHT, buff = 0)
        m4 = TextInRectangle(self, '0').next_to(m3, RIGHT, buff = 0)
        m5 = TextInRectangle(self, '0').next_to(m4, RIGHT, buff = 0)
        m6 = TextInRectangle(self, '0').next_to(m5, RIGHT, buff = 0)
        m7 = TextInRectangle(self, '0').next_to(m6, RIGHT, buff = 0)
        m8 = TextInRectangle(self, '0').next_to(m7, RIGHT, buff = 0)
        median_vgroup = VGroup(m1, m2, m3, m4, m5, m6, m7, m8).move_to(ORIGIN)

        # Animation
        self.play(Write(top))
        self.play(Write(bottom))
        self.play(
            ApplyMethod(top.next_to, m4, LEFT, 0),
            ApplyMethod(bottom.next_to, m3, RIGHT, 0),
        )
        self.play(
            ApplyMethod(top.next_to, m5, LEFT, 0),
            ApplyMethod(b1.next_to, m2, LEFT, 0),
        )

        # Surrounding rectangle
        rectangle = SurroundingRectangle(median_vgroup)
        self.play(ShowCreation(rectangle))

        # Write bottom text
        mathTex = writeText(self, '= (1 + 2) / 2 = 3')

        # Clear screen
        self.play(FadeOut(VGroup(top, bottom, rectangle, mathTex)))

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
