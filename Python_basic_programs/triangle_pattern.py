# ====================== triangular pattern ==================

"""   *
      *  *
      *  *  *
      *  *  *  *
      *  *  *  *  *        """

a,b = 0,0
while b<5:
    if a<=b:
        print("*",end="  ")
        a+=1
        continue

    if a>b:
        b+=1
        a=0
        print("")
