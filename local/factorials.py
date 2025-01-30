import logging 

# Set up logging
log = "bot.log"
logging.basicConfig(filename=log,level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('Log Entry Here.')


def factorials(num):
    logging.info(f'num = {num}')
    if num == 1:
        return 1
    return num * factorials(num-1)

def fact(num):
    ans = 1
    for x in range (1, num+1):
        ans = ans * x
    return ans


print(fact(6))
print(factorials(6))