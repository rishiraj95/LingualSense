## Write your program here

# this function is to check if chef should buy coupon
def coupon_buy(N,X,Y,prices):

    #total cost but, without the discount coupon
    without_cpn_total = sum(prices)

    #total cost including the coupon discount
    with_cpn_total = 0
    for pr in prices:

        #make it free in case cost is less than equal to discount coupon
        if pr <= Y:
            with_cpn_total+=0
        else:

            #else subtract discount from item cost and update it
            with_cpn_total+=pr-Y
    
    #add the coupon cost also
    with_cpn_total+=X
    
    #if the total cost with coupon is less, return "COUPON"
    if with_cpn_total<without_cpn_total:
        return "COUPON"
    else:

        #else return "NO COUPON"
        return "NO COUPON"


#create main function 
def main():

    #this part will take the number of test cases
    T = int(input())
    ans =[]

    #initialise a loop for each test case
    for _ in range(T):

        #read N, X, and Y for this test case
        N, X, Y = map(int, input().split())

        #read the prices of the items
        prices = list(map(int, input().split()))
        
        #call function to check if in the end chef should buy the coupon or not
        res = coupon_buy(N,X,Y,prices)

        #add the result to the list
        ans.append(res)

    #print all the results every line    
    print("\n".join(ans))

#lastly, run the main function
main()

#END OF PROGRAM 