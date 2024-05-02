class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = ""
        x=0
        roman = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        while num>0:
            if num>=1000:
                x = num
                val+="M"
                num-=1000
            elif num<1000 and num>=900:
                val+="CM"
                num-=900
            elif num<900 and num>=500:
                val+="D"
                num-=500
            elif num<500 and num>=400:
                val+="CD"
                num-=400
            elif num<400 and num>=100:
                val+="C"
                num-=100
            elif num<100 and num>=90:
                val+="XC"
                num-=90
            elif num<90 and num>=50:
                val+="L"
                num-=50
            elif num<50 and num>=40:
                val+="XL"
                num-=40
            elif num<40 and num>=10:
                val+="X"
                num-=10
            elif num==9:
                val+="IX"
                num-=9

            elif num<9 and num>=5:
                val+="V"
                num-=5
            elif num==4:
                val+="IV"
                num-=4
            else:
                val+="I"
                num-=1
        return val
            



        

