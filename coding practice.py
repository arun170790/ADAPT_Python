
class coding:

    def firstoccur(a):
        counter = {}
        for x in a:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1

        print(counter)


obj = coding
obj.firstoccur('Arunkumar Thangaraj')